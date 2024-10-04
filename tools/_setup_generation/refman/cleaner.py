import os
import shutil
import re


class Cleaner:

    MODULE_REGEX = r"^(pkg_)?taipy(\..*)?\.md$"
    PACKAGE_REGEX = r"^pkg_taipy(\..*)?$"

    def __init__(self, setup, reference_relative_path):
        # ...\docs\refmans\reference
        self.path = os.path.join(setup.docs_dir, reference_relative_path)

    def clean(self):
        for p in os.listdir(self.path):
            fp = os.path.join(self.path, p)
            if re.match(self.MODULE_REGEX, p):
                os.remove(fp)
            elif os.path.isdir(fp) and re.match(self.PACKAGE_REGEX, p):
                shutil.rmtree(fp)
