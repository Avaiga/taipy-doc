import os

from .item import Item


class FolderItem(Item):
    def __init__(self, parent_path: str, folder_name: str):
        self.folder_name = folder_name
        file_path = os.path.join(parent_path, folder_name, "index.md")
        super().__init__(parent_path, file_path)

    @property
    def href(self) -> str:
        """Return the href path."""
        return self.folder_name + "/"
