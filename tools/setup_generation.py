# ------------------------------------------------------------------------
# setup_generation.py
#   Prepares all files before running MkDocs to generate the complete
#   Taipy documentation set.
#
# This setup is two-fold:
#   - Generate the Markdown files for all visual elements.
#     This includes the Update of the Table of Contents for both the controls
#     and the blocks document pages.
#
#     For each visual element, this script combines its property list and core
#     documentation (located in [VELEMENTS_SOURCE_PATH]), and generates full
#     Markdown files in [VELEMENTS_DIR_PATH]. All these files ultimately get
#     integrated in the global dos set.
#
#     The skeleton documentation files [GUI_DOC_PATH]/user_[controls|blocks].md_template
#     are also completed with generated table of contents.
#
#   - Generate the entries for every documented class, method, and function.
#     This scripts browses the root package (ROOT_PACKAGE) and builds a
#     documentation file for every package and every class it finds.
#     It finally updates the top navigation bar content (in mkdocs.yml) to
#     reflect the root package structure.
# ------------------------------------------------------------------------
import os
import warnings
import re
import shutil
import pandas as pd
import math
import json
import importlib.util
from inspect import isclass, isfunction, ismodule
from pathlib import Path
import time

ROOT_PACKAGE      = "taipy"
MODULE_EXTENSIONS = ".py"

# Assuming that this script is located in <taipy-doc>/tools
tools_dir = os.path.dirname(__file__).replace("\\","/")
root_dir = os.path.dirname(tools_dir)

GUI_DOC_PATH = root_dir + "/docs/manuals/gui/"
VELEMENTS_DIR_PATH = root_dir + "/docs/manuals/gui/viselements"
VELEMENTS_SOURCE_PATH = root_dir + "/gui/doc"

REFERENCE_DIR_PATH = root_dir + "/docs/manuals/reference"
XREFS_PATH = root_dir + "/docs/manuals/xrefs"
MKDOCS_YML_TEMPLATE_PATH = root_dir + "/mkdocs.yml_template"
MKDOCS_YML_PATH = root_dir + "/mkdocs.yml"

# Check that the visual elements documentation is available
if not os.path.isdir(VELEMENTS_SOURCE_PATH):
    raise SystemExit(f"FATAL - Visual elements documentation not found in {VELEMENTS_SOURCE_PATH}")

# Check that the source files are available
if not os.path.exists(f"{root_dir}/{ROOT_PACKAGE}"):
    raise SystemError(f"FATAL - Could not not find root pacakge in {root_dir}/{ROOT_PACKAGE}")

# Read mkdocs yml template file
mkdocs_yml_content = None
with open(MKDOCS_YML_TEMPLATE_PATH) as mkdocs_yml_file:
    mkdocs_yml_content = mkdocs_yml_file.read()
if not mkdocs_yml_content:
    raise SystemError("FATAL - Could not read mkdocs configuration file at {MKDOCS_YML_TEMPLATE_PATH}")

# Temporarily move top package to 'tools' for this script to find it.
# MkDocs needs it at the root level so we will have to move it back.
shutil.move(f"{root_dir}/{ROOT_PACKAGE}", f"{tools_dir}/{ROOT_PACKAGE}")

# This moves back the package directory to 'root_dir'.
# It must be called from now on no matter why this program exits.
def restore_top_package_location():
    # Move top package back to the root level for MkDocs.
    shutil.move(f"{tools_dir}/{ROOT_PACKAGE}", f"{root_dir}/{ROOT_PACKAGE}")

# ------------------------------------------------------------------------
# Step 1
#   Generating the Visual Elements documentation
# ------------------------------------------------------------------------
print("Step 1/2: Generating Visual Elements documentation")

def read_skeleton(name):
    content = ""
    with open(os.path.join(GUI_DOC_PATH, "user_" + name + ".md_template")) as skeleton_file:
        content = skeleton_file.read()
    if not content:
        restore_top_package_location()
        raise SystemExit(f"FATAL - Could not read {name} markdown template")
    return content

controls_md_template = read_skeleton("controls")
blocks_md_template = read_skeleton("blocks")

controls_list = ["text", "button", "input", "number", "slider", "toggle", "date", "chart", "file_download", "file_selector", "image",
                 "indicator", "menu", "navbar", "selector", "status", "table", "dialog", "tree"]
