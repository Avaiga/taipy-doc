import json
import os

from .entry import Entry
from .package import Package
from .xref_updater import XRefUpdater
from ..setup import Setup


class Generator:

    def __init__(self, setup: Setup, reference_relative_path, entries: dict[str, Entry], pkg_docs: dict[str, str]):
        self.setup = setup
        self.ref_relative_path = reference_relative_path  # refmans/reference
        self.REFERENCE_DIR_PATH = os.path.join(setup.docs_dir, reference_relative_path)  # ...\docs\refmans\reference
        self.PACKAGE_GROUPS = [
            "taipy.common",
            "taipy.core",
            "taipy.gui",
            "taipy.gui_core",
            "taipy.rest",
            "taipy.auth",
            "taipy.enterprise",
        ]
        self.entries: dict[str, Entry] = entries  # All entries from taipy that are not private or hidden
        self.pkg_docs = pkg_docs

        # Navigation and xrefs
        self.navigation = ""  # Navigation
        self.xref_updater = XRefUpdater(setup)

    def generate(self):

        # Decides in which package each entry should be documented
        self._compute_destination_packages()

        # Build the packages from its docstring and entries
        packages = self._build_packages()

        # Generate the doc parsing packages alphabetically so the navigation is built in the right order
        for p_name in sorted(packages.keys()):
            package = packages[p_name]
            package.generate(self.xref_updater)
            self.navigation += package.navigation

        # Write the cross-references
        self.xref_updater.write()

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

    def _build_packages(self) -> dict[str, Package]:
        packages = {}
        # Create Packages from its doc and its entries
        for entry in self.entries.values():
            p_name = entry.doc_package
            if p_name not in packages:
                packages[p_name] = Package(p_name, self.pkg_docs.get(p_name), self.setup, self.ref_relative_path)
            packages[p_name].add_entry(entry)

        # Add taipy packages with doc but no entry
        for p_name, doc in self.pkg_docs.items():
            if not p_name.startswith("taipy"):
                continue
            if p_name in packages:
                continue
            if not doc:
                continue
            packages[p_name] = Package(p_name, self.pkg_docs.get(p_name), self.setup, self.ref_relative_path)
        return packages
