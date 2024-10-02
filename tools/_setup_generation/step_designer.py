# ##########################################################################################
# Step to generate the documentation pages for Taipy Designer, after they were copied
# locally from the taipy-designer repository.
#
# ##########################################################################################

import os
import re
from io import StringIO

from .setup import SetupStep, Setup


class DesignerStep(SetupStep):
    PREFIX = "userman/ecosystem/designer"

    def __init__(self):
        self.navigation = ""

    def get_id(self) -> str:
        return "designer"

    def get_description(self) -> str:
        return "Retrieve the Designer documentation files."

    def setup(self, setup: Setup): ...

    def enter(self, setup: Setup):
        if os.path.exists(os.path.join(setup.docs_dir, DesignerStep.PREFIX)):
            self.DESIGNER_PATH = os.path.join(
                setup.docs_dir, *DesignerStep.PREFIX.split("/")
            )
            self.MKDOCS_TMPL = os.path.join(self.DESIGNER_PATH, "mkdocs.yml_template")
            if not os.access(self.MKDOCS_TMPL, os.R_OK):
                raise FileNotFoundError(
                    f"FATAL - Could not read docs/{DesignerStep.PREFIX}/mkdocs.yml_template"
                )
            self.navigation = self._read_mkdocs_template()

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[DESIGNER_CONTENT\]\s*\n",
            self.navigation if self.navigation else "",
        )

    def _read_mkdocs_template(self) -> str:
        lines = []
        indentation = 0
        with open(self.MKDOCS_TMPL) as file:
            collect = False
            for line in file:
                if line.startswith("nav:"):  # Start collecting navigation
                    collect = True
                elif re.match(r"^[\w_]+\s*?:", line):  # Stop collecting navigation
                    if collect:
                        navigation = StringIO()
                        for navline in lines:
                            # Add each line with indentation removed
                            navigation.write("  ")
                            navigation.write(navline[indentation:])
                            navigation.write("\n")
                        return navigation.getvalue()
                elif collect:
                    if not lines:
                        # Retrieve initial indentation
                        sline = line.lstrip()
                        indentation = len(line) - len(sline)
                    sline = line.rstrip()
                    if sline:  # Skip potential empty lines
                        # Add prefix to doc path
                        match = re.match(
                            r"^(\s+(?:\".*?\")|(?:[^\"]+))\s*:(:?\s*)", sline
                        )
                        if match and sline[match.end() :]:
                            sline = f"{match[1]}: {DesignerStep.PREFIX}/{sline[match.end():]}"
                        lines.append(sline)
