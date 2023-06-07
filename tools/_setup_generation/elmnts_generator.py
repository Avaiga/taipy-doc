import json
import os
import re
from typing import Dict, List, Optional
from .setup import SetupStep

class ElementsGenerator(SetupStep):
    DEFAULT_PROPERTY = "default_property"
    PROPERTIES = "properties"
    NAME = "name"
    INHERITS = "inherits"

    # Load elements, test validity of doc and resolve inheritance
    def load_elements(self, elements_json_path: str, categories: List[str]) -> None:
        with open(elements_json_path) as elements_json_file:
            loaded_elements = json.load(elements_json_file)

        self.elements = {}
        self.categories = {}
        for category, elements in loaded_elements.items():
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
                self.elements[element_type] = element_desc
        # Find default property for all element types
        for element_type, element_desc in self.elements.items():
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

        for element_type, element_desc in self.elements.items():
            if parent_types := element_desc.get(__class__.INHERITS, None):
                del element_desc[__class__.INHERITS]
                default_property = element_desc[__class__.DEFAULT_PROPERTY]
                for parent_type in parent_types:
                    parent_desc = self.elements[parent_type]
                    default_property = merge(element_desc, parent_desc, default_property)
                element_desc[__class__.DEFAULT_PROPERTY] = default_property
        # Check that documented elements have a default property and a doc file,
        # and that their properties have the mandatory settings.
        for element in [elm for cat in categories for elm in self.categories[cat]]:
            element_desc = self.elements[element]
            if not __class__.DEFAULT_PROPERTY in element_desc:
                raise ValueError(
                    f"FATAL - No default property for element type '{element}'"
                )
            if not __class__.PROPERTIES in element_desc:
                raise ValueError(
                    f"FATAL - No properties for element type '{element}'"
                )
            doc_path = self.get_element_template_path(element)
            if not os.access(doc_path, os.R_OK):
                raise FileNotFoundError(
                    f"FATAL - Could not find doc for element type '{element}' at {doc_path}"
                )
            # Check completeness
            for property in element_desc[__class__.PROPERTIES]:
                for n in ["type", "doc"]:
                    if not n in property:
                        raise ValueError(
                            f"FATAL - No value for '{n}' in the '{property[__class__.NAME]}' properties of element type '{element_typ}' in {viselements_json_path}"
                        )

    FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
    FIRST_HEADER1_RE = re.compile(r"(^.*?)(\n#\s+)", re.MULTILINE | re.DOTALL)
    # Find first level 2 or 3 header
    FIRST_HEADER2_RE = re.compile(r"(^.*?)(\n###?\s+)", re.MULTILINE | re.DOTALL)

    def get_element_template_path(self, element_type: str) -> str:
        raise NotImplementedError(f"get_element_template_path() not implemented (element was {element}).")

    # Generate element doc pages for that category
    def generate_pages(self, category: str, md_path: str, md_template_path: str) -> None:
        def generate_element_doc(element_type: str, element_desc: Dict):
            """
            Returns the entry for the Table of Contents that is inserted
            in the global Visual Elements or Core Elements doc page.
            """
            doc_path = self.get_element_template_path(element_type) 
            with open(doc_path, "r") as doc_file:
                element_documentation = doc_file.read()
            # Retrieve first paragraph from element documentation
            match = ElementsGenerator.FIRST_PARA_RE.match(element_documentation)
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
            match = ElementsGenerator.FIRST_HEADER2_RE.match(element_documentation)
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

        md_template = ""
        with open(md_template_path) as template_file:
            md_template = template_file.read()
        if not md_template:
            raise FileNotFoundError(f"FATAL - Could not read {md_template_path} markdown template")
        toc = '<div class="tp-ve-cards">\n'
        for element_type in self.categories[category]:
            toc += generate_element_doc(element_type, self.elements[element_type])
        toc += "</div>\n"
        with open(md_path, "w") as md_file:
            md_file.write(md_template.replace("[TOC]", toc))

