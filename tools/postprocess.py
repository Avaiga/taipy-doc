# ######################################################################
#
# Syntax for cross-references to the Reference Manual:
#   `ClassName^`
#       generates a link from `ClassName` to the class doc page.
#   `functionName(*)^`
#       generates a link from `functionName(*)` to the function doc section.
#   `ClassName.methodName(*)^`
#       generates a link from `ClassName.methodName(*)` to the method doc section.
#   `(ClassName.)methodName(*)^`
#       generates a link from `methodName(*)` to the method doc section, hiding the class name.
#   `package.functionName(*)^`
#       generates a link from `package.functionName(*)` to the function doc section.
#   `(package.)functionName(*)^`
#       generates a link from `functionName(*)` to the function doc section, hiding the package.
#   `(package.)ClassName^`
#       generates a link from `ClassName` to the class doc page, hiding the package.
#   `(package.)ClassName.methodName(*)^`
#       generates a link from `ClassName.methodName(*)` to the method doc section, hiding the
#       package.
#   `(package.ClassName.)methodName(*)^`
#       generates a link from `methodName(*)` to the method doc section, hiding the package and the
#       class name.
# ######################################################################
import os
import re
from typing import Dict
import logging
import json


def define_env(env):
    """
    Mandatory to make this a proper MkDocs macro
    """
    match = re.search(r"/en/(develop|(?:release-(\d+\.\d+)))/$", env.conf["site_url"])
    env.conf["branch"] = (
        (f"release/{match[2]}" if match[2] else match[1]) if match else "unknown"
    )


TOC_ENTRY_PART1 = r"<li\s*class=\"md-nav__item\">\s*<a\s*href=\""
TOC_ENTRY_PART2 = r"\"\s*class=\"md-nav__link\">([^<]*)</a>\s*</li>\s*"
# XREF_RE details:
#  group(1) - The package, class or function name with a trailing '.'.
#    Can be empty.
#    This text will not appear as the anchor text.
#  group(2) - The name of a class, function, method... This text will appear in the anchor text
#  group(3) - The function parameters, with their (). Can be empty.
#  group(4) - The anchor text. Can be empty, then group(2)+group(3) is used.
## XREF_RE = re.compile(r"<code>(\()?((?:[^\d\W]\w*\.)*)"
##                     + r"(?:\))?([^\d\W][\w\.]*)(\(.*?\))?\^<\/code>")
XREF_RE = re.compile(
    r"<code>(?:\(([\w*\.]*)\))?([\.\w]*)(\(.*?\))?\^<\/code>(?:\(([^\)]*)\))?"
)


def find_dummy_h3_entries(content: str) -> Dict[str, str]:
    """
    Find 'dummy <h3>' entries.

    These are <h3> tags that are just redirections to another page.
    These need to be removed, and redirection must be used in TOC.
    """

    ids = {}
    TOC_ENTRY = re.compile(
        TOC_ENTRY_PART1 + r"(#[^\"]+)" + TOC_ENTRY_PART2, re.M | re.S
    )
    while True:
        toc_entry = TOC_ENTRY.search(content)
        if toc_entry is None:
            break
        content = content[toc_entry.end() :]
        id = toc_entry.group(1)[1:]
        dummy_h3 = re.search(
            r"<h3\s+id=\"" + id + r"\">\s*<a\s+href=\"(.*?)\".*?</h3>",
            content,
            re.M | re.S,
        )
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
            '<li class="md-nav__item"><a href="'
            + redirect
            + '" class="md-nav__link">\\1</a></li>\n',
            content,
            re.M | re.S,
        )
        # Remove dummy <h3>
        content = re.sub(
            r"<h3\s+id=\"" + id + r"\">\s*<a\s+href=\".*?\".*?</h3>",
            "",
            content,
            re.M | re.S,
        )
    return content


