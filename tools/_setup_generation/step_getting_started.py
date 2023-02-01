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
        self.navigation = {}
        self.GETTING_STARTED = "getting-started"
        self.GUI = "getting-started-gui"
        self.CORE = "getting-started-core"

    def get_id(self) -> str:
        return "getting_started"

    def get_description(self) -> str:
        return "Generating the Getting Started"

    def setup(self, setup: Setup) -> None:
        self.setup_repo(self.GUI)
        self.setup_repo(self.CORE)
        self.setup_repo(self.GETTING_STARTED)

    def setup_repo(self, repo):
        step_folders = glob.glob("docs/getting_started/" + repo + "/step_*")
        step_folders.sort()
        step_folders = map(lambda s: s[len('docs/getting_started/'):], step_folders)
        step_folders = map(self._format_getting_started_navigation, step_folders)
        self.navigation[repo] = "\n".join(step_folders) + '\n'

    def _format_getting_started_navigation(self,  filepath: str) -> str:
        readme_path = f"{filepath}/ReadMe.md".replace('\\', '/')
        readme_content = Path('docs/', 'getting_started/', readme_path).read_text().split('\n')
        step_name = next(filter(lambda l: "# Step" in l, readme_content))[len("# "):]
        return f"        - '{step_name}': '{readme_path}'"

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n",
            self.navigation[self.GETTING_STARTED] if self.navigation.get(self.GETTING_STARTED) else ""
        )
        setup.update_mkdocs_yaml_template(
            r"^\s*\[GETTING_STARTED_GUI_CONTENT\]\s*\n",
            self.navigation[self.GUI] if self.navigation.get(self.GUI) else ""
        )
        setup.update_mkdocs_yaml_template(
            r"^\s*\[GETTING_STARTED_CORE_CONTENT\]\s*\n",
            self.navigation[self.CORE] if self.navigation.get(self.CORE) else ""
        )
