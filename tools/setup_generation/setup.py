from abc import ABC, abstractmethod
from datetime import datetime
import os
import re
import shutil
from typing import List


class Setup(ABC):
    ROOT_PACKAGE = "taipy"

    ENTERPRISE_BANNER = """!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

"""

    def __init__(self, root_dir: str, steps: List["SetupStep"]):
        self.root_dir = root_dir.replace("\\", "/")
        self.docs_dir = self.root_dir + "/docs"
        self.manuals_dir = self.docs_dir + "/manuals"
        self.tools_dir = self.root_dir + "/tools"
        self.requested_steps = None  # Can be used later to filter out steps to be performed
        self.mkdocs_yml_template_content = None
        self.MKDOCS_YML_PATH = self.root_dir + "/mkdocs.yml"
        self.MKDOCS_YML_TEMPLATE_PATH = self.MKDOCS_YML_PATH + "_template"
        with open(self.MKDOCS_YML_TEMPLATE_PATH) as mkdocs_yml_file:
            self.mkdocs_yml_template_content = mkdocs_yml_file.read()
        if not self.mkdocs_yml_template_content:
            raise SystemError(
                "FATAL - Could not read MkDocs template configuration file at {MKDOCS_YML_TEMPLATE_PATH}"
            )
        self.steps = []
        for step in steps:
            if self.requested_steps is None or step.get_id() in self.requested_steps:
                self.steps.append(step)
                step.enter(self)
            else:
                step.exit(self)

    def setup(self):
        n_steps = len(self.steps)
        line = "+" + "-" * 60
        for step_index, step in enumerate(self.steps):
            description = step.get_description()
            if description:
                description = f": {description}"
            print(f"{line}\n| Step {step_index+1}/{n_steps}{description}\n{line}")
            step.setup(self)

    def exit(self):
        for step in self.steps:
            step.exit(self)
        self.update_mkdocs_yaml_template(r"\[YEAR\]", f"{str(datetime.now().year)}")
        with open(self.MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
            mkdocs_yml_file.write(self.mkdocs_yml_template_content)

    # Utility function to update the MkDocs yml template file
    def update_mkdocs_yaml_template(self, pattern, replacement):
        self.mkdocs_yml_template_content = re.sub(
            pattern,
            replacement if replacement else "",
            self.mkdocs_yml_template_content,
            flags=re.MULTILINE | re.DOTALL,
        )

    # Move the top package directory to 'tools' when generating the Reference
    # Manual, or when using Taipy classes.
    # MkDocs needs it at the root level so we will have to move it back.
    def move_package_to_tools(self, package: str) -> None:
        shutil.move(f"{self.root_dir}/{package}", f"{self.tools_dir}/{package}")

    def move_package_to_root(self, package: str) -> None:
        shutil.move(f"{self.tools_dir}/{package}", f"{self.root_dir}/{package}")


class SetupStep(ABC):
    @abstractmethod
    def get_id(self) -> str:
        return ""

    def get_description(self) -> str:
        return ""

    def enter(self, setup: Setup):
        pass

    def exit(self, setup: Setup):
        """Called after the step is executed.

        Note that this member function is also called, before _enter()_,
        if this step is skipped.
        """
        pass

    @abstractmethod
    def setup(self, setup: Setup):
        pass

def run_setup(root_dir: str, steps: List[SetupStep]):
    setup = Setup(root_dir, steps)
    setup.setup()
    setup.exit()
