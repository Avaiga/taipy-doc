# ################################################################################
# Taipy GUI Visual Elements documentation.
#
# This includes the update of the Table of Contents for both the controls
# and the blocks document pages.
#
# For each visual element, this script combines its property list and core
# documentation (located in [VISELEMENTS_SRC_PATH]), and generates full
# Markdown files in [VISELEMENTS_DIR_PATH]. All these files ultimately get
# integrated in the global dos set.
#
# The skeleton documentation files [GUI_DOC_PATH]/[controls|blocks].md_template
# are also completed with generated table of contents.
# ################################################################################
from .setup import Setup
from .elmnts_generator import ElementsGenerator
import os


class VisElementsStep(ElementsGenerator):
    def get_id(self) -> str:
        return "viselements"

    def get_description(self) -> str:
        return "Extraction of the visual elements documentation"

    def enter(self, setup: Setup):
        self.GUI_DIR_PATH = setup.manuals_dir + "/gui"
        self.VISELEMENTS_DIR_PATH = self.GUI_DIR_PATH + "/viselements"
        self.VISELEMENTS_SRC_PATH = setup.root_dir + "/gui/doc"
        self.controls_template_path = self.GUI_DIR_PATH + "/controls.md_template"
        if not os.access(self.controls_template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.controls_template_path} Markdown template"
            )
        self.blocks_template_path = self.GUI_DIR_PATH + "/blocks.md_template"
        if not os.access(self.blocks_template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.blocks_template_path} Markdown template"
            )
        self.charts_home_html_path = self.VISELEMENTS_DIR_PATH + "/charts/home.html_fragment"
        if not os.access(self.charts_home_html_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.charts_home_html_path} html fragment"
            )
        self.load_elements(self.VISELEMENTS_SRC_PATH + "/viselements.json",
                           ["controls", "blocks"])


    def get_element_template_path(self, element_type: str) -> str:
        return f"{self.VISELEMENTS_SRC_PATH}/{element_type}.md"

    def setup(self, setup: Setup) -> None:
        # Create VISELEMS_DIR_PATH directory if necessary
        if not os.path.exists(self.VISELEMENTS_DIR_PATH):
            os.mkdir(self.VISELEMENTS_DIR_PATH)
        dest_dir = setup.manuals_dir + "/gui/viselements"
        self.generate_pages("controls", os.path.join(dest_dir, "controls.md"), self.controls_template_path)
        self.generate_pages("blocks",   os.path.join(dest_dir, "blocks.md"), self.blocks_template_path)
