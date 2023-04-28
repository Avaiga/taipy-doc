import os
import re
import shutil
import subprocess

from _fetch_source_file import CLI, GitContext, read_doc_version_from_mkdocs_yml_template_file

# Assuming this script is in taipy-doc/tools
TOOLS_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(TOOLS_PATH)
TOP_DIR = os.path.dirname(ROOT_DIR)

# Where all the code from all directories/repositories is copied
DEST_DIR_NAME = "taipy"

REPOS = ["config", "core", "gui", "getting-started", "getting-started-core", "getting-started-gui", "rest"]
PRIVATE_REPOS = ["auth", "enterprise"]

OPTIONAL_PACKAGES = {
    "gui": ["pyarrow", "pyngrok", "python-magic", "python-magic-bin"]
}

args = CLI(os.path.basename(__file__), REPOS).get_args()

# Read version from mkdocs.yml template
mkdocs_yml_version = read_doc_version_from_mkdocs_yml_template_file(ROOT_DIR)

# Gather version information for each repository
repo_defs = {repo: {"version": "local", "tag": None} for repo in REPOS + PRIVATE_REPOS}
CATCH_VERSION_RE = re.compile(r"(^\d+\.\d+?)(?:(\.\d+)(\..*)?)?|develop|local$")
for version in args.version:
    repo = None
    if version == "MKDOCS":
        version = mkdocs_yml_version
        tag = None
    else:
        try:
            colon = version.index(":")
            repo = version[:colon]
            if repo.startswith("taipy-"):
                repo = repo[6:]
            version = version[colon + 1:]
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
    if repo:
        if not repo in repo_defs:
            raise ValueError(f"'{repo}' is not a valid repository name.")
        repo_defs[repo]["version"] = version
        repo_defs[repo]["tag"] = tag
    else:
        for repo in repo_defs.keys():
            repo_defs[repo]["version"] = version
            repo_defs[repo]["tag"] = tag

# Test git, if needed
git_command = "git"
if args.no_pull and all(v["version"] == "local" for v in repo_defs.values()):
    git_command = None
else:
    git_path = shutil.which(git_command)
    if git_path is None or subprocess.run(f"{git_path} --version", shell=True, capture_output=True) is None:
        raise IOError(f"Couldn't find command \"{git_command}\"")
    git_command = git_path

# Check that directory, branches and tags exist for each repository
github_token = os.environ.get("GITHUB_TOKEN", "")
if github_token:
    github_token += "@"
github_root = f"https://{github_token}github.com/Avaiga/taipy-"
for repo in repo_defs.keys():
    version = repo_defs[repo]["version"]
    if version == "local":
        repo_path = os.path.join(TOP_DIR, "taipy-" + repo)
        repo_defs[repo]["path"] = repo_path
        if not os.path.isdir(repo_path):
            if repo in PRIVATE_REPOS:
                repo_defs[repo]["skip"] = True
            else:
                raise IOError(f"Repository 'taipy-{repo}' must be cloned in \"{TOP_DIR}\".")
    elif version == "develop":
        with GitContext(repo, PRIVATE_REPOS):
            cmd = subprocess.run(f"{git_path} ls-remote -q -h {github_root}{repo}.git", shell=True, capture_output=True,
                                 text=True)
            if cmd.returncode:
                if repo in PRIVATE_REPOS:
                    repo_defs[repo]["skip"] = True
                    continue
                else:
                    raise SystemError(f"Problem with {repo}: {cmd.stdout}")
    else:
        with GitContext(repo, PRIVATE_REPOS):
            cmd = subprocess.run(f"{git_path} ls-remote --exit-code --heads {github_root}{repo}.git", shell=True,
                                 capture_output=True, text=True)
            if cmd.returncode:
                if repo in PRIVATE_REPOS:
                    repo_defs[repo]["skip"] = True
                    continue
                else:
                    raise SystemError(f"Couldn't query branches from {github_root}{repo}.")
            if not f"release/{version}\n" in cmd.stdout:
                raise ValueError(f"No branch 'release/{version}' in repository 'taipy-{repo}'.")
            tag = repo_defs[repo]["tag"]
            if tag:
                cmd = subprocess.run(f"{git_path} ls-remote -t --refs {github_root}{repo}.git", shell=True,
                                     capture_output=True, text=True)
                if not f"refs/tags/{tag}\n" in cmd.stdout:
                    raise ValueError(f"No tag '{tag}' in repository 'taipy-{repo}'.")

if args.check:
    print(f"Fetch should perform properly with the following settings:")
    for repo in repo_defs.keys():
        if not repo_defs[repo].get("skip", False):
            version = repo_defs[repo]['version']
            version = "(local)" if version == "local" else f"branch:{version if version == 'develop' else f'release/{version}'}"
            tag = repo_defs[repo]["tag"]
            if tag:
                version += f" tag:{tag}"
            print(f"- taipy-{repo} {version}")
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

