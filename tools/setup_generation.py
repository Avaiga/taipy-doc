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
from setup_generation.step_viselements import VisElementsStep
from setup_generation.step_refman import RefManStep
from setup_generation.step_rest_refman import RestRefManStep
from setup_generation.step_gui_ext_refman import GuiExtRefManStep
from setup_generation.step_getting_started import GettingStartedStep

# The setup steps to perform
steps = [
    VisElementsStep(),
    RefManStep(),
    RestRefManStep(),
    GuiExtRefManStep(),
    GettingStartedStep()
    ]

# Assuming that this script is located in <taipy-doc>/tools
run_setup(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), steps)
