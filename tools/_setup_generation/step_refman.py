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

    # Force API items to be exposed in a given package
    # (item_pattern, destination_package)
    # or ([item_pattern...], destination_package)
    FORCE_PACKAGE = [
        # GUI
        ("taipy.gui.*.(Gui|State|Markdown|Page)", "taipy.gui"),
        # Core
        ("typing.*", "taipy.core"),
        ("taipy.core._core.Core", "taipy.core"),
        ("taipy.core.common.mongo_default_document.MongoDefaultDocument", "taipy.core.common"),
        ("taipy.core.common.frequency.Frequency", "taipy.core"),
        ("taipy.core.common.scope.Scope", "taipy.core"),
        ("taipy.core.config.*", "taipy.core.config"),
        ("taipy.core.cycle.cycle_id.CycleId", "taipy.core"),
        ("taipy.core.cycle.cycle.Cycle", "taipy.core"),
        ("taipy.core.data.data_node_id.DataNodeId", "taipy.core"),
        ("taipy.core.data.data_node_id.Edit", "taipy.core"),
        ("taipy.core.data.*.*DataNode", "taipy.core.data"),
        ("taipy.core.data.data_node.DataNode", "taipy.core"),
        ("taipy.core.data.operator.Operator", "taipy.core.data.operator"),
        ("taipy.core.data.operator.JoinOperator", "taipy.core.data.operator"),
        ("taipy.core.exceptions.exceptions.*", "taipy.core.exceptions"),
        ("taipy.core.job.job_id.JobId", "taipy.core"),
        ("taipy.core.job.job.Job", "taipy.core"),
        ("taipy.core.job.status.Status", "taipy.core"),
        ("taipy.core.notification.CoreEventConsumerBase", "taipy.core.notification"),
        ("taipy.core.notification.EventEntityType", "taipy.core.notification"),
        ("taipy.core.notification.EventOperation", "taipy.core.notification"),
        ("taipy.core.notification.Event", "taipy.core.notification"),
        ("taipy.core.notification.Notifier", "taipy.core.notification"),
        ("taipy.core.sequence.sequence_id.SequenceId", "taipy.core"),
        ("taipy.core.sequence.sequence.Sequence", "taipy.core"),
        ("taipy.core.scenario.scenario_id.ScenarioId", "taipy.core"),
        ("taipy.core.scenario.scenario.Scenario", "taipy.core"),
        ("taipy.core.scenario.scenario_id.ScenarioId", "taipy.core"),
        ("taipy.core.sequence.sequence.Sequence", "taipy.core"),
        ("taipy.core.sequence.sequence_id.SequenceId", "taipy.core"),
        ("taipy.core.taipy.cancel_job", "taipy.core"),
        ("taipy.core.taipy.clean_all_entities", "taipy.core"),
        ("taipy.core.taipy.clean_all_entities_by_version", "taipy.core"),
        ("taipy.core.taipy.compare_scenarios", "taipy.core"),
        ("taipy.core.taipy.create_global_data_node", "taipy.core"),
        ("taipy.core.taipy.create_sequence", "taipy.core"),
        ("taipy.core.taipy.create_scenario", "taipy.core"),
        ("taipy.core.taipy.delete", "taipy.core"),
        ("taipy.core.taipy.delete_job", "taipy.core"),
        ("taipy.core.taipy.delete_jobs", "taipy.core"),
        ("taipy.core.taipy.export_scenario", "taipy.core"),
        ("taipy.core.taipy.exists", "taipy.core"),
        ("taipy.core.taipy.get", "taipy.core"),
        ("taipy.core.taipy.get_cycles", "taipy.core"),
        ("taipy.core.taipy.get_cycles_scenarios", "taipy.core"),
        ("taipy.core.taipy.get_data_nodes", "taipy.core"),
        ("taipy.core.taipy.get_entities_by_config_id", "taipy.core"),
        ("taipy.core.taipy.get_jobs", "taipy.core"),
        ("taipy.core.taipy.get_latest_job", "taipy.core"),
        ("taipy.core.taipy.get_parents", "taipy.core"),
        ("taipy.core.taipy.get_sequences", "taipy.core"),
        ("taipy.core.taipy.get_primary", "taipy.core"),
        ("taipy.core.taipy.get_primary_scenarios", "taipy.core"),
        ("taipy.core.taipy.get_scenarios", "taipy.core"),
        ("taipy.core.taipy.get_tasks", "taipy.core"),
        ("taipy.core.taipy.is_deletable", "taipy.core"),
        ("taipy.core.taipy.is_promotable", "taipy.core"),
        ("taipy.core.taipy.is_submittable", "taipy.core"),
        ("taipy.core.taipy.set", "taipy.core"),
        ("taipy.core.taipy.set_primary", "taipy.core"),
        ("taipy.core.taipy.submit", "taipy.core"),
        ("taipy.core.taipy.subscribe_sequence", "taipy.core"),
        ("taipy.core.taipy.subscribe_scenario", "taipy.core"),
        ("taipy.core.taipy.tag", "taipy.core"),
        ("taipy.core.taipy.unsubscribe_sequence", "taipy.core"),
        ("taipy.core.taipy.unsubscribe_scenario", "taipy.core"),
        ("taipy.core.taipy.untag", "taipy.core"),
        ("taipy.core.task.task_id.TaskId", "taipy.core"),
        ("taipy.core.task.task.Task", "taipy.core"),
        # Config
        ("taipy.config.config.Config", "taipy.config"),
        ("taipy.config.checker.issue.Issue", "taipy.config"),
        ("taipy.config.checker.issue_collector.IssueCollector", "taipy.config"),
        ("taipy.config.common.scope.Scope", "taipy.core.config"),
        ("taipy.config.common.frequency.Frequency", "taipy.core.config"),
        ("taipy.config.unique_section.*", "taipy.config"),
        # Rest
        ("taipy.rest.rest.Rest", "taipy.rest"),
        # Auth
        ("taipy.auth.config.authentication_config.AuthenticationConfig", "taipy.auth.config"),
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
            if re.match("^(pkg_)?taipy(\..*)?\.md$", p):
                os.remove(fp)
            elif os.path.isdir(fp) and re.match("^pkg_taipy(\..*)?$", p):
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
            for entry in dir(module):
                # Private?
                if entry.startswith("_"):
                    continue
                e = getattr(module, entry)
                if hasattr(e, "__class__") and e.__class__.__name__.startswith("_"):
                    continue
                entry_type = None
                if hasattr(e, "__module__") and e.__module__:
                    # Handling alias Types
                    if e.__module__.startswith(Setup.ROOT_PACKAGE):  # For local build
                        if e.__class__.__name__ == "NewType":
                            entry_type = TYPE_ID
                    elif e.__module__ == "typing" and hasattr(e, "__name__"):  # For Readthedoc build
                        # Manually remove class from 'typing'
                        if e.__name__ == "NewType":
                            continue
                        # Manually remove function from 'typing'
                        if e.__name__ == "overload":
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
                        print(
                            f"WARNING - {e.__name__} [in {e.__module__}] has no doc",
                            flush=True,
                        )
                    entries[full_name] = {
                        "name": entry,
                        "module": e.__module__,
                        "type": entry_type,
                        "doc": doc,
                        "packages": [module.__name__],
                    }

        taipy_config_dir = os.path.join(setup.tools_dir, "taipy", "config")
        config_backup_path = os.path.join(taipy_config_dir, "config.py.bak")
        if os.path.exists(config_backup_path):
            shutil.move(config_backup_path, os.path.join(taipy_config_dir, "config.py"))

        read_module(__import__(Setup.ROOT_PACKAGE))

        FORCE_PACKAGE_REGEXPS = []

        def convert_to_pattern(input, dest):
            pattern = "^" + input.replace(".", "\\.").replace("*", ".*") + "$"
            FORCE_PACKAGE_REGEXPS.append((re.compile(pattern), dest))

        for force_package in RefManStep.FORCE_PACKAGE:
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
                    if xref := xrefs.get(name):
                        print(
                            f"ERROR - {'Function' if type == FUNCTION_ID else 'Class'} {name} already declared as {xref[0]}.{xref[1]}"
                        )
                    xrefs[name] = [
                        force_package,
                        entry_info["module"],
                        entry_info["packages"],
                    ]

            with open(package_output_path, "w") as package_output_file:
                if package in module_doc and module_doc[package]:
                    package_output_file.write(module_doc[package])
                package_grouped = package == package_group
                if types:
                    package_output_file.write(f"## Types\n\n")
                    for type in types:
                        name = type["name"]
                        package_output_file.write(f"   - `{name}`" + f"{': ' + type.get('doc', ' - NOT DOCUMENTED')}\n")
                        if name in xrefs:
                            print(f"WARNING - Type {package}.{name} already declared in {xrefs[name]}")
                        xrefs[name] = [
                            package,
                            entry_info["module"],
                            entry_info.get("final_package"),
                        ]
                if functions:
                    package_output_file.write(f"## Functions\n\n")
                    generate_entries(
                        functions,
                        package,
                        FUNCTION_ID,
                        package_output_file,
                        package_grouped,
                    )
                if classes:
                    package_output_file.write(f"## Classes\n\n")
                    generate_entries(classes, package, CLASS_ID, package_output_file, package_grouped)

        self.add_external_methods_to_config_class(setup)

        # Filter out packages that are the exposed package and appear in the packages list
        for entry, entry_desc in xrefs.items():
            package = entry_desc[0]
            if entry_desc[2]:
                entry_desc[2] = [p for p in entry_desc[2] if p != package]
        with open(self.XREFS_PATH, "w") as xrefs_output_file:
            xrefs_output_file.write(json.dumps(xrefs))

    @staticmethod
    def add_external_methods_to_config_class(setup: Setup):
        if not os.path.exists("config_doc.txt"):
            print(f"WARNING - No methods found to inject to Config documentation!")
            return

        # Get code of methods to inject
        with open("config_doc.txt", "r") as f:
            print(f"INFO - Injecting methods to Config documentation.")
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
