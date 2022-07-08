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
#     documentation (located in [VISELEMENTS_SRC_PATH]), and generates full
#     Markdown files in [VISELEMENTS_DIR_PATH]. All these files ultimately get
#     integrated in the global dos set.
#
#     The skeleton documentation files [GUI_DOC_PATH]/[controls|blocks].md_template
#     are also completed with generated table of contents.
#
#   - Generate the entries for every documented class, method, and function.
#     This scripts browses the root package (ROOT_PACKAGE) and builds a
#     documentation file for every package and every class it finds.
#     It finally updates the top navigation bar content (in mkdocs.yml) to
#     reflect the root package structure.
# ------------------------------------------------------------------------
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
tools_dir = os.path.dirname(__file__).replace("\\", "/")
root_dir = os.path.dirname(tools_dir)

GUI_DOC_PATH = root_dir + "/docs/manuals/gui/"
VISELEMENTS_SRC_PATH = root_dir + "/gui/doc"
VISELEMENTS_DIR_PATH = root_dir + "/docs/manuals/gui/viselements"

# PACKAGES_VISIBILITY indicates which packages should be hidden
# should an entity are exposed from distinct packages.
PACKAGES_VISIBILITY = [
    ("taipy.core.config.config","taipy.core.exceptions"),
    ("taipy.core.config.job_config","taipy.core.exceptions"),
    ("taipy.core.config.scenario_config","taipy.core.exceptions"),
    ("taipy.core.data.csv","taipy.core.exceptions"),
    ("taipy.core.data.data_node","taipy.core.exceptions"),
    ("taipy.core.data.excel","taipy.core.exceptions"),
    ("taipy.core.data.generic","taipy.core.exceptions"),
    ("taipy.core.data.sql","taipy.core.exceptions"),
    ("taipy.core.data.data_node","taipy.core.data.operator")
    ]
# Change some item visibility from a package to another
#   (orig_package, item_name) -> dest_package
ITEMS_VISIBILITY = {
    ("taipy.gui.gui", "Gui") : "taipy.gui",
    ("taipy.gui.partial", "Partial") : "taipy.gui.partial",
    ("taipy.gui.page", "Page") : "taipy.gui.page",
    ("taipy.gui.state", "State") : "taipy.gui",
    ("taipy.gui.renderers", "Markdown") : "taipy.gui",
    ("typing", "CycleId") : "taipy.core",
    ("typing", "DataNodeId") : "taipy.core",
    ("typing", "JobId") : "taipy.core",
    ("typing", "PipelineId") : "taipy.core",
    ("typing", "ScenarioId") : "taipy.core",
    ("typing", "TaskId") : "taipy.core",
    ("taipy.core.cycle.cycle", "Cycle") : "taipy.core",
    ("taipy.core.data.data_node", "DataNode") : "taipy.core",
    ("taipy.core.common.frequency", "Frequency") : "taipy.core",
    ("taipy.core.job.job", "Job") : "taipy.core",
    ("taipy.core.pipeline.pipeline", "Pipeline") : "taipy.core",
    ("taipy.core.scenario.scenario", "Scenario") : "taipy.core",
    ("taipy.core.common.scope", "Scope") : "taipy.core",
    ("taipy.core.job.status", "Status") : "taipy.core",
    ("taipy.core.task.task", "Task") : "taipy.core",
    ("taipy.core.data.csv", "CSVDataNode") : "taipy.core.data",
    ("taipy.core.data.excel", "ExcelDataNode") : "taipy.core.data",
    ("taipy.core.data.generic", "GenericDataNode") : "taipy.core.data",
    ("taipy.core.data.in_memory", "InMemoryDataNode") : "taipy.core.data",
    ("taipy.core.data.pickle", "PickleDataNode") : "taipy.core.data",
    ("taipy.core.data.sql", "SQLDataNode") : "taipy.core.data",
    ("taipy.core.taipy", "clean_all_entities") : "taipy.core",
    ("taipy.core.taipy", "compare_scenarios") : "taipy.core",
    ("taipy.core.taipy", "create_pipeline") : "taipy.core",
    ("taipy.core.taipy", "create_scenario") : "taipy.core",
    ("taipy.core.taipy", "delete") : "taipy.core",
    ("taipy.core.taipy", "delete_job") : "taipy.core",
    ("taipy.core.taipy", "delete_jobs") : "taipy.core",
    ("taipy.core.taipy", "get") : "taipy.core",
    ("taipy.core.taipy", "get_cycles") : "taipy.core",
    ("taipy.core.taipy", "get_data_nodes") : "taipy.core",
    ("taipy.core.taipy", "get_jobs") : "taipy.core",
    ("taipy.core.taipy", "get_latest_job") : "taipy.core",
    ("taipy.core.taipy", "get_pipelines") : "taipy.core",
    ("taipy.core.taipy", "get_primary") : "taipy.core",
    ("taipy.core.taipy", "get_primary_scenarios") : "taipy.core",
    ("taipy.core.taipy", "get_scenarios") : "taipy.core",
    ("taipy.core.taipy", "get_tasks") : "taipy.core",
    ("taipy.core.taipy", "set") : "taipy.core",
    ("taipy.core.taipy", "set_primary") : "taipy.core",
    ("taipy.core.taipy", "submit") : "taipy.core",
    ("taipy.core.taipy", "subscribe_pipeline") : "taipy.core",
    ("taipy.core.taipy", "subscribe_scenario") : "taipy.core",
    ("taipy.core.taipy", "tag") : "taipy.core",
    ("taipy.core.taipy", "unsubscribe_pipeline") : "taipy.core",
    ("taipy.core.taipy", "unsubscribe_scenario") : "taipy.core",
    ("taipy.core.taipy", "untag") : "taipy.core",
    ("taipy.rest.rest", "Rest") : "taipy.rest",
}
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
print("Step 1/3: Generating Visual Elements documentation", flush=True)


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
print("Step 2/3: Generating the Reference Manual pages", flush=True)

