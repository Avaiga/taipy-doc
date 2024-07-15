import json
import os
from typing import Optional


class VELoader:
    """
    Class to load visual elements from a JSON file.

    The JSON file must contain a list of visual elements, each element being a list of two elements:
    - The first element is the element type
    - The second element is a dictionary containing the properties of the element. The dictionary may
        contain the following keys:
        - "properties": a list of properties for the element
        - "inherits": a list of element types to inherit from
        - "name": the name of the element
    """

    def __init__(self, default_property: str, properties: str, inherits: str, name: str):
        self.default_property = default_property
        self.properties = properties
        self.inherits = inherits
        self.name = name

        self.elements = {}
        self.categories = {}

    def load(self, json_path: str, prefix: str, doc_dir_path: str):
        """
        Load all visual elements described in elements_json_path and populate the elements
        and categories dictionaries. Check basic features and resolve inheritance.

        Args:
            json_path: Path to the JSON file containing the visual elements
            prefix: Prefix to add to the element type
            doc_dir_path: Path to the directory that will contain the generated documentation

        Returns:
            All the elements as a dictionary
        """

        # Read the JSON file
        with open(json_path) as elements_json_file:
            loaded_elements = json.load(elements_json_file)

        # Parse the JSON file and get the new elements to add
        new_elements = {}
        for category, elements in loaded_elements.items():
            if category not in self.categories:
                self.categories[category] = []
            for element in elements:
                element_type = element[0]
                self.categories[category].append(element_type)
                if element_type in self.elements:
                    raise ValueError(f"FATAL - Duplicate element type '{element_type}' in {json_path}")
                element_desc = element[1]
                if self.properties not in element_desc and self.inherits not in element_desc:
                    raise ValueError(f"FATAL - No properties in element type '{element_type}' in {json_path}")
                element_desc["prefix"] = prefix
                element_desc["doc_path"] = doc_dir_path
                element_desc["source"] = json_path
                new_elements[element_type] = element_desc

        # Add the new elements to the elements dictionary
        self.elements.update(new_elements)

        # Find default property for all element types
        # and remove hidden properties.
        for element_type, element_desc in new_elements.items():
            default_property = None
            if properties := element_desc.get(self.properties, None):
                for property in properties:
                    if self.default_property in property:
                        if property[self.default_property]:
                            default_property = property[self.name]
                        del property[self.default_property]
                    if property.get("hide", False):
                        property["doc"] = "UNDOCUMENTED"
            element_desc[self.default_property] = default_property

        # Resolve inheritance
        for element_desc in self.elements.values():
            self.__resolve_inheritance(element_desc)

    def check(self):
        """
        Check all the elements loaded are valid.

        Raises:
            ValueError: If an element type does not have a default property or properties
            FileNotFoundError: If a template file is missing
        """
        for category, element_type in [(c, e) for c, elts in self.categories.items() for e in elts]:
            if category == "undocumented":
                continue
            element_desc = self.elements[element_type]
            if self.default_property not in element_desc:
                raise ValueError(f"FATAL - No default property for element type '{element_type}'")
            if self.properties not in element_desc:
                raise ValueError(f"FATAL - No properties for element type '{element_type}'")
            template_path = f"{element_desc['doc_path']}/{element_type}.md_template"
            if not os.access(template_path, os.R_OK):
                raise FileNotFoundError(f"FATAL - Could not find template doc file for element type"
                                        f" '{element_type}' at {template_path}")
            # Check completeness
            for property in element_desc[self.properties]:
                for n in ["type", "doc"]:
                    if n not in property:
                        raise ValueError(f"FATAL - No value for '{n}' in the "
                                         f"'{property[self.name]}' properties of "
                                         f"element type '{element_type}' in {element_desc['source']}")

    def __resolve_inheritance(self, element_desc):
        if parent_types := element_desc.get(self.inherits, None):
            del element_desc[self.inherits]
            original_default_property = element_desc[self.default_property]
            default_property = original_default_property
            for parent_type in parent_types:
                parent_desc = self.elements[parent_type]
                self.__resolve_inheritance(parent_desc)
                default_property = self.__merge(element_desc, parent_desc, default_property)
            if original_default_property != default_property:
                element_desc[self.default_property] = default_property

    def __merge(self, element_desc, parent_element_desc, default_property: str) -> Optional[str]:
        element_properties = element_desc.get(self.properties, [])
        element_property_names = [p[self.name] for p in element_properties]
        for property in parent_element_desc.get(self.properties, []):
            property_name = property[self.name]
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
        element_desc[self.properties] = element_properties
        if not default_property and parent_element_desc.get(
            self.default_property, False
        ):
            default_property = parent_element_desc[self.default_property]
        return default_property
