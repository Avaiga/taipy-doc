import argparse
import os
import re
import shutil
import subprocess

SCRIPT_NAME = os.path.basename(__file__)

# Assuming this script is in taipy-doc/tools
TOOLS_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_PATH)
TOP_DIR = os.path.dirname(ROOT_DIR)

# Where all the code from all directories/repositories is copied
DEST_DIR_NAME = "taipy"

PACKAGES = ["config", "core", "gui", "getting-started", "rest" ]
PRIVATE_PACKAGES = [ "auth", "enterprise" ]

class GitContext(object):
    """Temporarily force GIT_TERMINAL_PROMPT to 0 for private repositories."""
    V="GIT_TERMINAL_PROMPT"
    def __init__(self, package: str):
        self.value = None
        self.save_value = package in PRIVATE_PACKAGES

    def __enter__(self):
        if self.save_value:
            self.value = os.environ.get(__class__.V, None)
            os.environ[__class__.V] = "0"

    def __exit__(self, exception_type, exception_value, traceback):
        if self.save_value:
            if self.value:
                os.environ[__class__.V] = self.value
            else:
                del os.environ[__class__.V]


p = PACKAGES[1]
parser = argparse.ArgumentParser(prog="python "+SCRIPT_NAME,
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 description="""\
Locally copies the source code of Taipy from different places
in order to allow the generation of the documentation set.
After this script has run, you can run 'mkdocs serve'.
""")
parser.add_argument("-n", "--no_pull", action='store_true',
                    help="Prevents the source repository update (local only).")
parser.add_argument("-c", "--check", action='store_true',
                    help="Only checks if the fetch can be performed then exits.")
parser.add_argument('version', nargs='*',
                    help="""\
The version for the whole doc set, or specific packages.
This can be 'local', 'develop' or a valid version number.
It can be prefixed with '<package>:', then the version applies
only to that package. If that prefix is not present, the version
applies to all packages.
Valid package names are:
"""
+ "\n".join(["  - " + p for p in PACKAGES ])
+ """

Note that each <version> arguments may overwrite the previous ones.
i.e.:
  '2.0 """ + p + """:1.0' will set all versions to 2.0 except for
    the '""" + p + """' package.
  '""" + p + """:1.0 2.0' will set version 2.0 for all packages.
If <version> is 'local', the code is retrieved from a directory called
'taipy-<package>', above the current directory.
If <version> is 'develop', the develop branch for the indicated repository
is used.
If <version> is '<Major>.<Minor>', the corresponding branch is used.
If <version> contains an additional '.<Patch>[.<More>]' fragment, then the
corresponding tag is extracted from the '<Major>.<Minor>' branch for that
package.
If any version is not 'local', then the 'git' command must be accessible.

The default behaviour is to use a local version for all packages.
""")

args = parser.parse_args()

# Read version from mkdocs.yml template
mkdocs_yml_template = None
mkdocs_yml_template_path = os.path.join(ROOT_DIR, "mkdocs.yml_template")
with open(mkdocs_yml_template_path, "r") as mkdocs_file:
    mkdocs_yml_template = mkdocs_file.read()
if mkdocs_yml_template is None:
    raise IOError(f"Couldn't open '{mkdocs_yml_template_path}'")
mkdocs_yml_version = re.search(r"site_url:\s*https://docs\.taipy\.io/en/(develop|release-(\d\.\d))$", mkdocs_yml_template, re.MULTILINE)
if mkdocs_yml_version is None:
    raise ValueError(f"'{mkdocs_yml_template_path}' has an invalid site_url value. This must be 'develop' or 'release-[M].[m]'.")
mkdocs_yml_version = mkdocs_yml_version.group(2) if mkdocs_yml_version.group(2) else mkdocs_yml_version.group(1)