blocks_list = ["part", "expandable", "layout", "pane"]
# -----------------------------------------------------------------------------
# Read all element properties, including parent elements that are not
# actual visual elements (shared, lovComp...)
# -----------------------------------------------------------------------------
element_properties = {}
element_documentation = {}

for current_file in os.listdir(VELEMENTS_SOURCE_PATH):
    def read_properties(path_name, element_name):
        try:
            df = pd.read_csv(path_name, encoding='utf-8')
        except Exception as e:
            raise RuntimeError(f"{path_name}: {e}")
        properties = []
        # Row fields: name, type, default_value, doc
        for row in list(df.to_records(index=False)):
            if row[0][0] == ">":  # Inherits?
                parent = row[0][1:]
                parent_props = element_properties.get(parent)
                if parent_props is None:
                    parent_file = parent + ".csv"
                    parent_path_name = os.path.join(VELEMENTS_SOURCE_PATH, parent_file)
                    if not os.path.exists(parent_path_name):
                        restore_top_package_location()
                        raise ValueError(f"FATAL - No csv file for '{parent}', inherited by '{element_name}'")
                    parent_props = read_properties(parent_path_name, parent)
                properties += parent_props
            else:
                properties.append(row)
        default_property_name = None
        for i, props in enumerate(properties):
            # Check if multiple default properties
            if props[0][0] == "*":  # Default property?
                name = props[0][1:]
                if default_property_name and name != default_property_name:
                    warnings.warn(
                        f"Property '{name}' in '{element_name}': default property already defined as {default_property_name}")
                default_property_name = name
            # Fix Boolean default property values
            if str(props[2]).lower() == "false":
                props = (props[0], props[1], "False", props[3])
                properties[i] = props
            elif str(props[2]).lower() == "true":
                props = (props[0], props[1], "True", props[3])
                properties[i] = props
            elif str(props[2]) == "nan":  # Empty cell in CSV - Pandas parsing?
                props = (props[0], props[1], "<i>Mandatory</i>", props[3])
                properties[i] = props
            # Drop inherited properties
            if props[1] == ">":  # Inherited property?
                try:
                    inherited_prop_index = [p[0] for p in properties[i + 1:]].index(props[0])
                    properties[i] = properties[i + 1 + inherited_prop_index]
                    properties.pop(i + 1 + inherited_prop_index)
                except:
                    restore_top_package_location()
                    raise ValueError(f"No inherited property '{props[0]}' in element '{element_name}'")
        if not default_property_name and (element_name in controls_list + blocks_list):
            restore_top_package_location()
            raise ValueError(f"Element '{element_name}' has no defined default property")
        element_properties[element_name] = properties
        return properties

    element_name = os.path.basename(current_file)
    if not element_name in element_properties:
        path_name = os.path.join(VELEMENTS_SOURCE_PATH, current_file)
        element_name, current_file_ext = os.path.splitext(element_name)
        if current_file_ext == ".csv":
            read_properties(path_name, element_name)
        elif current_file_ext == ".md":
            with open(path_name, "r") as doc_file:
                element_documentation[element_name] = doc_file.read()

# Create VELEMENTS_DIR_PATH directory if necessary
if not os.path.exists(VELEMENTS_DIR_PATH):
    os.mkdir(VELEMENTS_DIR_PATH)

FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
FIRST_HEADER2_RE = re.compile(r"(^.*?)(\n##\s+)", re.MULTILINE | re.DOTALL)


