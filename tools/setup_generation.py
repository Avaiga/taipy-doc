# ------------------------------------------------------------------------
# setup_generation.py
#   Prepares all files before running MkDocs to generate the complete
#   Taipy documentation set.
#
# This setup is multi-fold:
#   - Step 1: Generate the Markdown files for all visual elements.
#     This includes the Update of the Table of Contents for both the controls
#     and the blocks document pages.
#
#     For each visual element, this script combines its property list and core
#     documentation (located in [VISELEMENTS_SRC_PATH]), and generates full
#     Markdown files in [VISELEMENTS_DIR_PATH]. All these files ultimately get
#     integrated in the global dos set.
#
#     The skeleton documentation files [GUI_DOC_PATH]/[controls|blocks].md_template
#     are also completed with generated table of contents.
#
#   - Step 2: Generate the entries for every documented class, method, and function.
#     This scripts browses the root package (ROOT_PACKAGE) and builds a
#     documentation file for every package and every class it finds.
#     It finally updates the top navigation bar content (in mkdocs.yml) to
#     reflect the root package structure.
#
#   - Step 3: Generating the REST API documentation
#     A Taipy REST server is created and the API is queries dynamically.
#     Then documentation pages are generated from the retrieved structure.
#
#   - Step 4: Generating the GUI Extension API documentation
#     The Reference Manual pages for the Taipy GUI JavaScript extension module
#     is generated using the typedoc tools, directly from the JavaScript
#     source files.
#    
#   - Step 5: Generating the Getting Started
#     Files are listed and sorted after being copied from the taipy-getting-started
#     repository.
# ------------------------------------------------------------------------
from typing import Dict, Any
import glob
import json
import os
import re
import shutil
import warnings
from datetime import datetime
from inspect import isclass, isfunction, ismodule
from pathlib import Path

import pandas as pd

ROOT_PACKAGE = "taipy"
MODULE_EXTENSIONS = ".py"
PACKAGE_GROUP = [ "taipy.config", "taipy.core", "taipy.gui", "taipy.rest", "taipy.auth", "taipy.enterprise" ]

# Assuming that this script is located in <taipy-doc>/tools
tools_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
root_dir = os.path.dirname(tools_dir)

GUI_DOC_PATH = root_dir + "/docs/manuals/gui/"
VISELEMENTS_SRC_PATH = root_dir + "/gui/doc"
VISELEMENTS_DIR_PATH = root_dir + "/docs/manuals/gui/viselements"
REST_REF_DIR_PATH = root_dir + "/docs/manuals/reference_rest"

ENTERPRISE_BANNER = """!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

"""

# (item_pattern, destination_package)
# or ([item_pattern...], destination_package)
FORCE_PACKAGE = [
    ("typing.*", "taipy.core"),
    ("taipy.gui.*.(Gui|State|Markdown|Page)", "taipy.gui"),
    (["taipy.core.cycle.cycle.Cycle",
      "taipy.core.data.data_node.DataNode",
      "taipy.core.common.frequency.Frequency",
      "taipy.core.job.job.Job",
      "taipy.core.pipeline.pipeline.Pipeline",
      "taipy.core.scenario.scenario.Scenario",
      "taipy.core.common.scope.Scope",
      "taipy.core.job.status.Status",
      "taipy.core.task.task.Task",
      "taipy.core.taipy.clean_all_entities",
      "taipy.core.taipy.cancel_job",
      "taipy.core.taipy.compare_scenarios",
      "taipy.core.taipy.create_pipeline",
      "taipy.core.taipy.create_scenario",
      "taipy.core.taipy.delete",
      "taipy.core.taipy.delete_job",
      "taipy.core.taipy.delete_jobs",
      "taipy.core.taipy.get",
      "taipy.core.taipy.get_cycles",
      "taipy.core.taipy.get_data_nodes",
      "taipy.core.taipy.get_jobs",
      "taipy.core.taipy.get_latest_job",
      "taipy.core.taipy.get_pipelines",
      "taipy.core.taipy.get_primary",
      "taipy.core.taipy.get_primary_scenarios",
      "taipy.core.taipy.get_scenarios",
      "taipy.core.taipy.get_tasks",
      "taipy.core.taipy.set",
      "taipy.core.taipy.set_primary",
      "taipy.core.taipy.submit",
      "taipy.core.taipy.subscribe_pipeline",
      "taipy.core.taipy.subscribe_scenario",
      "taipy.core.taipy.tag",
      "taipy.core.taipy.unsubscribe_pipeline",
      "taipy.core.taipy.unsubscribe_scenario",
      "taipy.core.taipy.untag"], "taipy.core"),
    ("taipy.core.data.*.*DataNode", "taipy.core.data"),
    ("taipy.rest.rest.Rest", "taipy.rest")
]

