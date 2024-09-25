import os
from typing import List

from .entry import Entry


class Package:

    def __init__(self, name: str, setup, relative_ref_dir_path):
        self.name = name
        self.simple_name = name.split(".")[-1]
        self.setup = setup

        self.rel_ref_dir_path = relative_ref_dir_path
        self.rel_package_dir_path = f"{self.rel_ref_dir_path}/pkg_" + "/pkg_".join(self.name.split("."))
        self.rel_file_path = self.rel_package_dir_path + "/index.md"

        self.functions: List[Entry] = []
        self.classes: List[Entry] = []
        self.types: List[Entry] = []
        self.navigation = ""

    def add_entry(self, entry: Entry):
        if entry.is_function():
            self.functions.append(entry)
        elif entry.is_class():
            self.classes.append(entry)
        elif entry.is_type():
            self.types.append(entry)
        else:
            raise SystemError(f"FATAL - Invalid entry type '{entry.type}' for {entry.parent_module}.{entry.name}")

    def generate(self, module_doc) -> None:
        self._compute_navigation()
        self._write_doc(module_doc)

    def _compute_navigation(self) -> None:
        folders = self.name.split(".")
        prefix = ("." if len(folders) > 1 else "")
        self.navigation = (len(folders) - 1) * "    "
        self.navigation += f'- "<code>{prefix}{self.simple_name}</code>":\n'
        self.navigation += len(folders) * "    "
        self.navigation += f'- "<code>{prefix}{self.simple_name}</code>": {self.rel_file_path}\n'

    def _write_doc(self, module_doc) -> str:
        os.makedirs(os.path.join(self.setup.docs_dir, self.rel_package_dir_path), exist_ok=True)
        with open(os.path.join(self.setup.docs_dir, self.rel_file_path), "w") as file:
            if module_doc:
                file.write(module_doc)
            if self.types:
                file.write("# Types\n\n")
                for type_entry in self.types:
                    simple_name = type_entry.simple_name
                    file.write(f"   - `{simple_name}`: {type_entry.doc or ' - NOT DOCUMENTED'}\n")
                    # self._update_entry_xrefs(type_entry, self.name)
            if self.functions:
                file.write("\n# Functions\n\n")
                self.__write_entries(self.functions, file)
            if self.classes:
                file.write("\n# Classes\n\n")
                self.__write_entries(self.classes, file)
        return self.navigation

    def __write_entries(self, entries: List[Entry], file):
        for entry in sorted(entries, key=lambda e: e.simple_name):
            file.write(entry.index_documentation)
            entry.generate(self.setup.docs_dir, self.rel_package_dir_path)
            self.navigation += entry.navigation
            # self._update_entry_xrefs(entry, self.name)