def generate_element_doc(element_name: str, toc):
    """
    Returns the entry for the Table of Contents that is inserted
    in the global Visual Elements doc page.
    """
    properties = element_properties[element_name]
    documentation = element_documentation[element_name]
    # Retrieve first paragraph from element documentation
    match = FIRST_PARA_RE.match(documentation)
    if not match:
        restore_top_package_location()
        raise ValueError(f"Couldn't locate first paragraph in documentation for element '{element_name}'")
    first_documentation_paragraph = match.group(1)

    # Build properties table
    properties_table = """
## Properties\n\n
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
"""
    STAR = "(&#9733;)"
    default_property_name = None
    for name, type, default_value, doc in properties:
        if name[0] == "*":
            default_property_name = name[1:]
            full_name = f"<code id=\"p-{default_property_name}\"><u><bold>{default_property_name}</bold></u></code><sup><a href=\"#dv\">{STAR}</a></sup>"
        else:
            full_name = f"<code id=\"p-{name}\">{name}</code>"
        properties_table += ("<tr>\n"
                             + f"<td nowrap>{full_name}</td>\n"
                             + f"<td>{type}</td>\n"
                             + f"<td nowrap>{default_value}</td>\n"
                             + f"<td><p>{doc}</p></td>\n"
                             + "</tr>\n")
    properties_table += "  </tbody>\n</table>\n\n"
    if default_property_name:
        properties_table += (f"<p><sup id=\"dv\">{STAR}</sup>"
                             + f"<a href=\"#p-{default_property_name}\" title=\"Jump to the default property documentation.\">"
                             + f"<code>{default_property_name}</code></a>"
                             + " is the default property for this visual element.</p>\n")

    # Insert title and properties in element documentation
    match = FIRST_HEADER2_RE.match(documentation)
    if not match:
        restore_top_package_location()
        raise ValueError(f"Couldn't locate first header2 in documentation for element '{element_name}'")
    output_path = os.path.join(VELEMENTS_DIR_PATH, element_name + ".md")
    with open(output_path, "w") as output_file:
        output_file.write("---\nhide:\n  - navigation\n---\n\n"
                          + f"# <tt>{element_name}</tt>\n\n"
                          + match.group(1)
                          + properties_table
                          + match.group(2) + documentation[match.end():])
    e = element_name  # Shortcut
    return (f"<a class=\"tp-ve-card\" href=\"../viselements/{e}/\">\n"
            + f"<div>{e}</div>\n"
            + f"<img class=\"tp-ve-l\" src=\"../viselements/{e}-l.png\"/>\n"
            + f"<img class=\"tp-ve-lh\" src=\"../viselements/{e}-lh.png\"/>\n"
            + f"<img class=\"tp-ve-d\" src=\"../viselements/{e}-d.png\"/>\n"
            + f"<img class=\"tp-ve-dh\" src=\"../viselements/{e}-dh.png\"/>\n"
            + f"<p>{first_documentation_paragraph}</p>\n"
            + "</a>\n")
    # If you want a simple list, use
    # f"<li><a href=\"../viselements/{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
    # The toc header and footer must then be "<ui>" and "</ul>" respectively.


# Generate controls doc page
toc = "<div class=\"tp-ve-cards\">\n"
for name in controls_list:
    toc += generate_element_doc(name, toc)
toc += "</div>\n"
with open(os.path.join(GUI_DOC_PATH, "user_controls.md"), "w") as file:
    file.write(controls_md_template.replace("[TOC]", toc))

# Generate blocks doc page
toc = "<div class=\"tp-ve-cards\">\n"
for name in blocks_list:
    toc += generate_element_doc(name, toc)
toc += "</div>\n"
with open(os.path.join(GUI_DOC_PATH, "user_blocks.md"), "w") as file:
    file.write(blocks_md_template.replace("[TOC]", toc))

# ------------------------------------------------------------------------
# Step 2
#   Generating the Reference Manual
# ------------------------------------------------------------------------
print("Step 2/2: Generating the Reference Manual pages")

# Create empty REFERENCE_DIR_PATH directory
if os.path.exists(REFERENCE_DIR_PATH):
    shutil.rmtree(REFERENCE_DIR_PATH)
os.mkdir(REFERENCE_DIR_PATH)

CLASS_ID = "C"
FUNCTION_ID = "F"
FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\n|$)", re.DOTALL)
REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

