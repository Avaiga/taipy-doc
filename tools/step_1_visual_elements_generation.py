import re
import warnings

import pandas as pd

from constants import *
from utils import read_skeleton, restore_top_package_location


def generate_viz_elements():
    controls_md_template = read_skeleton("controls", GUI_DOC_PATH)
    blocks_md_template = read_skeleton("blocks", GUI_DOC_PATH)

    controls_list = ["text", "button", "input", "number", "slider", "toggle", "date", "chart", "file_download",
                     "file_selector", "image", "indicator", "menu", "navbar", "selector", "status", "table", "dialog",
                     "tree"]

    blocks_list = ["part", "expandable", "layout", "pane"]
    # -----------------------------------------------------------------------------
    # Read all element properties, including parent elements that are not
    # actual visual elements (shared, lovComp...)
    # -----------------------------------------------------------------------------
    element_properties = {}
    element_documentation = {}
    INHERITED_PROP = 1 << 0
    DEFAULT_PROP = 1 << 1
    MANDATORY_PROP = 1 << 2
    property_prefixes = {
        ">": INHERITED_PROP,
        "*": DEFAULT_PROP,
        "!": MANDATORY_PROP
    }
    for current_file in os.listdir(VISELEMENTS_SRC_PATH):
        def read_properties(path_name, element_name):
            try:
                df = pd.read_csv(path_name, encoding='utf-8')
            except Exception as e:
                raise RuntimeError(f"{path_name}: {e}")
            properties = []
            # Row fields: name, type, default_value, doc
            for row in list(df.to_records(index=False)):
                prop_flags = 0
                prop_name = row[0]
                while prop_name[0] in property_prefixes:
                    prop_flags |= property_prefixes.get(prop_name[0])
                    prop_name = prop_name[1:]
                if prop_flags & INHERITED_PROP:  # Inherits?
                    parent_props = element_properties.get(prop_name)
                    if parent_props is None:
                        parent_file = prop_name + ".csv"
                        parent_path_name = os.path.join(VISELEMENTS_SRC_PATH, parent_file)
                        if not os.path.exists(parent_path_name):
                            restore_top_package_location(ROOT_DIR, ROOT_PACKAGE, TOOLS_DIR)
                            raise ValueError(f"FATAL - No csv file for '{prop_name}', inherited by '{element_name}'")
                        parent_props = read_properties(parent_path_name, prop_name)
                    # Merge inherited properties
                    for parent_prop in parent_props:
                        try:
                            prop_index = [p[1] for p in properties].index(parent_prop[1])
                            p = list(properties[prop_index])
                            if p[2] == ">":
                                p[2] = parent_prop[2]
                                print(f"WARNING: Element {element_name}: legacy '>' in '{p[1]}''s Type")
                            # Testing for equality detects NaN
                            properties[prop_index] = (p[0], p[1],
                                                      p[2] if p[2] == p[2] else parent_prop[2],
                                                      p[3] if p[3] == p[3] else parent_prop[3],
                                                      p[4] if p[4] == p[4] else parent_prop[4])
                        except:
                            properties.append(parent_prop)
                else:
                    row[0] = prop_name
                    row = (prop_flags, prop_name, *row.tolist()[1:])
                    properties.append(row)
            default_property_name = None
            for i, props in enumerate(properties):
                # TODO: Remove properties that have an hidden type
                # props = (flags, name, type, default value,description)
                if props[0] & DEFAULT_PROP:  # Default property?
                    name = props[1]
                    if default_property_name and name != default_property_name:
                        warnings.warn(
                            f"Property '{name}' in '{element_name}': default property already defined as {default_property_name}")
                    default_property_name = name
                # Fix Boolean default property values
                if str(props[3]).lower() == "false":
                    properties[i] = (props[0], props[1], props[2], "False", props[4])
                elif str(props[3]).lower() == "true":
                    properties[i] = (props[0], props[1], props[2], "True", props[4])
                elif props[3] != props[3]:  # Empty cell in CSV - Pandas parsing
                    default_value = "<i>Mandatory</i>" if props[0] & MANDATORY_PROP else ""
                    properties[i] = (props[0], props[1], props[2], default_value, props[4])
            if not default_property_name and (element_name in controls_list + blocks_list):
                restore_top_package_location()
                raise ValueError(f"Element '{element_name}' has no defined default property")
            element_properties[element_name] = properties
            return properties


        path_name = os.path.join(VISELEMENTS_SRC_PATH, current_file)
        element_name = os.path.basename(current_file)
        element_name, current_file_ext = os.path.splitext(element_name)
        if current_file_ext == ".csv":
            if not element_name in element_properties:
                read_properties(path_name, element_name)
        elif current_file_ext == ".md":
            with open(path_name, "r") as doc_file:
                element_documentation[element_name] = doc_file.read()

    # Create VISELEMS_DIR_PATH directory if necessary
    if not os.path.exists(VISELEMENTS_DIR_PATH):
        os.mkdir(VISELEMENTS_DIR_PATH)

    FIRST_PARA_RE = re.compile(r"(^.*?)(:?\n\n)", re.MULTILINE | re.DOTALL)
    FIRST_HEADER2_RE = re.compile(r"(^.*?)(\n##\s+)", re.MULTILINE | re.DOTALL)


    def generate_element_doc(element_name: str, toc):
        """
        Returns the entry for the Table of Contents that is inserted
        in the global Visual Elements doc page.
        """
        properties = element_properties[element_name]
        documentation = element_documentation[element_name]
        # Retrieve first paragraph from element documentation
        match = FIRST_PARA_RE.match(documentation)
        if not match:
            restore_top_package_location()
            raise ValueError(f"Couldn't locate first paragraph in documentation for element '{element_name}'")
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
        default_property_name = None
        for flags, name, type, default_value, doc in properties:
            if flags & DEFAULT_PROP:
                default_property_name = name
                full_name = f"<code id=\"p-{default_property_name}\"><u><bold>{default_property_name}</bold></u></code><sup><a href=\"#dv\">{STAR}</a></sup>"
            else:
                full_name = f"<code id=\"p-{name}\">{name}</code>"
            properties_table += ("<tr>\n"
                                 + f"<td nowrap>{full_name}</td>\n"
                                 + f"<td>{type}</td>\n"
                                 + f"<td nowrap>{default_value}</td>\n"
                                 + f"<td><p>{doc}</p></td>\n"
                                 + "</tr>\n")
        properties_table += "  </tbody>\n</table>\n\n"
        if default_property_name:
            properties_table += (f"<p><sup id=\"dv\">{STAR}</sup>"
                                 + f"<a href=\"#p-{default_property_name}\" title=\"Jump to the default property documentation.\">"
                                 + f"<code>{default_property_name}</code></a>"
                                 + " is the default property for this visual element.</p>\n")

        # Insert title and properties in element documentation
        match = FIRST_HEADER2_RE.match(documentation)
        if not match:
            restore_top_package_location()
            raise ValueError(f"Couldn't locate first header2 in documentation for element '{element_name}'")
        output_path = os.path.join(VISELEMENTS_DIR_PATH, element_name + ".md")
        with open(output_path, "w") as output_file:
            output_file.write("---\nhide:\n  - navigation\n---\n\n"
                              + f"# <tt>{element_name}</tt>\n\n"
                              + match.group(1)
                              + properties_table
                              + match.group(2) + documentation[match.end():])
        e = element_name  # Shortcut
        return (f"<a class=\"tp-ve-card\" href=\"../viselements/{e}/\">\n"
                + f"<div>{e}</div>\n"
                + f"<img class=\"tp-ve-l\" src=\"../viselements/{e}-l.png\"/>\n"
                + f"<img class=\"tp-ve-lh\" src=\"../viselements/{e}-lh.png\"/>\n"
                + f"<img class=\"tp-ve-d\" src=\"../viselements/{e}-d.png\"/>\n"
                + f"<img class=\"tp-ve-dh\" src=\"../viselements/{e}-dh.png\"/>\n"
                + f"<p>{first_documentation_paragraph}</p>\n"
                + "</a>\n")
        # If you want a simple list, use
        # f"<li><a href=\"../viselements/{e}/\"><code>{e}</code></a>: {first_documentation_paragraph}</li>\n"
        # The toc header and footer must then be "<ui>" and "</ul>" respectively.


    # Generate controls doc page
    toc = "<div class=\"tp-ve-cards\">\n"
    for name in controls_list:
        toc += generate_element_doc(name, toc)
    toc += "</div>\n"
    with open(os.path.join(GUI_DOC_PATH, "controls.md"), "w") as file:
        file.write(controls_md_template.replace("[TOC]", toc))

    # Generate blocks doc page
    toc = "<div class=\"tp-ve-cards\">\n"
    for name in blocks_list:
        toc += generate_element_doc(name, toc)
    toc += "</div>\n"
    with open(os.path.join(GUI_DOC_PATH, "blocks.md"), "w") as file:
        file.write(blocks_md_template.replace("[TOC]", toc))
