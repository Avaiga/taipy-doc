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
from .setup import Setup, SetupStep
import json
import os
import re
from typing import Dict, List, Optional

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
        self.VISELEMENTS_DIR_PATH = setup.manuals_dir + "/gui/viselements"
        self.CORELEMENTS_DIR_PATH = setup.manuals_dir + "/gui/corelements"
        self.controls_path = f"{self.VISELEMENTS_DIR_PATH}/controls.md"
        template_path = f"{self.controls_path}_template"
        if not os.access(template_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {template_path} Markdown template"
            )
        self.blocks_path = f"{self.VISELEMENTS_DIR_PATH}/blocks.md"
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
        # Load Taipy GUI and Taipy elements
        # -----------------------------------------------------------
        # Load elements, check basic features and resolve inheritance
        def load_elements(self, elements_json_path: str, prefix: str, doc_pages_path: str) -> None:
            with open(elements_json_path) as elements_json_file:
                loaded_elements = json.load(elements_json_file)

            new_elements = {}
            for category, elements in loaded_elements.items():
                if category not in self.categories:
                    self.categories[category] = []
                for element in elements:
                    element_type = element[0]
                    self.categories[category].append(element_type)
                    if element_type in self.elements:
                        raise ValueError(
                            f"FATAL - Duplicate element type '{element_type}' in {elements_json_path}"
                        )
                    element_desc = element[1]
                    if not __class__.PROPERTIES in element_desc and not __class__.INHERITS in element_desc:
                        raise ValueError(
                            f"FATAL - No properties in element type '{element_type}' in {elements_json_path}"
                        )
                    element_desc["prefix"] = prefix
                    element_desc["doc_path"] = doc_pages_path
                    element_desc["source"] = elements_json_path
                    new_elements[element_type] = element_desc
            self.elements.update(new_elements)
            # Find default property for all element types
            for element_type, element_desc in new_elements.items():
                default_property = None
                if properties := element_desc.get(__class__.PROPERTIES, None):
                    for property in properties:
                        if __class__.DEFAULT_PROPERTY in property:
                            if property[__class__.DEFAULT_PROPERTY]:
                                default_property = property[__class__.NAME]
                            del property[__class__.DEFAULT_PROPERTY]
                element_desc[__class__.DEFAULT_PROPERTY] = default_property

            # Resolve inheritance
            def merge(element_desc, parent_element_desc, default_property: str) -> Optional[str]:
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
            def resolve_inheritance(element_desc):
                if parent_types := element_desc.get(__class__.INHERITS, None):
                    del element_desc[__class__.INHERITS]
                    original_default_property = element_desc[__class__.DEFAULT_PROPERTY]
                    default_property = original_default_property
                    for parent_type in parent_types:
                        parent_desc = self.elements[parent_type]
                        resolve_inheritance(parent_desc)
                        default_property = merge(element_desc, parent_desc, default_property)
                    if original_default_property != default_property:
                        element_desc[__class__.DEFAULT_PROPERTY] = default_property
            for element_desc in self.elements.values():
                resolve_inheritance( element_desc)

        self.elements = {}
        self.categories = {}
        load_elements(self, setup.root_dir + "/taipy/gui/viselements.json", "", self.VISELEMENTS_DIR_PATH)
        load_elements(self, setup.root_dir + "/taipy/gui_core/viselements.json", "core_", self.CORELEMENTS_DIR_PATH)

        # Check that documented elements have a default property and a doc file,
        # and that their properties have the mandatory settings.
        for category, element_type in [(c, e) for c,elts in self.categories.items() for e in elts]:
            if category == "undocumented":
                continue
            element_desc = self.elements[element_type]
            if not __class__.DEFAULT_PROPERTY in element_desc:
                raise ValueError(
                    f"FATAL - No default property for element type '{element_type}'"
                )
            if not __class__.PROPERTIES in element_desc:
                raise ValueError(
                    f"FATAL - No properties for element type '{element_type}'"
                )
            template_path = f"{element_desc['doc_path']}/{element_type}.md_template"            
            if not os.access(template_path, os.R_OK):
                raise FileNotFoundError(
                    f"FATAL - Could not find template doc file for element type '{element_type}' at {template_path}"
                )
            # Check completeness
            for property in element_desc[__class__.PROPERTIES]:
                for n in ["type", "doc"]:
                    if not n in property:
                        raise ValueError(
                            f"FATAL - No value for '{n}' in the '{property[__class__.NAME]}' properties of element type '{element_type}' in {element_desc['source']}"
                        )

    # Generate element doc pages for that category
    # Find first level 2 or 3 header
    def generate_pages(self, category: str, md_path: str) -> None:
        FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
        # Find first level 2 or 3 header
        FIRST_HEADER2_RE = re.compile(r"(^.*?)(\n###?\s+)", re.MULTILINE | re.DOTALL)

        md_template = ""
        with open(f"{md_path}_template") as template_file:
            md_template = template_file.read()
        if not md_template:
            raise FileNotFoundError(f"FATAL - Could not read {md_path}_template markdown template")
        prefixes = set([desc["prefix"] for desc in self.elements.values()])
        toc = {}
        for prefix in prefixes:
            toc[prefix] = '<div class="tp-ve-cards">\n'

        def generate_element_doc(element_type: str, element_desc: Dict, prefix: str):
            """
            Returns the entry for the Table of Contents that is inserted
            in the global Visual Elements or Core Elements doc page.
            """
            template_doc_path = f"{element_desc['doc_path']}/{element_type}.md_template"
            with open(template_doc_path, "r") as template_doc_file:
                element_documentation = template_doc_file.read()
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
            # Convert properties array to a dict
            property_descs = { p["name"]: p for p in element_desc[__class__.PROPERTIES]}
            for property_name in [default_property_name] + list(filter(lambda x: x != default_property_name, property_descs.keys())):
                property_desc = property_descs[property_name]
                name  = property_desc[__class__.NAME]
                type  = property_desc["type"]
                default_value  = property_desc.get("default_value", None)
                doc  = property_desc.get("doc", None)
                if not default_value:
                    default_value = "<i>Required</i>" if property_desc.get("required", False) else ""
                full_name = f"<code id=\"p-{re.sub('<[^>]+>', '', name)}\">"
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

            # Chart hook
            if element_type == "chart":
                values = self.chart_page_hook(element_documentation, before_properties, after_properties)
                before_properties = values[0]
                after_properties = values[1]

            with open(f"{element_desc['doc_path']}/{element_type}.md", "w") as md_file:
                md_file.write(
                    "---\nhide:\n  - navigation\n---\n\n"
                    + f"<!-- Category: {category} -->\n"
                    + f"# <tt>{element_type}</tt>\n\n"
                    + before_properties
                    + properties_table
                    + after_properties
                )
            e = element_type  # Shortcut
            d = "../corelements/" if prefix == "core_" else ""
            s = " style=\"font-size: .8em;\"" if e == "scenario_selector" or e == "data_node_selector" else ""
            return (
                f'<a class="tp-ve-card" href="../{d}{e}/">\n'
                + f"<div{s}>{e}</div>\n"
                + f'<img class="tp-ve-l" src="../{d}{e}-l.png"/><img class="tp-ve-lh" src="../{d}{e}-lh.png"/>\n'
                + f'<img class="tp-ve-d" src="../{d}{e}-d.png"/><img class="tp-ve-dh" src="../{d}{e}-dh.png"/>\n'
                + f"<p>{first_documentation_paragraph}</p>\n"
                + "</a>\n"
            )
            # If you want a simple list, use
            # f"<li><a href=\"../{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
            # The toc header and footer must then be "<ui>" and "</ul>" respectively.

        for element_type in self.categories[category]:
            element_desc = self.elements[element_type]
            prefix = element_desc["prefix"]
            toc[prefix] += generate_element_doc(element_type, element_desc, prefix)

        with open(md_path, "w") as md_file:
            for prefix in prefixes:
                md_template = md_template.replace(f"[{prefix}TOC]", toc[prefix]+"</div>\n")
            md_file.write(md_template)

    def setup(self, setup: Setup) -> None:
        self.generate_pages("controls", self.controls_path)
        self.generate_pages("blocks", self.blocks_path)

    # Special case for charts: we want to insert the chart gallery that is stored in the
    # file whose path is in self.charts_home_html_path
    # This should be inserted before the first level 1 header
    def chart_page_hook(self, element_documentation: str, before: str, after: str) -> tuple[str, str]:
        FIRST_HEADER1_RE = re.compile(r"(^.*?)(\n#\s+)", re.MULTILINE | re.DOTALL)

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

        match = FIRST_HEADER1_RE.match(element_documentation)
        if not match:
            raise ValueError(
                f"Couldn't locate first header1 in documentation for element 'chart'"
            )
        return (match.group(1) + chart_gallery + match.group(2) + before[match.end() :], after + chart_sections)
