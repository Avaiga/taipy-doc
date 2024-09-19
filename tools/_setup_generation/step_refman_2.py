# ################################################################################
# Taipy Reference Manual generation setup step.
#
# Generate the entries for every documented class, method, and function.
# This scripts browses the root package (Setup.ROOT_PACKAGE) and builds a
# documentation file for every package and every class it finds.
# It finally updates the top navigation bar content (in mkdocs.yml) to
# reflect the root package structure.
# ################################################################################
import os

from .refman.cleaner import Cleaner
from .refman.config_handler import ConfigHandler
from .refman.generator import Generator
from .setup import Setup, SetupStep


class RefManStep2(SetupStep):

    # Where the Reference Manual files are generated (MUST BE relative to docs_dir)
    REFERENCE_REL_PATH = "refmans/reference"

    def __init__(self):
        self.generator = None

    def get_id(self) -> str:
        return "refman"

    def get_description(self) -> str:
        return "Generation of the Reference Manual pages"

    def enter(self, setup: Setup):
        os.environ["GENERATING_TAIPY_DOC"] = "true"

    def setup(self, setup: Setup) -> None:
        # Remove previous Reference Manual files before to generate the new ones
        Cleaner(setup, self.REFERENCE_REL_PATH).clean()

        saved_dir = os.getcwd()
        try:
            os.chdir(setup.tools_dir)
            if not os.path.isdir(os.path.join(setup.tools_dir, Setup.ROOT_PACKAGE)):
                setup.move_package_to_tools(Setup.ROOT_PACKAGE)

            # TODO explain what is done here and why
            config_handler = ConfigHandler(setup)
            config_handler.back_up()

            # Generate the Ref manual and Cross-references
            self.generator = Generator(setup, self.REFERENCE_REL_PATH)
            self.generator.generate()

            # TODO explain what is done here and why
            config_handler.add_external_methods()

        except Exception as e:
            raise e
        finally:
            os.chdir(saved_dir)
            setup.move_package_to_root(Setup.ROOT_PACKAGE)

    def exit(self, setup: Setup):
        setup.update_mkdocs_yaml_template(
            r"^\s*\[REFERENCE_CONTENT\]\s*\n",
            self.generator.navigation if self.generator.navigation else "")

        if "GENERATING_TAIPY_DOC" in os.environ:
            del os.environ["GENERATING_TAIPY_DOC"]
