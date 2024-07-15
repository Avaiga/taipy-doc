# ################################################################################
# Taipy GUI Visual Elements documentation.
#
# This includes the update of the Table of Contents for both the controls
# and blocks page.
#
# For each visual element, this script combines its property list and core
# documentation, and generates full Markdown files in [STANDARD_AND_BLOCKS_DIR_PATH]. All
# these files ultimately get integrated in the global doc set.
#
# The skeleton documentation files
# [STANDARD_AND_BLOCKS_DIR_PATH]/[controls|blocks].md_template
# are also completed with generated table of contents.
# ################################################################################
import os
import re
from io import StringIO
from typing import Dict

from .setup import Setup, SetupStep
from .viselements import VELoader, VEToc


class VisElementsStep(SetupStep):
    DEFAULT_PROPERTY = "default_property"
    PROPERTIES = "properties"
    INHERITS = "inherits"
    NAME = "name"

    def get_id(self) -> str:
        return "viselements"

    def get_description(self) -> str:
        return "Extraction of the visual elements documentation"

    def enter(self, setup: Setup):
        self.VISELEMENTS_DIR_PATH = setup.manuals_dir + "/userman/gui/viselements"
        self.STANDARD_AND_BLOCKS_DIR_PATH = setup.manuals_dir + "/userman/gui/viselements/standard-and-blocks"
        self.CORELEMENTS_DIR_PATH = setup.manuals_dir + "/userman/gui/viselements/corelements"
        self.TOC_PATH = self.VISELEMENTS_DIR_PATH + "/index.md"
        self.TOC_TEMPLATE_PATH = self.VISELEMENTS_DIR_PATH + "/viselements.md_template"
        self.CHARTS_HOME_HTML_PATH = self.STANDARD_AND_BLOCKS_DIR_PATH + "/charts/home.html_fragment"
        self.__check_paths()

        # Use a VELoader to load all the visual elements from the json files,
        # check the elements are valid,
        # and keep only the categories we need for the documentation.
        loader = VELoader(self.DEFAULT_PROPERTY, self.PROPERTIES, self.INHERITS, self.NAME)
        loader.load(setup.root_dir + "/taipy/gui/viselements.json", "", self.STANDARD_AND_BLOCKS_DIR_PATH)
        loader.load(setup.root_dir + "/taipy/gui_core/viselements.json", "core_", self.CORELEMENTS_DIR_PATH)
        loader.check()
        categories_to_keep = {"controls", "blocks"}
        self.categories = {k:loader.categories[k] for k in categories_to_keep if k in loader.categories}
        self.elements = loader.elements

    def setup(self, setup: Setup) -> None:
        tocs = self.__generate_element_pages()
        self.__generate_toc_file(tocs)
        self.generate_builder_api()

    def __check_paths(self):
        if not os.access(self.TOC_TEMPLATE_PATH, os.R_OK):
            raise FileNotFoundError(f"FATAL - Could not read {self.TOC_TEMPLATE_PATH} html fragment")
        if not os.access(self.CHARTS_HOME_HTML_PATH, os.R_OK):
            raise FileNotFoundError(f"FATAL - Could not read {self.CHARTS_HOME_HTML_PATH} html fragment")

    def __generate_element_pages(self) -> Dict[str, str]:
        tocs = {}
        for category in self.categories:
            for element_type in self.categories[category]:
                hook = self.__build_hook(element_type, category)
                if hook not in tocs:
                    tocs[hook] = VEToc('<div class="tp-ve-cards">\n', '</div>\n', hook)
                tocs[hook].add(element_type, category, self.__generate_element_doc(element_type, category))
        return tocs

    def __build_hook(self, element_type, category: str) -> str:
        return f"[{self.elements[element_type]['prefix']}{category}_TOC]"

    def __generate_toc_file(self, tocs: Dict[str, VEToc]):
        with open(self.TOC_TEMPLATE_PATH) as template_file:
            md_template = template_file.read()
            if not md_template:
                raise FileNotFoundError(f"FATAL - Could not read {self.TOC_TEMPLATE_PATH}_template markdown template")
            with open(self.TOC_PATH, "w") as md_file:
                for hook, toc in tocs.items():
                    md_template = md_template.replace(hook, str(toc))
                md_file.write(md_template)

    def __generate_element_doc(self, element_type: str, category: str):
        """
        Generates the markdown file for a given element type with a given category.

        Returns the entry for the Table of Contents that is inserted
        in the global Visual Elements or Core Elements doc page.
        """
        element_desc = self.elements[element_type]
        template_doc_path = f"{element_desc['doc_path']}/{element_type}.md_template"
        with open(template_doc_path, "r") as template_doc_file:
            element_documentation = template_doc_file.read()
        # Retrieve first paragraph from element documentation
        FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
        match = FIRST_PARA_RE.match(element_documentation)
        if not match:
            raise ValueError(
                f"Couldn't locate first paragraph in documentation for element '{element_type}'"
            )
        first_documentation_paragraph = match.group(1)
        element_desc['short_doc'] = first_documentation_paragraph

        element_documentation = self.process_element_md_file(element_type, element_documentation)

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
        default_property_name = element_desc[self.DEFAULT_PROPERTY]
        # Convert properties array to a dict
        property_descs = {p["name"]: p for p in element_desc[self.PROPERTIES]}
        for property_name in [default_property_name] + list(
            filter(lambda x: x != default_property_name, property_descs.keys())
        ):
            property_desc = property_descs[property_name]
            name = property_desc[self.NAME]
            doc = property_desc.get("doc", "")
            if doc.startswith("UNDOCUMENTED"):
                continue
            type = property_desc["type"]
            if m := re.match(r"dynamic\((.*?)\)", type):
                type = f"<code>{m[1]}</code><br/><i>dynamic</i>"
            elif m := re.match(r"indexed\((.*?)\)", type):
                type = f"<code>{m[1]}</code><br/><i>indexed</i>"
            else:
                type = f"<code>{type}</code>"
            default_value = property_desc.get("default_value", None)
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
        # Find first level 2 or 3 header
        FIRST_HEADER_RE = re.compile(r"(^.*?)(\n#+\s+)", re.MULTILINE | re.DOTALL)
        match = FIRST_HEADER_RE.match(element_documentation)
        if not match:
            raise ValueError(
                f"Couldn't locate first header in documentation for element '{element_type}'"
            )
        before_properties = match.group(1)
        after_properties = match.group(2) + element_documentation[match.end():]

        # Chart hook
        if element_type == "chart":
            before_properties, after_properties = self.chart_page_hook(
                element_documentation, before_properties, after_properties,
                f"{element_desc['doc_path']}/charts"
            )

        with open(f"{element_desc['doc_path']}/{element_type}.md", "w") as md_file:
            md_file.write(
                f"---\ntitle: <tt>{element_type}</tt>\n---\n\n"
                + f"<!-- Category: {category} -->\n"
                + before_properties
                + properties_table
                + after_properties
            )
        e = element_type  # Shortcut
        d = "corelements/" if element_desc["prefix"] == "core_" else "standard-and-blocks/"
        s = (
            ' style="font-size: .8em;"'
            if e == "scenario_selector" or e == "data_node_selector"
            else ""
        )
        return (
            f'<a class="tp-ve-card" href="./{d}{e}/">\n'
            + f"<div{s}>{e}</div>\n"
            + f'<img class="tp-ve-l" src="./{d}{e}-l.png"/><img class="tp-ve-lh" src="./{d}{e}-lh.png"/>\n'
            + f'<img class="tp-ve-d" src="./{d}{e}-d.png"/><img class="tp-ve-dh" src="./{d}{e}-dh.png"/>\n'
            + f"<p>{first_documentation_paragraph}</p>\n"
            + "</a>\n"
        )
        # If you want a simple list, use
        # f"<li><a href=\"../{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
        # The toc header and footer must then be "<ui>" and "</ul>" respectively.

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
                type = desc["type"]
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
                        raise SyntaxError(f"Default value for property '{property}' of element '{element_type}' is "
                                          f"not a valid Python expression ({default_value})")
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
                doc = build_doc(default_prop["name"], default_prop, doc_indent)
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

    # Special case for charts: we want to insert the chart gallery that
    # is stored in the file whose path is in self.charts_home_html_path
    # This should be inserted before the first level 1 header
    def chart_page_hook(
        self, element_documentation: str, before: str, after: str, charts_md_dir: str
    ) -> tuple[str, str]:
        with open(self.CHARTS_HOME_HTML_PATH, "r") as html_fragment_file:
            chart_gallery = html_fragment_file.read()
            # The chart_gallery begins with a comment where all sub-sections
            # are listed.
        SECTIONS_RE = re.compile(
            r"^(?:\s*<!--\s+)(.*?)(?:-->)", re.MULTILINE | re.DOTALL
        )
        if not (match := SECTIONS_RE.match(chart_gallery)):
            raise ValueError(
                f"{self.CHARTS_HOME_HTML_PATH} should begin with an HTML comment that lists the chart types"
            )
        chart_gallery = "\n" + chart_gallery[match.end() :]
        SECTION_RE = re.compile(r"^([\w-]+):(.*)$")
        chart_sections = ""
        for line in match.group(1).splitlines():
            if match := SECTION_RE.match(line):
                type = match.group(1)
                chart_sections += f"- [{match.group(2)}](charts/{type}.md)\n"
                template_doc_path = f"{charts_md_dir}/{type}.md_template"
                # Generate chart type documentation page if possible
                if os.access(template_doc_path, os.R_OK):
                    with open(template_doc_path, "r") as template_doc_file:
                        documentation = template_doc_file.read()
                        documentation = self.process_element_md_file('chart', documentation)
                    with open(f"{charts_md_dir}/{type}.md", "w") as md_file:
                        md_file.write(documentation)

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
            new_documentation += "!!! example \"Definition\"\n"
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
            new_documentation += "\n    === \"Markdown\"\n\n"
            new_documentation += "        ```\n"
            new_documentation += "        <|"
            if default_property:
                new_documentation += f"{default_property}|"
            new_documentation += f"{type}|"
            for n, v, t in properties:
                new_documentation += f"{md_property_value(n, v, t)}|"
            new_documentation += ">\n"
            new_documentation += "        ```\n"
            # HTML format
            def html_value(property: str, value: str, type: str) -> str:
                if type.startswith("b"):
                    if value.lower() == "true":
                        return f"{property}"
                    else:
                        value = value.lower()
                value = value.replace("\"", "'")
                return f"{property}=\"{value}\""
            new_documentation += "\n    === \"HTML\"\n\n"
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
            new_documentation += f"{html_2}\n        ```\n"
            # Page Builder syntax "^$"
            BP_IDX_PROP_RE = re.compile(r"^(.*?)\[([\w\d]+)\]$", re.M)
            generate_page_builer_api = True
            pb_properties = []
            for n, v, t in properties:
                if "[" in n:
                    if (idx_prop_match := BP_IDX_PROP_RE.match(n)) is None:
                        print(f"WARNING - Property '{n}' in examples for {type} prevents Python code generation")
                        generate_page_builer_api = False
                    else:
                        pname = f"{idx_prop_match[1]}__{idx_prop_match[2]}"
                        pb_properties.append((pname, v, t))
                else:
                    pb_properties.append((n, v, t))
            if generate_page_builer_api:
                new_documentation += "\n    === \"Python\"\n\n"
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
                for n, v, t in pb_properties:
                    new_documentation += f"{prefix}{n}={builder_value(v, t)}"
                    prefix = ", "
                new_documentation += ")\n"
                new_documentation += "        ```\n"
            last_location = definition.end()
        return new_documentation + documentation[last_location:] if documentation else documentation