pipfile_packages = {}
PIPFILE_PACKAGE_RE = re.compile(r"(.*?)\s?=\s?(.*)")


# Fetch files
def move_files(repo: str, src_path: str):
    # Read Pipfile dependency packages
    pipfile_path = os.path.join(src_path, "Pipfile")
    if os.path.isfile(pipfile_path):
        reading_packages = False
        repo_optional_packages = OPTIONAL_PACKAGES.get(repo, None)
        with open(pipfile_path, "r") as pipfile:
            while True:
                line = pipfile.readline()
                if str(line) == "" or (reading_packages and (not line.strip() or line[0] == "[")):
                    break
                line = line.strip()
                if line == "[packages]":
                    reading_packages = True
                elif reading_packages:
                    match = PIPFILE_PACKAGE_RE.fullmatch(line)
                    if match and not match.group(1).startswith("taipy"):
                        package = match.group(1).lower()
                        version = match.group(2)
                        if repo_optional_packages is None or not package in repo_optional_packages:
                            if package in pipfile_packages:
                                versions = pipfile_packages[package]
                                if version in versions:
                                    versions[version].append(repo)
                                else:
                                    versions[version] = [repo]
                            else:
                                pipfile_packages[package] = {version: [repo]}
    # Copy relevant files for doc generation
    if repo.startswith("getting-started"):
        gs_dir = os.path.join(ROOT_DIR, "docs", "getting_started", repo)
        # safe_rmtree(os.path.join(gs_dir, "src"))
        for step_dir in [step_dir for step_dir in os.listdir(gs_dir) if
                         step_dir.startswith("step_") and os.path.isdir(os.path.join(gs_dir, step_dir))]:
            safe_rmtree(os.path.join(gs_dir, step_dir))
        for step_dir in [step_dir for step_dir in os.listdir(src_path) if
                         step_dir.startswith("step_") and os.path.isdir(os.path.join(src_path, step_dir))]:
            shutil.copytree(os.path.join(src_path, step_dir), os.path.join(gs_dir, step_dir))
        safe_rmtree(os.path.join(gs_dir, "src"))
        shutil.copytree(os.path.join(src_path, "src"), os.path.join(gs_dir, "src"))
        shutil.copy(os.path.join(src_path, "index.md"), os.path.join(gs_dir, "index.md"))
        saved_dir = os.getcwd()
        os.chdir(os.path.join(ROOT_DIR, "docs", "getting_started", repo))
        subprocess.run(f"python {os.path.join(src_path, 'generate_notebook.py')}",
                       shell=True,
                       capture_output=True,
                       text=True)
        os.chdir(saved_dir)
    else:
        tmp_dir = os.path.join(ROOT_DIR, f"{repo}.tmp")
        safe_rmtree(tmp_dir)
        gui_dir = os.path.join(ROOT_DIR, f"gui") if repo == "gui" else None
        if gui_dir and os.path.isdir(gui_dir):
            if os.path.isdir(os.path.join(gui_dir, "node_modules")):
                shutil.move(os.path.join(gui_dir, "node_modules"), os.path.join(ROOT_DIR, f"gui_node_modules"))
            shutil.rmtree(gui_dir)
        try:
            def keep_py_files(dir, filenames):
                return [name for name in filenames if not os.path.isdir(os.path.join(dir, name)) and not (
                    name.endswith('.py') or name.endswith('.pyi') or name.endswith('.json') or name.endswith('.ipynb'))]

            shutil.copytree(os.path.join(src_path, "src", "taipy"), tmp_dir, ignore=keep_py_files)
            entries = os.listdir(tmp_dir)
            for entry in entries:
                try:
                    if entry != "__pycache__":
                        shutil.move(os.path.join(tmp_dir, entry), DEST_DIR)
                except shutil.Error as e:
                    if entry != "__init__.py":  # Top-most __entry__.py gets overwritten over and over
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


