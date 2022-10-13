import os
import re
import shutil

from datetime import datetime

from constants import MKDOCS_YML_PATH


# Check that the visual elements' documentation is available
def check_viz_elements_documentation(viz_elements_src_path):
    if not os.path.isdir(viz_elements_src_path):
        raise SystemExit(f"FATAL - Visual elements documentation not found in {viz_elements_src_path}")


# Check that the source files are available
def check_source_files(root_dir, root_package, tools_dir):
    if not os.path.exists(f"{root_dir}/{root_package}"):
        # Result of a fail previous run?
        if os.path.exists(f"{tools_dir}/{root_package}"):
            shutil.move(f"{tools_dir}/{root_package}", f"{root_dir}/{root_package}")
        else:
            raise SystemError(f"FATAL - Could not find root package in {root_dir}/{root_package}")


# Read mkdocs yml template file
def read_mkdocs_yml_tmpl(mkdocs_yml_template_path):
    mkdocs_yml_content = None
    with open(mkdocs_yml_template_path) as mkdocs_yml_file:
        mkdocs_yml_content = mkdocs_yml_file.read()
    if not mkdocs_yml_content:
        raise SystemError("FATAL - Could not read mkdocs configuration file at {MKDOCS_YML_TEMPLATE_PATH}")
    return mkdocs_yml_content


# Temporarily move top package to 'tools' for this script to find it.
# MkDocs needs it at the root level so we will have to move it back.
def move_top_package_to_tools(root_dir, root_package, tools_dir):
    shutil.move(f"{root_dir}/{root_package}", f"{tools_dir}/{root_package}")


# This moves back the package directory to 'root_dir'.
# It must be called from now on no matter why this program exits.
def restore_top_package_location(root_dir, root_package, tools_dir):
    # Move top package back to the root level for MkDocs.
    shutil.move(f"{tools_dir}/{root_package}", f"{root_dir}/{root_package}")


def read_skeleton(name, path):
    content = ""
    with open(os.path.join(path, name + ".md_template")) as skeleton_file:
        content = skeleton_file.read()
    if not content:
        restore_top_package_location()
        raise SystemExit(f"FATAL - Could not read {name} markdown template")
    return content


def write_yml_file(navigation, rest_navigation, getting_started_navigation, mkdocs_yml_content):
    # Update mkdocs.yml
    copyright_content = f"{str(datetime.now().year)}"
    mkdocs_yml_content = re.sub(r"\[YEAR\]",
                                copyright_content,
                                mkdocs_yml_content)
    mkdocs_yml_content = re.sub(r"^\s*\[REFERENCE_CONTENT\]\s*\n",
                                navigation,
                                mkdocs_yml_content,
                                flags=re.MULTILINE | re.DOTALL)
    mkdocs_yml_content = re.sub(r"^\s*\[REST_REFERENCE_CONTENT\]\s*\n",
                                rest_navigation,
                                mkdocs_yml_content,
                                flags=re.MULTILINE | re.DOTALL)
    mkdocs_yml_content = re.sub(r"^\s*\[GETTING_STARTED_CONTENT\]\s*\n",
                                getting_started_navigation,
                                mkdocs_yml_content,
                                flags=re.MULTILINE | re.DOTALL)
    with open(MKDOCS_YML_PATH, "w") as mkdocs_yml_file:
        mkdocs_yml_file.write(mkdocs_yml_content)