# Entries that should be hidden for the time being
HIDDEN_ENTRIES = ["Decimator", "get_context_id", "invoke_state_callback"]

REFERENCE_REL_PATH = "manuals/reference"
REFERENCE_DIR_PATH = root_dir + "/docs/" + REFERENCE_REL_PATH
XREFS_PATH = root_dir + "/docs/manuals/xrefs"
MKDOCS_YML_TEMPLATE_PATH = root_dir + "/mkdocs.yml_template"
MKDOCS_YML_PATH = root_dir + "/mkdocs.yml"

# Check that the visual elements' documentation is available
if not os.path.isdir(VISELEMENTS_SRC_PATH):
    raise SystemExit(f"FATAL - Visual elements documentation not found in {VISELEMENTS_SRC_PATH}")

# Check that the source files are available
if not os.path.exists(f"{root_dir}/{ROOT_PACKAGE}"):
    # Result of a fail previous run?
    if os.path.exists(f"{tools_dir}/{ROOT_PACKAGE}"):
        shutil.move(f"{tools_dir}/{ROOT_PACKAGE}", f"{root_dir}/{ROOT_PACKAGE}")
    else:
        raise SystemError(f"FATAL - Could not find root package in {root_dir}/{ROOT_PACKAGE}")

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
print("Step 1/5: Generating Visual Elements documentation", flush=True)


def read_skeleton(name):
    content = ""
    with open(os.path.join(GUI_DOC_PATH, name + ".md_template")) as skeleton_file:
        content = skeleton_file.read()
    if not content:
        restore_top_package_location()
        raise SystemExit(f"FATAL - Could not read {name} markdown template")
    return content


controls_md_template = read_skeleton("controls")
blocks_md_template = read_skeleton("blocks")

controls_list = ["text", "button", "input", "number", "slider", "toggle", "date", "chart", "file_download",
                 "file_selector", "image",
                 "indicator", "menu", "navbar", "selector", "status", "table", "dialog", "tree"]
