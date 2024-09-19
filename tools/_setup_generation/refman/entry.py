class Entry:
    CLASS_ID = "C"
    FUNCTION_ID = "F"
    TYPE_ID = "T"

    def __init__(self, name, simple_name, parent_module, type, doc, packages):
        self.name = name
        self.simple_name = simple_name
        self.parent_module = parent_module
        self.type = type
        self.doc = doc
        self.packages = packages

        self.at_root = False
        self.doc_package = None

    def set_at_root(self):
        self.at_root = True

    def remove_package(self, package):
        if package in self.packages:
            self.packages.remove(package)

    def add_doc_package(self, package):
        self.doc_package = package

    def is_function(self):
        return False

    def is_class(self):
        return False

    def is_type(self):
        return False

    def get_type_name(self):
        raise NotImplementedError


class FunctionEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, packages):
        super().__init__(name, simple_name, parent_module, self.FUNCTION_ID, doc, packages)

    def is_function(self):
        return True

    def get_type_name(self):
        raise "Function"


class ClassEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, packages):
        super().__init__(name, simple_name, parent_module, self.CLASS_ID, doc, packages)

    def is_class(self):
        return True

    def get_type_name(self):
        return "Class"


class TypeEntry(Entry):

    def __init__(self, name, simple_name, parent_module, doc, packages):
        super().__init__(name, simple_name, parent_module, self.TYPE_ID, doc, packages)

    def is_type(self):
        return True

    def get_type_name(self):
        return "Type"


class EntryBuilder:

    @staticmethod
    def build_entry(name, simple_name, parent_module, type, doc, packages) -> Entry:
        if type == Entry.CLASS_ID:
            return ClassEntry(name, simple_name, parent_module, doc, packages)
        elif type == Entry.FUNCTION_ID:
            return FunctionEntry(name, simple_name, parent_module, doc, packages)
        else:
            return TypeEntry(name, simple_name, parent_module, doc, packages)