for repo in repo_defs.keys():
    if repo_defs[repo].get("skip", False):
        continue
    version = repo_defs[repo]['version']
    print(f"Fetching file for repository {repo} ({version})", flush=True)
    if version == "local":
        src_path = repo_defs[repo]['path']
        if not args.no_pull:
            subprocess.run(f"{git_path} pull {src_path}", shell=True, capture_output=True, text=True)
        print(f"    Copying from {src_path}...", flush=True)
        move_files(repo, src_path)
    else:
        clone_dir = os.path.join(ROOT_DIR, f"{repo}.clone")
        if version != "develop":
            version = f"release/{version}"
        print("    Cloning...", flush=True)
        subprocess.run(f"{git_path} clone -b {version} {github_root}{repo}.git {clone_dir}", shell=True,
                       capture_output=True, text=True)
        tag = repo_defs[repo]['tag']
        if tag:
            # Checkout tag version
            saved_dir = os.getcwd()
            os.chdir(clone_dir)
            subprocess.run(f"{git_path} checkout {tag}", shell=True, capture_output=True, text=True)
            os.chdir(saved_dir)
        move_files(repo, clone_dir)


        # For some reason, we need to protect the removal of the clone dirs...
        # See https://stackoverflow.com/questions/1213706/what-user-do-python-scripts-run-as-in-windows
        def handleRemoveReadonly(func, path, exc):
            import errno, stat
            if func == os.unlink and exc[1].errno == errno.EACCES:
                os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
                func(path)
            else:
                raise


        shutil.rmtree(clone_dir, onerror=handleRemoveReadonly)

# Manually add the taipy.run() function.
# TODO: Automate this, grabbing the function from the 'taipy' repository,
# so we benefit from potential updates.
init_path = os.path.join(ROOT_DIR, "taipy", "__init__.py")
with open(init_path, "a") as init:
    run_method = """
import typing as t

def run(*services: t.List[t.Union[Gui, Rest, Core]], **kwargs) -> t.Optional[t.Union[Gui, Rest, Core]]:
    \"\"\"Run one or multiple Taipy services.

    A Taipy service is an instance of a class that runs code as a Web application.

    Parameters:
        *services (List[Union[`Gui^`, `Rest^`, `Core^`]]): Services to run.
            If several services are provided, all the services run simultaneously. If this is empty or set to None,
            this method does nothing.
        **kwargs: Other parameters to provide to the services.
    \"\"\"
    pass\n"""
    init.write(run_method)

# Generate Pipfile from package dependencies from all repositories
pipfile_path = os.path.join(ROOT_DIR, "Pipfile")
pipfile_message = "WARNING: Package versions mismatch in Pipfiles - Pipfile not updated."
for package, versions in pipfile_packages.items():
    if len(versions) != 1:
        if pipfile_message:
            print(pipfile_message)
            pipfile_message = None
        print(f"- {package}:")
        for version, repos in versions.items():
            print(f"  {version} in {', '.join(repos)}.")
        pipfile_path = None
# Update Pipfile from all other Pipfiles
if pipfile_path:
    pipfile_lines = None
    with open(pipfile_path, "r") as pipfile:
        pipfile_lines = pipfile.readlines()
    new_pipfile_path = os.path.join(ROOT_DIR, "Pipfile.new")
    in_packages_section = False
    legacy_pipfile_packages = {}
    pipfile_changes = []
    with open(new_pipfile_path, "w") as new_pipfile:
        for line in pipfile_lines:
            if in_packages_section:
                if not line or line[0] == "[":
                    in_packages_section = False
                    # List packages
                    for package in sorted(pipfile_packages.keys(), key=str.casefold):
                        versions = pipfile_packages[package]
                        version = list(versions.keys())[0]
                        if package == "modin":
                            # Remove 'extras' from modin package requirements
                            version = re.sub(r"\{\s*extras.*?,\s*version\s*=\s*(.*?)\s*}", r"\1", version)
                        new_pipfile.write(f"{package} = {version}\n")
                        if not package in legacy_pipfile_packages:
                            pipfile_changes.append(f"Package '{package}' added ({version})")
                        elif legacy_pipfile_packages[package] != version:
                            pipfile_changes.append(
                                f"Package '{package}' version changed from {legacy_pipfile_packages[package]} to {version}")
                            del legacy_pipfile_packages[package]
                        else:
                            del legacy_pipfile_packages[package]
                    new_pipfile.write("\n")
                    skip_line = True
                    new_pipfile.write(line)
                match = PIPFILE_PACKAGE_RE.fullmatch(line.strip())
                if match and not match.group(1).startswith("taipy"):
                    legacy_pipfile_packages[match.group(1).lower()] = match.group(2)
            else:
                new_pipfile.write(line)
                if line.strip() == "[packages]":
                    in_packages_section = True
    for package, version in legacy_pipfile_packages.items():
        pipfile_changes.append(f"Package '{package}' removed ({version})")
    if pipfile_changes:
        print(f"Pipfile was updated (Pipfile.bak saved):")
        for change in pipfile_changes:
            print(f"- {change}")
        shutil.move(pipfile_path, os.path.join(ROOT_DIR, "Pipfile.bak"))
        shutil.move(new_pipfile_path, pipfile_path)
        print(f"You may want to rebuild you virtual environment:")
        print(f"  - pipenv --rm")
        print(f"  - pipenv install --dev")
    else:
        print(f"No changes in Pipfile")
        os.remove(new_pipfile_path)