blocks_list = ["part", "expandable", "layout", "pane"]
# -----------------------------------------------------------------------------
# Read all element properties, including parent elements that are not
# actual visual elements (shared, lovComp...)
# -----------------------------------------------------------------------------
element_properties = {}
element_documentation = {}
INHERITED_PROP = 1<<0
DEFAULT_PROP   = 1<<1
MANDATORY_PROP = 1<<2
property_prefixes = {
    ">": INHERITED_PROP,
    "*": DEFAULT_PROP,
    "!": MANDATORY_PROP
}
for current_file in os.listdir(VISELEMENTS_SRC_PATH):
    def read_properties(path_name, element_name):
        try:
            df = pd.read_csv(path_name, encoding='utf-8')
        except Exception as e:
            raise RuntimeError(f"{path_name}: {e}")
        properties = []
        # Row fields: name, type, default_value, doc
        for row in list(df.to_records(index=False)):
            prop_flags = 0
            prop_name = row[0]
            while prop_name[0] in property_prefixes:
                prop_flags |= property_prefixes.get(prop_name[0])
                prop_name = prop_name[1:]
            if prop_flags & INHERITED_PROP:  # Inherits?
                parent_props = element_properties.get(prop_name)
                if parent_props is None:
                    parent_file = prop_name + ".csv"
                    parent_path_name = os.path.join(VISELEMENTS_SRC_PATH, parent_file)
                    if not os.path.exists(parent_path_name):
                        restore_top_package_location()
                        raise ValueError(f"FATAL - No csv file for '{prop_name}', inherited by '{element_name}'")
                    parent_props = read_properties(parent_path_name, prop_name)
                # Merge inherited properties
                for parent_prop in parent_props:
                    try:
                        prop_index = [p[1] for p in properties].index(parent_prop[1])
                        p = list(properties[prop_index])
                        if p[2] == ">":
                            p[2] = parent_prop[2]
                            print(f"WARNING: Element {element_name}: legacy '>' in '{p[1]}''s Type")
                        # Testing for equality detects NaN
                        properties[prop_index] = (p[0], p[1],
                                                  p[2] if p[2] == p[2] else parent_prop[2],
                                                  p[3] if p[3] == p[3] else parent_prop[3],
                                                  p[4] if p[4] == p[4] else parent_prop[4])
                    except:
                        properties.append(parent_prop)
            else:
                row[0] = prop_name
                row = (prop_flags, prop_name, *row.tolist()[1:])
                properties.append(row)
        default_property_name = None
        for i, props in enumerate(properties):
            # TODO: Remove properties that have an hidden type
            # props = (flags, name, type, default value,description)
            if props[0] & DEFAULT_PROP:  # Default property?
                name = props[1]
                if default_property_name and name != default_property_name:
                    warnings.warn(
                        f"Property '{name}' in '{element_name}': default property already defined as {default_property_name}")
                default_property_name = name
            # Fix Boolean default property values
            if str(props[3]).lower() == "false":
                properties[i] = (props[0], props[1], props[2], "False", props[4])
            elif str(props[3]).lower() == "true":
                properties[i] = (props[0], props[1], props[2], "True", props[4])
            elif props[3] != props[3]:  # Empty cell in CSV - Pandas parsing
                default_value = "<i>Mandatory</i>" if props[0] & MANDATORY_PROP else ""
                properties[i] = (props[0], props[1], props[2], default_value, props[4])
        if not default_property_name and (element_name in controls_list + blocks_list):
            restore_top_package_location()
            raise ValueError(f"Element '{element_name}' has no defined default property")
        element_properties[element_name] = properties
        return properties


    path_name = os.path.join(VISELEMENTS_SRC_PATH, current_file)
    element_name = os.path.basename(current_file)
    element_name, current_file_ext = os.path.splitext(element_name)
    if current_file_ext == ".csv":
        if not element_name in element_properties:
            read_properties(path_name, element_name)
    elif current_file_ext == ".md":
        with open(path_name, "r") as doc_file:
            element_documentation[element_name] = doc_file.read()

# Create VISELEMS_DIR_PATH directory if necessary
if not os.path.exists(VISELEMENTS_DIR_PATH):
    os.mkdir(VISELEMENTS_DIR_PATH)

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
    for flags, name, type, default_value, doc in properties:
        if flags & DEFAULT_PROP:
            default_property_name = name
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
    output_path = os.path.join(VISELEMENTS_DIR_PATH, element_name + ".md")
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
with open(os.path.join(GUI_DOC_PATH, "controls.md"), "w") as file:
    file.write(controls_md_template.replace("[TOC]", toc))

# Generate blocks doc page
toc = "<div class=\"tp-ve-cards\">\n"
for name in blocks_list:
    toc += generate_element_doc(name, toc)
toc += "</div>\n"
with open(os.path.join(GUI_DOC_PATH, "blocks.md"), "w") as file:
    file.write(blocks_md_template.replace("[TOC]", toc))

# ------------------------------------------------------------------------
# Step 2
#   Generating the Reference Manual
# ------------------------------------------------------------------------
print("Step 2/5: Generating the Reference Manual pages", flush=True)

# Create empty REFERENCE_DIR_PATH directory
if os.path.exists(REFERENCE_DIR_PATH):
    shutil.rmtree(REFERENCE_DIR_PATH)
os.mkdir(REFERENCE_DIR_PATH)

CLASS_ID = "C"
FUNCTION_ID = "F"
TYPE_ID = "T"
FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\s*\n|$)", re.DOTALL)
REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

# Entries:
#   full_entry_name ->
#     name
#     module (source)
#     type
#     doc
#     packages
entries: Dict[str, Dict[str, Any]] = {}
entry_to_package = {}
module_doc = {}


