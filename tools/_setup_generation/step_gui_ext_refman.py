# ################################################################################
# Taipy GUI Extension Reference Manual generation setup step.
#
# The Reference Manual pages for the Taipy GUI JavaScript extension module
# is generated using the typedoc tools, directly from the JavaScript
# source files.
# ################################################################################
from .setup import Setup, SetupStep
import os
import re
import shutil
import subprocess


class GuiExtRefManStep(SetupStep):
    def get_id(self) -> str:
        return "guiext"

    def get_description(self) -> str:
        return "Generating the GUI Extension API documentation"

    def enter(self, setup: Setup):
        self.GUI_EXT_REF_DIR_PATH = setup.ref_manuals_dir + "/reference_guiext"
        if os.path.exists(self.GUI_EXT_REF_DIR_PATH):
            shutil.rmtree(self.GUI_EXT_REF_DIR_PATH)
        npm_path = shutil.which("npm")
        if npm_path:
            if " " in npm_path:
                npm_path = f'"{npm_path}"'
            try:
                subprocess.run(f"{npm_path} --version", shell=True, capture_output=True)
            except OSError:
                print(f"WARNING: Couldn't run npm, ignoring this step.", flush=True)
                npm_path = None
        self.npm_path = npm_path

    def setup(self, setup: Setup) -> None:
        if self.npm_path:
            saved_cwd = os.getcwd()
            gui_path = os.path.join(setup.root_dir, "taipy-fe")
            os.chdir(gui_path)
            print(f"... Installing node modules...", flush=True)
            subprocess.run(f"{self.npm_path} i --omit=optional", shell=True)
            print(f"... Generating documentation...", flush=True)
            subprocess.run(f"{self.npm_path} run mkdocs", shell=True)
            # Process and copy files to docs/userman
            os.mkdir(self.GUI_EXT_REF_DIR_PATH)
            dst_dir = os.path.abspath(self.GUI_EXT_REF_DIR_PATH)
            src_dir = os.path.abspath(os.path.join(gui_path, "reference_guiext"))
            JS_EXT_RE = re.compile(r"^(.*?)(\n#.*?\n)", re.MULTILINE | re.DOTALL)
            for root, dirs, files in os.walk(src_dir):
                for file in files:
                    file_content = None
                    path_name = os.path.join(root, file)
                    with open(path_name) as input:
                        file_content = input.read()
                    match = JS_EXT_RE.search(file_content)
                    if match:
                        file_content = (
                            match.group(2)
                            + match.group(1)
                            + file_content[match.end() :]
                        )
                    path_name = path_name.replace(src_dir, dst_dir)
                    with open(path_name, "w") as output:
                        output.write(file_content)
                for dir in dirs:
                    os.mkdir(os.path.join(dst_dir, dir))
            os.chdir(saved_cwd)
