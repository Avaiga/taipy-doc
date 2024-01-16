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
import json
import os
import re
from typing import Dict, Optional

from .setup import Setup, SetupStep
from io import StringIO

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
        self.charts_home_html_path = (
            self.VISELEMENTS_DIR_PATH + "/charts/home.html_fragment"
        )
        if not os.access(self.charts_home_html_path, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.charts_home_html_path} html fragment"
            )

        # Load Taipy GUI and Taipy elements
        # -----------------------------------------------------------
        # Load elements, check basic features and resolve inheritance
        def load_elements(
            self, elements_json_path: str, prefix: str, doc_pages_path: str
        ) -> None:
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
                    if (
                        __class__.PROPERTIES not in element_desc
                        and __class__.INHERITS not in element_desc
                    ):
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
            def merge(
                element_desc, parent_element_desc, default_property: str
            ) -> Optional[str]:
                element_properties = element_desc.get(__class__.PROPERTIES, [])
                element_property_names = [p[__class__.NAME] for p in element_properties]
                for property in parent_element_desc.get(__class__.PROPERTIES, []):
                    property_name = property[__class__.NAME]
                    if property_name in element_property_names:
                        element_property = element_properties[
                            element_property_names.index(property_name)
                        ]
                        for n in ["type", "default_value", "doc"]:
                            if n not in element_property and n in property:
                                element_property[n] = property[n]
                    else:
                        element_property_names.append(property_name)
                        element_properties.append(property)
                element_desc[__class__.PROPERTIES] = element_properties
                if not default_property and parent_element_desc.get(
                    __class__.DEFAULT_PROPERTY, False
                ):
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
                        default_property = merge(
                            element_desc, parent_desc, default_property
                        )
                    if original_default_property != default_property:
                        element_desc[__class__.DEFAULT_PROPERTY] = default_property

            for element_desc in self.elements.values():
                resolve_inheritance(element_desc)

        self.elements = {}
        self.categories = {}
        load_elements(
            self,
            setup.root_dir + "/taipy/gui/viselements.json",
            "",
            self.VISELEMENTS_DIR_PATH,
        )
        load_elements(
            self,
            setup.root_dir + "/taipy/gui_core/viselements.json",
            "core_",
            self.CORELEMENTS_DIR_PATH,
        )

        # Check that documented elements have a default property and a doc file,
        # and that their properties have the mandatory settings.
        for category, element_type in [
            (c, e) for c, elts in self.categories.items() for e in elts
        ]:
            if category == "undocumented":
                continue
            element_desc = self.elements[element_type]
            if __class__.DEFAULT_PROPERTY not in element_desc:
                raise ValueError(
                    f"FATAL - No default property for element type '{element_type}'"
                )
            if __class__.PROPERTIES not in element_desc:
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
                    if n not in property:
                        raise ValueError(
                            f"FATAL - No value for '{n}' in the '{property[__class__.NAME]}' properties of element type '{element_type}' in {element_desc['source']}"
                        )

    # Generate element doc pages for that category
    # Find first level 2 or 3 header
    def generate_pages(self, category: str, md_path: str) -> None:
        FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
        # Find first level 2 or 3 header
        FIRST_HEADER_RE = re.compile(r"(^.*?)(\n#+\s+)", re.MULTILINE | re.DOTALL)

        md_template = ""
        with open(f"{md_path}_template") as template_file:
            md_template = template_file.read()
        if not md_template:
            raise FileNotFoundError(
                f"FATAL - Could not read {md_path}_template markdown template"
            )
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
            element_desc['short_doc'] = first_documentation_paragraph

            # Build properties table
            properties_table = """
# Properties\n\n
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
            property_descs = {p["name"]: p for p in element_desc[__class__.PROPERTIES]}
            for property_name in [default_property_name] + list(
                filter(lambda x: x != default_property_name, property_descs.keys())
            ):
                property_desc = property_descs[property_name]
                name = property_desc[__class__.NAME]
                type = property_desc["type"]
                if m := re.match(r"dynamic\((.*?)\)", type):
                    type = f"<code>{m[1]}</code><br/><i>dynamic</i>"
                elif m := re.match(r"indexed\((.*?)\)", type):
                    type = f"<code>{m[1]}</code><br/><i>indexed</i>"
                else:
                    type = f"<code>{type}</code>"
                default_value = property_desc.get("default_value", None)
                doc = property_desc.get("doc", None)
                if not default_value:
                    default_value = (
                        "<i>Required</i>"
                        if property_desc.get("required", False)
                        else ""
                    )
                full_name = f"<code id=\"p-{re.sub('<[^>]+>', '', name)}\">"
                if name == default_property_name:
                    full_name += f'<u><bold>{name}</bold></u></code><sup><a href="#dv">{STAR}</a></sup>'
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
            match = FIRST_HEADER_RE.match(element_documentation)
            if not match:
                raise ValueError(
                    f"Couldn't locate first header in documentation for element '{element_type}'"
                )
            before_properties = match.group(1)
            after_properties = match.group(2) + element_documentation[match.end() :]

            # Chart hook
            if element_type == "chart":
                values = self.chart_page_hook(
                    element_documentation, before_properties, after_properties
                )
                before_properties = values[0]
                after_properties = values[1]

            with open(f"{element_desc['doc_path']}/{element_type}.md", "w") as md_file:
                md_file.write(
                    f"---\ntitle: <tt>{element_type}</tt>\nhide:\n  - navigation\n---\n\n"
                    + f"<!-- Category: {category} -->\n"
                    + before_properties
                    + properties_table
                    + after_properties
                )
            e = element_type  # Shortcut
            d = "../corelements/" if prefix == "core_" else ""
            s = (
                ' style="font-size: .8em;"'
                if e == "scenario_selector" or e == "data_node_selector"
                else ""
            )
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
                md_template = md_template.replace(
                    f"[{prefix}TOC]", toc[prefix] + "</div>\n"
                )
            md_file.write(md_template)

    def generate_builder_api(self) -> None:
        separator = "# Generated code for Page Builder"
        py_file = "taipy/gui/builder/__init__.py"
        py_content = None
        with open(py_file, "r") as file:
            py_content = file.read()
        # Remove generated code
        if m := re.search(f"\\n*{separator}", py_content):
            py_content = py_content[:m.start(0)+1]

        def generate(self, category, base_class: str) -> str:

            element_types = self.categories[category]
            def build_doc(property: str, desc, indent: int):
                type = desc['type']
                dynamic = ""
                dynamic_re = re.match(r"^dynamic\(\s*(.*)\s*\)$", type)
                if False and dynamic_re:
                    type = dynamic_re[1]
                    dynamic = " (<i>dynamic</i>)"
                doc = ""
                if "doc" in desc:
                    doc = str(desc["doc"])
                    # Update internal links
                    new_doc = ""
                    last_loc = 0
                    INNER_HREF = re.compile(r"(?<=<a\shref=\")(#|\.)")
                    for a in INNER_HREF.finditer(doc):
                        new_doc += doc[last_loc:a.start()]
                        new_doc += f"../../gui/viselements/{element_type}/{a.group(0)}"
                        last_loc = a.end()
                    if last_loc:
                        doc = new_doc + doc[last_loc:]
                    doc = doc.replace("\n", f'\n{(indent+4)*" "}').replace("<br/>", f'<br/>\n{(indent+4)*" "}')
                default_value = f'{desc["default_value"]}' if "default_value" in desc else ""
                if m := re.match(r"^(<i>.*?</i>)$", default_value):
                    default_value = f"\"{m[1]}\""
                elif m := re.match(r"^`(.*?)`$", default_value):
                    default_value = f"{m[1]}"
                elif default_value == "scatter" or default_value == "lines+markers":
                    default_value = f"\"{default_value}\""
                if default_value:
                    try:
                        _ = eval(default_value)
                    except Exception:
                        raise SyntaxError(f"Default value for property '{property}' of element '{element_type}' is not a valid Python expression ({default_value})")
                return (f"{property}={default_value if default_value else 'None'}, ", 
                        f"{indent*' '}{desc['name']} ({type}){dynamic}: {doc}\n")

            template = f"""

