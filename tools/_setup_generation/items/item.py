import os
from typing import TextIO, Dict, List

from .exceptions import WrongHeader, NoHeader, NoIndexFile


class Item:
    CATEGORIES = ["fundamentals", "scenario_management", "visuals", "integration", "large_data",
                  "finance", "decision_support", "llm", "visualization", "other"]
    TYPES = ["code", "video", "article"]

    def __init__(self, parent_path: str, file_path: str):
        self.parent_path = parent_path # ex: docs/tutorials/fundamentals
        self.file_path = file_path # ex: docs/tutorials/fundamentals/1_understanding_gui/index.md
        if not os.path.exists(self.file_path):
            raise NoIndexFile(f"File {self.file_path} not found")
        with open(self.file_path) as file:
            self.header = self._read_header(file)
            self.title = self.header.get("title")
            self.category = self.header.get("category", "scenario_management")
            self.data_keywords = self.header.get("data-keywords")
            self.short_description = self.header.get("short-description")
            self.img = self.header.get("img")
        self._check_header()

    @property
    def href(self) -> str:
        raise NotImplemented

    @property
    def icon(self) -> str:
        """Return the icon path."""
        return f"images/icon-code.svg"

    def generate_content_for_article(self, main_index=False) -> str:
        """Generate content of an HTML list item."""
        tags_lov = ["enterprise"]
        path_to_img = '/'.join([self.category, self.img]) if main_index else self.img
        href = '/'.join([self.category, self.href]) if main_index else self.href
        lines: List[str] = list()
        lines.append(f'  <li class="tp-col-12 tp-col-md-6 d-flex" data-keywords="{self.data_keywords}">')
        lines.append(f'    <a class="tp-content-card tp-content-card--horizontal tp-content-card--small" href="'
                     f'{href}">')
        lines.append(f'      <header class="tp-content-card-header">')
        lines.append(f'        <img class="tp-content-card-image" src="{path_to_img}">')
        lines.append(f'      </header>')
        lines.append(f'      <div class="tp-content-card-body">')
        lines.append(f'        <h4>{self.title}</h4>')
        for tag in tags_lov:
            if tag in self.data_keywords:
                lines.append(f'        <span class="tp-tag">{tag}</span>')
        lines.append(f'        <p>')
        lines.append(f'          {self.short_description}')
        lines.append(f'        </p>')
        lines.append(f'      </div>')
        lines.append(f'    </a>')
        lines.append(f'  </li>')
        return "\n".join(lines)
    

    def _read_header(self, file: TextIO) -> Dict[str, str]:
        """Read a multiline header starting with '---' and ending with '---'."""
        header_content = {}
        line = file.readline()
        if line.strip() != "---":
            raise NoHeader(f"No header found in {self.file_path}")
        line = file.readline()
        while line.strip() != "---":
            k, v = self._split_header_line(line)
            if k in header_content:
                raise WrongHeader(f"Duplicate key '{k}' in {self.file_path} header.")
            header_content[k] = v
            line = file.readline()
        return header_content

    @staticmethod
    def _split_header_line(header_line: str) -> (str, str):
        """Split a header line to a key and value pair."""
        key, value = header_line.split(":")
        return key.strip(), value.strip()

    def _check_header(self):
        """Check the header content."""
        errors = []
        if not self.title:
            errors.append(f"Missing title in {self.file_path} header")
        if self.category not in self.CATEGORIES:
            errors.append(f"Invalid category '{self.category}' in {self.file_path}")
        if not self.data_keywords:
            errors.append(f"Missing data-keywords in {self.file_path} header")
        if not self.short_description:
            errors.append(f"Missing short_description in {self.file_path} header")
        if len(errors) > 0:
            raise WrongHeader("\n".join(errors))
