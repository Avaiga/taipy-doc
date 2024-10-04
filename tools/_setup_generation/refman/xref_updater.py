import json
import os

from .entry import Entry
from ..setup import Setup


class XRefUpdater:
    """ Update the cross-references for the Reference Manual."""
    def __init__(self, setup: Setup):
        self.XREFS_PATH = os.path.join(setup.docs_dir, "xrefs")  # ...\docs\xrefs
        self.xrefs = {}

    def update(self, entry: Entry, p_name):
        """Update the cross-references for the Reference Manual with the given entry and its package name."""
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
                            f"FATAL - {entry._get_type_title()} {entry.simple_name} "
                            f"exposed in {p_name} already declared as {xref[0]}.{xref[1]}"
                        )
                self.xrefs[f"{entry.simple_name}/{last_index}"] = [p_name, entry.parent_module, entry.packages]
                self.xrefs[entry.simple_name] = last_index + 1
            else:  # Create multiple indexed entries for 'name'
                self.xrefs[entry.simple_name] = 2
                self.xrefs[f"{entry.simple_name}/0"] = xref
                self.xrefs[f"{entry.simple_name}/1"] = [p_name, entry.parent_module, entry.packages]
        else:
            self.xrefs[entry.simple_name] = [p_name, entry.parent_module, entry.packages]

    def write(self):
        # Filter out packages that are the exposed package and appear in the packages list
        for _, entry_desc in self.xrefs.items():
            if not isinstance(entry_desc, int):
                package = entry_desc[0]
                if entry_desc[2]:
                    entry_desc[2] = [p for p in entry_desc[2] if p != package]

        with open(self.XREFS_PATH, "w") as xrefs_output_file:
            xrefs_output_file.write(json.dumps(self.xrefs))