# Create empty REFERENCE_DIR_PATH directory
if os.path.exists(REFERENCE_DIR_PATH):
    shutil.rmtree(REFERENCE_DIR_PATH)
os.mkdir(REFERENCE_DIR_PATH)

CLASS_ID = "C"
FUNCTION_ID = "F"
TYPE_ID = "T"
FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\s*\n|$)", re.DOTALL)
REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

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
        key = (e.__module__, entry, entry_type, doc)
        if key in entry_to_package:
            package_changed = False
            for src_pkg, dst_pkg in PACKAGES_VISIBILITY:
                if module.__name__.startswith(dst_pkg) and entry_to_package[key].startswith(src_pkg):
                    entry_to_package[key] = module.__name__
                    package_changed = True
                    break
            if not package_changed and e.__module__ != module.__name__:
                # Keep the top-most package
                if e.__module__.startswith(module.__name__) and entry_to_package[key].startswith(module.__name__):
                    entry_to_package[key] = module.__name__
                else: # Is there a package with a higher priority?
                    for src_pkg, dst_pkg in PACKAGES_VISIBILITY:
                        if module.__name__.startswith(dst_pkg) and entry_to_package[key].startswith(src_pkg):
                            entry_to_package[key] = module.__name__
                            break
        else:
            if doc is None:
                print(f"WARNING - {e.__name__} [in {e.__module__}] has no doc", flush=True)
            entry_to_package[key] = module.__name__

read_module(__import__(ROOT_PACKAGE))

restore_top_package_location()

# Group entries by package
package_to_entries = {}
for entry, package in entry_to_package.items():
    if force_package:= ITEMS_VISIBILITY.get((entry[0], entry[1])):
        package = force_package
    if package in package_to_entries:
        package_to_entries[package].append(entry)
    else:
        package_to_entries[package] = [entry]

# Generate all Reference manual pages and update navigation
navigation = ""
xrefs = {}
package_group = None
for package in sorted(package_to_entries.keys()):
    functions = []
    classes = []
    types = []
    for entry in package_to_entries[package]:
        if entry[2] == CLASS_ID:
            classes.append(entry)
        elif entry[2] == FUNCTION_ID:
            functions.append(entry)
        elif entry[2] == TYPE_ID:
            types.append(entry)
        else:
            raise SystemError("FATAL - Invalid entry type '{entry[2]}' for {entry[0]}.{entry[1]}")
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


    def generate_entries(entries, package, type, package_output_file, in_group):
        in_group = "../" if in_group else ""
        for entry in sorted(entries, key=lambda e: e[1]):
            name = entry[1]
            package_output_file.write(f"   - [`{name}"
                                      + f"{'()' if type == FUNCTION_ID else ''}`]({in_group}{package}.{name}.md)"
                                      + f"{': ' + entry[3] if entry[3] else ' - NOT DOCUMENTED'}\n")
            output_path = os.path.join(REFERENCE_DIR_PATH, f"{package}.{name}.md")
            with open(output_path, "w") as output_file:
                output_file.write("---\nhide:\n  - navigation\n---\n\n"
                                  + f"::: {package}.{name}\n")
            if name in xrefs:
                print(
                    f"ERROR - {'Function' if type == FUNCTION_ID else 'Class'} {name} already declared in {xrefs[name]}")
            xrefs[name] = (package, entry[0])


    with open(package_output_path, "w") as package_output_file:
        package_output_file.write(f"---\ntitle: \"{package}\" package\n---\n\n")
        package_output_file.write(f"## Package: `{package}`\n\n")
        if package in module_doc and module_doc[package]:
            package_output_file.write(module_doc[package])
        package_grouped = package == package_group
        if types:
            package_output_file.write(f"### Types\n\n")
            for type in types:
                name = type[1]
                package_output_file.write(f"   - `{name}`"
                                        + f"{': ' + type[3] if type[3] else ' - NOT DOCUMENTED'}\n")
                if name in xrefs:
                    print(f"WARNING - Type {package}.{name} already declared in {xrefs[name]}")
                xrefs[name] = (package, type[0])
        if functions:
            package_output_file.write(f"### Functions\n\n")
            generate_entries(functions, package, FUNCTION_ID, package_output_file, package_grouped)
        if classes:
            package_output_file.write(f"### Classes\n\n")
            generate_entries(classes, package, CLASS_ID, package_output_file, package_grouped)
with open(XREFS_PATH, "w") as xrefs_output_file:
    xrefs_output_file.write(json.dumps(xrefs))



# ------------------------------------------------------------------------
# Step 3
#   Generating the Getting Started
# ------------------------------------------------------------------------
print("Step 3/3: Generating the Getting Started navigation bar", flush=True)

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
mkdocs_yml_content = re.sub(r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n",
                            getting_started_navigation,
                            mkdocs_yml_content,
                            flags=re.MULTILINE|re.DOTALL)
with open(MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
    mkdocs_yml_file.write(mkdocs_yml_content)
