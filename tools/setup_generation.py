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
tools_dir = os.path.dirname(__file__).replace("\\", "/")
root_dir = os.path.dirname(tools_dir)

GUI_DOC_PATH = root_dir + "/docs/manuals/gui/"
VISELEMENTS_SRC_PATH = root_dir + "/gui/doc"
VISELEMENTS_DIR_PATH = root_dir + "/docs/manuals/gui/viselements"

# PACKAGES_VISIBILITY indicates which packages should be hidden
# should an entity are exposed from distinct packages.
FLE_TODO_PACKAGES_VISIBILITY = [
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

# (destination_package, item_pattern)
# or (destination_package, item_patterns)
FORCE_PACKAGE = [
    ("typing.*", "taipy.core"),
    ("taipy.gui.*.(Gui|State|Markdown)", "taipy.gui"),
    ("taipy.gui.partial.Partial", "taipy.gui.partial"),
    ("taipy.gui.page.Page", "taipy.gui.page"),
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

restore_top_package_location()

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
    if entry.endswith("entities"):
        print("ASDASASDASD")
    if len(entry_info["packages"]) != 1:
        print(f"WEIRD - Entry {entry}")
    # "name": "module" "type" "doc" "packages"
    for force_package in FORCE_PACKAGE_REGEXPS:
        if force_package[0].match(entry):
            entry_info["force_package"] = force_package[1]
            break
# DEBUG
with open("all_entries.json", "w") as debug_output_file:
    debug_output_file.write(json.dumps(entries, indent=2))

#exit(0)

# Group entries by package
package_to_entries = {}
for entry, info in entries.items():
    if entry.endswith("all_entities"):
        print(f"Entry: {info}")
    package = info.get("force_package", info["packages"][0])
    if package in package_to_entries:
        package_to_entries[package].append(info)
    else:
        package_to_entries[package] = [info]
# DEBUG
with open("all_packages.json", "w") as debug_output_file:
    debug_output_file.write(json.dumps(package_to_entries, indent=2))

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
            package = entry_info.get("force_package", package)
            package_output_file.write(f"   - [`{name}"
                                      + f"{'()' if type == FUNCTION_ID else ''}`]({in_group}{package}.{name}.md)"
                                      + f"{': ' + entry_info['doc'] if entry_info['doc'] else ' - NOT DOCUMENTED'}\n")
            output_path = os.path.join(REFERENCE_DIR_PATH, f"{package}.{name}.md")
            with open(output_path, "w") as output_file:
                output_file.write("---\nhide:\n  - navigation\n---\n\n"
                                  + f"::: {package}.{name}\n")
            if name in xrefs:
                print(
                    f"ERROR - {'Function' if type == FUNCTION_ID else 'Class'} {name} already declared in {xrefs[name]}")
            xrefs[name] = (package, name, entry_info.get("final_package"))


    with open(package_output_path, "w") as package_output_file:
        package_output_file.write(f"---\ntitle: \"{package}\" package\n---\n\n")
        package_output_file.write(f"## Package: `{package}`\n\n")
        if package in module_doc and module_doc[package]:
            package_output_file.write(module_doc[package])
        package_grouped = package == package_group
        if types:
            package_output_file.write(f"### Types\n\n")
            for type in types:
                name = type["name"]
                package_output_file.write(f"   - `{name}`"
                                        + f"{': ' + type.get('doc', ' - NOT DOCUMENTED')}\n")
                if name in xrefs:
                    print(f"WARNING - Type {package}.{name} already declared in {xrefs[name]}")
                xrefs[name] = (package, name, entry_info.get("final_package"))
        if functions:
            package_output_file.write(f"### Functions\n\n")
            generate_entries(functions, package, FUNCTION_ID, package_output_file, package_grouped)
        if classes:
            package_output_file.write(f"### Classes\n\n")
            generate_entries(classes, package, CLASS_ID, package_output_file, package_grouped)
with open(XREFS_PATH, "w") as xrefs_output_file:
    xrefs_output_file.write(json.dumps(xrefs))


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
                            "",
                            mkdocs_yml_content,
                            flags=re.MULTILINE|re.DOTALL)
# TODO

with open(MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
    mkdocs_yml_file.write(mkdocs_yml_content)