def read_module(module):
    if not module.__name__.startswith(ROOT_PACKAGE):
        return
    for entry in dir(module):
        # Private?
        if entry.startswith("_"):
            continue
        e = getattr(module, entry)
        if hasattr(e, '__class__') and e.__class__.__name__.startswith("_"):
            continue
        entry_type = None
        if hasattr(e, '__module__') and e.__module__:
            # Type alias?
            if e.__module__ == 'typing' and hasattr(e, '__name__'):
                # Manually remove class from 'typing'
                if e.__name__ == "NewType":
                    continue
                entry_type = TYPE_ID
            # Not in our focus package?
            elif not e.__module__.startswith(ROOT_PACKAGE):
                continue
        # Remove hidden entries
        if entry in HIDDEN_ENTRIES:
            continue
        # Not a function or a class?
        if not entry_type:
            if isclass(e):
                entry_type = CLASS_ID
            elif isfunction(e):
                entry_type = FUNCTION_ID
            elif ismodule(e):
                module_doc[e.__name__] = e.__doc__
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
        full_name = f"{e.__module__}.{entry}"
        if entry_info := entries.get(full_name):
            packages = entry_info["packages"]
            new_packages = []
            add_package = None
            # Current module is prefix to known packages?
            for package in packages:
                if package.startswith(module.__name__):
                    add_package = module.__name__
                else:
                    new_packages.append(package)
            if add_package:
                new_packages.insert(0, add_package)
                packages = new_packages
            # Any known package is prefix to module?
            add_package = module.__name__
            for package in packages:
                if module.__name__.startswith(package):
                    add_package = None
                    break
            if add_package:
                new_packages.append(add_package)
            entry_info["packages"] = new_packages
        else:
            if doc is None:
                print(f"WARNING - {e.__name__} [in {e.__module__}] has no doc", flush=True)
            entries[full_name] = {
                "name": entry,
                "module": e.__module__,
                "type": entry_type,
                "doc": doc,
                "packages": [module.__name__],
            }

read_module(__import__(ROOT_PACKAGE))

FORCE_PACKAGE_REGEXPS = []
def convert_to_pattern(input, dest):
    pattern = "^" + input.replace(".", "\\.").replace("*", ".*") + "$"
    FORCE_PACKAGE_REGEXPS.append((re.compile(pattern), dest))
for force_package in FORCE_PACKAGE:
    if isinstance(force_package[0], list):
        for fp in force_package[0]:
            convert_to_pattern(fp, force_package[1])
    else:
        convert_to_pattern(force_package[0], force_package[1])
for entry, entry_info in entries.items():
    # Entries with multiple packages
    # if len(entry_info["packages"]) != 1:
    #     print(f"MULTIPLE PACKAGES - Entry {entry}")
    for force_package in FORCE_PACKAGE_REGEXPS:
        if force_package[0].match(entry):
            entry_info["force_package"] = force_package[1]
            break

# Group entries by package
package_to_entries = {}
for entry, info in entries.items():
    package = info.get("force_package", info["packages"][0])
    if package in package_to_entries:
        package_to_entries[package].append(info)
    else:
        package_to_entries[package] = [info]

