from .entry import Entry


class Package:

    def __init__(self, name: str):
        self.name = name
        self.functions = []
        self.classes = []
        self.types = []

    def add_entry(self, entry: Entry):
        if entry.is_function():
            self.functions.append(entry)
        elif entry.is_class():
            self.classes.append(entry)
        elif entry.is_type():
            self.types.append(entry)
        else:
            raise SystemError(f"FATAL - Invalid entry type '{entry.type}' for {entry.parent_module}.{entry.name}")
