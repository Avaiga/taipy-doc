# ################################################################################
# Taipy GUI Visual Elements documentation.
#
# This includes the update of the Table of Contents for the controls and blocks
# documentation page.
#
# For each visual element, this script combines its property list and core
# documentation, and generates full Markdown files in [GENERICELEMENTS_DIR_PATH]. All
# these files ultimately get integrated in the global doc set.
#
# The skeleton documentation files
# [GENERICELEMENTS_DIR_PATH]/[controls|blocks].md_template
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

    def __init__(self):
        self.navigation = ""
        self.navigation_by_library = {}

    def get_id(self) -> str:
        return "viselements"

    def get_description(self) -> str:
        return "Extraction of the visual elements documentation"

    def enter(self, setup: Setup):
        self.FE_DIR_PATH = setup.root_dir
        self.VISELEMENTS_DIR_PATH = setup.ref_manuals_dir + "/gui/viselements"
        self.TOC_PATH = self.VISELEMENTS_DIR_PATH + "/index.md"
        self.GENERICELEMENTS_DIR_PATH = self.VISELEMENTS_DIR_PATH + "/generic"
        self.CORELEMENTS_DIR_PATH = self.VISELEMENTS_DIR_PATH + "/corelements"
        self.CHARTS_HOME_HTML_PATH = (
            self.GENERICELEMENTS_DIR_PATH + "/charts/home.html_fragment"
        )
        self.__check_paths()

        # Use a VELoader to load all the visual elements from the json files,
        # check the elements are valid,
        # and keep only the categories we need for the documentation.
        loader = VELoader(
            self.DEFAULT_PROPERTY, self.PROPERTIES, self.INHERITS, self.NAME
        )
        loader.load(
            setup.root_dir + "/taipy/gui/viselements.json",
            "",
            self.GENERICELEMENTS_DIR_PATH,
        )
        loader.load(
            setup.root_dir + "/taipy/gui_core/viselements.json",
            "core_",
            self.CORELEMENTS_DIR_PATH,
        )
        loader.check()
        categories_to_keep = {"controls", "blocks"}
        self.categories = {
            k: loader.categories[k]
            for k in categories_to_keep
            if k in loader.categories
        }
        self.elements = loader.elements
        self.mui_icons = None

    def setup(self, setup: Setup) -> None:
        self.__read_mui_icons()
        tocs = self.__generate_element_pages()
        self.__build_navigation()
        self.__generate_toc_file(tocs)
        self.__generate_builder_api()

    # Read MUI icons symbol names from mui-icons.svg if it exists, so we can check references
    # from Markdown body text.
    def __read_mui_icons(self):
        SVG_ICON_RE = re.compile(r"<symbol\s+id=\"(.*?)\"")
        self.mui_icons = None
        mui_icons_path = self.VISELEMENTS_DIR_PATH + "/mui-icons.svg"
        if os.path.isfile(mui_icons_path):
            with open(mui_icons_path, "r") as file:
                content = file.read()
                self.mui_icons = [m[1] for m in SVG_ICON_RE.finditer(content)]

    def __check_paths(self):
        if not os.access(f"{self.TOC_PATH}_template", os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.TOC_PATH}_template template file"
            )
        if not os.access(self.CHARTS_HOME_HTML_PATH, os.R_OK):
            raise FileNotFoundError(
                f"FATAL - Could not read {self.CHARTS_HOME_HTML_PATH} html fragment"
            )

    def __generate_element_pages(self) -> Dict[str, str]:
        tocs = {}
        for category in self.categories:
            for element_type in self.categories[category]:
                hook = self.__build_hook(element_type, category)
                if hook not in tocs:
                    tocs[hook] = VEToc('<div class="tp-ve-cards">\n', "</div>\n", hook)
                tocs[hook].add(
                    element_type,
                    category,
                    self.__generate_element_doc(element_type, category),
                )
        return tocs

    def __build_hook(self, element_type, category: str) -> str:
        return f"[{self.elements[element_type]['prefix']}{category}_TOC]"

    def __build_navigation(self):
        for k in self.navigation_by_library:
            if not k == "Blocks":
                self.navigation += self.navigation_by_library[k]
        self.navigation += self.navigation_by_library["Blocks"]

    def __generate_toc_file(self, tocs: Dict[str, VEToc]):
        with open(f"{self.TOC_PATH}_template") as template_file:
            md_template = template_file.read()
            if not md_template:
                raise FileNotFoundError(
                    f"FATAL - Could not read {self.TOC_PATH}_template Markdown template"
                )
            with open(self.TOC_PATH, "w") as md_file:
                for hook, toc in tocs.items():
                    md_template = md_template.replace(hook, str(toc))
                md_file.write(md_template)

    @staticmethod
    def __get_navigation_section(category: str, prefix: str) -> str:
        if category == "blocks":
            return "Blocks"
        if prefix == "core_":
            return "Scenario and Data management controls"
        return "Standard controls"

    def __generate_element_doc(self, element_type: str, category: str):
        """
        Generates the Markdown file for a given element type with a given category.

        Returns the entry for the Table of Contents that is inserted
        in the global Visual Elements or Core Elements doc page.
        """
        element_desc = self.elements[element_type]
        section = self.__get_navigation_section(category, element_desc["prefix"])
        folder = "corelements/" if element_desc["prefix"] == "core_" else "generic/"
        if self.navigation_by_library.get(section) is None:
            self.navigation_by_library[section] = f'- "{section}":\n'
        self.navigation_by_library[section] += (
            f'    - "{element_type}": refmans/gui/viselements/{folder}{element_type}.md\n'
        )
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
        element_desc["short_doc"] = first_documentation_paragraph

        element_documentation = self.__process_element_md_file(
            element_type, element_documentation
        )

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
                    "<i>Required</i>" if property_desc.get("required", False) else ""
                )
            full_name = f"<code id=\"p-{re.sub('<[^>]+>', '', name)}\">"
            if name == default_property_name:
                full_name += f'<u><bold>{name}</bold></u></code><sup><a href="#dv">{STAR}</a></sup>'
            else:
                full_name += f"{name}</code>"
            # Hack to replace the element name placeholder by the actual element name
            if name == "class_name":
                doc = doc.replace("[element_type]", element_type)
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
        before_properties = match[1]
        after_properties = match[2] + element_documentation[match.end() :]

        # Chart hook
        if element_type == "chart":
            before_properties, after_properties = self.__chart_page_hook(
                element_documentation,
                before_properties,
                after_properties,
                f"{element_desc['doc_path']}/charts",
            )

        # Check potential MUI icons
        if self.mui_icons is not None:
            for m in re.finditer(r"\[MUI\s*:s*(.*?)s*\]", after_properties):
                if m[1] not in self.mui_icons:
                    print(
                        f"WARNING: Unknown MUI icon '{m[1]}' used in doc for element '{element_type}'"
                    )

        # Generate the Markdown output
        with open(f"{element_desc['doc_path']}/{element_type}.md", "w") as md_file:
            md_file.write(
                f"---\ntitle: <tt>{element_type}</tt>\nsearch:\n  boost: 2\n---\n\n"
                + f"<!-- Category: {category} -->\n"
                + before_properties
                + properties_table
                + after_properties
            )
        e = element_type  # Shortcut
        folder = "corelements/" if element_desc["prefix"] == "core_" else "generic/"
        s = (
            ' style="font-size: .8em;"'
            if e == "scenario_selector" or e == "data_node_selector"
            else ""
        )
        return (
            f'<a class="tp-ve-card" href="./{folder}{e}/">\n'
            + f"<div{s}>{e}</div>\n"
            + f'<img class="tp-ve-l" src="./{folder}{e}-l.png"/><img class="tp-ve-lh" src="./{folder}{e}-lh.png"/>\n'
            + f'<img class="tp-ve-d" src="./{folder}{e}-d.png"/><img class="tp-ve-dh" src="./{folder}{e}-dh.png"/>\n'
            + f"<p>{first_documentation_paragraph}</p>\n"
            + "</a>\n"
        )
        # If you want a simple list, use
        # f"<li><a href=\"../{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
        # The toc header and footer must then be "<ui>" and "</ul>" respectively.

    def __generate_builder_api(self) -> None:
        separator = "# Generated code for Page Builder"
        py_file = "taipy/gui/builder/__init__.py"
        py_content = None
        with open(py_file, "r") as file:
            py_content = file.read()
        # Remove generated code
        if m := re.search(f"\\n*{separator}", py_content):
            py_content = py_content[: m.start(0) + 1]

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
                        new_doc += doc[last_loc : a.start()]
                        new_doc += f"../../../refmans/gui/viselements/{element_type}/{a.group(0)}"
                        last_loc = a.end()
                    if last_loc:
                        doc = new_doc + doc[last_loc:]
                    doc = doc.replace("\n", f'\n{(indent+4)*" "}').replace(
                        "<br/>", f'<br/>\n{(indent+4)*" "}'
                    )
                default_value = (
                    f'{desc["default_value"]}' if "default_value" in desc else ""
                )
                if m := re.match(r"^(<(\w+)>.*?</\2>)$", default_value):
                    default_value = f'"{m[1]}"'
                if default_value:
                    try:
                        _ = eval(default_value)
                    except Exception:
                        if "lambda" not in default_value:
                            print(
                                f"WARNING: Default value for property '{property}' of element "
                                f"'{element_type}' is not a valid Python expression ({default_value})"
                            )
                return (
                    f"{property}={default_value if default_value else 'None'}, ",
                    f"{indent*' '}{desc['name']} ({type}){dynamic}: {doc}\n",
                )

            template = f"""

class [element_type]({base_class}):
    \"\"\"[short_doc]

    data-viselement: [control_or_block] [element_md_page]
    \"\"\"
    def __init__(self, [arguments]) -> None:
        \"\"\"Create a new `[element_type]` element.

        Arguments:
            [arguments_doc]
        \"\"\"
        ...
"""

            buffer = StringIO()
            docline_in_template = next(
                l
                for l in template.splitlines()
                if l.lstrip().startswith("[arguments_doc]")
            )
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
                    if (
                        property_name != desc["default_property"]
                        and "[" not in property_name
                    ):
                        doc = build_doc(property_name, property, doc_indent)
                        arguments += doc[0]
                        arguments_doc += doc[1]
                # Process short doc
                short_doc = desc["short_doc"]
                # Link to element doc page
                element_md_location = (
                    "corelements" if desc["prefix"] == "core_" else "generic"
                )
                if m := (re.search(r"(\[`(\w+)`\]\()\2\.md\)", short_doc)):
                    # Replacing links from the doc in the Python source to another element
                    # At this time, this works only if the source and target elements are in the
                    # same directory (generic, corelements or blocks).
                    short_doc = (
                        short_doc[: m.start()]
                        + f"<a href=\"../{m[2]}/\"><tt>{m[2]}</tt></a>"
                        + short_doc[m.end() :]
                    )

                element_md_page = (
                    f"[`{element_type}`](../../../../../../refmans/gui/viselements/{element_md_location}"
                    f"/{element_type}.md)"
                )
                buffer.write(
                    template.replace("[element_type]", element_type)
                    .replace("[element_md_page]", element_md_page)
                    .replace("[arguments]", arguments)
                    .replace("[short_doc]", short_doc)
                    .replace(
                        "[control_or_block]",
                        "control" if category == "controls" else "block",
                    )
                    .replace(" " * doc_indent + "[arguments_doc]\n", arguments_doc)
                )
            return buffer.getvalue()

        with open(py_file, "wt") as file:
            file.write(py_content)
            file.write(f"\n\n{separator}\n\n")
            file.write("from ._element import _Block, _Control\n\n")
            file.write(generate(self, "controls", "_Control"))
            file.write(generate(self, "blocks", "_Block"))

    # Special case for charts: we want to insert the chart gallery that
    # is stored in the file whose path is in self.charts_home_html_path
    # This should be inserted before the first header.
    # Simultaneously, we build a list of chart types to point to type pages as text.
    # This should be inserted before the "Styling" header.
    def __chart_page_hook(
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
        for line in match[1].splitlines():
            if match := SECTION_RE.match(line):
                type = match.group(1)
                chart_sections += f"\n- [{match.group(2)}](charts/{type}.md)"
                # Generate chart type documentation page from template, if possible
                template_doc_path = f"{charts_md_dir}/{type}.md_template"
                if os.access(template_doc_path, os.R_OK):
                    with open(template_doc_path, "r") as template_doc_file:
                        documentation = template_doc_file.read()
                        documentation = self.__process_element_md_file(
                            "chart", documentation
                        )
                    with open(f"{charts_md_dir}/{type}.md", "w") as md_file:
                        md_file.write(documentation)

        match = re.match(
            r"(^.*?)(?:\n#\s+)", element_documentation, re.MULTILINE | re.DOTALL
        )
        if not match:
            raise ValueError(
                "Couldn't locate first header1 in documentation for element 'chart'"
            )
        styling_match = re.search(r"\n# Styling\n", after, re.MULTILINE | re.DOTALL)
        if not styling_match:
            raise ValueError(
                "Couldn't locate \"Styling\" header1 in documentation for element 'chart'"
            )
        return (
            match[1] + chart_gallery + before[match.end() :],
            after[: styling_match.start()]
            + chart_sections
            + "\n\n"
            + after[styling_match.start() :],
        )

    def __process_element_md_file(self, type: str, documentation: str) -> str:
        DEF_RE = re.compile(
            r"^!!!\s+taipy-element\s*?\n((?:\s+\w+(?:\[.*?\])?(?::\w+)?\s*=\s*.*\n)*)",
            re.M,
        )
        PROP_RE = re.compile(r"(\w+(?:\[.*?\])?)(?::(\w+))?\s*=\s*(.*)\n", re.M)
        new_documentation = ""
        last_location = 0
        for definition in DEF_RE.finditer(documentation):
            new_documentation += documentation[last_location : definition.start()]
            default_property = ""
            properties = []
            for p in PROP_RE.finditer(definition.group(1)):
                if p[1] == "default":
                    default_property = p[3]
                else:
                    properties.append((p[1], p[3], p[2] if p[2] else "-"))
            new_documentation += '!!! example "Definition"\n'

            # Page Builder syntax
            BP_IDX_PROP_RE = re.compile(r"^(.*?)\[([\w\d]+)\]$", re.M)
            generate_page_builder_api = True
            pb_properties = []
            for n, v, t in properties:
                if "[" in n:
                    if (idx_prop_match := BP_IDX_PROP_RE.match(n)) is None:
                        print(
                            f"WARNING - Property '{n}' in examples for {type} prevents Python code generation"
                        )
                        generate_page_builder_api = False
                    else:
                        pname = f"{idx_prop_match[1]}__{idx_prop_match[2]}"
                        pb_properties.append((pname, v, t))
                else:
                    pb_properties.append((n, v, t))
            if generate_page_builder_api:
                new_documentation += '    === "Python"\n'
                new_documentation += "        ```python\n"
                new_documentation += (
                    "        import taipy.gui.builder as tgb\n        ...\n"
                )
                new_documentation += f"        tgb.{type}("

                def builder_value(value: str, type: str) -> str:
                    if type in ["n", "f"]:
                        return value
                    if type.startswith("b"):
                        return value.title()
                    value = value.replace('"', "'")
                    return f'"{value}"'

                prefix = ""
                if default_property:
                    new_documentation += f'"{default_property}"'
                    prefix = ", "
                for n, v, t in pb_properties:
                    new_documentation += f"{prefix}{n}={builder_value(v, t)}"
                    prefix = ", "
                new_documentation += ")\n"
                new_documentation += "        ```\n"
            last_location = definition.end()

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
                    elif type.endswith("no"):
                        return f"no {property}"
                    return f"not {property}"
                if value.startswith("lambda"):
                    return f"{property}={{{value}}}"
                return f"{property}={value}"

            new_documentation += '    === "Markdown"\n'
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
                elif value.startswith("lambda"):
                    value = f"{{{value}}}"
                value = value.replace('"', "'")
                return f'{property}="{value}"'

            new_documentation += '    === "HTML"\n'
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

        return (
            new_documentation + documentation[last_location:]
            if documentation
            else documentation
        )

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[VISELEMENTS_CONTENT\]\s*\n",
            self.navigation if self.navigation else "",
        )