def create_navigation_buttons() -> str:
    def create_button(label: str, path: str, class_name: str, group: str = "") -> str:
        gclass = " .tp-nav-button-group_element" if group else ""
        html = f"""
                <a class="tp-content-card tp-content-card--extra-small {class_name}{gclass}" href="http://TAIPY_DOCS_URL/{path}">
                <header class="tp-content-card-header">
                    <h4>{label}</h4>
                </header>
                </a>
    """
        if group == "start-group":
            return '<div class="tp-nav-button-group">' + html
        elif group == "end-group":
            return html + "</div>"
        else:
            return '<div class="tp-nav-button-single">' + html + "</div>"

    buttons_html = """
        <div style="margin-bottom: 1rem;">
"""
    for desc in [
        ("Tutorials", "tutorials/getting_started/", "tp-content-card--primary"),
        ("User Manual", "userman/", "tp-content-card--accent"),
        (
            "Visual Elements",
            "refmans/gui/viselements/",
            "tp-content-card--beta",
            "start-group",
        ),
        ("Reference", "refmans/", "tp-content-card--beta", "end-group"),
        ("Gallery", "gallery/", "tp-content-card--alpha"),
    ]:
        buttons_html += create_button(*desc)
    buttons_html += """
        </div>
"""
    return buttons_html


