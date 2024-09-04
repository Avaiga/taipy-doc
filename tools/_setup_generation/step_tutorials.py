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
# integration, large_data, finance, decision_support, llm, visualization or other)
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
    APPLICATIONS_FOLDER_NAME = "articles"
    NO_CONTENT_TYPE_FOLDERS = ["images", "articles"]

    def __init__(self):
        self.content_types = self._initialize_content_types()
        self.TUTORIALS_BASE_PATH = None
        self.APPLICATIONS_BASE_PATH = None

    def _initialize_content_types(self) -> Dict[str, Dict]:
        # Define your content types here. You can add or remove any type according to your needs.
        return {}

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

    def enter(self, setup: Setup):
        self.TUTORIALS_BASE_PATH = os.path.join(setup.docs_dir, self.TUTORIALS_FOLDER_NAME)
        self.APPLICATIONS_BASE_PATH = os.path.join(self.TUTORIALS_BASE_PATH, self.APPLICATIONS_FOLDER_NAME)

        items = os.listdir(self.TUTORIALS_BASE_PATH)

        # Filter out only the directories
        self.content_types = {item: [] for item in items if os.path.isdir(os.path.join(self.TUTORIALS_BASE_PATH, item)) and item not in self.NO_CONTENT_TYPE_FOLDERS}

        for content_type in self.content_types.keys():
            folder_path = os.path.join(self.TUTORIALS_BASE_PATH, content_type)
            self.content_types[content_type] = {
                "folder_path": folder_path,
                "index_path": os.path.join(folder_path, "index.md"),
            }

    def get_id(self) -> str:
        return "tutorials_step"

    def get_description(self) -> str:
        return "Generates the list of items for the tutorials index page from various content types."

    def setup(self, setup: Setup):
        items_info = {}
        items = self._get_list_of_items(self.APPLICATIONS_BASE_PATH)
        for content_type, paths in self.content_types.items():
            sublist_of_items = [items for items in items if items.category == content_type]
            content, items_info_category = self._build_content(sublist_of_items)
            self._update_index_file(paths["index_path"], content)
            print(f"{len(sublist_of_items)} {content_type} items processed.")
            items_info.update(items_info_category)
        content = self._build_content_for_main_index(items_info)
        self._update_tutorials_index_file(content)

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
        items_info = {}
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        items = sorted(items, key=lambda item: item.order)
        for item in items:
            items_info[(item.category, item.order)] = item.generate_content_for_article(main_index=True)
            content = item.generate_content_for_article()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines), items_info

    def _build_content_for_main_index(self, items_info: dict):
        items_info = dict(sorted(items_info.items()))
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        for item in items_info.values():
            lines.append(item)
        lines.append("</ul>")
        return "\n".join(lines)

    def _update_index_file(self, index_path: str, content: str):
        with open(index_path+"_template") as file:
            tpl_content = file.read()
        updated_content = re.sub(r"\[LIST_OF_ITEMS\]", content, tpl_content)
        with open(index_path, "w") as file:
            file.write(updated_content)

    def _update_tutorials_index_file(self, content):
        with open(self.TUTORIALS_BASE_PATH + "/index.md_template") as file:
            tpl_content = file.read()
        updated_content = re.sub(r"\[LIST_OF_ITEMS\]", content, tpl_content)
        with open(self.TUTORIALS_BASE_PATH + "/index.md", "w") as file:
            file.write(updated_content)

    def exit(self, setup: Setup):
        pass
