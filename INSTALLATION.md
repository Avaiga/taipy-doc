# Installation

There are three steps to follow if you want to generate the full content of the
Taipy documentation:

1. Locally copy the mandatory files from other repositories.

   Because source files (where the Reference Manual information is stored) are
   spread among different directories, those files need to be locally copied
   before you run MkDocs.<br/>
   This can be done quickly and safely using the Python script `fetch_source_files.py`
   that you can find in the `tools` directory.

   Run the script when your current directory is the root of the `taipy-doc` checkout:
   ```
   python tools/fetch_source_files.py
   ```

   The script can copy the source files from two locations:

   - your local filesystem (next to the current directory `taipy-doc`, you would have
     cloned the repositories that make the whole Taipy product: `taipy-config`,
     `taipy-core`, `taipy-getting-started`, `taipy-gui` and `taipy-rest`).<br/>
   - the Taipy repositories on GitHub.

   By default, the script will copy all repositories from a local clone. Before files
   are copied, a `git pull` command is launched from each local clone directory, in
   order to update the files locally.<br/>
   You can prevent the script from doing so using the `--no_pull` option.

   To specify that you want to clone the repositories from GitHub, you can
   indicate the version of Taipy you wish to clone.<br/>
   If you want to build the documentation set for Taipy 2.0, you will run:
   `python tools/fetch_source_files.py 2.0`.<br/>
   You can also indicate a specific tag (i.e., `python tools/fetch_source_files.py 1.0.2`).<br/>
   To use the `develop` branch, replace the version number with the string "develop"
   (i.e., `python tools/fetch_source_files.py develop`).

   See the help text (`python tools/fetch_source_files.py --help`) for more information.

   After the script has run successfully, you will notice that two new directories are created
   in the root directory: `taipy` and `gui`. There are where mandatory files are copied. Git
   ignores these two directories, and you should not bother with them.

2. Generate the Reference Manual and Visual Elements' documentation files.

   The Reference Manual and the documentation for the Visual Elements of the `taipy-gui` module
   are generated from source files copied from a set of repositories.<br/>
   To generate all mandatory files, execute the Python script `setup_generation.py` located
   in the `tools` directory. Run the script when your current directory is the root
   of the `taipy-doc` checkout:
   ```
   # Install pipenv if necessary
   pip install pipenv
   # Install the mandatory Python modules from Pipfile to the virtual env
   pipenv install --dev
   # Run the setup
   python tools/setup_generation.py
   ```

3. Generate the documentation set.<br/>
   When all files are copied and generated, you can finally use MkDocs to generate the
   documentation set. You can use any of the three predefined generation modes:

   - `mkdocs serve`: This is a great way to let MkDocs generate the documentation and
     locally run a web server that lets you watch your changes impact on the fly.

   - `mkdocs build`: Generates the documentation set as a whole hierarchy of files (in
     `site`). These files can be copied wherever you need to deploy them.

   - `mkdocs gh-deploy`: Generates and deploys the documentation set as a _GitHub Pages_
     site to publish the result of the documentation build.