def on_post_build(env):
    """
    Post-build actions for Taipy documentation
    """

    log = logging.getLogger("mkdocs")

    site_dir = env.conf["site_dir"]
    site_dir_unix = site_dir.replace("\\", "/")
    site_url = env.conf["site_url"]
    xrefs = {}
    multi_xrefs = {}
    xrefs_path = "xrefs"
    if os.path.exists(f"{site_dir}/{xrefs_path}"):
        with open(f"{site_dir}/{xrefs_path}") as xrefs_file:
            xrefs = json.load(xrefs_file)
    if not xrefs:
        log.error(f"Could not read any xrefs from '{xrefs_path}'")
    x_packages = set()
    for xref, xref_desc in xrefs.items():
        if isinstance(xref_desc, list):
            x_packages.add(xref_desc[0])
            if xref_desc[2]:
                x_packages.update(xref_desc[2])
        else:
            descs = [xrefs[f"{xref}/{i}"] for i in range(0, xref_desc)]
            # If unspecified, the first xref will be used (the one with the shortest package)
            multi_xrefs[xref] = sorted(descs, key=lambda p: len(p[0]))
    ref_files_path = os.path.join(site_dir, "refmans", "reference")
    fixed_cross_refs = {}
    # Create navigation button once for all pages
    navigation_buttons = create_navigation_buttons()
    for root, _, file_list in os.walk(site_dir):
        for f in file_list:
            # Post-process generated '.html' files
            if f.endswith(".html"):
                filename = os.path.join(root, f)
                with open(filename) as html_file:
                    try:
                        html_content = html_file.read()
                    except Exception as e:
                        log.error(f"Couldn't read HTML file {filename}")
                        raise e

                    # Remove useless spaces for improved processing
                    # This breaks the code blocks - so needs to avoid the <pre> elements before
                    # we bring it back.
                    # html_content = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", html_content))
                    # html_content = html_content.replace("\n\n", "\n")

                    html_content = html_content.replace(
                        '<nav class="md-nav md-nav--primary md-nav--lifted" aria-label="Navigation" data-md-level="0">',
                        '<nav class="md-nav md-nav--primary md-nav--lifted" aria-label="Navigation" data-md-level="0">'
                        + navigation_buttons,
                    )
                    # Replace references to http://TAIPY_DOCS_URL by relative path
                    new_content = ""
                    last_location = 0
                    for m in re.finditer(
                        r"(?<=href=\")http://TAIPY_DOCS_URL(.*?)(?=\")", html_content
                    ):
                        new_content += html_content[
                            last_location : m.start()
                        ] + os.path.relpath(f"{site_dir_unix}{m[1]}", root).replace(
                            "\\", "/"
                        )
                        last_location = m.end()
                    if last_location:
                        html_content = new_content + html_content[last_location:]
                    # Rebuild coherent links from TOC to sub-pages
                    ids = find_dummy_h3_entries(html_content)
                    if ids:
                        html_content = remove_dummy_h3(html_content, ids)
                    # Remove <h1>Index</h1> part of relevant pages
                    INDEX_H1_RE = re.compile(
                        r"<h1>Index</h1>\s*<h2(.*?)>(.*?)</h2>", re.M | re.S
                    )
                    match = INDEX_H1_RE.search(html_content)
                    if match:
                        before = html_content[: match.start()]
                        new_title = match.group(2)
                        if new_title.startswith("Package"):
                            USELESS_TITLE_RE = re.compile(
                                r"(?<=<title>)Index(.*?)(?=</title>)", re.M | re.S
                            )
                            t_match = USELESS_TITLE_RE.search(before)
                            if t_match:
                                new_title = re.sub(r"<a\s+.*?</a>", "", new_title)
                                new_title, n = re.subn(
                                    r"<code>(.*?)</code>", r"\g<1>", new_title
                                )
                                new_title = "Taipy p" + new_title[1:]
                        before = (
                            before[: match.start()] + new_title + before[match.end() :]
                        )
                        html_content = (
                            before
                            + f"<h1{match.group(1)}>{match.group(2)}</h1>"
                            + html_content[match.end() :]
                        )
                    # """
                    # Collapse doubled <h1>/<h2> page titles
                    REPEATED_H1_H2 = re.compile(
                        r"<h1>(.*?)</h1>\s*<h2\s+(id=\".*?\")>\1(<a\s+class=\"headerlink\".*?</a>)?</h2>",
                        re.M | re.S,
                    )
                    html_content, n_changes = REPEATED_H1_H2.subn(
                        "<h1 \\2>\\1\\3</h1>", html_content
                    )

                    # """
                    # Specific processing for Getting Started documentation files
                    if "getting_started" in filename:
                        GS_H1_H2 = re.compile(
                            r"<h1>(.*?)</h1>(.*?<h2.*?>\1)<", re.M | re.S
                        )
                        html_content, n_changes = GS_H1_H2.subn("\\2<", html_content)
                        gs_rel_path = (
                            os.path.relpath(site_dir, filename)
                            .replace("\\", "/")
                            .replace("../", "", 1)
                        )
                        GS_DOCLINK = re.compile(
                            r"(href=\")https://docs\.taipy\.io/en/latest(.*?\")",
                            re.M | re.S,
                        )
                        html_content, n_changes = GS_DOCLINK.subn(
                            f"\\1{gs_rel_path}\\2", html_content
                        )
                        GS_IPYNB = re.compile(
                            r"(<a\s*href=\"([^\"]*?)\.ipynb\")\s*>", re.M | re.S
                        )
                        html_content, n_changes = GS_IPYNB.subn(
                            r"\1 download>", html_content
                        )

                    # Add external link icons (and open in new tab)
                    # Note we want this only for the simple [text](http*://ext_url) cases
                    EXTLINK = re.compile(
                        r"<a\s+(href=\"http[^\"]+\">.*?<\/a>)", re.M | re.S
                    )
                    html_content, n_changes = EXTLINK.subn(
                        '<a class="ext-link" target="_blank" \\1', html_content
                    )

                    # Find and resolve automatic cross-references to the Reference Manual
                    # The syntax in Markdown is `(class.)method()^` and similar.
                    rel_path = (
                        os.path.relpath(ref_files_path, filename)
                        .replace("\\", "/")
                        .replace("../", "", 1)
                    )
                    new_content = ""
                    last_location = 0
                    for xref in XREF_RE.finditer(html_content):
                        all_parts = (xref[1] + xref[2]) if xref[1] else xref[2]
                        parts = all_parts.split(".")
                        c_name: str = parts.pop()  # Class of function name
                        m_name: str = None  # Method name
                        # Get potential destination link descriptor from last part
                        desc = xrefs.get(c_name)
                        # Check for class.method (looking at part before last)
                        if len(parts) > 0:
                            potential_class_name = parts[-1]
                            if class_xref := xrefs.get(potential_class_name):
                                desc = class_xref
                                m_name = c_name
                                c_name = potential_class_name
                                parts.pop()
                        if isinstance(desc, int):
                            if parts:
                                package = ".".join(parts)
                                try:
                                    desc = next(
                                        d
                                        for d in multi_xrefs.get(c_name)
                                        if d[0].endswith(package)
                                    )
                                except Exception:
                                    desc = None
                            else:
                                desc = multi_xrefs.get(c_name)[0]
                        link = None
                        if not desc:
                            # Test for package: a.b.c -> pkg_a/pkg_b/pkg_c
                            paths = "/".join([f"pkg_{e}" for e in all_parts.split(".")])
                            if os.path.exists(f"{ref_files_path}/{paths}/index.html"):
                                link = f"{paths}"
                            else:
                                (dir, file) = os.path.split(filename)
                                (dir, dir1) = os.path.split(dir)
                                (dir, dir2) = os.path.split(dir)
                                message = f"Unresolved crossref '{re.sub(r'</?code>', '`', xref[0])}' found in "
                                if file == "index.html":
                                    (dir, dir3) = os.path.split(dir)
                                    log.error(f"{message}{dir3}/{dir2}/{dir1}.md")
                                else:
                                    log.error(f"{message}{dir2}/{dir1}/{file}")
                        else:
                            split = f"{desc[0]}.{c_name}".split(".")
                            last = split.pop()
                            link = "pkg_" + "/pkg_".join(split) + "/" + last
                            if m_name:
                                link += f"/index.html#{desc[0]}.{c_name}.{m_name}"
                        if link:
                            new_content += html_content[last_location : xref.start()]
                            new_content += f'<a href="{rel_path}/{link}">'
                            if xref[4]:  # Anchor text
                                new_content += xref[4]
                            elif xref[2] or xref[3]:
                                new_content += "<code>"
                                if xref[2]:
                                    new_content += xref[2]
                                if xref[3]:
                                    new_content += xref[3]
                                new_content += "</code>"
                            else:
                                new_content += "<b>NO CONTENT</b>"
                            new_content += "</a>"
                        last_location = xref.end()
                    if last_location:
                        html_content = new_content + html_content[last_location:]

                    # Find 'free' crossrefs to the Reference Manual
                    # Syntax in Markdown is [free text]((class.)method()^) and similar
                    new_content = ""
                    last_location = 0
                    FREE_XREF_RE = re.compile(
                        r"(<a\s+href=\")"
                        + r"([^\d\W]\w*)(?:\.\))?"
                        + r"((?:\.)?(?:[^\d\W]\w*))?(\(.*?\))?\^"
                        + r"(\">.*?</a>)"
                    )
                    for xref in FREE_XREF_RE.finditer(html_content):
                        groups = xref.groups()
                        entry = groups[1]
                        method = groups[2]
                        # Function in package? Or method in class?
                        packages = (
                            [entry, None] if entry in x_packages else xrefs.get(entry)
                        )
                        if packages is None:
                            (dir, file) = os.path.split(filename)
                            (dir, dir1) = os.path.split(dir)
                            (dir, dir2) = os.path.split(dir)
                            bad_xref = xref.group(0)
                            message = (
                                f"Unresolved leftover crossref '{bad_xref}' found in "
                            )
                            if file == "index.html":
                                (dir, dir3) = os.path.split(dir)
                                log.error(f"{message}{dir3}/{dir2}/{dir1}.md")
                            else:
                                log.error(f"{message}{dir2}/{dir1}/{file}")
                            continue
                        else:  # Free XRef was found: forget about the previous warning after all
                            md_file = filename[len(site_dir) :]
                            sep = md_file[0]
                            (dir, file) = os.path.split(
                                md_file[1:]
                            )  # Drop the separator
                            (dir, dir1) = os.path.split(dir)
                            if (
                                file == "index.html"
                            ):  # Other cases to be treated as they come
                                source = f"{dir}{sep}{dir1}.md"
                                dest = f"{dir}{sep}{entry}{method}{groups[3]}^"
                                sources = fixed_cross_refs.get(dest, None)
                                if sources:
                                    sources.add(source)
                                else:
                                    fixed_cross_refs[dest] = {source}
                        package = packages[0]
                        orig_package = packages[1]
                        new_content += html_content[last_location : xref.start()]
                        new_content += f"{groups[0]}{rel_path}/{package}."
                        if orig_package:
                            new_content += f"{entry}"
                            if method:
                                new_content += (
                                    f'/index.html#{orig_package}.{entry}{method}"'
                                )
                        else:
                            new_content += f"{method}/"
                        new_content += f'"{groups[4]}'
                        last_location = xref.end()
                    if last_location:
                        html_content = new_content + html_content[last_location:]

                    # Finding xrefs in 'Parameters', 'Returns' and similar constructs.
                    # These would be <typeName>^ fragments located in potentially
                    # complex constructs such as "Optional[Union[str, <typeName>^]]"
                    #
                    # These fragments appear in single-line <td> blocks.
                    #
                    # At this point, this code is pretty suboptimal and heavily
                    # depends on the MkDocs generation. Time will tell if we can
                    # keep it as is...
                    typing_code = re.compile(
                        r"(<td>\s*<code>)(.*\^.*)(</code>\s*</td>)"
                    )
                    # This will match a single <typeName>^ fragment.
                    typing_type = re.compile(r"\w+\^")
                    for xref in typing_code.finditer(html_content):
                        groups = xref.groups()
                        table_line = groups[1]
                        table_line_to_replace = "".join(groups)
                        new_table_line = table_line_to_replace
                        typing_xref_found = False

                        for type_ in typing_type.finditer(table_line):
                            class_ = type_[0][:-1]  # Remove ^
                            packages = xrefs.get(class_)
                            if packages:
                                # TODO - Retrieve the actual XREF
                                if isinstance(packages, int):
                                    packages = xrefs.get(f"{class_}/0")  # WRONG
                                typing_xref_found = True
                                new_content = f'<a href="{rel_path}/{packages[0]}.{class_}">{class_}</a>'
                                new_table_line = new_table_line.replace(
                                    f"{class_}^", new_content
                                )
                        if typing_xref_found:
                            html_content = html_content.replace(
                                table_line_to_replace, new_table_line
                            )

                    # Replace data-source attributes in h<N> tags to links to
                    # files in the appropriate repositories.
                    process = process_data_source_attr(html_content, env)
                    if process[0]:
                        html_content = process[1]
                    # Replace hrefs to GitHub containing [BRANCH] with proper branch name.
                    process = process_links_to_github(html_content, env)
                    if process[0]:
                        html_content = process[1]
                    # Shorten Table of contents in REST API files
                    if "rest/apis_" in filename or "rest\\apis_" in filename:
                        REST_TOC_ENTRY_RE = re.compile(
                            r"(<a\s+href=\"#apiv.*?>\s+)" + r"/api/v\d+(.*?)(?=\s+</a>)"
                        )
                        new_content = ""
                        last_location = 0
                        for toc_entry in REST_TOC_ENTRY_RE.finditer(html_content):
                            new_content += html_content[
                                last_location : toc_entry.start()
                            ]
                            new_content += f"{toc_entry.group(1)}{toc_entry.group(2)}"
                            last_location = toc_entry.end()
                        if last_location:
                            html_content = new_content + html_content[last_location:]

                    # Rename the GUI Extension API type aliases
                    elif "reference_guiext" in filename:
                        for in_out in [
                            ("TaipyAction", "Action", "../interfaces/Action"),
                            ("TaipyContext", "Context", "#context"),
                        ]:
                            LINK_RE = re.compile(f"<code>{in_out[0]}</code>")
                            new_content = ""
                            last_location = 0
                            for link in LINK_RE.finditer(html_content):
                                new_content += html_content[
                                    last_location : link.start()
                                ]
                                new_content += f'<a href="{in_out[2]}"><code>{in_out[1]}</code></a>'
                                last_location = link.end()
                            if last_location:
                                html_content = (
                                    new_content + html_content[last_location:]
                                )
                    # Change title of Python reference pages
                    # - Taipy.module.class -> taipy.module.class
                    # - Taipy.module.some function -> taipy.module.some_function
                    elif (
                        "refmans/reference" in filename
                        or "refmans\\reference" in filename
                    ):

                        def rewrite_title(s: str, start: int, end: int) -> str:
                            return (
                                html_content[:start]
                                + "taipy."
                                + ".".join(
                                    map(lambda x: x.replace(" ", "_"), s.split("."))
                                )
                                + html_content[end:]
                            )

                        REF_TITLE_RE = re.compile(
                            r"(?<=<title>)(Taipy\.)(.*)(\s+-\s+Taipy</title>)"
                        )
                        if m := REF_TITLE_RE.search(html_content):
                            html_content = rewrite_title(m[2], m.start(1), m.end(2))
                        REF_H1_RE = re.compile(r"(?<=<h1>)(Taipy\.)(.*)</h1>")
                        if m := REF_H1_RE.search(html_content):
                            html_content = rewrite_title(m[2], m.start(1), m.end(2))
                        # Class page?
                        # Replace 'function' to 'method'
                        # Add parenthesis to method names
                        if re.search(
                            r"([/\\])(?!pkg_)\w+\1index.html$", filename
                        ) and re.search(r"<title>\w+\s+class\s", html_content):
                            # Navigation
                            if m := re.search(
                                r"""(<li\s+class="md-nav__item">\s*
                                    <a\s+href="(.*?)-functions"\s+class="md-nav__link">\s*
                                    <span\s+class="md-ellipsis">\s*)
                                    Functions
                                    (?=\s*</span>)""",
                                html_content,
                                re.X,
                            ):
                                class_ref = m[2].replace("#", "\\#")
                                new_content = (
                                    html_content[0 : m.start()] + m[1] + "Methods"
                                )
                                html_content = html_content[m.end() :]
                                last_location = 0
                                for m in re.finditer(
                                    rf"""(<li\s+class="md-nav__item">\s*
                                         <a\s+href="{class_ref}(\.|-)\w+"\s+class="md-nav__link">\s*
                                         <span\s+class="md-ellipsis">\s*
                                         \w+)
                                         (?=\s*</span>)""",
                                    html_content,
                                    re.X,
                                ):
                                    if m[2] == "-":
                                        # End of the methods list
                                        break
                                    new_content += html_content[
                                        last_location : m.start()
                                    ]
                                    new_content += m[1] + "()"
                                    last_location = m.end()
                                if last_location:
                                    html_content = (
                                        new_content + html_content[last_location:]
                                    )
                            new_content = ""
                            last_location = 0
                            for m in re.finditer(
                                r"""<span\s+class="(?:[-\w]+\s+)*doc-function-name(?:\s+[-\w]+)*">
                                    \w+(?=\s*</span>)""",
                                html_content,
                                re.X,
                            ):
                                new_content += (
                                    html_content[last_location : m.end()] + "()"
                                )
                                last_location = m.end()
                            if last_location:
                                html_content = (
                                    new_content + html_content[last_location:]
                                )
                            html_content = re.sub(
                                r"(<h2\s+id=\"(?:[\w\.]+)-functions\">)Functions",
                                "\\1Methods",
                                html_content,
                            )

                            # Page Builder class?
                            m = re.search(r"([/\\])pkg_gui\1pkg_builder\1(\w+)\1index.html$", filename)
                            if m and re.search(r"<title>\w+\s+class\s", html_content):
                                element_type = m[2]
                                # Replace, in signature, styled strings by None and comment
                                new_content = ""
                                last_location = 0
                                # Find signatures
                                for s_m in re.finditer(
                                    r"""<div\s+class="doc-signature
                                                    (.*?)
                                                    div>""",
                                    html_content,
                                    re.X | re.S,
                                ):
                                    new_content += html_content[
                                        last_location : s_m.start()
                                    ]
                                    last_location = s_m.end()
                                    signature = s_m[0]
                                    sig_content = ""
                                    sig_location = 0
                                    # Within those signatures, find ill-defined default values
                                    for p_m in re.finditer(
                                        r"""<span\s+class="s2">
                                            &quot;(&lt;.*?)&quot;
                                            </span>
                                            (<span\s+class="p">,</span>)?""",
                                        signature,
                                        re.X | re.S,
                                    ):
                                        sig_content += signature[
                                            sig_location : p_m.start()
                                        ]
                                        # Style ill-defined default values in a comment
                                        comment = re.sub(
                                            r"&lt;(/)?(i|tt)&gt;", r"<\1\2>", p_m[1]
                                        )
                                        sig_content += f'<span class="kc">None</span>{p_m[2]}<span class="sd"> # {comment}</span>'
                                        sig_location = p_m.end()
                                    if sig_location:
                                        signature = (
                                            sig_content + signature[sig_location:]
                                        )
                                    new_content += signature
                                if last_location:
                                    html_content = (
                                        new_content + html_content[last_location:]
                                    )
                                # Properly style default values, in parameters description
                                # Fix issue with indexed and dynamic properties
                                new_content = ""
                                last_location = 0
                                # Find parameters type and default value
                                for p_m in re.finditer(
                                    r"""<tr\s+class="doc-section-item">
                                        \s+<td.*?td> # name
                                        \s+<td>\s+<code>\s*(.*?)\s*</code>\s*</td> # type
                                        \s+<td.*?td> # doc
                                        \s+<td>\s+<code>\s*(.*?)\s*</code>\s*</td> # default value
                                        \s+</tr>""",
                                    html_content,
                                    re.X | re.S,
                                ):
                                    p_type = p_m[1]
                                    if t_m := re.match(
                                        r"(dynamic|indexed)\((.*)", p_type
                                    ):
                                        p_type = f"{t_m[2]}<br/><small><i>{t_m[1]}</i></small>"
                                    # A property can be both dynamic and indexed
                                    if t_m := re.match(
                                        r"(dynamic|indexed)\((.*)", p_type
                                    ):
                                        p_type = f"{t_m[2]}<br/><small><i>{t_m[1]}</i></small>"
                                    p_def_value = re.sub(
                                        r"&\#39;(.*?)&\#39;", r"\1", p_m[2]
                                    )
                                    p_def_value = re.sub(
                                        r"&lt;(/)?(i|tt)&gt;", r"<\1\2>", p_def_value
                                    )
                                    new_content += (
                                        html_content[last_location : p_m.start(1)]
                                        + p_type
                                        + re.sub(
                                            r"(?<=<code>taipy-)\[element_type\](?=</code>)",
                                            element_type,
                                            html_content[p_m.end(1) : p_m.start(2)],
                                            re.X | re.S,
                                        )
                                        + p_def_value
                                    )
                                    last_location = p_m.end(2)
                                if last_location:
                                    html_content = (
                                        new_content + html_content[last_location:]
                                    )
                                # Remove "Bases" information
                                html_content = re.sub(
                                    r"<p\s+class=\"doc\s+doc-class-bases\">.*?</p>",
                                    "",
                                    html_content,
                                    flags=re.S,
                                )
                                # Add link to element documentation page
                                if m := re.search(
                                    r"<p>data-viselement:\s+(\w+)\s+<a\s+href=\"(.*)(?:\".*?</p>)",
                                    html_content,
                                ):
                                    html_content = (
                                        html_content[: m.start()]
                                        + f"""<div class="tp-ved"><a class="tp-btn tp-btn--alpha" href="{m[2]}">
                                        See full documentation and examples for this {m[1]}</a></div>"""
                                        + html_content[m.end() :]
                                    )

                    # Processing for visual element pages:
                    # - Remove <tt> from title
                    # - Add breadcrumbs to Taipy GUI's standard and scenario mgmt element pages
                    fn_match = re.search(
                        r"(/|\\)gui\1viselements\1(generic|corelements)\1(.*?)\1index.html",
                        filename,
                    )
                    element_category = None
                    package = None
                    if fn_match is not None:
                        package = fn_match[2]
                        if title_match := re.search(
                            r"<title><tt>(.*?)</tt> - Taipy</title>", html_content
                        ):
                            html_content = (
                                html_content[: title_match.start()]
                                + f"<title>{title_match.group(1)} - Taipy</title>"
                                + html_content[title_match.end() :]
                            )

                    if False:
                        # All this code was meant to inject breadcrumbs in the visual elements pages hierarchy to
                        # simplify navigation.
                        # With the reordering of the doc that happened just before this change, this seems not to
                        # be useful any longer.
                        # Keeping it anyway if we have a change of heart in the short term.

                        if category_match := re.search(
                            r"<!--\s+Category:\s+(\w+)\s+-->", html_content
                        ):
                            element_category = category_match[1]
                        elif re.match(r"^charts(/|\\).*$", fn_match[3]):
                            element_category = "chart"

                        if element_category:
                            # Insert breadcrumbs
                            ARTICLE_RE = re.compile(
                                r"(<div\s+class=\"md-content\".*?>)(\s*<article)"
                            )
                            if article_match := ARTICLE_RE.search(html_content):
                                repl = '\n<ul class="tp-bc">'
                                if package == "corelements":
                                    repl += (
                                        '<li><a href="../../../viselements"><b>Visual Elements</b></a></li>'
                                        '<li><a href="../../../../../refmans/gui/viselements/#scenario-and-data-management-controls">'
                                        "<b>Scenario management controls</b></a></li>"
                                    )
                                else:
                                    chart_part = (
                                        "../" if element_category == "chart" else ""
                                    )
                                    repl += f'<li><a href="{chart_part}../.."><b>Visual Elements</b></a></li>'
                                    if element_category == "blocks":
                                        repl += f'<li><a href="{chart_part}../..#block-elements"><b>Blocks</b></a></li>'
                                    else:
                                        repl += f'<li><a href="{chart_part}../..#generic-controls"><b>Generic controls</b></a></li>'
                                        if chart_part:
                                            repl += f'<li><a href="{chart_part}../../generic/chart"><b>Charts</b></a></li>'
                                repl += "</ul>"
                                html_content = (
                                    html_content[: article_match.start()]
                                    + article_match.group(1)
                                    + repl
                                    + article_match.group(2)
                                    + html_content[article_match.end() :]
                                )

                    # Handle title and header in packages documentation file
                    def code(s: str) -> str:
                        return f"<code><font size='+2'>{s}</font></code>"

                    fn_match = re.search(
                        r"refmans(/|\\)reference\1pkg_taipy\1index.html",
                        filename,
                    )
                    if (
                        fn_match is not None
                    ):  # The root 'taipy' package# The root 'taipy' package
                        html_content = re.sub(
                            r"(<h1>)taipy(</h1>)",
                            f"\\1{code('taipy')}\\2",
                            html_content,
                        )
                    fn_match = re.search(
                        r"refmans(/|\\)reference\1pkg_taipy(\..*)\1index.html",
                        filename,
                    )
                    if fn_match is not None:
                        pkg = fn_match[1]
                        sub_match = re.search(r"(\.\w+)(\..*)", pkg)
                        if sub_match is None:
                            html_content = re.sub(
                                r"(<title>)Index\s", f"\\1taipy{pkg} ", html_content
                            )
                            html_content = re.sub(
                                r"(<h1>)Index(</h1>)",
                                f"\\1{code('taipy'+pkg)}\\2",
                                html_content,
                            )
                            html_content = re.sub(
                                r"(<h1>){pkg}(</h1>)",
                                f"\\1{code('taipy'+pkg)}\\2",
                                html_content,
                            )
                        else:
                            html_content = re.sub(
                                f"(<title>)({sub_match[2]})\\s",
                                f"\\1taipy{sub_match[1]}\\2 ",
                                html_content,
                            )
                            html_content = re.sub(
                                f"(<h1>)(?:<code>){sub_match[2]}(?:</code>)(</h1>)",
                                f"\\1{code('taipy'+pkg)}\\2",
                                html_content,
                            )

                with open(filename, "w") as html_file:
                    html_file.write(html_content)
            # Replace path to doc in '.ipynb' files
            elif f.endswith(".ipynb"):
                filename = os.path.join(root, f)
                with open(filename) as ipynb_file:
                    try:
                        content = ipynb_file.read()
                    except Exception as e:
                        log.error(f"Couldn't read Notebook file {filename}")
                        raise e
                    (new_content, n) = re.subn(
                        "(?<=https://docs.taipy.io/en/)latest",
                        f"{env.conf['branch']}",
                        content,
                    )
                    if n > 0:
                        with open(filename, "w") as ipynb_file:
                            ipynb_file.write(new_content)
    if fixed_cross_refs:
        for dest in sorted(fixed_cross_refs.keys()):
            sources = ", ".join(sorted(fixed_cross_refs[dest]))
            log.info(f"FIXED cross-ref to '{dest}' from {sources}")


