import json
import os
import re
from inspect import isclass, isfunction, ismodule

from .entry import Entry, EntryBuilder
from .package import Package
from ..setup import Setup


class Generator:
    CLASS_ID = "C"
    FUNCTION_ID = "F"
    TYPE_ID = "T"
    FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\s*\n|$)", re.DOTALL)
    REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

    def __init__(self, setup: Setup, reference_relative_path):
        self.setup = setup
        self.reference_relative_path = reference_relative_path  # refmans/reference
        self.REFERENCE_DIR_PATH = os.path.join(setup.docs_dir, reference_relative_path)  # ...\docs\refmans\reference
        self.XREFS_PATH = os.path.join(setup.user_manuals_dir, "xrefs")  # ...\docs\userman\xrefs
        self.PACKAGE_GROUPS = [
            "taipy.config",
            "taipy.core",
            "taipy.gui",
            "taipy.gui_core",
            "taipy.rest",
            "taipy.auth",
            "taipy.enterprise",
        ]
        self.HIDDEN_ENTRIES = ["get_context_id", "invoke_state_callback"]
        self.HIDDEN_ENTRIES_FULL = ["taipy.gui.utils._css.get_style"]

        # Read module outputs
        self.entries: dict[str, Entry] = {}  # All entries from taipy that are not private or hidden
        self.module_doc = {}  # Documentation for each module
        self.loaded_modules = set()  # All the module already processed and loaded

        # Entries
        self.grouped_entries = {}  # All entries grouped by package

        # Navigation and xrefs
        self.navigation = ""  # Navigation
        self.xrefs = {}  # All cross-references

    def generate(self):
        # Computes in a recursive way the entries and module_doc.
        self._read_module(__import__(self.setup.ROOT_PACKAGE))

        # Decides in which package an entry should be documented
        self._compute_destination_packages()

        # Group entries by package so the entry parsing is done
        # one package at a time. The navigation build is made easier.
        self._group_entries_by_package()
        self._add_taipy_packages_with_doc_but_no_entry()

        # For each package
        package_group = None
        for p_name in sorted(self.grouped_entries.keys()):
            # Get the package group if needed
            previous_package_group = package_group
            package_group = self._get_package_group(package_group, p_name)

            # Compute and append the navigation
            self._compute_navigation(previous_package_group, package_group, p_name)

            # Get the documentation path
            package_doc_path = self._get_package_doc_path(p_name)

            # - Write the package documentation
            # - Write the package entries documentation
            # - Update the package entries cross-references
            self._write_package_doc(p_name, package_group, package_doc_path)

        # Write the cross-references
        self._write_xrefs()

    def _read_module(self, module):
        if module in self.loaded_modules:
            return
        self.loaded_modules.add(module)
        if not module.__name__.startswith(self.setup.ROOT_PACKAGE):
            return
        simple_name: str
        for simple_name in dir(module):
            # Private?
            if simple_name.startswith("_"):
                continue
            e = getattr(module, simple_name)
            if hasattr(e, "__class__") and e.__class__.__name__.startswith("_"):
                continue

            # Type ?
            entry_type: str = None
            if hasattr(e, "__module__") and e.__module__:
                # Handling alias Types
                if e.__module__.startswith(self.setup.ROOT_PACKAGE):  # For local build
                    # Remove hidden entry
                    if f"{e.__module__}.{simple_name}" in self.HIDDEN_ENTRIES_FULL:
                        continue
                    if e.__class__.__name__ == "NewType":
                        entry_type = self.TYPE_ID
                elif e.__module__ == "typing" and hasattr(e, "__name__"):  # For Readthedocs build
                    # Manually remove classes from 'typing'
                    if e.__name__ in ["NewType", "TypeVar", "overload", "cast"]:
                        continue
                    entry_type = self.TYPE_ID
                else:
                    continue
            # Remove hidden entries
            if simple_name in self.HIDDEN_ENTRIES:
                continue
            # Not a function or a class?
            if not entry_type:
                if isclass(e):
                    entry_type = self.CLASS_ID
                elif isfunction(e):
                    entry_type = self.FUNCTION_ID
                elif ismodule(e):
                    self.module_doc[e.__name__] = e.__doc__
                    self._read_module(e)
            if not entry_type:
                continue

            # Add doc to all entries
            if doc := e.__doc__:
                first_line = self.FIRST_DOC_LINE_RE.match(doc.strip())
                if first_line:
                    if first_line.group(0).startswith("NOT DOCUMENTED"):
                        continue
                    doc = self.REMOVE_LINE_SKIPS_RE.subn(" ", first_line.group(0))[0].strip()
                else:
                    print(f"WARNING - Couldn't extract doc summary for {e.__name__} in {e.__module__}", flush=True)
            full_name = f"{e.__module__}.{simple_name}"
            # Entry module: e.__module__
            # Current module: module.__name__
            if entry := self.entries.get(full_name):
                packages = entry.packages
                if module.__name__ != self.setup.ROOT_PACKAGE:
                    # Is current module a parent of known packages? Use that instead if yes
                    child_idxs = [
                        i
                        for i, p in enumerate(packages)
                        if p.startswith(module.__name__)
                    ]
                    if child_idxs:
                        for index in reversed(child_idxs):
                            del packages[index]
                        packages.append(module.__name__)
                    else:
                        # Is any known package a parent of the current module? If yes ignore it
                        parent_idxs = [
                            i
                            for i, p in enumerate(packages)
                            if module.__name__.startswith(p)
                        ]
                        if not parent_idxs:
                            packages.append(module.__name__)
            else:
                if doc is None:
                    print(f"WARNING - {e.__name__} [in {e.__module__}] has no doc", flush=True)
                self.entries[full_name] = EntryBuilder.build_entry(
                    name=full_name,
                    simple_name=simple_name,
                    parent_module=e.__module__,
                    type=entry_type,
                    doc=doc,
                    packages=[module.__name__])
            if module.__name__ == self.setup.ROOT_PACKAGE:
                entry = self.entries[full_name]
                entry.set_at_root()
                entry.remove_package(self.setup.ROOT_PACKAGE)

    def _compute_destination_packages(self):
        for entry in self.entries.values():
            entry.add_doc_package(self._compute_destination_package(entry))

    def _compute_destination_package(self, entry: Entry) -> str:
        # If no packages, it has to be at the root level
        if not entry.packages:
            if not entry.at_root:
                raise SystemError(f"FATAL - Entry '{entry.name}' has no package, and not in root")
            return self.setup.ROOT_PACKAGE
        else:
            # If visible from a package above entry module, pick this one
            parents = list(filter(lambda p: entry.parent_module.startswith(p), entry.packages))
            if len(parents) > 1:
                raise SystemError(f"FATAL - Entry '{entry.name}' has several parent packages: {entry.packages}")
            elif len(parents) == 0:
                if len(entry.packages) == 1:
                    return entry.packages[0]
                else:
                    package_groups = list(filter(lambda p: p in self.PACKAGE_GROUPS, entry.packages))
                    if len(package_groups) == 1:
                        return package_groups[0]
                    else:
                        raise SystemError(f"FATAL - Entry '{entry.name}' has no target package")
            else:
                return parents[0]

    def _group_entries_by_package(self) -> dict[str, list[Entry]]:
        for entry in self.entries.values():
            if entry.doc_package not in self.grouped_entries:
                self.grouped_entries[entry.doc_package] = Package(entry.doc_package)
            self.grouped_entries[entry.doc_package].add_entry(entry)
        return self.grouped_entries

    def _add_taipy_packages_with_doc_but_no_entry(self):
        for p_name, doc in self.module_doc.items():
            if not p_name.startswith("taipy"):
                continue
            if p_name in self.grouped_entries:
                continue
            if not doc:
                continue
            self.grouped_entries[p_name] = Package(p_name)

    def _get_package_group(self, package_group, p_name):
        if p_name in self.PACKAGE_GROUPS:
            return p_name
        else:
            new_package_group = None
            for p in self.PACKAGE_GROUPS:
                if p_name.startswith(p + "."):
                    new_package_group = p
                    break
            if new_package_group != package_group:
                if not new_package_group:
                    raise SystemExit(f"FATAL - No high package group for package '{p_name}' "
                                     f"(renamed from '{package_group}')")
                return new_package_group
            return package_group

    def _compute_navigation(self, previous_package_group, package_group, p_name):
        if p_name in self.PACKAGE_GROUPS:
            self.navigation += f'- "<code>{p_name}</code>":\n  - {self.reference_relative_path}/pkg_{p_name}/index.md\n'
        else:
            if package_group != previous_package_group:
                self.navigation += f"- {package_group}:\n"
            package_nav_entry = p_name
            if package_group:
                self.navigation += "  "
                package_nav_entry = p_name[len(package_group):]
            self.navigation += f'- "<code>{package_nav_entry}</code>": {self.reference_relative_path}/pkg_{p_name}.md\n'

    def _get_package_doc_path(self, p_name):
        if p_name in self.PACKAGE_GROUPS:
            package_path = f"{self.REFERENCE_DIR_PATH}/pkg_{p_name}"
            os.mkdir(package_path)
            package_doc_path = os.path.join(package_path, "index.md")
        else:
            package_doc_path = os.path.join(self.REFERENCE_DIR_PATH, f"pkg_{p_name}.md")
        return package_doc_path

    def _write_package_doc(self, p_name, package_group, package_doc_path):
        with open(package_doc_path, "w") as package_doc_file:
            package = self.grouped_entries[p_name]
            if p_name in self.module_doc and self.module_doc[p_name]:
                package_doc_file.write(self.module_doc[p_name])

            if package.types:
                package_doc_file.write("## Types\n\n")
                for type_entry in package.types:
                    simple_name = type_entry.simple_name
                    package_doc_file.write(f"   - `{simple_name}`: {type_entry.doc or ' - NOT DOCUMENTED'}\n")
                    self._update_entry_xrefs(type_entry, p_name)
            if package.functions:
                package_doc_file.write("## Functions\n\n")
                self._generate_entries(package.functions, p_name, package_doc_file, p_name == package_group)
            if package.classes:
                package_doc_file.write("## Classes\n\n")
                self._generate_entries(package.classes, p_name, package_doc_file, p_name == package_group)

    def _update_entry_xrefs(self, entry: Entry, p_name):
        if not entry.packages:
            print(f"NOTE - {entry.simple_name} has no other packages in update_xrefs")
        # xrefs:
        # entry_name <-> [ exposed_package, entry_module, other_packages]
        #   or
        # name <-> <number of similar entries> (int)
        # +  entry_name/<index> <-> [ exposed_package, entry_module, other_packages]
        if xref := self.xrefs.get(entry.simple_name):
            if isinstance(xref, int):  # If there already are duplicates
                last_index = int(xref)
                for index in range(last_index):
                    xref = self.xrefs.get(f"{entry.simple_name}/{index}")
                    if p_name == xref[0]:
                        raise SystemError(
                            f"FATAL - {entry.get_type_name()} {entry.simple_name} exposed in {p_name} already declared "
                            f"as {xref[0]}.{xref[1]}"
                        )
                self.xrefs[f"{entry.simple_name}/{last_index}"] = [p_name, entry.parent_module, entry.packages]
                self.xrefs[entry.simple_name] = last_index + 1
            else:  # Create multiple indexed entries for 'name'
                self.xrefs[entry.simple_name] = 2
                self.xrefs[f"{entry.simple_name}/0"] = xref
                self.xrefs[f"{entry.simple_name}/1"] = [p_name, entry.parent_module, entry.packages]
        else:
            self.xrefs[entry.simple_name] = [p_name, entry.parent_module, entry.packages]

    def _generate_entries(self, entries, p_name, package_doc_file, in_group):
        in_group = "../" if in_group else ""
        for entry in sorted(entries, key=lambda e: e.simple_name):
            simple_name = entry.simple_name
            package_doc_file.write(
                f"   - [`{simple_name}{'()' if entry.is_function() else ''}`]({in_group}{p_name}.{simple_name}.md)"
                + f"{': ' + entry.doc if entry.doc else ' - NOT DOCUMENTED'}\n"
            )
            output_path = os.path.join(self.REFERENCE_DIR_PATH, f"{p_name}.{simple_name}.md")
            with open(output_path, "w") as output_file:
                output_file.write("---\n---\n\n" + f"::: {p_name}.{simple_name}\n")
            self._update_entry_xrefs(entry, p_name)

    def _write_xrefs(self):
        # Filter out packages that are the exposed package and appear in the packages list
        for _, entry_desc in self.xrefs.items():
            if not isinstance(entry_desc, int):
                package = entry_desc[0]
                if entry_desc[2]:
                    entry_desc[2] = [p for p in entry_desc[2] if p != package]

        with open(self.XREFS_PATH, "w") as xrefs_output_file:
            xrefs_output_file.write(json.dumps(self.xrefs))
