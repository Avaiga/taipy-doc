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
import json
from typing import Dict, List, Optional
from .setup import Setup, SetupStep
import os
import re


class VisElementsStep(SetupStep):
    DEFAULT_PROPERTY = "default_property"
    PROPERTIES = "properties"
    NAME = "name"
    INHERITS = "inherits"

    def get_id(self) -> str:
        return "viselements"

    def get_description(self) -> str:
        return "Extraction of the visual elements documentation"

    def enter(self, setup: Setup):
        self.VISELEMENTS_SRC_PATH = setup.root_dir + "/gui/doc"
        self.GUI_DOC_PATH = setup.manuals_dir + "/gui/"
        self.VISELEMENTS_DIR_PATH = self.GUI_DOC_PATH + "/viselements"
        self.controls_md_template_path = self.GUI_DOC_PATH + "/controls.md_template"
        if not os.access(self.controls_md_template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.controls_md_template_path} markdown template"
            )
        self.blocks_md_template_path = self.GUI_DOC_PATH + "/blocks.md_template"
        if not os.access(self.blocks_md_template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.blocks_md_template_path} markdown template"
            )
        self.charts_home_html_path = self.VISELEMENTS_DIR_PATH + "/charts/home.html_fragment"
        if not os.access(self.charts_home_html_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.charts_home_html_path} html fragment"
            )
        viselements_json_path = self.VISELEMENTS_SRC_PATH + "/viselements.json"
        with open(viselements_json_path) as viselements_json_file:
            self.viselements = json.load(viselements_json_file)
        # Test validity of visual elements doc and resolve inheritance
        self.controls = self.viselements["controls"]
        self.blocks = self.viselements["blocks"]
        undocumented = self.viselements["undocumented"]
        self.all_elements = {}
        for element in self.controls+self.blocks+undocumented:
            element_type = element[0]
            if element_type in self.all_elements:
                raise ValueError(
                    f"FATAL - Duplicate element type '{element_type}' in {viselements_json_path}"
                )
            element_desc = element[1]
            if not __class__.PROPERTIES in element_desc and not __class__.INHERITS in element_desc:
                raise ValueError(
                    f"FATAL - No properties in element type '{element_type}' in {viselements_json_path}"
                )
            self.all_elements[element_type] = element_desc
        # Find default property for all element types
        for element_type, element_desc in self.all_elements.items():
            default_property = None
            if properties := element_desc.get(__class__.PROPERTIES, None):
                for property in properties:
                    if __class__.DEFAULT_PROPERTY in property:
                        if property[__class__.DEFAULT_PROPERTY]:
                            default_property = property[__class__.NAME]
                        del property[__class__.DEFAULT_PROPERTY]
            element_desc[__class__.DEFAULT_PROPERTY] = default_property
        # Resolve inheritance
        def merge(element_desc, parent_element_desc, default_property) -> Optional[str]:
            element_properties = element_desc.get(__class__.PROPERTIES, [])
            element_property_names = [p[__class__.NAME] for p in element_properties]
            for property in parent_element_desc.get(__class__.PROPERTIES, []):
                property_name = property[__class__.NAME]
                if property_name in element_property_names:
                    element_property = element_properties[element_property_names.index(property_name)]
                    for n in ["type", "default_value", "doc"]:
                        if not n in element_property and n in property:
                            element_property[n] = property[n]
                else:
                    element_property_names.append(property_name)
                    element_properties.append(property)
            element_desc[__class__.PROPERTIES] = element_properties
            if not default_property and parent_element_desc.get(__class__.DEFAULT_PROPERTY, False):
                default_property = parent_element_desc[__class__.DEFAULT_PROPERTY]
            return default_property

        for element_type, element_desc in self.all_elements.items():
            if parent_types := element_desc.get(__class__.INHERITS, None):
                del element_desc[__class__.INHERITS]
                default_property = element_desc[__class__.DEFAULT_PROPERTY]
                for parent_type in parent_types:
                    parent_desc = self.all_elements[parent_type]
                    default_property = merge(element_desc, parent_desc, default_property)
                element_desc[__class__.DEFAULT_PROPERTY] = default_property
        # Check that documented elements have a default property and a doc file,
        # and that their properties have the mandatory settings.
        for element in self.controls+self.blocks:
            element_type = element[0]
            element_desc = element[1]
            if not __class__.DEFAULT_PROPERTY in element_desc:
                raise ValueError(
                    f"FATAL - No default property for element type '{element_type}' in {viselements_json_path}"
                )
            if not __class__.PROPERTIES in element_desc:
                raise ValueError(
                    f"FATAL - No properties for element type '{element_type}' in {viselements_json_path}"
                )
            doc_path = self.VISELEMENTS_SRC_PATH + "/" + element_type + ".md"
            if not os.access(doc_path, os.R_OK):
                raise FileNotFoundError(
                    f"FATAL - Could not find doc for element type '{element_type}' in {self.VISELEMENTS_SRC_PATH}"
                )
            # Check completeness
            for property in element_desc[__class__.PROPERTIES]:
                for n in ["type", "doc"]:
                    if not n in property:
                        raise ValueError(
                            f"FATAL - No value for '{n}' in the '{property[__class__.NAME]}' properties of element type '{element_type}' in {viselements_json_path}"
                        )

    def setup(self, setup: Setup) -> None:
        # Create VISELEMS_DIR_PATH directory if necessary
        if not os.path.exists(self.VISELEMENTS_DIR_PATH):
            os.mkdir(self.VISELEMENTS_DIR_PATH)

        FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
        FIRST_HEADER1_RE = re.compile(r"(^.*?)(\n#\s+)", re.MULTILINE | re.DOTALL)
        # Find first level 2 or 3 header
        FIRST_HEADER2_RE = re.compile(r"(^.*?)(\n###?\s+)", re.MULTILINE | re.DOTALL)

        def generate_element_doc(element_type: str, element_desc: Dict):
            """
            Returns the entry for the Table of Contents that is inserted
            in the global Visual Elements doc page.
            """
            doc_path = self.VISELEMENTS_SRC_PATH + "/" + element_type + ".md"
            with open(doc_path, "r") as doc_file:
                element_documentation = doc_file.read()
            # Retrieve first paragraph from element documentation
            match = FIRST_PARA_RE.match(element_documentation)
            if not match:
                raise ValueError(
                    f"Couldn't locate first paragraph in documentation for element '{element_type}'"
                )
            first_documentation_paragraph = match.group(1)

            # Build properties table
            properties_table = """
## Properties\n\n
<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Default</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
"""
            STAR = "(&#9733;)"
            default_property_name = element_desc[__class__.DEFAULT_PROPERTY]
            for property in element_desc[__class__.PROPERTIES]:
                name  = property[__class__.NAME]
                type  = property["type"]
                default_value  = property.get("default_value", None)
                doc  = property.get("doc", None)
                if not default_value:
                    default_value = "<i>Required</i>" if property.get("required", False) else ""
                full_name = f"<code id=\"p-{name}\">"
                if name == default_property_name:
                    full_name += f"<u><bold>{name}</bold></u></code><sup><a href=\"#dv\">{STAR}</a></sup>"
                else:
                    full_name += f"{name}</code>"
                properties_table += (
                    "<tr>\n"
                    + f"<td nowrap>{full_name}</td>\n"
                    + f"<td>{type}</td>\n"
                    + f"<td nowrap>{default_value}</td>\n"
                    + f"<td><p>{doc}</p></td>\n"
                    + "</tr>\n"
                )
            properties_table += "  </tbody>\n</table>\n\n"
            if default_property_name:
                properties_table += (
                    f'<p><sup id="dv">{STAR}</sup>'
                    + f'<a href="#p-{default_property_name}" title="Jump to the default property documentation.">'
                    + f"<code>{default_property_name}</code></a>"
                    + " is the default property for this visual element.</p>\n"
                )

            # Insert title and properties in element documentation
            match = FIRST_HEADER2_RE.match(element_documentation)
            if not match:
                raise ValueError(
                    f"Couldn't locate first header2 in documentation for element '{element_type}'"
                )
            before_properties = match.group(1)
            after_properties = match.group(2) + element_documentation[match.end() :]
            output_path = os.path.join(self.VISELEMENTS_DIR_PATH, element_type + ".md")

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
                SECTION_RE = re.compile(r"^(\w+):(.*)$")
                chart_sections = ""
                for line in match.group(1).splitlines():
                    match = SECTION_RE.match(line)
                    if match:
                        chart_sections += f"- [{match.group(2)}](charts/{match.group(1)}.md)\n"

                match = FIRST_HEADER1_RE.match(element_documentation)
                if not match:
                    raise ValueError(
                        f"Couldn't locate first header1 in documentation for element 'chart'"
                    )
                before_properties = match.group(1) + chart_gallery + match.group(2) + before_properties[match.end() :]
                after_properties += chart_sections

            with open(output_path, "w") as output_file:
                output_file.write(
                    "---\nhide:\n  - navigation\n---\n\n"
                    + f"# <tt>{element_type}</tt>\n\n"
                    + before_properties
                    + properties_table
                    + after_properties
                )
            e = element_type  # Shortcut
            return (
                f'<a class="tp-ve-card" href="../viselements/{e}/">\n'
                + f"<div>{e}</div>\n"
                + f'<img class="tp-ve-l" src="../viselements/{e}-l.png"/>\n'
                + f'<img class="tp-ve-lh" src="../viselements/{e}-lh.png"/>\n'
                + f'<img class="tp-ve-d" src="../viselements/{e}-d.png"/>\n'
                + f'<img class="tp-ve-dh" src="../viselements/{e}-dh.png"/>\n'
                + f"<p>{first_documentation_paragraph}</p>\n"
                + "</a>\n"
            )
            # If you want a simple list, use
            # f"<li><a href=\"../viselements/{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
            # The toc header and footer must then be "<ui>" and "</ul>" respectively.

        # Generate element doc pages
        def generate_doc_page(category: str, elements: List, md_template_path: str):
            md_template = ""
            with open(md_template_path) as template_file:
                md_template = template_file.read()
            if not md_template:
                raise FileNotFoundError(f"FATAL - Could not read {md_template_path} markdown template")
            toc = '<div class="tp-ve-cards">\n'
            for element_type, element_desc in elements:
                toc += generate_element_doc(element_type, element_desc)
            toc += "</div>\n"
            with open(os.path.join(self.GUI_DOC_PATH, f"{category}.md"), "w") as file:
                file.write(md_template.replace("[TOC]", toc))

        generate_doc_page("controls", self.controls, self.controls_md_template_path)
        generate_doc_page("blocks", self.blocks, self.blocks_md_template_path)