# Generate all Reference manual pages and update navigation
navigation = ""
xrefs = {}
package_group = None
for package in sorted(package_to_entries.keys()):
    functions = []
    classes = []
    types = []
    for entry_info in package_to_entries[package]:
        if entry_info["type"] == CLASS_ID:
            classes.append(entry_info)
        elif entry_info["type"] == FUNCTION_ID:
            functions.append(entry_info)
        elif entry_info["type"] == TYPE_ID:
            types.append(entry_info)
        else:
            raise SystemError("FATAL - Invalid entry type '{entry_info['type']}' for {entry_info['module']}.{entry_info['name']}")
    if not classes and not functions and not types:
        print(f"INFO - Skipping package {package}: no documented elements")
        continue
    if package in PACKAGE_GROUP:
        package_group = package
        package_path = f"{REFERENCE_DIR_PATH}/pkg_{package}"
        os.mkdir(package_path)
        package_output_path = os.path.join(package_path, "index.md")
        navigation += (" " * 4 + f"- {package}:\n"
                     + " " * 6 + f"- {REFERENCE_REL_PATH}/pkg_{package}/index.md\n")
    else:
        new_package_group = None
        for p in PACKAGE_GROUP:
            if package.startswith(p + "."):
                new_package_group = p
                break
        if new_package_group != package_group:
            if not new_package_group:
                raise SystemExit(f"FATAL - Unknown package '{new_package_group}' for package '{package}' (renamed from '{package_group}')")
            package_group = new_package_group
            navigation += (" " * 4 + f"- {package_group}:\n")
        navigation += (" " * (6 if package_group else 4)
                    + f"- {package}: manuals/reference/pkg_{package}.md\n")
        package_output_path = os.path.join(REFERENCE_DIR_PATH, f"pkg_{package}.md")


    def generate_entries(entry_infos, package, type, package_output_file, in_group):
        in_group = "../" if in_group else ""
        for entry_info in sorted(entry_infos, key=lambda i: i["name"]):
            name = entry_info["name"]
            force_package = entry_info.get("force_package", package)
            package_output_file.write(f"   - [`{name}"
                                      + f"{'()' if type == FUNCTION_ID else ''}`]({in_group}{force_package}.{name}.md)"
                                      + f"{': ' + entry_info['doc'] if entry_info['doc'] else ' - NOT DOCUMENTED'}\n")
            output_path = os.path.join(REFERENCE_DIR_PATH, f"{force_package}.{name}.md")
            with open(output_path, "w") as output_file:
                output_file.write("---\nhide:\n  - navigation\n---\n\n"
                                  + f"::: {force_package}.{name}\n")
            if xref := xrefs.get(name):
                print(
                    f"ERROR - {'Function' if type == FUNCTION_ID else 'Class'} {name} already declared as {xref[0]}.{xref[1]}")
            xrefs[name] = [force_package, entry_info["module"], entry_info["packages"]]


    with open(package_output_path, "w") as package_output_file:
        package_output_file.write(f"---\ntitle: \"{package}\" package\n---\n\n")
        package_output_file.write(f"# Package: `{package}`\n\n")
        if package in module_doc and module_doc[package]:
            package_output_file.write(module_doc[package])
        package_grouped = package == package_group
        if types:
            package_output_file.write(f"## Types\n\n")
            for type in types:
                name = type["name"]
                package_output_file.write(f"   - `{name}`"
                                        + f"{': ' + type.get('doc', ' - NOT DOCUMENTED')}\n")
                if name in xrefs:
                    print(f"WARNING - Type {package}.{name} already declared in {xrefs[name]}")
                xrefs[name] = [package, entry_info["module"], entry_info.get("final_package")]
        if functions:
            package_output_file.write(f"## Functions\n\n")
            generate_entries(functions, package, FUNCTION_ID, package_output_file, package_grouped)
        if classes:
            package_output_file.write(f"## Classes\n\n")
            generate_entries(classes, package, CLASS_ID, package_output_file, package_grouped)

# Filter out packages that are the exposed pagckage and appear in the packages list
for entry, entry_desc in xrefs.items():
    package = entry_desc[0]
    if entry_desc[2]:
        entry_desc[2] = [p for p in entry_desc[2] if p != package]
with open(XREFS_PATH, "w") as xrefs_output_file:
    xrefs_output_file.write(json.dumps(xrefs))


# ------------------------------------------------------------------------
# Step 3
#   Generating the REST API documentation
# ------------------------------------------------------------------------
print("Step 3/5: Generating the REST API Reference Manual pages", flush=True)
from taipy.rest.app import create_app as rest_create_app
from taipy.rest.extensions import apispec as rest_apispec
from taipy.rest.api.views import register_views as rest_register_views

app = rest_create_app()
with app.app_context():
    rest_register_views()
    rest_specs = rest_apispec.swagger_json().json

rest_navigation = ""

rest_path_descs = {
    "cycle": "Entry points that interact with `Cycle^` entities.",
    "scenario": "Entry points that interact with `Scenario^` entities.",
    "pipeline": "Entry points that interact with `Pipeline^` entities.",
    "datanode": "Entry points that interact with `DataNode^` entities.",
    "task": "Entry points that interact with `Task^` entities.",
    "job": "Entry points that interact with `Job^` entities.",
    "auth": "Entry points that deal with authentication."
}
rest_path_files = {}
enterprise_rest_paths = ["auth"]

