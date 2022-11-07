# ################################################################################
# setup_generation.py
#   Prepares all files before running MkDocs to generate the complete
#   Taipy documentation set.
#
# This setup is performed by executing successive steps, depending on the
# topic (Reference Manual generation, JavaScript documentation integration
# within MkDocs...)
# ################################################################################

import os

from setup_generation import run_setup

# Assuming that this script is located in <taipy-doc>/tools
run_setup(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