# Gather version information for each package
package_defs = { package: { "version" : "local", "tag": None } for package in PACKAGES+PRIVATE_PACKAGES }
CATCH_VERSION_RE = re.compile(r"(^\d+\.\d+?)(?:(\.\d+)(\..*)?)?|develop|local$")
for version in args.version:
    package = None
    if version == "MKDOCS":
        version = mkdocs_yml_version
        tag = None
    else:
        try:
            colon = version.index(":")
            package = version[:colon]
            if package.startswith("taipy-"):
                package = package[6:]
            version = version[colon+1:]
        except ValueError as e:
            pass
        version_match = CATCH_VERSION_RE.fullmatch(version)
        if not version_match:
            raise ValueError(f"'{version}' is not a valid version.")
        tag = None
        if version_match.group(1):
            version = version_match.group(1)
            if version_match.group(2):
                tag = version + version_match.group(2)
                if version_match.group(3):
                    tag += version_match.group(3)
    if package:
        if not package in package_defs:
            raise ValueError(f"'{package}' is not a valid package.")
        package_defs[package]["version"] = version
        package_defs[package]["tag"] = tag
    else:
        for package in package_defs.keys():
            package_defs[package]["version"] = version
            package_defs[package]["tag"] = tag

# Test git, if needed
git_command="git"
if args.no_pull and all(v["version"] == "local" for v in package_defs.values()):
    git_command=None
else:
    git_path = shutil.which(git_command)
    if git_path is None or subprocess.run(f"{git_path} --version", shell=True, capture_output=True) is None:
        raise IOError(f"Couldn't find command \"{git_command}\"")
    git_command=git_path

# Check that directory, branches and tags exist for each package
github_token = os.environ.get("GITHUB_TOKEN", "")
if github_token:
    github_token += "@"
github_root=f"https://{github_token}github.com/Avaiga/taipy-"
for package in package_defs.keys():
    version = package_defs[package]["version"]
    if version == "local":
        package_path = os.path.join(TOP_DIR, "taipy-" + package)
        package_defs[package]["path"] = package_path
        if not os.path.isdir(package_path):
            raise IOError(f"Repository 'taipy-{package}' must be cloned in \"{TOP_DIR}\".")
    elif version == "develop":
        with GitContext(package):
            cmd = subprocess.run(f"{git_path} ls-remote -q -h {github_root}{package}.git", shell=True, capture_output=True, text=True)
            if cmd.returncode:
                raise SystemError(f"Problem with {package}: {cmd.stdout}")
    else:
        with GitContext(package):
            cmd = subprocess.run(f"{git_path} ls-remote --exit-code --heads {github_root}{package}.git", shell=True, capture_output=True, text=True)
            if cmd.returncode:
                if package in PRIVATE_PACKAGES:
                    package_defs[package]["skip"] = True
                    continue
                else:
                    raise SystemError(f"Couldn't query branches from {github_root}{package}.")
            if not f"release/{version}\n" in cmd.stdout:
                raise ValueError(f"No branch 'release/{version}' in repository 'taipy-{package}'.")
            tag = package_defs[package]["tag"]
            if tag:
                cmd = subprocess.run(f"{git_path} ls-remote -t --refs {github_root}{package}.git", shell=True, capture_output=True, text=True)
                if not f"refs/tags/{tag}\n" in cmd.stdout:
                    raise ValueError(f"No tag '{tag}' in repository 'taipy-{package}'.")

if args.check:
    print(f"Fetch should perform properly with the following settings:")
    for package in package_defs.keys():
        if not package_defs[package].get("skip", False):
            version = package_defs[package]['version']
            version = "(local)" if version == "local" else f"branch:{version if version == 'develop' else f'release/{version}'}"
            tag = package_defs[package]["tag"]
            if tag:
                version += f" tag:{tag}"
            print(f"- taipy-{package} {version}")
    exit(0)

DEST_DIR = os.path.join(ROOT_DIR, DEST_DIR_NAME)

def safe_rmtree(dir: str):
    if os.path.isdir(dir):
        shutil.rmtree(dir)
    
# Remove target 'taipy' directory
safe_rmtree(DEST_DIR)
os.makedirs(DEST_DIR)
# If a leftover of a previous failed run
safe_rmtree(os.path.join(TOOLS_PATH, DEST_DIR_NAME))

