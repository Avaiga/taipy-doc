# ################################################################################
# Generates MUI icons used in Taipy
#
# All Material UI icons that are used in the entire Taipy product are extracted
# in a list of SVG symbols in
#  setup.ref_manuals_dir + "/gui/viselements/mui-icons.svg"
# In the documentation Markdown body, references to these icons can be referenced
# using the [MUI:<IconName>] syntax, which is transformed in the post-process step
# into a SVG element referencing the symbol itself.
# ################################################################################
import os
import re

from .setup import Setup, SetupStep


class MuiIconsStep(SetupStep):
    def __init__(self):
        self.mui_icons = None

    def get_id(self) -> str:
        return "mui-icons"

    def get_description(self) -> str:
        return "Extracts and groups all MUI icons used in the front-end code"

    def enter(self, setup: Setup):
        self.FE_DIR_PATH = setup.root_dir + "/taipy-fe"
        if not os.path.isdir(self.FE_DIR_PATH):
            raise FileNotFoundError(
                f"FATAL - Could not find front-end code directory in {self.FE_DIR_PATH}"
            )
        self.VISELEMENTS_DIR_PATH = setup.ref_manuals_dir + "/gui/viselements"
        # Location of the front-end node_modules directory
        self.MODULES_DIR_PATH = None  # Initialized in setup()

    def setup(self, setup: Setup) -> None:
        # This directory may exist only after GuiExtRefManStep was executed
        MODULES_DIR_PATH = self.FE_DIR_PATH + "/node_modules"
        if not os.path.isdir(MODULES_DIR_PATH):
            raise FileNotFoundError(
                f"FATAL - Could not find node_modules directory in {MODULES_DIR_PATH}"
            )
        mui_icons_path = self.VISELEMENTS_DIR_PATH + "/mui-icons.svg"
        current_icons = []
        # Read all known icon symbols in *current_icons* if they were generated
        if os.path.isfile(mui_icons_path):
            with open(mui_icons_path, "r") as file:
                current_icons = [
                    m[1] for m in re.finditer(r"<symbol\s+id=\"(.*?)\"", file.read())
                ]

        self.mui_icons = set()

        # Find all used MUI icons and list them in *self.mui_icons*
        MUI_ICON_IMPORT_RE = re.compile(r"import.*?from\s+\"@mui/icons-material/(.*)\"")

        def search_mui_icons(dir_name: str):
            for file_name in os.listdir(dir_name):
                if file_name == "node_modules":
                    continue
                file_path = os.path.join(dir_name, file_name)
                if os.path.isdir(file_path):
                    search_mui_icons(file_path)
                elif file_name.endswith(".tsx") and ".spec." not in file_name:
                    with open(file_path, "r") as file:
                        content = file.read()
                        for m in MUI_ICON_IMPORT_RE.finditer(content):
                            icon = m[1]
                            if icon not in self.mui_icons:
                                self.mui_icons.add(icon)

        search_mui_icons(self.FE_DIR_PATH)

        # Generate the SVG icons symbol list
        self.mui_icons = sorted(self.mui_icons)
        if current_icons != self.mui_icons:
            print("NOTE - Generating MUI icons")
            SVG_PATH_RE = re.compile(
                r"\"path\"\s*,\s*{\s*d\s*:\s*\"(.*?)\"\s*}", re.MULTILINE | re.DOTALL
            )
            ICON_PATH_PATTERN = MODULES_DIR_PATH + "/@mui/icons-material/{icon}.js"

            def extract_svg_paths(icon: str) -> list[str]:
                icon_path = ICON_PATH_PATTERN.format(icon=icon)
                try:
                    with open(icon_path, "r") as icon_file:
                        icon_def = icon_file.read()
                    return [m[1] for m in SVG_PATH_RE.finditer(icon_def)]
                except Exception:
                    print(f"ERROR - Couldn't read source for icon '{icon}'")

            with open(mui_icons_path, "w") as file:
                print(
                    '<svg xmlns="http://www.w3.org/2000/svg" width="0" height="0">',
                    file=file,
                )
                for icon in self.mui_icons:
                    paths = extract_svg_paths(icon)
                    if paths is None:
                        continue
                    print(f'  <symbol id="{icon}" viewBox="0 0 24 24">', file=file)
                    paths = extract_svg_paths(icon)
                    if len(paths) > 1:
                        print("    <g>", file=file)
                        for path in paths:
                            print(f'      <path d="{path}"/>', file=file)
                        print("    </g>", file=file)
                    else:
                        print(f'    <path d="{paths[0]}"/>', file=file)
                    print("  </symbol>", file=file)
                print("</svg>", file=file)
