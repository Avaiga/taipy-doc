import json
import os

from .entry import Entry
from .package import Package
from ..setup import Setup


class Generator:

    def __init__(self, setup: Setup, reference_relative_path, entries: dict[str, Entry], module_doc: dict[str, str]):
        self.setup = setup
        self.ref_relative_path = reference_relative_path  # refmans/reference
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

        self.entries: dict[str, Entry] = entries  # All entries from taipy that are not private or hidden
        self.module_doc = module_doc
        self.grouped_entries = {}  # All entries grouped by package

        # Navigation and xrefs
        self.navigation = ""  # Navigation
        self.xrefs = {}  # All cross-references

    def generate(self):

        # Decides in which package an entry should be documented
        self._compute_destination_packages()

        # Group entries by package so the entry parsing is done
        # one package at a time. The navigation build is made easier.
        self._group_entries_by_package()
        self._add_taipy_packages_with_doc_but_no_entry()

        # For each package
        # package_group = None
        for p_name in sorted(self.grouped_entries.keys()):
            package = self.grouped_entries[p_name]

            package.generate(self.module_doc.get(p_name))
            self.navigation += package.navigation

            # ############################################
            # Get the package group if needed
            # previous_package_group = package_group
            # package_group = self._get_package_group(package_group, p_name)

            # Get the documentation path
            # package_doc_path = self._get_package_doc_path(p_name)

            # - Write the package documentation
            # - Write the package entries documentation
            # - Update the package entries cross-references
            # self._write_package_doc(p_name, package_group, package_doc_path)

            # Compute and append the navigation
            # self._compute_navigation(previous_package_group, package_group, p_name)

        # Write the cross-references
        # self._write_xrefs()

    def _compute_destination_packages(self):
        for entry in self.entries.values():
            entry.set_doc_package(self.__compute_destination_package(entry))

    def __compute_destination_package(self, entry: Entry) -> str:
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
                self.grouped_entries[entry.doc_package] = Package(entry.doc_package, self.setup, self.ref_relative_path)
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
            self.grouped_entries[p_name] = Package(p_name, self.setup, self.ref_relative_path)

    # def _get_package_group(self, package_group, p_name):
    #     if p_name in self.PACKAGE_GROUPS:
    #         return p_name
    #     else:
    #         new_package_group = None
    #         for p in self.PACKAGE_GROUPS:
    #             if p_name.startswith(p + "."):
    #                 new_package_group = p
    #                 break
    #         if new_package_group != package_group:
    #             if not new_package_group:
    #                 raise SystemExit(f"FATAL - No high package group for package '{p_name}' "
    #                                  f"(renamed from '{package_group}')")
    #             return new_package_group
    #         return package_group

    # def _compute_navigation(self, previous_package_group, package_group, p_name):
    #     if p_name in self.PACKAGE_GROUPS:
    #         self.navigation += f'- "<code>{p_name}</code>":\n  - {self.ref_relative_path}/pkg_{p_name}/index.md\n'
    #     else:
    #         if package_group != previous_package_group:
    #             self.navigation += f"- {package_group}:\n"
    #         pkg_nav_entry = p_name
    #         if package_group:
    #             self.navigation += "  "
    #             pkg_nav_entry = p_name[len(package_group):]
    #         self.navigation += f'- "<code>{pkg_nav_entry}</code>": {self.ref_relative_path}/pkg_{p_name}.md\n'

    # def _get_package_doc_path(self, p_name):
    #     if p_name in self.PACKAGE_GROUPS:
    #         package_path = f"{self.REFERENCE_DIR_PATH}/pkg_{p_name}"
    #         os.mkdir(package_path)
    #         package_doc_path = os.path.join(package_path, "index.md")
    #     else:
    #         package_doc_path = os.path.join(self.REFERENCE_DIR_PATH, f"pkg_{p_name}.md")
    #     return package_doc_path

    # def _write_package_doc(self, p_name, package_group, package_doc_path):
    #     with open(package_doc_path, "w") as package_doc_file:
    #         package = self.grouped_entries[p_name]
    #         if p_name in self.module_doc and self.module_doc[p_name]:
    #             package_doc_file.write(self.module_doc[p_name])
    #
    #         if package.types:
    #             package_doc_file.write("## Types\n\n")
    #             for type_entry in package.types:
    #                 simple_name = type_entry.simple_name
    #                 package_doc_file.write(f"   - `{simple_name}`: {type_entry.doc or ' - NOT DOCUMENTED'}\n")
    #                 self._update_entry_xrefs(type_entry, p_name)
    #         if package.functions:
    #             package_doc_file.write("## Functions\n\n")
    #             self._generate_entries(package.functions, p_name, package_doc_file, p_name == package_group)
    #         if package.classes:
    #             package_doc_file.write("## Classes\n\n")
    #             self._generate_entries(package.classes, p_name, package_doc_file, p_name == package_group)

    # def _update_entry_xrefs(self, entry: Entry, p_name):
    #     if not entry.packages:
    #         print(f"NOTE - {entry.simple_name} has no other packages in update_xrefs")
    #     # xrefs:
    #     # entry_name <-> [ exposed_package, entry_module, other_packages]
    #     #   or
    #     # name <-> <number of similar entries> (int)
    #     # +  entry_name/<index> <-> [ exposed_package, entry_module, other_packages]
    #     if xref := self.xrefs.get(entry.simple_name):
    #         if isinstance(xref, int):  # If there already are duplicates
    #             last_index = int(xref)
    #             for index in range(last_index):
    #                 xref = self.xrefs.get(f"{entry.simple_name}/{index}")
    #                 if p_name == xref[0]:
    #                     raise SystemError(
    #                         f"FATAL - {entry.get_type_title()} {entry.simple_name} "
    #                         f"exposed in {p_name} already declared as {xref[0]}.{xref[1]}"
    #                     )
    #             self.xrefs[f"{entry.simple_name}/{last_index}"] = [p_name, entry.parent_module, entry.packages]
    #             self.xrefs[entry.simple_name] = last_index + 1
    #         else:  # Create multiple indexed entries for 'name'
    #             self.xrefs[entry.simple_name] = 2
    #             self.xrefs[f"{entry.simple_name}/0"] = xref
    #             self.xrefs[f"{entry.simple_name}/1"] = [p_name, entry.parent_module, entry.packages]
    #     else:
    #         self.xrefs[entry.simple_name] = [p_name, entry.parent_module, entry.packages]

    # def _generate_entries(self, entries, p_name, package_doc_file, in_group):
    #     in_group = "../" if in_group else ""
    #     for entry in sorted(entries, key=lambda e: e.simple_name):
    #         simple_name = entry.simple_name
    #         package_doc_file.write(
    #             f"   - [`{simple_name}{'()' if entry.is_function() else ''}`]({in_group}{p_name}.{simple_name}.md)"
    #             + f"{': ' + entry.doc if entry.doc else ' - NOT DOCUMENTED'}\n"
    #         )
    #         output_path = os.path.join(self.REFERENCE_DIR_PATH, f"{p_name}.{simple_name}.md")
    #         with open(output_path, "w") as output_file:
    #             output_file.write("---\n---\n\n" + f"::: {p_name}.{simple_name}\n")
    #         self._update_entry_xrefs(entry, p_name)

    # def _write_xrefs(self):
    #     # Filter out packages that are the exposed package and appear in the packages list
    #     for _, entry_desc in self.xrefs.items():
    #         if not isinstance(entry_desc, int):
    #             package = entry_desc[0]
    #             if entry_desc[2]:
    #                 entry_desc[2] = [p for p in entry_desc[2] if p != package]
    #
    #     with open(self.XREFS_PATH, "w") as xrefs_output_file:
    #         xrefs_output_file.write(json.dumps(self.xrefs))
