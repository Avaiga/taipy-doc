from constants import *
from utils import *

# ------------------------------------------------------------------------
# Step 0
#   Preparing environment
# ------------------------------------------------------------------------

check_viz_elements_documentation(VISELEMENTS_SRC_PATH)
check_source_files(ROOT_DIR, ROOT_PACKAGE, TOOLS_DIR)
mkdocs_yml_content = read_mkdocs_yml_tmpl(MKDOCS_YML_TEMPLATE_PATH)
move_top_package_to_tools(ROOT_DIR, ROOT_PACKAGE, TOOLS_DIR)

# ------------------------------------------------------------------------
# Step 1
#   Generating the Visual Elements documentation
# ------------------------------------------------------------------------
print("Step 1/5: Generating Visual Elements documentation", flush=True)
from step_1_visual_elements_generation import generate_viz_elements

generate_viz_elements()

# ------------------------------------------------------------------------
# Step 2
#   Generating the Reference Manual
# ------------------------------------------------------------------------
print("Step 2/5: Generating the Reference Manual pages", flush=True)
from step_2_reference_manual_generation import generate_ref_manual

navigation = generate_ref_manual()

# ------------------------------------------------------------------------
# Step 3
#   Generating the REST API documentation
# ------------------------------------------------------------------------
print("Step 3/5: Generating the REST API Reference Manual pages", flush=True)
from step_3_rest_api_ref_man_generation import generate_rest_api

rest_navigation = generate_rest_api()

# ------------------------------------------------------------------------
# Step 4
#   Generating the GUI Extension API documentation
# ------------------------------------------------------------------------
print("Step 4/5: Generating the GUI Extension API Reference Manual pages", flush=True)

from step_4_gui_extension_api_generation import generate_gui_extension

generate_gui_extension()

# ------------------------------------------------------------------------
# Step 5
#   Generating the Getting Started
# ------------------------------------------------------------------------
print("Step 5/5: Generating the Getting Started navigation bar", flush=True)
from step_5_getting_started_generation import generate_getting_started

getting_started_navigation = generate_getting_started()

# ------------------------------------------------------------------------
# Step 6
#   Writing final yml file
# ------------------------------------------------------------------------
write_yml_file(navigation, rest_navigation, getting_started_navigation, mkdocs_yml_content)
