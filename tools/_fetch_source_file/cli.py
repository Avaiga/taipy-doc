import argparse


class CLI():
    DESCRIPTION = """\
Locally copies the source code of Taipy from different places
in order to allow the generation of the documentation set.
After this script has run, you can run 'mkdocs serve'.
"""
    ARG_N_HELP = "Prevents the source repository update (local only)."
    ARG_C_HELP = "Only checks if the fetch can be performed then exits."
    ARG_VERSION_HELP_1 = """\
The version for the whole doc set, or specific repositories.
This can be 'local', 'develop' or a valid version number.
It can be prefixed with '<repository>:', then the version applies
only to that repository. If that prefix is not present, the version
applies to all repositories.
Valid repository names are:
"""
    ARG_VERSION_HELP_2 = """
Note that each <version> arguments may overwrite the previous ones.
E.g.:
  '2.0 core:1.0' will set all versions to 2.0 except for
    the 'core' repository.
  'core:1.0 2.0' will set version 2.0 for all repositories.
If <version> is 'local', the code is retrieved from a directory called
'taipy-<repository-name>', above the current directory.
If <version> is 'develop', the develop branch for the indicated repository
is used.
If <version> is '<Major>.<Minor>', the corresponding branch is used.
If <version> contains an additional '.<Patch>[.<More>]' fragment, then the
corresponding tag is extracted from the '<Major>.<Minor>' branch for that
repository.
If any version is not 'local', then the 'git' command must be accessible.

The default behaviour is to use a local version for all repositories.
"""

    def __init__(self, script_name, repos):
        self.parser = argparse.ArgumentParser(prog="python " + script_name,
                                              formatter_class=argparse.RawTextHelpFormatter,
                                              description=self.DESCRIPTION)
        self.parser.add_argument("-n", "--no_pull", action='store_true',
                                 help=self.ARG_N_HELP)
        self.parser.add_argument("-c", "--check", action='store_true',
                                 help=self.ARG_C_HELP)
        self.parser.add_argument('version', nargs='*',
                                 help=self.ARG_VERSION_HELP_1 +
                                      "\n".join(["  - " + p for p in repos]) +
                                      self.ARG_VERSION_HELP_2)

    def get_args(self):
        return self.parser.parse_args()