# Fetch files
def move_package(package: str, src_path: str):
    if package == "getting-started":
        gs_dir = os.path.join(ROOT_DIR, "docs", "getting_started")
        safe_rmtree(os.path.join(gs_dir, "src"))
        for step_dir in [step_dir for step_dir in os.listdir(gs_dir) if step_dir.startswith("step_") and os.path.isdir(os.path.join(gs_dir, step_dir))]:
            safe_rmtree(os.path.join(gs_dir, step_dir))
        for step_dir in [step_dir for step_dir in os.listdir(src_path) if step_dir.startswith("step_") and os.path.isdir(os.path.join(src_path, step_dir))]:
            shutil.copytree(os.path.join(src_path, step_dir), os.path.join(gs_dir, step_dir))
        safe_rmtree(os.path.join(gs_dir, "src"))
        shutil.copytree(os.path.join(src_path, "src"), os.path.join(gs_dir, "src"))
        shutil.copy(os.path.join(src_path, "index.md"), os.path.join(gs_dir, "index.md"))
        saved_dir = os.getcwd()
        os.chdir(os.path.join(ROOT_DIR, "docs", "getting_started"))
        subprocess.run(f"python {os.path.join(src_path), 'generate_notebook.py'}", shell=True, capture_output=True, text=True)
        os.chdir(saved_dir)
    else:
        tmp_dir = os.path.join(ROOT_DIR, f"{package}.tmp")
        gui_dir = os.path.join(ROOT_DIR, f"gui") if package == "gui" else None
        if gui_dir and os.path.isdir(gui_dir):
            if os.path.isdir(os.path.join(gui_dir, "node_modules")):
                shutil.move(os.path.join(gui_dir, "node_modules"), os.path.join(ROOT_DIR, f"gui_node_modules"))
            shutil.rmtree(gui_dir)
        try:
            def keep_py_files(dir, filenames):
                return [name for name in filenames if not os.path.isdir(os.path.join(dir, name)) and not name.endswith('.py')]
            shutil.copytree(os.path.join(src_path, "src", "taipy"), tmp_dir, ignore=keep_py_files)
            entries = os.listdir(tmp_dir)
            for entry in entries:
                try:
                    if entry != "__pycache__":
                        shutil.move(os.path.join(tmp_dir, entry), DEST_DIR)
                except shutil.Error as e:
                    if entry != "__init__.py": # Top-most __entry__.py gets overwritten over and over
                        raise e
            if gui_dir:
                os.mkdir(gui_dir)
                src_gui_dir = os.path.join(src_path, "gui")
                shutil.copytree(os.path.join(src_gui_dir, "doc"), os.path.join(gui_dir, "doc"))
                shutil.copytree(os.path.join(src_gui_dir, "src"), os.path.join(gui_dir, "src"))
                for f in [f for f in os.listdir(src_gui_dir) if f.endswith(".md") or f.endswith(".json")]:
                    shutil.copy(os.path.join(src_gui_dir, f), os.path.join(gui_dir, f))
                if os.path.isdir(os.path.join(ROOT_DIR, "gui_node_modules")):
                    shutil.move(os.path.join(ROOT_DIR, "gui_node_modules"), os.path.join(gui_dir, "node_modules"))
        finally:
            shutil.rmtree(tmp_dir)

for package in package_defs.keys():
    version = package_defs[package]['version']
    print(f"Fetching package {package} ({version})", flush=True)
    if version == "local":
        src_path = package_defs[package]['path']
        if not args.no_pull:
            subprocess.run(f"{git_path} pull {src_path}", shell=True, capture_output=True, text=True)
        print(f"    Copying from {src_path}...", flush=True)
        move_package(package, src_path)
    elif not package_defs[package].get("skip", False):
        clone_dir = os.path.join(ROOT_DIR, f"{package}.clone")
        if version != "develop":
            version = f"release/{version}"
        print("    Cloning...", flush=True)
        subprocess.run(f"{git_path} clone -b {version} {github_root}{package}.git {clone_dir}", shell=True, capture_output=True, text=True)
        tag = package_defs[package]['tag']
        if tag:
            # Checkout tag version
            saved_dir = os.getcwd()
            os.chdir(clone_dir)
            subprocess.run(f"{git_path} checkout {tag}", shell=True, capture_output=True, text=True)
            os.chdir(saved_dir)
        move_package(package, clone_dir)
        # For some reason, we need to protect the removal of the clone dirs...
        # See https://stackoverflow.com/questions/1213706/what-user-do-python-scripts-run-as-in-windows
        def handleRemoveReadonly(func, path, exc):
            import errno, stat
            if func == os.unlink and exc[1].errno == errno.EACCES:
                os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
                func(path)
            else:
                raise
        shutil.rmtree(os.path.join(ROOT_DIR, f"{package}.clone"), onerror=handleRemoveReadonly)