class [element_type]({base_class}):
    '''[short_doc]

    This class represents the [control_or_block] documented in the [element_md_page] section.
    '''
    _ELEMENT_NAME: str
    def __init__(self, [arguments]) -> None:
        '''Create a new `[element_type]` element.

        Arguments:
            [arguments_doc]
        '''
        ...
"""

            buffer = StringIO()
            docline_in_template = next(l for l in template.splitlines() if l.lstrip().startswith("[arguments_doc]"))
            doc_indent = len(docline_in_template) - len(docline_in_template.lstrip())

            for element_type in element_types:
                desc = self.elements[element_type]
                properties = desc["properties"]
                default_prop = next(
                    p for p in properties if p["name"] == desc["default_property"]
                )
                doc = build_doc(default_prop['name'], default_prop, doc_indent)
                arguments = doc[0]
                arguments_doc = doc[1]
                for property in properties:
                    property_name = property["name"]
                    if property_name != desc["default_property"] and "[" not in property_name:
                        doc = build_doc(property_name, property, doc_indent)
                        arguments += doc[0]
                        arguments_doc += doc[1]
                # Process short doc
                short_doc = desc["short_doc"]
                if m := re.search(r"(\[`(\w+)`\]\()\2\.md\)", short_doc):
                    short_doc = short_doc[:m.start()]+f"{m[1]}../gui/viselements/{m[2]}.md)"+short_doc[m.end():]
                # Link to element doc page
                element_md_location = "corelements" if desc["prefix"] == "core_" else "viselements"
                element_md_page = f"[`{element_type}`](../gui/{element_md_location}/{element_type}.md)"
                buffer.write(template.replace("[element_type]", element_type)
                                     .replace("[element_md_page]", element_md_page)
                                     .replace("[arguments]", arguments)
                                     .replace("[short_doc]", short_doc)
                                     .replace("[control_or_block]", "control" if category=="controls" else "block")
                                     .replace(" "*doc_indent+"[arguments_doc]\n", arguments_doc))
            return buffer.getvalue()

        with open(py_file, "wt") as file:
            file.write(py_content)
            file.write(f"\n\n{separator}\n\n")
            file.write("from ._element import _Block, _Control\n\n")
            file.write(generate(self, "controls", "_Control"))
            file.write(generate(self, "blocks",   "_Block"))

    def setup(self, setup: Setup) -> None:
        self.generate_pages("controls", self.controls_path)
        self.generate_pages("blocks", self.blocks_path)
        self.generate_builder_api()

    # Special case for charts: we want to insert the chart gallery that is stored in the
    # file whose path is in self.charts_home_html_path
    # This should be inserted before the first level 1 header
    def chart_page_hook(
        self, element_documentation: str, before: str, after: str
    ) -> tuple[str, str]:
        with open(self.charts_home_html_path, "r") as html_fragment_file:
            chart_gallery = html_fragment_file.read()
            # The chart_gallery begins with a comment where all sub-sections
            # are listed.
        SECTIONS_RE = re.compile(
            r"^(?:\s*<!--\s+)(.*?)(?:-->)", re.MULTILINE | re.DOTALL
        )
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

        match = re.match(
            r"(^.*?)(?:\n#\s+)", element_documentation, re.MULTILINE | re.DOTALL
        )
        if not match:
            raise ValueError(
                "Couldn't locate first header1 in documentation for element 'chart'"
            )
        return (
            match.group(1) + chart_gallery + before[match.end() :],
            after + chart_sections,
        )

    
    def process_element_md_file(self, type: str, documentation: str) -> str:
        DEF_RE = re.compile(r"^!!!\s+taipy-element\s*?\n((?:\s+\w+(?:\[.*?\])?(?::\w+)?\s*=\s*.*\n)*)", re.M)
        PROP_RE = re.compile(r"(\w+(?:\[.*?\])?)(?::(\w+))?\s*=\s*(.*)\n", re.M)
        new_documentation = ""
        last_location = 0
        for definition in DEF_RE.finditer(documentation):
            new_documentation += documentation[last_location:definition.start()]
            default_property = ""
            properties = []
            for p in PROP_RE.finditer(definition.group(1)):
                if p[1] == "default":
                    default_property = p[3]
                else:
                    properties.append((p[1], p[3], p[2] if p[2] else "-"))
            new_documentation += "!!! example \"Definition\"\n\n"
            # Markdown format
            def md_property_value(property: str, value: str, type: str) -> str:
                if type.startswith("b"):
                    if value.lower() == "true":
                        return property
                    if value.lower() != "false":
                        raise ValueError(
                            f"Invalid value for Boolean property '{property}' in '{type}.md_template'"
                        )
                    if type.endswith("dont"):
                        return f"don't {property}"
                    return f"not {property}"
                return f"{property}={value}"
            new_documentation += "    === \"Markdown\"\n\n"
            new_documentation += "        ```\n"
            new_documentation += "        <|"
            if default_property:
                new_documentation += f"{default_property}|"
            new_documentation += f"{type}|"
            for n, v, t in properties:
                new_documentation += f"{md_property_value(n, v, t)}|"
            new_documentation += ">\n"
            new_documentation += "        ```\n\n"
            # HTML format

            def html_value(property: str, value: str, type: str) -> str:
                if type.startswith("b"):
                    if value.lower() == "true":
                        return f"{property}"
                    else:
                        value = value.lower()
                value = value.replace("\"", "'")
                return f"{property}=\"{value}\""
            new_documentation += "    === \"HTML\"\n\n"
            new_documentation += "        ```html\n"
            new_documentation += f"        <taipy:{type}"
            html_1 = ""
            html_2 = ""
            if properties:
                for n, v, t in properties:
                    html_1 += f" {html_value(n, v, t)}"
            if default_property:
                html_1 += ">"
                html_2 = f"{default_property}</taipy:{type}>"
            else:
                html_1 += "/>"
            new_documentation += f"{html_1}"
            if len(html_1) > 120 and html_2:
                new_documentation += "\n        "
            new_documentation += f"{html_2}\n        ```\n\n"
            # Page Builder syntax
            new_documentation += "    === \"Python\"\n\n"
            new_documentation += "        ```python\n"
            new_documentation += "        import taipy.gui.builder as tgb\n        ...\n"
            new_documentation += f"        tgb.{type}("
            def builder_value(value: str, type: str) -> str:
                if type == "f":
                    return value
                if type.startswith("b"):
                    return value.title()
                value = value.replace("\"", "'")
                return f"\"{value}\""
            prefix = ""
            if default_property:
                new_documentation += f"\"{default_property}\""
                prefix = ", "
            for n, v, t in properties:
                new_documentation += f"{prefix}{n}={builder_value(v, t)}"
                prefix = ", "
                if "[" in n:
                    print(f"WARNING - Property '{n}' in examples for {type}")
            new_documentation += ")\n"
            new_documentation += "        ```\n"
            last_location = definition.end()
        return new_documentation + documentation[last_location:] if documentation else documentation
