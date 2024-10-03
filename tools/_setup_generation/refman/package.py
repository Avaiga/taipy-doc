import os
from typing import List

from .entry import Entry
from .xref_updater import XRefUpdater


class Package:

    def __init__(self, name: str, doc, setup, relative_ref_dir_path):
        self.name = name
        self._set_doc_and_title(doc)
        self.simple_name = name.split(".")[-1]
        self.setup = setup

        self.rel_ref_dir_path = relative_ref_dir_path
        self.rel_package_dir_path = f"{self.rel_ref_dir_path}/pkg_" + "/pkg_".join(self.name.split("."))
        self.rel_file_path = self.rel_package_dir_path + "/index.md"

        self.functions: List[Entry] = []
        self.classes: List[Entry] = []
        self.types: List[Entry] = []
        self.navigation = ""
        self.xrefs = {}

    def _set_doc_and_title(self, doc):
        if doc and doc.startswith("# "):
            if "\n" in doc:
                # Get the title from the module doc directly if the first line is H1
                self.title, self.doc = doc.split("\n", 1)
                self.title = self.title[2:]  # Remove # and space
            else:
                self.title = doc[2:]
                self.doc = ""
        else:
            self.title = f"<code>{self.name}</code> package"
            self.doc = doc

    def add_entry(self, entry: Entry):
        if entry.is_function():
            self.functions.append(entry)
        elif entry.is_class():
            self.classes.append(entry)
        elif entry.is_type():
            self.types.append(entry)
        else:
            raise SystemError(f"FATAL - Invalid entry type '{entry.type}' for {entry.parent_module}.{entry.name}")

    def generate(self, xref_updater: XRefUpdater) -> None:
        self._compute_navigation()
        self._write_doc(xref_updater)

    def _compute_navigation(self) -> None:
        folders = self.name.split(".")
        indentation = ""
        prefix = ""
        if len(folders) == 2:
            prefix = "taipy."
        elif len(folders) > 2:
            indentation = (len(folders) - 2) * "  "
            prefix = "."
        self.navigation += f'{indentation}- "<code>{prefix}{self.simple_name}</code>":\n'
        self.navigation += f'{indentation}  - {self.title}: {self.rel_file_path}\n'

    def _write_doc(self, xref_updater) -> str:
        os.makedirs(os.path.join(self.setup.docs_dir, self.rel_package_dir_path), exist_ok=True)
        with open(os.path.join(self.setup.docs_dir, self.rel_file_path), "w") as file:
            if self.doc:
                file.write(self.doc)
            if self.types:
                file.write("# Types\n\n")
                for type_entry in self.types:
                    simple_name = type_entry.simple_name
                    file.write(f"- `{simple_name}`: {type_entry.doc or ' - NOT DOCUMENTED'}\n")
                    xref_updater.update(type_entry, self.name)
            if self.functions:
                file.write("\n# Functions\n\n")
                self.__write_entries(self.functions, file, xref_updater)
            if self.classes:
                file.write("\n# Classes\n\n")
                self.__write_entries(self.classes, file, xref_updater)
        return self.navigation

    def __write_entries(self, entries: List[Entry], file, xref_updater):
        for entry in sorted(entries, key=lambda e: e.simple_name):
            file.write(entry.index_documentation)
            entry.generate(self.setup.docs_dir, self.rel_package_dir_path)
            self.navigation += entry.navigation
            xref_updater.update(entry, self.name)

