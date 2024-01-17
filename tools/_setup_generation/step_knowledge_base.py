# ##########################################################################################
# Step to generate the list of knowledge base items in the knowledge base index page
#
# The knowledge base index page is generated from the tutorials, demos and tips folders.
# Each folder contains a list of sub folders, each sub folder is a knowledge base item.
# Each item has an index.md file with a header containing the necessary information to
# generate the list of items in the knowledge base index page.
#
# The header of an item is a multiline header starting with '---' and ending with '---'.
# The header contains the following information:
# - title: The title of the item
# - category: The category of the item (tutorials, demos or tips)
# - type: The type of the item (code, video or article)
# - data-keywords: A comma separated list of keywords
# - short_description: A short description of the item
#
# ##########################################################################################
import os
import re
from typing import List

from .setup import SetupStep, Setup
from .step_knowedge_base import FolderItem, FileItem, Item
from .step_knowedge_base.exceptions import WrongHeader, NoHeader, NoIndexFile


class KnowledgeBaseStep(SetupStep):

    # The name of the knowledge base folder
    KNOWLEDGE_BASE_FOLDER_NAME = "knowledge_base"

    # The placeholders in the knowledge base index file to be replaced by the generated content
    TUTORIALS_PLACEHOLDER = r"\[LIST_OF_TUTORIALS\]"
    DEMOS_PLACEHOLDER = r"\[LIST_OF_DEMOS\]"
    TIPS_PLACEHOLDER = r"\[LIST_OF_TIPS\]"

    def __init__(self):
        self.KB_INDEX_PATH = None
        self.KB_INDEX_TEMPLATE_PATH = None
        self.TUTORIALS_FOLDER_PATHS = None
        self.TUTORIALS_INDEX_PATH = None
        self.TUTORIALS_INDEX_TPL_PATH = None
        self.DEMOS_FOLDER_PATHS = None
        self.DEMOS_INDEX_PATH = None
        self.DEMOS_INDEX_TPL_PATH = None
        self.TIPS_FOLDER_PATHS = None
        self.TIPS_INDEX_PATH = None
        self.TIPS_INDEX_TPL_PATH = None
        self.tutorials_on_kb = ""
        self.tutorials = ""
        self.demos_on_kb = ""
        self.demos = ""
        self.tips_on_kb = ""
        self.tips = ""

    def enter(self, setup: Setup):
        self.KB_INDEX_PATH = os.path.join(setup.docs_dir, self.KNOWLEDGE_BASE_FOLDER_NAME, "index.md")
        self.KB_INDEX_TEMPLATE_PATH = os.path.join(setup.docs_dir, self.KNOWLEDGE_BASE_FOLDER_NAME, "index.md_template")
        self.TUTORIALS_FOLDER_PATHS = os.path.join(setup.docs_dir, self.KNOWLEDGE_BASE_FOLDER_NAME, "tutorials")
        self.TUTORIALS_INDEX_PATH = os.path.join(self.TUTORIALS_FOLDER_PATHS, "index.md")
        self.TUTORIALS_INDEX_TPL_PATH = os.path.join(self.TUTORIALS_FOLDER_PATHS, "index.md_template")
        self.DEMOS_FOLDER_PATHS = os.path.join(setup.docs_dir, self.KNOWLEDGE_BASE_FOLDER_NAME, "demos")
        self.DEMOS_INDEX_PATH = os.path.join(self.DEMOS_FOLDER_PATHS, "index.md")
        self.DEMOS_INDEX_TPL_PATH = os.path.join(self.DEMOS_FOLDER_PATHS, "index.md_template")
        self.TIPS_FOLDER_PATHS = os.path.join(setup.docs_dir, self.KNOWLEDGE_BASE_FOLDER_NAME, "tips")
        self.TIPS_INDEX_PATH = os.path.join(self.TIPS_FOLDER_PATHS, "index.md")
        self.TIPS_INDEX_TPL_PATH = os.path.join(self.TIPS_FOLDER_PATHS, "index.md_template")
    def get_id(self) -> str:
        return "knowledge_base"

    def get_description(self) -> str:
        return "Generating the list of items on the knowledge base page."

    def setup(self, setup: Setup) -> None:
        try:
            # Parse the tutorials, demos and tips folders and get all the items
            tutorials_items = self._get_list_of_items(self.TUTORIALS_FOLDER_PATHS)
            demos_items = self._get_list_of_items(self.DEMOS_FOLDER_PATHS)
            tips_items = self._get_list_of_items(self.TIPS_FOLDER_PATHS)

            # Generate content for the tutorials index page
            self.tutorials = self._build_tutorials_content(tutorials_items)
            self._update_index_file(self.TUTORIALS_INDEX_TPL_PATH,
                                    self.TUTORIALS_INDEX_PATH,
                                    self.TUTORIALS_PLACEHOLDER,
                                    self.tutorials)

            # Generate content for the demos index page
            self.demos = self._build_demos_content(demos_items)
            self._update_index_file(self.DEMOS_INDEX_TPL_PATH,
                                    self.DEMOS_INDEX_PATH,
                                    self.DEMOS_PLACEHOLDER,
                                    self.demos)

            # Generate content for the tips index page
            self.tips = self._build_tips_content(tips_items)
            self._update_index_file(self.TIPS_INDEX_TPL_PATH,
                                    self.TIPS_INDEX_PATH,
                                    self.TIPS_PLACEHOLDER,
                                    self.tips)

            # Generate content for the kb index page
            self.tutorials_on_kb = self._build_content(tutorials_items)
            self.demos_on_kb = self._build_content(demos_items)
            self.tips_on_kb = self._build_content(tips_items)
            self._update_kb_index_file()

            print(f"{len(tutorials_items)} tutorials, {len(demos_items)} demos and {len(tips_items)} tips processed.")
        except Exception as e:
            print(f"WARNING - Exception raised while generating the knowledge base index:\n{e}")

    def exit(self, setup: Setup):
        pass

    @staticmethod
    def _get_list_of_items(folder_path) -> List[Item]:
        """List all folders in folder_path and return a list of Item objects built from the sub folders."""
        items = []
        for sub_folder in os.listdir(folder_path):
            path = os.path.join(folder_path, sub_folder)
            isdir = os.path.isdir(path)
            try:
                if isdir:
                    if sub_folder != "images":
                        try:
                            item = FolderItem(folder_path, sub_folder)
                            items.append(item)
                        except NoIndexFile as e:
                            print(f"WARNING - ", e)
                else:
                    if not sub_folder.startswith("index.md"):
                        item = FileItem(folder_path, sub_folder)
                        items.append(item)
            except NoHeader as e:
                print(f"WARNING - ", e)
            except WrongHeader as e:
                print(f"WARNING - ", e)
        return items

    @staticmethod
    def _build_tutorials_content(items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        for item in items:
            content = item.generate_content_for_tutorials()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines)

    @staticmethod
    def _build_demos_content(items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        for item in items:
            content = item.generate_content_for_demos()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines)

    @staticmethod
    def _build_tips_content(items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        for item in items:
            content = item.generate_content_for_tips()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines)

    def _update_index_file(self, read_file_path: str, write_file_path: str, placeholder:str, content: str):
        with open(read_file_path) as index_file:
            index_content = index_file.read()
        index_content = self._replace(placeholder, content, index_content)
        with open(write_file_path, "w") as index_file:
            index_file.write(index_content)

    @staticmethod
    def _build_content(items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-cards-list tp-filtered">')
        for item in items:
            content = item.generate_content_for_kb()
            lines.append(content)
        lines.append("</ul>")
        return "\n".join(lines)

    @staticmethod
    def _replace(pattern, by: str, in_content: str):
        return re.sub(pattern, by, in_content)

    def _update_kb_index_file(self):
        with open(self.KB_INDEX_TEMPLATE_PATH) as kb_index_file:
            kb_index_content = kb_index_file.read()
        kb_index_content = self._replace(self.TUTORIALS_PLACEHOLDER, self.tutorials_on_kb, kb_index_content)
        kb_index_content = self._replace(self.DEMOS_PLACEHOLDER, self.demos_on_kb, kb_index_content)
        kb_index_content = self._replace(self.TIPS_PLACEHOLDER, self.tips_on_kb, kb_index_content)
        with open(self.KB_INDEX_PATH, "w") as kb_index_file:
            kb_index_file.write(kb_index_content)