response_statuses = {
    "200": ("OK", "https://httpwg.org/specs/rfc7231.html#status.200"),
    "201": ("Created", "https://httpwg.org/specs/rfc7231.html#status.201"),
    "202": ("Accepted", "https://httpwg.org/specs/rfc7231.html#status.202"),
    "204": ("No Content", "https://httpwg.org/specs/rfc7231.html#status.204"),
    "401": ("Unauthorized", "https://httpwg.org/specs/rfc7235.html#status.401"),
    "404": ("Not Found", "https://httpwg.org/specs/rfc7231.html#status.404"),
}

def get_property_type(property_desc, from_schemas):
    type_name = property_desc.get("type", None)
    a_pre = ""
    a_post = ""
    if type_name == "array":
        property_desc = property_desc['items']
        type_name = property_desc.get("type", None)
        a_pre = "\\["
        a_post = "\\]"
    if type_name is None:
        type_name = property_desc.get("$ref", None)
        if type_name is None:
            # print(f"WARNING - No type...")
            return ""
        type_name = type_name[type_name.rfind('/')+1:]
        prefix = "" if from_schemas else "../schemas/"
        type_name = f"[`{type_name}`]({prefix}#{type_name.lower()})"
    return f"{a_pre}{type_name}{a_post}"

for path, desc in rest_specs["paths"].items():
  dest_path = None
  dest_path_desc = None
  for p, d in rest_path_descs.items():
      if f"/{p}" in path:
          dest_path = p
          dest_path_desc = d
          break
  if dest_path is None:
        print(f"Path {path} has no paths bucket")
        continue

  file = rest_path_files.get(dest_path)
  if file is None:
      file = open(f"{REST_REF_DIR_PATH}/apis_{dest_path}.md", "w")
      if dest_path in enterprise_rest_paths:
          file.write(ENTERPRISE_BANNER)
      file.write(f"{dest_path_desc}\n\n")
      rest_navigation += " " * 6 + f"- Paths for {dest_path}: manuals/reference_rest/apis_{dest_path}.md\n"
      rest_path_files[dest_path] = file

  file.write(f"# `{path}`\n\n")
  for method, method_desc in desc.items():
    file.write(f"## {method.upper()}\n\n")
    file.write(f"{method_desc['description']}\n\n")
    parameters = method_desc.get("parameters")
    if parameters is not None:
      file.write(f"<h4>Parameters</h4>\n\n")
      file.write("|Name|Type|Required|Description|\n")
      file.write("|---|---|---|---|\n")
      for param in parameters:
          param_type = "TODO"
          if "schema" in param and len(param["schema"]) == 1:
              param_type = param["schema"]["type"]
          file.write(f"|{param['name']}|{param_type}|{'Yes' if param['name'] else 'No'}|{param.get('description', '-')}|\n")
      file.write("\n")
    request_body = method_desc.get("requestBody")
    if request_body is not None:
        file.write(f"<div><h4 style=\"display: inline-block;\">Request body:</h4>\n")
        schema = request_body["content"]["application/json"]["schema"]["$ref"]
        schema = schema[schema.rfind('/')+1:]
        file.write(f"<span><a href=\"../schemas/#{schema.lower()}\">{schema}</a></div>\n\n")
    responses = method_desc.get("responses")
    if responses is not None:
      file.write(f"<h4>Responses</h4>\n\n")
      for response, response_desc in responses.items():
          file.write(f"- <b><code>{response}</code></b><br/>\n")
          status = response_statuses[response]
          file.write(f"    Status: [`{status[0]}`]({status[1]})\n\n")
          description = response_desc.get("description")
          if description is not None:
              file.write(f"    {description}\n")
          content = response_desc.get("content", None)
          if content is not None:
              schema = content["application/json"]["schema"]
              allOf = schema.get("allOf")
              if allOf is not None:
                  schema = allOf[0]
              properties = schema.get("properties")
              if properties is not None:
                  file.write("    |Name|Type|\n")
                  file.write("    |---|---|\n")
                  for property, property_desc in properties.items():
                      file.write(f"    |{property}|{get_property_type(property_desc, False)}|\n")
              else:
                  print(f"No properties in content in response {response} in method {method} of {path}")
          elif response != "404":
              print(f"No content in response {response} in method {method} of {path}")
          file.write("\n")

for f in rest_path_files.values():
    f.close()

