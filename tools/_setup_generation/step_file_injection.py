# ################################################################################
# Taipy installation page generation setup step.
#
# ################################################################################
import os

from .setup import SetupStep, Setup


class FileInjectionStep(SetupStep):

    def __init__(self, id, desc, pattern, src_relative_path, dest_relative_path):
        self.id = id
        self.desc = desc
        self.src_relative_path = src_relative_path
        self.dest_relative_path = dest_relative_path

        self.pattern = pattern
        self.src_path = None
        self.dst_path = None
        self.dst_tpl_path = None

    def enter(self, setup: Setup):
        self.src_path = os.path.join(setup.root_dir, self.src_relative_path)
        self.dst_path = os.path.join(setup.docs_dir, self.dest_relative_path)
        self.dst_tpl_path = os.path.join(setup.docs_dir, str(self.dest_relative_path) + "_template")

    def get_id(self) -> str:
        return self.id

    def get_description(self) -> str:
        return self.desc

    def setup(self, setup: Setup) -> None:
        try:
            with open(self.src_path, "r", encoding="utf-8") as file:
                content = file.read()
                self._replace(self.dst_tpl_path, self.pattern, content, self.dst_path)
        except Exception as e:
            print(f"ERROR - Cannot generate page: {e}")

    @staticmethod
    def _replace(in_tpl_file_path, pattern, by, into_file_path):
        # Read template file
        with open(in_tpl_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        # Replace the pattern by the contents
        content = content.replace(pattern, by)
        # Write the file to_file
        with open(into_file_path, "w", encoding="utf-8") as file:
            file.write(content)