# ################################################################################
# Functions that are used in the postprocessing phase.
# I wish we could move them elsewhere, but couldn't figure out how
# ################################################################################
def process_data_source_attr(html: str, env):
    _DATASOURCE_RE = re.compile(r"(<(h\d+))\s+data-source=\"(.*?)\"(.*</\2>)")
    new_content = ""
    last_location = 0
    for m in _DATASOURCE_RE.finditer(html):
        ref = m.group(3)
        repo_m = re.search(r"^([\w\d]+):", ref)
        if repo_m:
            target = ref[repo_m.end() :]
            if target.startswith("doc/"):
                target = f"{repo_m.group(0)[:-1]}/{target[4:]}"
                ref = f"https://github.com/Avaiga/taipy/blob/{env.conf['branch']}/doc/{target}"
            else:
                logging.warning("Suspicious data-source attribute: {m.group(0)}")
                ref = f"https://github.com/Avaiga/taipy-{repo_m.group(0)[:-1]}/blob/{env.conf['branch']}/{target}"
        new_content += (
            html[last_location : m.start()]
            + f"{m.group(1)}{m.group(4)}"
            + '\n<div class="tp-gcs">'
            + f'<a class="tp-btn tp-btn--accent" href="{ref}" target="blank">'
            + "See the entire code for this example</a></div>"
        )
        last_location = m.end()
    if last_location:
        return (True, new_content + html[last_location:])
    else:
        return (False, None)


def process_links_to_github(html: str, env):
    _LINK_RE = re.compile(
        r"(?<=href=\"https://github.com/Avaiga/)(taipy/tree/)\[BRANCH\](.*?\")"
    )
    new_content = ""
    last_location = 0
    for m in _LINK_RE.finditer(html):
        new_content += (
            html[last_location : m.start()]
            + m.group(1)
            + env.conf["branch"]
            + m.group(2)
        )
        last_location = m.end()
    if last_location:
        return (True, new_content + html[last_location:])
    else:
        return (False, None)
