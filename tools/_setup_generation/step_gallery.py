# ##########################################################################################
# Step to generate the list of gallery items in the gallery index page
#
# The gallery index page is generated from all the gallery.
# Each demo is an index.md file with a header containing the necessary information to
# generate the list of items in the gallery index page.
#
# The header of an item is a multiline header starting with '---' and ending with '---'.
# The header contains the following information:
# - title: The title of the item
# - category: The category of the item (tutorials, gallery or tips)
# - type: The type of the item (code, video or article)
# - data-keywords: A comma separated list of keywords
# - short_description: A short description of the item
#
# ##########################################################################################
import os
import re
from typing import List

from .setup import SetupStep, Setup
from .items import FolderItem, FileItem, Item
from .items.exceptions import WrongHeader, NoHeader, NoIndexFile


class GalleryStep(SetupStep):

    # The name of the gallery folder
    GALLERY_FOLDER_NAME = "gallery"

    # The placeholders in the gallery index file to be replaced by the generated content
    GALLERY_PLACEHOLDER = r"\[LIST_FOR_GALLERY\]"

    def __init__(self):
        self.GALLERY_FOLDER_PATH = None
        self.GALLERY_INDEX_PATH = None
        self.GALLERY_INDEX_TEMPLATE_PATH = None
        self.gallery = ""


    def enter(self, setup: Setup):
        self.GALLERY_FOLDER_PATH = os.path.join(setup.docs_dir, self.GALLERY_FOLDER_NAME)
        self.GALLERY_INDEX_PATH = os.path.join(self.GALLERY_FOLDER_PATH, "index.md")
        self.GALLERY_INDEX_TEMPLATE_PATH = os.path.join(self.GALLERY_FOLDER_PATH, "index.md_template")
  
    def get_id(self) -> str:
        return "gallery"

    def get_description(self) -> str:
        return "Generating the list of items on the gallery page."

    def setup(self, setup: Setup) -> None:
        try:
            # Parse the gallery folders and get all the items
            gallery_items = self._get_list_of_items(self.GALLERY_FOLDER_PATH)

            # Generate content for the kb index page
            self.gallery = self._build_gallery_content(gallery_items)
            self._update_gallery_index_file()

            print(f"{len(gallery_items)} gallery items processed.")
        except Exception as e:
            print(f"WARNING - Exception raised while generating the gallery index:\n{e}")

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
            except (NoHeader, WrongHeader) as e:
                print(f"WARNING - ", e)
        return items

    @staticmethod
    def _build_gallery_content(items: List[Item]) -> str:
        lines: List[str] = list()
        lines.append('<ul class="tp-row tp-row--gutter-sm tp-filtered">')
        for item in items:
            content = item.generate_content_for_gallery()
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
    def _replace(pattern, by: str, in_content: str):
        return re.sub(pattern, by, in_content)

    def _update_gallery_index_file(self):
        with open(self.GALLERY_INDEX_TEMPLATE_PATH) as gallery_index_file:
            gallery_index_content = gallery_index_file.read()
        gallery_index_content = self._replace(self.GALLERY_PLACEHOLDER, self.gallery, gallery_index_content)
        with open(self.GALLERY_INDEX_PATH, "w") as gallery_index_file:
            gallery_index_file.write(gallery_index_content)
