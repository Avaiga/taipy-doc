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

from _setup_generation import run_setup

steps = None
# --------------------------------------------------------------------------------
# You may want to replace that 'step' initial value with a list of steps you
# want to run.
# E.g. say you want to run only the Reference Manual generation step.
# You could add the following code:
#   from _setup_generation.step_refman import RefManStep
#   steps = [RefManStep()]
# --------------------------------------------------------------------------------

# Assuming that this script is located in <taipy-doc>/tools
run_setup(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), steps)
