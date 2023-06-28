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
            template_path = self.get_element_md_path(element) + "_template"
            if not os.access(template_path, os.R_OK):
                raise FileNotFoundError(
                    f"FATAL - Could not find doc for element type '{element}' at {template_path}"
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

    def has_category(self) -> bool:
        raise NotImplementedError(f"has_category() not implemented.")

    def get_element_md_path(self, element_type: str) -> str:
        raise NotImplementedError(f"get_element_md_path() not implemented (element was {element_type}).")

    # Returns before_properties and after_properties if needed
    # Returned tuple would be: (new_before_properties, after_properties) where each can be None, indicating
    # we don't want to change them
    def element_page_hook(self, element_type:str, doc:str, before_properties: str, after_properties: str) -> tuple[str, str]:
        return (None, None)

    # Generate element doc pages for that category
    def generate_pages(self, category: str, md_path: str) -> None:
        def generate_element_doc(element_type: str, element_desc: Dict):
            """
            Returns the entry for the Table of Contents that is inserted
            in the global Visual Elements or Core Elements doc page.
            """
            template_doc_path = self.get_element_md_path(element_type) + "_template"
            with open(template_doc_path, "r") as template_doc_file:
                element_documentation = template_doc_file.read()
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
            match = ElementsGenerator.FIRST_HEADER2_RE.match(element_documentation)
            if not match:
                raise ValueError(
                    f"Couldn't locate first header2 in documentation for element '{element_type}'"
                )
            before_properties = match.group(1)
            after_properties = match.group(2) + element_documentation[match.end() :]

            # Process element hook
            hook_values = self.element_page_hook(element_type, element_documentation, before_properties, after_properties)
            if hook_values[0]:
                before_properties = hook_values[0]
            if hook_values[1]:
                after_properties = hook_values[1]

            with open(self.get_element_md_path(element_type), "w") as md_file:
                md_file.write(
                    "---\nhide:\n  - navigation\n---\n\n"
                    + f"# <tt>{element_type}</tt>\n\n"
                    + before_properties
                    + properties_table
                    + after_properties
                )
            e = element_type  # Shortcut
            d = f"../{e}" if self.has_category() else e
            return (
                f'<a class="tp-ve-card" href="{d}/">\n'
                + f"<div>{e}</div>\n"
                + f'<img class="tp-ve-l" src="{d}-l.png"/>\n'
                + f'<img class="tp-ve-lh" src="{d}-lh.png"/>\n'
                + f'<img class="tp-ve-d" src="{d}-d.png"/>\n'
                + f'<img class="tp-ve-dh" src="{d}-dh.png"/>\n'
                + f"<p>{first_documentation_paragraph}</p>\n"
                + "</a>\n"
            )
            # If you want a simple list, use
            # f"<li><a href=\"../{d}/{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
            # The toc header and footer must then be "<ui>" and "</ul>" respectively.

        md_template = ""
        with open(f"{md_path}_template") as template_file:
            md_template = template_file.read()
        if not md_template:
            raise FileNotFoundError(f"FATAL - Could not read {md_path}_template markdown template")
        toc = '<div class="tp-ve-cards">\n'
        for element_type in self.categories[category]:
            toc += generate_element_doc(element_type, self.elements[element_type])
        toc += "</div>\n"
        with open(md_path, "w") as md_file:
            md_file.write(md_template.replace("[TOC]", toc))