entry_to_package  = {}
potential_types = set()
def read_module(module):
    print(f"FLE - ENTERING read_module({module})")
    if not module.__name__.startswith(ROOT_PACKAGE):
        return
    print(f"     -> dir({module})")
    for entry in dir(module):
        # Private?
        if entry.startswith("_"):
            continue
        e = getattr(module, entry)
        if hasattr(e, '__class__') and e.__class__.__name__.startswith("_"):
            continue
        if hasattr(e, '__module__') and e.__module__:
            # Type alias?
            if e.__module__ == 'typing' and hasattr(e, '__name__'):
                if not e.__name__ in potential_types:
                    print(f"INFO - {e.__name__} might be a type alias in {module.__name__}", flush=True)
                    potential_types.add(e.__name__)
            # Not in our focus package?
            if not e.__module__.startswith(ROOT_PACKAGE):
                continue
        print(f"... entry {entry}")
        # Not a function or a class?
        entry_type = None
        if isclass(e):
            print("         is a CLASS")
            entry_type = CLASS_ID
        elif isfunction(e):
            print("         is a FUNCTION")
            entry_type = FUNCTION_ID
        elif ismodule(e):
            print("         is a MODULE")
            read_module(e)
        if not entry_type:
            continue
        # Add to all entries
        doc = e.__doc__
        if doc:
            first_line = FIRST_DOC_LINE_RE.match(doc.strip())
            if first_line:
                doc = REMOVE_LINE_SKIPS_RE.subn(" ", first_line.group(0))[0].strip()
            else:
                print(f"WARNING - Couldn't extract doc summary for {e.__name__} in {e.__module__}", flush=True)
        key = (e.__module__, entry, entry_type, doc)
        if key in entry_to_package:
            if e.__module__ != module.__name__:
                # Keep the top-most package
                if e.__module__.startswith(module.__name__) and entry_to_package[key].startswith(module.__name__):
                    entry_to_package[key]  = module.__name__
        else:
            if doc is None:
                print(f"WARNING - {e.__name__} [in {e.__module__}] has no doc", flush=True)
            entry_to_package[key] = module.__name__
            print(f"FLE - entry_to_package[{key}]={module.__name__}")
    print(f"FLE - EXITING read_module({module})")


read_module(__import__(ROOT_PACKAGE))

restore_top_package_location()

# Group entries by package
package_to_entries = {}
for entry, package in entry_to_package.items():
    print(f"FLE - Entry {entry} -> {package}")
    if package in package_to_entries:
        package_to_entries[package].append(entry)
    else:
        package_to_entries[package] = [entry]

# Generate all Reference manual pages and update navigation
navigation = ""
xrefs = {}
for package in sorted(package_to_entries.keys()):
    functions = []
    classes = []
    for entry in package_to_entries[package]:
        if entry[2] == CLASS_ID:
            classes.append(entry)
        elif entry[2] == FUNCTION_ID:
            functions.append(entry)
        else:
            raise SystemError("Invalid entry type '{entry[2]}' for {entry[0]}.{entry[1]}")
    if not classes and not functions:
        print(f"Skipping package {package}: no documented elements")
        continue
    navigation += f"    - {package}: manuals/reference/pkg_{package}.md\n"
    package_output_path = os.path.join(REFERENCE_DIR_PATH, f"pkg_{package}.md")

    def generate_entries(entries, package, type, package_output_file):
        for entry in entries:
            name = entry[1]
            package_output_file.write(f"   - [`{name}"
                                    + f"{'()' if type == FUNCTION_ID else ''}`]({package}.{name}.md)"
                                    + f"{': '+entry[3] if entry[3] else ' - NOT DOCUMENTED'}\n")
            output_path = os.path.join(REFERENCE_DIR_PATH, f"{package}.{name}.md")
            print(f"INFO - Generating entry in {output_path} [{type}]")
            with open(output_path, "w") as output_file:
                output_file.write("---\nhide:\n  - navigation\n---\n\n"
                                + f"::: {package}.{name}\n")
            if name in xrefs:
                print(f"ERROR - {'Function' if type == FUNCTION_ID else 'Class'} {name} already declared in {xrefs[name]}")
            xrefs[name] = (package, entry[0])

    print(f"INFO - Generating package in {package_output_path}")
    with open(package_output_path, "w") as package_output_file:
        package_output_file.write(f"## Package: {package}\n\n")
        if functions:
            package_output_file.write(f"### Functions\n\n")
            generate_entries(functions, package, FUNCTION_ID, package_output_file)
        if classes:
            package_output_file.write(f"### Classes\n\n")
            generate_entries(classes, package, CLASS_ID, package_output_file)
with open(XREFS_PATH, "w") as xrefs_output_file:
  xrefs_output_file.write(json.dumps(xrefs))

# Update mkdocs.yml
mkdocs_yml_content = re.sub(r"^\s*\[REFERENCE_CONTENT\]\s*$",
                            navigation,
                            mkdocs_yml_content,
                            flags = re.MULTILINE)
with open(MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
    mkdocs_yml_file.write(mkdocs_yml_content)