file = open(f"{REST_REF_DIR_PATH}/schemas.md", "w")
for schema, schema_desc in rest_specs["components"]["schemas"].items():
    properties = schema_desc.get("properties")
    if properties is not None:
        file.write(f"## {schema}\n\n")
        file.write("|Name|Type|Description|\n")
        file.write("|---|---|---|\n")
        for property, property_desc in properties.items():
            file.write(f"|{property}|{get_property_type(property_desc, True)}|-|\n")
        file.write("\n")
file.close()
rest_navigation += " " * 6 + "- Schemas: manuals/reference_rest/schemas.md\n"

restore_top_package_location()


# ------------------------------------------------------------------------
# Step 4
#   Generating the GUI Extension API documentation
# ------------------------------------------------------------------------
print("Step 4/5: Generating the GUI Extension API Reference Manual pages", flush=True)
import subprocess

GUI_EXT_REF_DIR_PATH=root_dir + "/docs/manuals/reference_guiext"

npm_path=shutil.which("npm")
if npm_path:
    try:
        subprocess.run([npm_path, "--version"], shell=True, capture_output=True)
    except OSError:
        print(f"Couldn't run npm, ignoring this step.")
        npm_path=None
if npm_path:
    saved_cwd = os.getcwd()
    gui_path=os.path.join(root_dir, "gui")
    os.chdir(gui_path)
    print(f"    Installing node modules...", flush=True)
    subprocess.run([npm_path, "i", "--omit=optional"], shell=True)
    print(f"    Generating documentation...", flush=True)
    subprocess.run([npm_path, "run", "mkdocs"], shell=True)
    # Process and copy files to docs/manuals
    if os.path.exists(GUI_EXT_REF_DIR_PATH):
        shutil.rmtree(GUI_EXT_REF_DIR_PATH)
    os.mkdir(GUI_EXT_REF_DIR_PATH)
    dst_dir = os.path.abspath(GUI_EXT_REF_DIR_PATH)
    src_dir = os.path.abspath(os.path.join(gui_path, "reference_guiext"))
    JS_EXT_RE = re.compile(r"^(.*?)(\n#.*?\n)", re.MULTILINE|re.DOTALL)
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_content = None
            path_name = os.path.join(root, file)
            with open(path_name) as input:
                file_content = input.read()
            match = JS_EXT_RE.search(file_content)
            if match:
                file_content = match.group(2) + match.group(1) + file_content[match.end():]
            path_name = path_name.replace(src_dir, dst_dir)
            with open(path_name, "w") as output:
                output.write(file_content)
        for dir in dirs:
            os.mkdir(os.path.join(dst_dir, dir))
    os.chdir(saved_cwd)

# ------------------------------------------------------------------------
# Step 5
#   Generating the Getting Started
# ------------------------------------------------------------------------
print("Step 4/5: Generating the Getting Started navigation bar", flush=True)

def format_getting_started_navigation(filepath: str) -> str:
    readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
    readme_content = Path('docs', readme_path).read_text().split('\n')
    step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
    return f"    - '{step_name}': '{readme_path}'"

step_folders = glob.glob("docs/getting_started/step_*")
step_folders.sort()
step_folders = map(lambda s: s[len('docs/'):], step_folders)
step_folders = map(format_getting_started_navigation, step_folders)
getting_started_navigation = "\n".join(step_folders) + '\n'


# Update mkdocs.yml
copyright_content = f"{str(datetime.now().year)}"
mkdocs_yml_content = re.sub(r"\[YEAR\]",
                            copyright_content,
                            mkdocs_yml_content)
mkdocs_yml_content = re.sub(r"^\s*\[REFERENCE_CONTENT\]\s*\n",
                            navigation,
                            mkdocs_yml_content,
                            flags=re.MULTILINE|re.DOTALL)
mkdocs_yml_content = re.sub(r"^\s*\[REST_REFERENCE_CONTENT\]\s*\n",
                            rest_navigation,
                            mkdocs_yml_content,
                            flags=re.MULTILINE|re.DOTALL)
mkdocs_yml_content = re.sub(r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n",
                            getting_started_navigation,
                            mkdocs_yml_content,
                            flags=re.MULTILINE|re.DOTALL)
with open(MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
    mkdocs_yml_file.write(mkdocs_yml_content)
