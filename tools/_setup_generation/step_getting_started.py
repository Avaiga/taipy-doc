# ################################################################################
# Taipy Getting Started generation setup step.
#
# Files are listed and sorted after being copied from the taipy-getting-started
# repository.
# ################################################################################
from .setup import Setup, SetupStep
import glob
from pathlib import Path


class GettingStartedStep(SetupStep):
    def __init__(self):
        # {page: (pattern_to_replace, content)}
        self.DEFAULT_CONTENT = {
            "getting-started": (r"\[GETTING_STARTED_CONTENT\]", ""),
            "getting-started-gui": (r"\[GETTING_STARTED_GUI_CONTENT\]", ""),
            "getting-started-core": (r"\[GETTING_STARTED_CORE_CONTENT\]", "")
        }
        self.content = dict()

    def get_id(self) -> str:
        return "getting_started"

    def get_description(self) -> str:
        return "Generating the Getting Started"

    def setup(self, setup: Setup) -> None:
        for page in self.DEFAULT_CONTENT.keys():
            self.get_content_for_page(page)

    def get_content_for_page(self, page):
        step_folders = glob.glob("docs/getting_started/" + page + "/step_*")
        step_folders.sort()
        step_folders = map(lambda s: s[len('docs/getting_started/'):], step_folders)
        step_folders = map(self._format_getting_started_navigation, step_folders)

        self.content[page] = (self.DEFAULT_CONTENT[page][0], "\n".join(step_folders) + '\n')

    def _format_getting_started_navigation(self, filepath: str) -> str:
        readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
        readme_content = Path('docs/', 'getting_started/', readme_path).read_text().split('\n')
        step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
        return f"        - '{step_name}': '{readme_path}'"

    def exit(self, setup: Setup):
        for page_key in self.content.keys():
            setup.update_mkdocs_yaml_template(r"^\s*" + self.content[page_key][0] + r"\s*\n", self.content[page_key][1])
