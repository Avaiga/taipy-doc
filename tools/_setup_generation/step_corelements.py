# ################################################################################
# Taipy GUI Core Elements documentation.
#
# This includes the update of the Table of Contents of the controls
# document pages.
#
# For each element, this script combines its property list and
# documentation (located in [CORELEMENTS_SRC_PATH]), and generates full
# Markdown files in [CORELEMENTS_DIR_PATH]. All these files ultimately get
# integrated in the global dos set.
#
# The template documentation files [CORELEMENTS_SRC_PATH]/[controls|blocks].md_template
# are also completed with generated table of contents.
# ################################################################################
from .setup import Setup
from .elmnts_generator import ElementsGenerator
import os

class CoreElementsStep(ElementsGenerator):

    def get_id(self) -> str:
        return "corelements"

    def get_description(self) -> str:
        return "Extraction of the Core elements documentation"

    def get_doc_dir(self) -> str:
        return "corelements"

    def enter(self, setup: Setup):
        self.CORELEMENTS_DIR_PATH = setup.manuals_dir + "/gui/corelements"
        self.template_path = self.CORELEMENTS_DIR_PATH + "/index.md_template"
        if not os.access(self.template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.template_path} markdown template"
            )
        self.load_elements(setup.root_dir + "/taipy/gui_core/viselements.json",
                           ["controls"])

    def get_element_template_path(self, element_type: str) -> str:
        return f"{self.CORELEMENTS_DIR_PATH}/{element_type}.md_template"
    
    def get_element_md_path(self, element_type: str) -> str:
        return f"{self.CORELEMENTS_DIR_PATH}/{element_type}.md"

    def setup(self, setup: Setup) -> None:
        self.generate_pages("controls", os.path.join(self.CORELEMENTS_DIR_PATH, "index.md"), self.template_path)
