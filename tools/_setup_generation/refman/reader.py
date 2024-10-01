import re
from inspect import isclass, isfunction, ismodule

from .entry import Entry, EntryBuilder
from ..setup import Setup


class Reader:
    CLASS_ID = "C"
    FUNCTION_ID = "F"
    TYPE_ID = "T"

    FIRST_DOC_LINE_RE = re.compile(r"^(.*?)(:?\n\s*\n|$)", re.DOTALL)
    REMOVE_LINE_SKIPS_RE = re.compile(r"\s*\n\s*", re.MULTILINE)

    HIDDEN_ENTRIES = []
    HIDDEN_ENTRIES_FULL = []

    def __init__(self, setup: Setup):
        self.setup = setup
        self.entries: dict[str, Entry] = {}  # All entries from taipy that are not private or hidden
        self.package_doc = {}  # Documentation for each package

        self.loaded_modules = set()  # All the modules already processed and loaded

    def read_module(self):
        self._read_module(__import__(self.setup.ROOT_PACKAGE))

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
                    self.package_doc[e.__name__] = e.__doc__
                    self._read_module(e)
            if not entry_type:
                continue

            # Add doc to all entries
            if first_line_doc := e.__doc__:
                first_line = self.FIRST_DOC_LINE_RE.match(first_line_doc.strip())
                if first_line:
                    if first_line.group(0).startswith("NOT DOCUMENTED"):
                        continue
                    first_line_doc = self.REMOVE_LINE_SKIPS_RE.subn(" ", first_line.group(0))[0].strip()
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
                if first_line_doc is None:
                    print(f"WARNING - {e.__name__} [in {e.__module__}] has no doc", flush=True)
                self.entries[full_name] = EntryBuilder.build_entry(
                    name=full_name,
                    simple_name=simple_name,
                    parent_module=e.__module__,
                    entry_type=entry_type,
                    doc=e.__doc__,
                    first_line_doc=first_line_doc,
                    packages=[module.__name__])
            if module.__name__ == self.setup.ROOT_PACKAGE:
                entry = self.entries[full_name]
                entry.set_at_root()
                entry.remove_package(self.setup.ROOT_PACKAGE)

