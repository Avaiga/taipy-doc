import os
from abc import ABC, abstractmethod
from datetime import datetime
import re
import shutil
import sys
from typing import List


class Setup(ABC):
    ROOT_PACKAGE = "taipy"

    ENTERPRISE_BANNER = """!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

"""

    def __init__(self, root_dir: str, steps: List["SetupStep"]):
        self.root_dir = root_dir.replace("\\", "/")
        self.docs_dir = self.root_dir + "/docs"
        self.user_manuals_dir = self.docs_dir + "/userman"
        self.ref_manuals_dir = self.docs_dir + "/refmans"
        self.tools_dir = self.root_dir + "/tools"
        # self.requested_steps, if not None, indicates which steps should be performed.
        self.requested_steps = None
        if len(sys.argv) > 1:
            self.requested_steps = []
            for step_id in sys.argv[1:]:
                if not [step for step in steps if step_id == step.get_id()]:
                    raise SystemError(
                        f"FATAL - '{step_id}' is not a valid step identifier"
                    )
            for step in steps:
                if step.get_id() in sys.argv[1:]:
                    self.requested_steps.append(step)
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
            if not self.requested_steps or step in self.requested_steps:
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
            print(
                f"{line}\n| Step {step_index + 1}/{n_steps}{description}\n{line}",
                flush=True,
            )
            step.setup(self)

    def exit(self):
        for step in self.steps:
            step.exit(self)
        self.update_mkdocs_yaml_template(r"\[YEAR\]", f"{str(datetime.now().year)}")
        with open(self.MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
            mkdocs_yml_file.write(self.mkdocs_yml_template_content)

    # Utility function to update the MkDocs yml template file
    def update_mkdocs_yaml_template(self, pattern: str, replacement: str):
        # Retrieve and keep indentation
        if pattern.startswith(r"^\s*"):
            pattern = r"^(\s*)" + pattern[4:]
            lines = replacement.split("\n")
            if not lines[-1]:
                lines = lines[:-1]
            replacement = "\n".join(map(lambda s: r"\1" + s, lines)) + "\n"

        self.mkdocs_yml_template_content = re.sub(
            pattern,
            replacement if replacement else "",
            self.mkdocs_yml_template_content,
            flags=re.MULTILINE | re.DOTALL,
        )

    # Move the top package directory to 'tools' when generating the Reference
    # Manual, or when using Taipy classes.
    # MkDocs needs it at the root level, so we will have to move it back.
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


def run_setup(root_dir: str, steps: List[SetupStep] = None):
    if not steps:
        from .step_tutorials import TutorialsStep
        from .step_gallery import GalleryStep
        from .step_viselements import VisElementsStep
        from .step_refman import RefManStep
        from .step_rest_refman import RestRefManStep
        from .step_gui_ext_refman import GuiExtRefManStep
        from .step_mui_icons import MuiIconsStep
        from .step_contributors import ContributorsStep
        from .step_file_injection import FileInjectionStep
        from .step_designer import DesignerStep

        steps = [
            GalleryStep(),
            TutorialsStep(),
            VisElementsStep(),
            RefManStep(),
            RestRefManStep(),
            GuiExtRefManStep(),
            MuiIconsStep(),
            ContributorsStep(),
            FileInjectionStep("installation",
                              "Generating the installation page.",
                              "[INSTALLATION]",
                              os.path.join("taipy-doc-files", "INSTALLATION.md"),
                              os.path.join("tutorials", "getting_started", "installation.md")),
            FileInjectionStep("code_of_conduct",
                              "Generating the code of conduct page.",
                              "[CODE_OF_CONDUCT]",
                              os.path.join("taipy-doc-files", "CODE_OF_CONDUCT.md"),
                              os.path.join("contributing", "code_of_conduct.md")),
            FileInjectionStep("contributing",
                              "Generating the contributing page.",
                              "[CONTRIBUTING]",
                              os.path.join("taipy-doc-files", "CONTRIBUTING.md"),
                              os.path.join("contributing", "index.md")),
            DesignerStep(),
        ]
    setup = Setup(root_dir, steps)
    setup.setup()
    setup.exit()
