import os
import re
import shutil
import subprocess

from constants import ROOT_DIR

GUI_EXT_REF_DIR_PATH = ROOT_DIR + "/docs/manuals/reference_guiext"

def generate_gui_extension():
    npm_path = shutil.which("npm")
    if npm_path:
        try:
            subprocess.run(f"{npm_path} --version", shell=True, capture_output=True)
        except OSError:
            print(f"Couldn't run npm, ignoring this step.", flush=True)
            npm_path = None
    if npm_path:
        saved_cwd = os.getcwd()
        gui_path = os.path.join(ROOT_DIR, "gui")
        os.chdir(gui_path)
        print(f"... Installing node modules...", flush=True)
        subprocess.run(f"{npm_path} ci --omit=optional", shell=True)
        print(f"... Generating documentation...", flush=True)
        subprocess.run(f"{npm_path} run mkdocs", shell=True)
        # Process and copy files to docs/manuals
        if os.path.exists(GUI_EXT_REF_DIR_PATH):
            shutil.rmtree(GUI_EXT_REF_DIR_PATH)
        os.mkdir(GUI_EXT_REF_DIR_PATH)
        dst_dir = os.path.abspath(GUI_EXT_REF_DIR_PATH)
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
                    file_content = match.group(2) + match.group(1) + file_content[match.end():]
                path_name = path_name.replace(src_dir, dst_dir)
                with open(path_name, "w") as output:
                    output.write(file_content)
            for dir in dirs:
                os.mkdir(os.path.join(dst_dir, dir))
        os.chdir(saved_cwd)
