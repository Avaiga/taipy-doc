import os


class Entry:
    CLASS_ID = "C"
    FUNCTION_ID = "F"
    TYPE_ID = "T"

    def __init__(self, name, simple_name, parent_module, entry_type, doc, first_line_doc, packages):
        self.name = name
        self.simple_name = simple_name
        self.parent_module = parent_module
        self.type = entry_type
        self.doc = doc
        self.first_line_doc = first_line_doc
        self.packages = packages

        self.navigation = ""
        self.at_root = False
        self.doc_package = None
        self.suffix = ""

    @property
    def index_documentation(self):
        line = self.first_line_doc if self.first_line_doc else ' - NOT DOCUMENTED'
        return f"- [`{self.simple_name}{self.suffix}`]({self.simple_name}/index.md){': ' + line}\n"

    def set_at_root(self) -> None:
        self.at_root = True

    def remove_package(self, package) -> None:
        if package in self.packages:
            self.packages.remove(package)

    def set_doc_package(self, package) -> None:
        self.doc_package = package

    def generate(self, docs_path, folder_path) -> None:
        self._compute_navigation(folder_path)
        self._write_doc(docs_path, folder_path)

    @property
    def _doc_full_name(self):
        return f"{self.doc_package}.{self.simple_name}"

    def _write_doc(self, docs_path, folder_path) -> None:
        os.makedirs(os.path.join(docs_path, folder_path, self.simple_name), exist_ok=True)
        with open(os.path.join(docs_path, folder_path, self.simple_name, "index.md"), "w") as file:
            file.write("---\n"
                       f"title: {self.simple_name}{self.suffix} {str(self._get_type_title()).lower()}\n"
                       "---\n\n"
                       f"::: {self._doc_full_name}\n")

    def _compute_navigation(self, folder_path) -> None:
        pass

    def is_function(self):
        return False

    def is_class(self):
        return False

    def is_type(self):
        return False

    def _get_type_title(self):
        raise NotImplementedError


class FunctionEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, first_line_doc, packages):
        super().__init__(name, simple_name, parent_module, self.FUNCTION_ID, doc, first_line_doc, packages)
        self.suffix = "()"

    def is_function(self):
        return True

    def _get_type_title(self):
        return "Function"


class ClassEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, first_line_doc, packages):
        super().__init__(name, simple_name, parent_module, self.CLASS_ID, doc, first_line_doc, packages)

    def is_class(self):
        return True

    def _get_type_title(self):
        return "Class"

    def _compute_navigation(self, folder_path) -> None:
        folders = self._doc_full_name.split(".")
        self.navigation = (len(folders) - 2) * "  " + f'- "<code>{self.simple_name}</code>":\n'
        self.navigation += ((len(folders)) * "  " +
                            f'- "{self.simple_name} {str(self._get_type_title()).lower()}": '
                            f'{folder_path}/{self.simple_name}/index.md\n')


class TypeEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, first_line_doc, packages):
        super().__init__(name, simple_name, parent_module, self.TYPE_ID, doc, first_line_doc, packages)

    def is_type(self):
        return True

    def _get_type_title(self):
        return "Type"


class EntryBuilder:

    @staticmethod
    def build_entry(name, simple_name, parent_module, entry_type, doc, first_line_doc, packages) -> Entry:
        if entry_type == Entry.CLASS_ID:
            return ClassEntry(name, simple_name, parent_module, doc, first_line_doc, packages)
        elif entry_type == Entry.FUNCTION_ID:
            return FunctionEntry(name, simple_name, parent_module, doc, first_line_doc, packages)
        else:
            return TypeEntry(name, simple_name, parent_module, doc, first_line_doc, packages)
