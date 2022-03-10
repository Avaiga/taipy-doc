# ######################################################################
#
# Syntax for cross-references to the Reference Manual:
#   `ClassName^`
#       generates a link from `ClassName` to the class doc page
#   `functionName(*)^`
#       generates a link from `functionName(*)` to the function doc page
#   `ClassName.methodName(*)^`
#       generates a link from `ClassName.methodName(*)` to the method
#       doc page.
#   `(ClassName.)methodName(*)^`
#       generates a link from `methodName(*)` to the method doc page.
#   `package.functionName(*)^`
#       generates a link from `functionName` to the function doc page
#   `(package.)functionName(*)^`
#       generates a link from `functionName` to the function doc page,
#       hiding the package.
# ######################################################################
import os
import re
from typing import Dict
import logging
import json
from weakref import ref

from importlib_metadata import pass_none

def define_env(env):
    """
    Mandatory to make this a proper MdDocs macro
    """
    pass


TOC_ENTRY_PART1 = r"<li\s*class=\"md-nav__item\">\s*<a\s*href=\""
TOC_ENTRY_PART2 = r"\"\s*class=\"md-nav__link\">([^<]*)</a>\s*</li>\s*"
# XREF_RE details:
#  group(1) - A potential opening '('.
#  group(2) - The class or function name.
#  group(3) - If not empty, the name of a method, with the '.' prefix
#    if the classname is to be preserved (group(1) is empty).
#  group(4) - The function parameters, with their ().
XREF_RE = re.compile(r"<code>(\()?([^\d\W]\w*)(?:\.\))?"
                     + r"((?:\.)?(?:[^\d\W]\w*))?(\(.*?\))?\^</code>")

def find_dummy_h3_entries(content: str) -> Dict[str, str]:
    """
    Find 'dummy <h3>' entries.

    These are <h3> tags that are just redirections to another page.
    These need to be removed, and redirection must be used in TOC.
    """

    ids = {}
    TOC_ENTRY = re.compile(TOC_ENTRY_PART1 + r"(#[^\"]+)" + TOC_ENTRY_PART2, re.M | re.S)
    while True:
        toc_entry = TOC_ENTRY.search(content)
        if toc_entry is None:
            break
        content = content[toc_entry.end() :]
        id = toc_entry.group(1)[1:]
        dummy_h3 = re.search(r"<h3\s+id=\"" + id + r"\">\s*<a\s+href=\"(.*?)\".*?</h3>", content, re.M | re.S)
        if dummy_h3 is not None:
            ids[id] = dummy_h3.group(1)
    return ids


def remove_dummy_h3(content: str, ids: Dict[str, str]) -> str:
    """
    Removes dummy <h3> entries and fix TOC.
    """

    for id, redirect in ids.items():
        # Replace redirection in TOC
        content = re.sub(
            TOC_ENTRY_PART1 + "#" + id + TOC_ENTRY_PART2,
            '<li class="md-nav__item"><a href="' + redirect + '" class="md-nav__link">\\1</a></li>\n',
            content,
            re.M | re.S,
        )
        # Remove dummy <h3>
        content = re.sub(r"<h3\s+id=\"" + id + r"\">\s*<a\s+href=\".*?\".*?</h3>", "", content, re.M | re.S)
    return content


