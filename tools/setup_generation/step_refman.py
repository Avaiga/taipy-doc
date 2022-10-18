# ################################################################################
# Taipy Reference Manual generation setup step.
#
# Generate the entries for every documented class, method, and function.
# This scripts browses the root package (Setup.ROOT_PACKAGE) and builds a
# documentation file for every package and every class it finds.
# It finally updates the top navigation bar content (in mkdocs.yml) to
# reflect the root package structure.
# ################################################################################
from .setup import Setup, SetupStep
from inspect import isclass, isfunction, ismodule
import json
import os
import re
import shutil


class RefManStep(SetupStep):

    # Package grouping
    PACKAGE_GROUP = [
        "taipy.config",
        "taipy.core",
        "taipy.gui",
        "taipy.rest",
        "taipy.auth",
        "taipy.enterprise",
    ]

    # Force API items to be exposed in a given package
    # (item_pattern, destination_package)
    # or ([item_pattern...], destination_package)
    FORCE_PACKAGE = [
        ("typing.*", "taipy.core"),
        ("taipy.gui.*.(Gui|State|Markdown|Page)", "taipy.gui"),
        (
            [
                "taipy.core.cycle.cycle.Cycle",
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
                "taipy.core.taipy.untag",
            ],
            "taipy.core",
        ),
        ("taipy.core.data.*.*DataNode", "taipy.core.data"),
        ("taipy.rest.rest.Rest", "taipy.rest"),
    ]
    # Entries that should be hidden for the time being
    HIDDEN_ENTRIES = ["Decimator", "get_context_id", "invoke_state_callback"]
    # Where the Reference Manual files are generated (MUST BE relative to docs_dir)
    REFERENCE_REL_PATH = "manuals/reference"

    def get_id(self) -> str:
        return "refman"

    def get_description(self) -> str:
        return "Generation of the Reference Manual pages"

    def enter(self, setup: Setup):
        self.REFERENCE_DIR_PATH = setup.docs_dir + "/" + RefManStep.REFERENCE_REL_PATH
        self.XREFS_PATH = setup.manuals_dir + "/xrefs"
        self.navigation = None

    def setup(self, setup: Setup) -> None:
        # Create empty REFERENCE_DIR_PATH directory
        if os.path.exists(self.REFERENCE_DIR_PATH):
            shutil.rmtree(self.REFERENCE_DIR_PATH)
            os.mkdir(self.REFERENCE_DIR_PATH)

        setup.move_package_to_tools(Setup.ROOT_PACKAGE)
        try:
            self.generate_refman_pages()
        except Exception as e:
            raise e
        finally:
            setup.move_package_to_root(Setup.ROOT_PACKAGE)

    def generate_refman_pages(self) -> None:
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
        entries: dict[str, dict[str, any]] = {}
        entry_to_package = {}
        module_doc = {}

        def read_module(module):
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
                    # Type alias?
                    if e.__module__ == "typing" and hasattr(e, "__name__"):
                        # Manually remove class from 'typing'
                        if e.__name__ == "NewType":
                            continue
                        entry_type = TYPE_ID
                    # Not in our focus package?
                    elif not e.__module__.startswith(Setup.ROOT_PACKAGE):
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
                        doc = REMOVE_LINE_SKIPS_RE.subn(" ", first_line.group(0))[
                            0
                        ].strip()
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
            if not classes and not functions and not types:
                print(f"INFO - Skipping package {package}: no documented elements")
                continue
            if package in RefManStep.PACKAGE_GROUP:
                package_group = package
                package_path = f"{self.REFERENCE_DIR_PATH}/pkg_{package}"
                os.mkdir(package_path)
                package_output_path = os.path.join(package_path, "index.md")
                self.navigation += (
                    " " * 4
                    + f"- {package}:\n"
                    + " " * 6
                    + f"- {RefManStep.REFERENCE_REL_PATH}/pkg_{package}/index.md\n"
                )
            else:
                new_package_group = None
                for p in RefManStep.PACKAGE_GROUP:
                    if package.startswith(p + "."):
                        new_package_group = p
                        break
                if new_package_group != package_group:
                    if not new_package_group:
                        raise SystemExit(
                            f"FATAL - Unknown package '{new_package_group}' for package '{package}' (renamed from '{package_group}')"
                        )
                    package_group = new_package_group
                    self.navigation += " " * 4 + f"- {package_group}:\n"
                self.navigation += (
                    " " * (6 if package_group else 4)
                    + f"- {package}: manuals/reference/pkg_{package}.md\n"
                )
                package_output_path = os.path.join(
                    self.REFERENCE_DIR_PATH, f"pkg_{package}.md"
                )

            def generate_entries(
                entry_infos, package, type, package_output_file, in_group
            ):
                in_group = "../" if in_group else ""
                for entry_info in sorted(entry_infos, key=lambda i: i["name"]):
                    name = entry_info["name"]
                    force_package = entry_info.get("force_package", package)
                    package_output_file.write(
                        f"   - [`{name}"
                        + f"{'()' if type == FUNCTION_ID else ''}`]({in_group}{force_package}.{name}.md)"
                        + f"{': ' + entry_info['doc'] if entry_info['doc'] else ' - NOT DOCUMENTED'}\n"
                    )
                    output_path = os.path.join(
                        self.REFERENCE_DIR_PATH, f"{force_package}.{name}.md"
                    )
                    with open(output_path, "w") as output_file:
                        output_file.write(
                            "---\nhide:\n  - navigation\n---\n\n"
                            + f"::: {force_package}.{name}\n"
                        )
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
                package_output_file.write(f'---\ntitle: "{package}" package\n---\n\n')
                package_output_file.write(f"# Package: `{package}`\n\n")
                if package in module_doc and module_doc[package]:
                    package_output_file.write(module_doc[package])
                package_grouped = package == package_group
                if types:
                    package_output_file.write(f"## Types\n\n")
                    for type in types:
                        name = type["name"]
                        package_output_file.write(
                            f"   - `{name}`"
                            + f"{': ' + type.get('doc', ' - NOT DOCUMENTED')}\n"
                        )
                        if name in xrefs:
                            print(
                                f"WARNING - Type {package}.{name} already declared in {xrefs[name]}"
                            )
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
                    generate_entries(
                        classes, package, CLASS_ID, package_output_file, package_grouped
                    )

        # Filter out packages that are the exposed pagckage and appear in the packages list
        for entry, entry_desc in xrefs.items():
            package = entry_desc[0]
            if entry_desc[2]:
                entry_desc[2] = [p for p in entry_desc[2] if p != package]
        with open(self.XREFS_PATH, "w") as xrefs_output_file:
            xrefs_output_file.write(json.dumps(xrefs))


    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[REFERENCE_CONTENT\]\s*\n", self.navigation
        )
