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
        self.navigation = None

    def get_id(self) -> str:
        return "getting_started"

    def get_description(self) -> str:
        return "Generating the Getting Started"

    def setup(self, setup: Setup) -> None:
        def format_getting_started_navigation(filepath: str) -> str:
            readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
            readme_content = Path('docs', readme_path).read_text().split('\n')
            step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
            return f"    - '{step_name}': '{readme_path}'"

        step_folders = glob.glob("docs/getting_started/step_*")
        step_folders.sort()
        step_folders = map(lambda s: s[len('docs/'):], step_folders)
        step_folders = map(format_getting_started_navigation, step_folders)
        self.navigation = "\n".join(step_folders) + '\n'


    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n", self.navigation
        )
