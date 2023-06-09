# ################################################################################
# Taipy GUI Visual Elements documentation.
#
# This includes the update of the Table of Contents for both the controls
# and the blocks document pages.
#
# For each visual element, this script combines its property list and core
# documentation, and generates full Markdown files in [VISELEMENTS_DIR_PATH]. All
# these files ultimately get integrated in the global doc set.
#
# The skeleton documentation files
# [VISELEMENTS_DIR_PATH]/[controls|blocks].md_template
# are also completed with generated table of contents.
# ################################################################################
from .setup import Setup
from .elmnts_generator import ElementsGenerator
import os
import re


class VisElementsStep(ElementsGenerator):
    def get_id(self) -> str:
        return "viselements"

    def get_description(self) -> str:
        return "Extraction of the visual elements documentation"

    def enter(self, setup: Setup):
        self.VISELEMENTS_DIR_PATH = setup.manuals_dir + "/gui/viselements"
        self.controls_path = self.get_element_md_path("controls")
        template_path = f"{self.controls_path}_template"
        if not os.access(template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {template_path} Markdown template"
            )
        self.blocks_path = self.get_element_md_path("blocks")
        template_path = f"{self.blocks_path}_template"
        if not os.access(template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {template_path} Markdown template"
            )
        self.charts_home_html_path = self.VISELEMENTS_DIR_PATH + "/charts/home.html_fragment"
        if not os.access(self.charts_home_html_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.charts_home_html_path} html fragment"
            )
        self.load_elements(setup.root_dir + "/taipy/gui/viselements.json",
                           ["controls", "blocks"])


    def get_element_md_path(self, element_type: str) -> str:
        return f"{self.VISELEMENTS_DIR_PATH}/{element_type}.md"

    def setup(self, setup: Setup) -> None:
        self.generate_pages("controls", self.controls_path)
        self.generate_pages("blocks", self.blocks_path)

    def element_page_hook(self, element_type:str, element_documentation: str, before: str, after: str) -> tuple[str, str]:
        # Special case for charts: we want to insert the chart gallery that is stored in the
        # file whose path is in self.charts_home_html_path
        # This should be inserted before the first level 1 header
        if element_type == "chart":
            with open(self.charts_home_html_path, "r") as html_fragment_file:
                chart_gallery = html_fragment_file.read()
                # The chart_gallery begins with a comment where all sub-sections
                # are listed.
            SECTIONS_RE = re.compile(r"^(?:\s*<!--\s+)(.*?)(?:-->)", re.MULTILINE | re.DOTALL)
            match = SECTIONS_RE.match(chart_gallery)
            if not match:
                raise ValueError(
                    f"{self.charts_home_html_path} should begin with an HTML comment that lists the chart types"
                )
            chart_gallery = "\n" + chart_gallery[match.end() :]
            SECTION_RE = re.compile(r"^([\w-]+):(.*)$")
            chart_sections = ""
            for line in match.group(1).splitlines():
                match = SECTION_RE.match(line)
                if match:
                    chart_sections += f"- [{match.group(2)}](charts/{match.group(1)}.md)\n"

            match = ElementsGenerator.FIRST_HEADER1_RE.match(element_documentation)
            if not match:
                raise ValueError(
                    f"Couldn't locate first header1 in documentation for element 'chart'"
                )
            return (match.group(1) + chart_gallery + match.group(2) + before[match.end() :], after + chart_sections)

        return super().element_page_hook(element_type, element_documentation, before, after)