def on_post_build(env):
    "Post-build actions for Taipy documentation"

    site_dir = env.conf["site_dir"]
    log = logging.getLogger("mkdocs")
    xrefs = {}
    if os.path.exists(site_dir + "/manuals/xrefs"):
        with open(site_dir + "/manuals/xrefs") as xrefs_file:
            xrefs = json.load(xrefs_file)
    if xrefs is None:
        log.error(f"Could not find xrefs in /manuals/xrefs")
    x_packages = set()
    for ps in xrefs.values():
        x_packages.add(ps[0])
    ref_files_path = os.path.join(site_dir, "manuals", "reference")
    for root, _, file_list in os.walk(site_dir):
        for f in file_list:
            # Post-process generated '.html' files
            if f.endswith(".html"):
                filename = os.path.join(root, f)
                file_was_changed = False
                with open(filename) as html_file:
                    try:
                        html_content = html_file.read()
                    except Exception as e:
                        print(f"Couldn't read HTML file {filename}")
                        raise e
                    # Rebuild coherent links from TOC to sub-pages
                    ids = find_dummy_h3_entries(html_content)
                    if ids:
                        html_content = remove_dummy_h3(html_content, ids)
                        file_was_changed = True
                    # Collapse doubled <h1>/<h2> page titles
                    REPEATED_H1_H2 = re.compile(
                        r"<h1>(.*?)</h1>\s*<h2\s+(id=\".*?\")>\1(<a\s+class=\"headerlink\".*?</a>)?</h2>", re.M | re.S
                    )
                    html_content, n_changes = REPEATED_H1_H2.subn('<h1 \\2>\\1\\3</h1>', html_content)
                    if n_changes != 0:
                        file_was_changed = True
                    # Add external link icons
                    # Note we want this only for the simple [text](http*://ext_url) cases
                    EXTLINK = re.compile(
                        r"<a\s+(href=\"http[^\"]+\">.*?<\/a>)", re.M | re.S
                    )
                    html_content, n_changes = EXTLINK.subn('<a class="ext-link" \\1', html_content)
                    if n_changes != 0:
                        file_was_changed = True
                    # Find and resolve potential cross-references to the Reference Manual
                    rel_path = os.path.relpath(ref_files_path, filename).replace("\\", "/").replace("../", "", 1)
                    new_content = ""
                    last_location = 0
                    for xref in XREF_RE.finditer(html_content):
                        groups = xref.groups()
                        # function_name -> None, function_name, None, *
                        # package.function_name -> None, package, .function_name, *
                        # (package.)function_name -> '(', package, function_name, *
                        # class_name -> None, class_name, None, *
                        # package.class_name -> None, package, .class_name, *
                        # class_name.method_name -> None, class_name, .method_name, *
                        # (class_name.)method_name -> '(', class_name, method_name, *
                        entry = groups[1]
                        method = groups[2]
                        if method and not groups[0]: # Remove leading '.'
                            method = method[1:]
                        # Function in package? Or method in class?
                        packages  = [entry, None] if entry in x_packages else xrefs.get(entry)
                        if packages is None:
                            (dir, file) = os.path.split(filename)
                            (dir, dir1) = os.path.split(dir)
                            (dir, dir2) = os.path.split(dir)
                            bad_xref = re.sub(r"</?code>", "`", xref.group(0))
                            message = f"Unresolve crossref '{bad_xref}' found in "
                            if file == "index.html":
                                (dir, dir3) = os.path.split(dir)
                                log.error(f"{message}{dir3}/{dir2}/{dir1}.md")
                            else:
                                log.error(f"{message}{dir2}/{dir1}/{file}")
                            continue
                        package = packages[0]
                        orig_package = packages[1]
                        new_content += html_content[last_location:xref.start()]
                        new_content += f"<a href=\"{rel_path}/{package}."
                        if orig_package:
                            new_content += f"{entry}"
                            if method:
                                new_content += f"/index.html#{orig_package}.{entry}.{method}\"><code>"
                                if not groups[0]:
                                    new_content += f"{entry}."
                                new_content += f"{method}"
                            else:
                                new_content += f"\"><code>{entry}"
                        else:
                            new_content += f"{method}/\"><code>"
                            if not groups[0]:
                                new_content += f"{package}."
                            new_content += f"{method}"
                        new_content += f"{groups[3] if groups[3] else ''}</code></a>"
                        last_location = xref.end()
                    if last_location:
                        file_was_changed = True
                        html_content = new_content + html_content[last_location:]
                if file_was_changed:
                    with open(filename, "w") as html_file:
                        html_file.write(html_content)
            # Remove '.md_template' files
            elif f.endswith(".md_template"):
                os.remove(os.path.join(root, f))
