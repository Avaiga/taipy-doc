import os

from .item import Item


class FileItem(Item):
    def __init__(self, parent_path: str, file_name: str):
        self.file_name = file_name
        self.file_base_name = os.path.splitext(file_name)[0]
        file_path = os.path.join(parent_path, self.file_name)
        super().__init__(parent_path, file_path)

    @property
    def href(self) -> str:
        """Return the href path."""
        return self.file_base_name + "/"
