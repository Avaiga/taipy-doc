# ################################################################################
# Taipy Reference Manual generation setup step.
#
# Generate the entries for every documented class, method, and function.
# This scripts browses the root package (Setup.ROOT_PACKAGE) and builds a
# documentation file for every package and every class it finds.
# It finally updates the top navigation bar content (in mkdocs.yml) to
# reflect the root package structure.
# ################################################################################
import json
import os
import re
import shutil
from inspect import isclass, isfunction, ismodule

from .setup import Setup, SetupStep


class RefManStep(SetupStep):
    # Package grouping (order is kept in generation)
    PACKAGE_GROUPS = [
        "taipy.config",
        "taipy.core",
        "taipy.gui",
        "taipy.gui_core",
        "taipy.rest",
        "taipy.auth",
        "taipy.enterprise",
    ]

    # Entries that should be hidden for the time being
    HIDDEN_ENTRIES = ["get_context_id", "invoke_state_callback"]
    # Where the Reference Manual files are generated (MUST BE relative to docs_dir)
    REFERENCE_REL_PATH = "manuals/reference"

    def __init__(self):
        self.navigation = None

    def get_id(self) -> str:
        return "refman"

    def get_description(self) -> str:
        return "Generation of the Reference Manual pages"

    def enter(self, setup: Setup):
        os.environ["GENERATING_TAIPY_DOC"] = "true"
        self.REFERENCE_DIR_PATH = os.path.join(setup.docs_dir, RefManStep.REFERENCE_REL_PATH)
        self.XREFS_PATH = os.path.join(setup.manuals_dir, "xrefs")

    def setup(self, setup: Setup) -> None:
        # Clean REFERENCE_DIR_PATH directory
        for p in os.listdir(self.REFERENCE_DIR_PATH):
            fp = os.path.join(self.REFERENCE_DIR_PATH, p)
            if re.match(r"^(pkg_)?taipy(\..*)?\.md$", p):
                os.remove(fp)
            elif os.path.isdir(fp) and re.match(r"^pkg_taipy(\..*)?$", p):
                shutil.rmtree(fp)

        saved_dir = os.getcwd()
        try:
            os.chdir(setup.tools_dir)
            if not os.path.isdir(os.path.join(setup.tools_dir, Setup.ROOT_PACKAGE)):
                setup.move_package_to_tools(Setup.ROOT_PACKAGE)
            self.generate_refman_pages(setup)
        except Exception as e:
            raise e
        finally:
            os.chdir(saved_dir)
            setup.move_package_to_root(Setup.ROOT_PACKAGE)

    def generate_refman_pages(self, setup: Setup) -> None:
        CLASS_ID = "C"
        FUNCTION_ID = "F"
        TYPE_ID = "T"
        FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\s*\n|$)", re.DOTALL)
        REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

        loaded_modules = set()

        # Entries:
        #   full_entry_name ->
        #     name
        #     module (source)
        #     type
        #     doc
        #     packages
        entries: dict[str, dict[str, any]] = {}
        module_doc = {}

        def read_module(module):
            if module in loaded_modules:
                return
            loaded_modules.add(module)
            if not module.__name__.startswith(Setup.ROOT_PACKAGE):
                return
            entry: str
            for entry in dir(module):
                # Private?
                if entry.startswith("_"):
                    continue
                e = getattr(module, entry)
                if hasattr(e, "__class__") and e.__class__.__name__.startswith("_"):
                    continue
                entry_type: str = None
                if hasattr(e, "__module__") and e.__module__:
                    # Handling alias Types
                    if e.__module__.startswith(Setup.ROOT_PACKAGE):  # For local build
                        if e.__class__.__name__ == "NewType":
                            entry_type = TYPE_ID
                    elif e.__module__ == "typing" and hasattr(e, "__name__"):  # For Readthedoc build
                        # Manually remove classes from 'typing'
                        if e.__name__ in ["NewType", "TypeVar", "overload"]:
                            continue
                        entry_type = TYPE_ID
                    else:
                        continue
                # Remove hidden entries
                if entry in RefManStep.HIDDEN_ENTRIES:
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
                        if first_line.group(0).startswith("NOT DOCUMENTED"):
                            continue
                        doc = REMOVE_LINE_SKIPS_RE.subn(" ", first_line.group(0))[0].strip()
                    else:
                        print(
                            f"WARNING - Couldn't extract doc summary for {e.__name__} in {e.__module__}",
                            flush=True,
                        )
                full_name = f"{e.__module__}.{entry}"
                # Entry module: e.__module__
                # Current module: module.__name__
                if entry_info := entries.get(full_name):
                    packages = entry_info["packages"]
                    if module.__name__ != Setup.ROOT_PACKAGE:
                        # Is current module a parent of known packages? Use that instead if yes
                        child_idxs = [i for i, p in enumerate(packages) if p.startswith(module.__name__)]
                        if child_idxs:
                            for index in reversed(child_idxs):
                                del packages[index]
                            packages.append(module.__name__)
                        else:
                        # Is any known package a parent of the current module? If yes ignore it
                            parent_idxs = [i for i, p in enumerate(packages) if module.__name__.startswith(p)]
                            if not parent_idxs:
                                packages.append(module.__name__)
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
                if module.__name__ == Setup.ROOT_PACKAGE:
                    entry = entries[full_name]
                    entry["at_root"] = True
                    if Setup.ROOT_PACKAGE in entry["packages"]:
                        entry["packages"].remove(Setup.ROOT_PACKAGE)

        taipy_config_dir = os.path.join(setup.tools_dir, "taipy", "config")
        config_backup_path = os.path.join(taipy_config_dir, "config.py.bak")
        if os.path.exists(config_backup_path):
            shutil.move(config_backup_path, os.path.join(taipy_config_dir, "config.py"))

        read_module(__import__(Setup.ROOT_PACKAGE))

        # Compute destination package for each entry
        for entry, entry_desc in entries.items():
            doc_package = None # Where this entity should be exposed
            module = entry_desc["module"]
            packages = entry_desc["packages"]
            # If no packages, it has to be at the root level
            if not packages:
                if not entry_desc.get("at_root", False):
                    raise SystemError(f"FATAL - Entry '{entry}' has no package, and not in root")
                doc_package = Setup.ROOT_PACKAGE
            else:
                # If visible from a package above entry module, pick this one
                parents = list(filter(lambda p: module.startswith(p), packages))
                if len(parents) > 1:
                    raise SystemError(
                        "FATAL - Entry '{entry}' has several matching parent packages ([packages])"
                    )
                elif len(parents) == 0:
                    if len(packages) == 1:
                        doc_package = packages[0]
                    else:
                        package_groups = list(filter(lambda p: p in RefManStep.PACKAGE_GROUPS, packages))
                        if len(package_groups) == 1:
                            doc_package = package_groups[0]
                else:
                    doc_package = parents[0]
            if doc_package is None:
                raise SystemError(f"FATAL - Entry '{entry}' has no target package")
            entry_desc["doc_package"] = doc_package

        # Group entries by package
        package_to_entries = {}
        for entry, info in entries.items():
            package = info["doc_package"]
            if package in package_to_entries:
                package_to_entries[package].append(info)
            else:
                package_to_entries[package] = [info]

        # Add taipy packages with documentation but no entry
        for package, doc in module_doc.items():
            if not package.startswith("taipy"):
                continue
            if package in package_to_entries:
                continue
            if not doc:
                continue
            package_to_entries[package] = {}

        # Generate all Reference manual pages and update navigation
        self.navigation = ""
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
                    raise SystemError(
                        "FATAL - Invalid entry type '{entry_info['type']}' for {entry_info['module']}.{entry_info['name']}"
                    )
            if package in RefManStep.PACKAGE_GROUPS:
                package_group = package
                package_path = f"{self.REFERENCE_DIR_PATH}/pkg_{package}"
                os.mkdir(package_path)
                package_output_path = os.path.join(package_path, "index.md")
                self.navigation += (
                    f"- \"<code>{package}</code>\":\n  - {RefManStep.REFERENCE_REL_PATH}/pkg_{package}/index.md\n"
                )
            else:
                high_package_group = None
                for p in RefManStep.PACKAGE_GROUPS:
                    if package.startswith(p + "."):
                        high_package_group = p
                        break
                if high_package_group != package_group:
                    if not high_package_group:
                        raise SystemExit(
                            f"FATAL - Unknown package '{high_package_group}' for package '{package}' (renamed from '{package_group}')"
                        )
                    package_group = high_package_group
                    self.navigation += f"- {package_group}:\n"
                package_nav_entry = package
                if package_group:
                    self.navigation += "  "
                    package_nav_entry = package[len(package_group):]
                self.navigation += f"- \"<code>{package_nav_entry}</code>\": {RefManStep.REFERENCE_REL_PATH}/pkg_{package}.md\n"
                package_output_path = os.path.join(
                    self.REFERENCE_DIR_PATH, f"pkg_{package}.md"
                )
                package_output_path = os.path.join(self.REFERENCE_DIR_PATH, f"pkg_{package}.md")

            def update_xrefs(name, type, force_package, module, others):
                if not others:
                    print(f"{name}")
                    pass
                # xrefs:
                # entry_name <-> [ exposed_package, entry_module, other_packages]
                #   or
                # name <-> <number of similar entries> (int)
                # +  entry_name/<index> <-> [ exposed_package, entry_module, other_packages]
                type_name = "Function" if type == FUNCTION_ID else "Class" if type == CLASS_ID else "Type"
                if xref := xrefs.get(name):
                    if force_package == xref[0]:
                        raise SystemError(
                            f"FATAL -  - {type_name} {name} exposed in {force_package} already declared as {xref[0]}.{xref[1]}"
                            )
                    print(f"NOTE: duplicate entry {name} - {xref[0]}/{force_package}")
                    if isinstance(xref, int): # If there already are duplicates
                        for index in range(0..int(xref)):
                            xref = xrefs.get(f"{name}/{index}")
                            if force_package == xref[0]:
                                raise SystemError(
                                    "FATAL -  - {type_name} {name} exposed in {force_package} already declared as {xref[0]}.{xref[1]}"
                                    )
                        xrefs[f"{name}/{index}"] = [ force_package, module, others ]
                    else: # Create multiple indexed entries for 'name'
                        xrefs[name] = 2
                        xrefs[f"{name}/0"] = xref
                        xrefs[f"{name}/1"] = [ force_package, module, others ]
                else:
                    xrefs[name] = [force_package, module, others ]

            def generate_entries(entry_infos, package, type, package_output_file, in_group):
                in_group = "../" if in_group else ""
                for entry_info in sorted(entry_infos, key=lambda i: i["name"]):
                    name = entry_info["name"]
                    force_package = entry_info.get("force_package", package)
                    package_output_file.write(
                        f"   - [`{name}"
                        + f"{'()' if type == FUNCTION_ID else ''}`]({in_group}{force_package}.{name}.md)"
                        + f"{': ' + entry_info['doc'] if entry_info['doc'] else ' - NOT DOCUMENTED'}\n"
                    )
                    output_path = os.path.join(self.REFERENCE_DIR_PATH, f"{force_package}.{name}.md")
                    with open(output_path, "w") as output_file:
                        output_file.write("---\nhide:\n  - navigation\n---\n\n" + f"::: {force_package}.{name}\n")
                    update_xrefs(name, type, force_package, entry_info["module"], entry_info["packages"])

            with open(package_output_path, "w") as package_output_file:
                if package in module_doc and module_doc[package]:
                    package_output_file.write(module_doc[package])
                package_grouped = package == package_group
                if types:
                    package_output_file.write("## Types\n\n")
                    for type in types:
                        name = type["name"]
                        package_output_file.write(f"   - `{name}`" + f"{': ' + type.get('doc', ' - NOT DOCUMENTED')}\n")
                        update_xrefs(name, TYPE_ID, package, entry_info["module"], entry_info.get("packages"))
                if functions:
                    package_output_file.write("## Functions\n\n")
                    generate_entries(
                        functions,
                        package,
                        FUNCTION_ID,
                        package_output_file,
                        package_grouped,
                    )
                if classes:
                    package_output_file.write("## Classes\n\n")
                    generate_entries(classes, package, CLASS_ID, package_output_file, package_grouped)

        self.add_external_methods_to_config_class(setup)

        # Filter out packages that are the exposed package and appear in the packages list
        for entry, entry_desc in xrefs.items():
            if not isinstance(entry_desc, int):
                package = entry_desc[0]
                if entry_desc[2]:
                    entry_desc[2] = [p for p in entry_desc[2] if p != package]
        with open(self.XREFS_PATH, "w") as xrefs_output_file:
            xrefs_output_file.write(json.dumps(xrefs))

    @staticmethod
    def add_external_methods_to_config_class(setup: Setup):
        if not os.path.exists("config_doc.txt"):
            print("WARNING - No methods found to inject to Config documentation")
            return

        # Get code of methods to inject
        with open("config_doc.txt", "r") as f:
            print("INFO - Injecting methods to Config documentation.")
            methods_to_inject = f.read()

        # Delete temporary file
        if os.path.exists("config_doc.txt"):
            os.remove("config_doc.txt")

        # Backup file taipy/config/config.py
        taipy_config_dir = os.path.join(setup.tools_dir, "taipy", "config")
        config_path = os.path.join(taipy_config_dir, "config.py")
        shutil.copyfile(config_path, os.path.join(taipy_config_dir, "config.py.bak"))

        # Read config.py file
        with open(config_path, "r") as f:
            contents = f.readlines()

        # Inject imports and code
        imports_to_inject = """
from types import NoneType
from typing import Any, Callable, Dict, List, Union, Optional
import json
from .common.scope import Scope
from .common.frequency import Frequency
from taipy.core.common.mongo_default_document import MongoDefaultDocument
from taipy.core.config.job_config import JobConfig
from taipy.core.config.data_node_config import DataNodeConfig
from taipy.core.config.task_config import TaskConfig
from taipy.core.config.scenario_config import ScenarioConfig
from taipy.core.config.sequence_config import SequenceConfig\n"""
        contents.insert(11, imports_to_inject)
        contents.insert(len(contents) - 2, methods_to_inject)

        # Fix code injection
        with open(config_path, "w") as f:
            new_content = "".join(contents)
            new_content = new_content.replace(
                "custom_document: Any = <class 'taipy.core.common.mongo_default_document.MongoDefaultDocument'>",
                "custom_document: Any = MongoDefaultDocument",
            )
            new_content = new_content.replace("taipy.config.common.scope.Scope", "Scope")
            new_content = new_content.replace("<Scope.SCENARIO: 2>", "Scope.SCENARIO")
            new_content = new_content.replace("taipy.core.config.data_node_config.DataNodeConfig", "DataNodeConfig")
            new_content = new_content.replace("taipy.core.config.task_config.TaskConfig", "TaskConfig")
            new_content = new_content.replace("taipy.core.config.sequence_config.SequenceConfig", "SequenceConfig")
            new_content = new_content.replace("taipy.config.common.frequency.Frequency", "Frequency")
            f.write(new_content)

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(r"^\s*\[REFERENCE_CONTENT\]\s*\n", self.navigation if self.navigation else "")
        if "GENERATING_TAIPY_DOC" in os.environ:
            del os.environ["GENERATING_TAIPY_DOC"]
