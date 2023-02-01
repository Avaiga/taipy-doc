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
        # {page: (title, content)}
        self.DEFAULT_CONTENT = {
            "getting-started-gui": ('Getting started with GUI', ""),
            "getting-started-core": ('Getting started with Core', ""),
            "getting-started": ('Getting started with Taipy', ""),
        }
        self.content = []

    def get_id(self) -> str:
        return "getting_started"

    def get_description(self) -> str:
        return "Generating the Getting Started"

    def setup(self, setup: Setup) -> None:
        for page in self.DEFAULT_CONTENT.keys():
            self.set_content_for_page(page)
        self.content = "\n".join(self.content) + "\n"

    def set_content_for_page(self, page):
        step_folders = glob.glob("docs/getting_started/" + page + "/step_*")
        step_folders.sort()
        print(len(step_folders))
        step_folders = map(lambda s: s[len('docs/'):], step_folders)
        step_folders = map(self._format_page_content, step_folders)

        content = f"    - '{self.DEFAULT_CONTENT[page][0]}':\n"
        content += f"      - getting_started/{page}/index.md\n"
        content += "\n".join(step_folders)
        self.content.append(content)

    def _format_page_content(self, filepath: str) -> str:
        readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
        readme_content = Path('docs/', readme_path).read_text().split('\n')
        step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
        return f"      - '{step_name}': '{readme_path}'"

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n", self.content)
