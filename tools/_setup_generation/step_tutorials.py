# ##########################################################################################
# Step to generate the list of tutorials items in the tutorials index page
#
# The tutorials index page is generated from all the folders beneath folders.
# Each folder contains a list of sub folders, each sub folder is a tutorials item.
# Each item has an index.md file with a header containing the necessary information to
# generate the list of items in the tutorials index page.
#
# The header of an item is a multiline header starting with '---' and ending with '---'.
# The header contains the following information:
# - title: The title of the item
# - category: The category of the item (fundamentals, visuals, scenario_management, 
# integration or large data)
# - type: The type of the item (code, video or article)
# - data-keywords: A comma separated list of keywords
# - short-description: A short description of the item
# - img: The path to the image associated with the item
#
# ##########################################################################################

import os
import re
from typing import List, Dict

from .setup import SetupStep, Setup
from .items import FolderItem, FileItem, Item
from .items.exceptions import WrongHeader, NoHeader, NoIndexFile

class TutorialsStep(SetupStep):
    TUTORIALS_FOLDER_NAME = "tutorials"

    def __init__(self):
        self.content_types = self._initialize_content_types()

    def _initialize_content_types(self) -> Dict[str, Dict]:
        # Define your content types here. You can add or remove any type according to your needs.
        return {
            "fundamentals": {},
            "scenario_management": {},
            "visuals": {},
            "integration": {},
            "large_data": {}
        }

    def enter(self, setup: Setup):
        tutorials_base_path = os.path.join(setup.docs_dir, self.TUTORIALS_FOLDER_NAME)
        for content_type in self.content_types.keys():
            folder_path = os.path.join(tutorials_base_path, content_type)
            self.content_types[content_type] = {
                "folder_path": folder_path,
                "index_path": os.path.join(folder_path, "index.md"),
            }

    def get_id(self) -> str:
        return "tutorials_step"

    def get_description(self) -> str:
        return "Generates the list of items for the tutorials index page from various content types."

    def setup(self, setup: Setup):
        for content_type, paths in self.content_types.items():
            items = self._get_list_of_items(paths["folder_path"])
            content = self._build_content(items)
            self._update_index_file(paths["index_path"], content)
            print(f"{len(items)} {content_type} items processed.")

    def _get_list_of_items(self, folder_path) -> List[Item]:
        items = []
        for sub_folder in os.listdir(folder_path):
            path = os.path.join(folder_path, sub_folder)
            if os.path.isdir(path) and sub_folder != "images":
                try:
                    item = FolderItem(folder_path, sub_folder)
                    items.append(item)
                except NoIndexFile as e:
                    print(f"WARNING - ", e)
        return items

    def _build_content(self, items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        items = sorted(items, key=lambda item: item.href)
        for item in items:
            content = item.generate_content_for_article()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines)

    def _update_index_file(self, index_path: str, content: str):
        with open(index_path+"_template") as file:
            tpl_content = file.read()
        updated_content = re.sub(r"\[LIST_OF_ITEMS\]", content, tpl_content)
        with open(index_path, "w") as file:
            file.write(updated_content)

    def exit(self, setup: Setup):
        pass
