<p>
    <a href="https://pypi.org/user/Avaiga/">
        <img src="https://img.shields.io/pypi/v/taipy.svg" alt = "Release Status">
    </a>

    <!-- a href="https://github.com/avaiga/taipy-doc/actions">
        <img src="https://github.com/avaiga/taipy-doc/actions/workflows/dev.yml/badge.svg" alt="CI Status">
    </a -->

</p>

!!! info "Licence"

    Taipy is a free software under [MIT](https://tlo.mit.edu/learn-about-intellectual-property/software-and-open-source-licensing) Licence.

!!! abstract "TODO: fix PYPI package or version link"

# Taipy Documentation

The Taipy documentation set uses [MkDocs](https://www.mkdocs.org/) to generate its entire
content.

## Building the documentation

There are three steps to follow if you want to generate the full content of the
Taipy documentation:

   - Locally copy the mandatory files from other repositories.<br/>
     Because sources files (where the Reference Manual information is stored) are
     spread among different directories, you need to locally copy those files
     before you run MkDocs.<br/>
     This can be done quickly using the shell script `fetch_source_files.sh` located
     in the `tools` directory. Just run the script when your current directory is
     the root of the `taipy-doc` checkout:
        ```
        sh tools/fetch_source_files.sh
        ```
     You will notice that two new directories are created in the root directory:
     `taipy` and `gui`. There are where mandatory files are copied.
     Git ignores these two directories, and you should not bother with them.

   - Pre-process source files.<br/>
     The Reference Manual and the documentation for the Visual Elements of the
     `taipy-gui` module need additional documentation files that are generated
     by a pre-processing script.<br/>
     To generate those files, execute the Python script `setup_generation.py` located
     in the `tools` directory. Run this script from the root of the `taipy-doc` checkout before you generate the documentation set:
        ```
        python tools/setup_generation.py
        ```
     Sometimes this script cannot navigate the top-most package, 'taipy'.
     You will get an error message indicating: `"Root package taipy was not found."`,
     and the script will try again a few times.<br/>
     In the situation where it cannot solve the problem, it will exit on error.<br/>
     After a few seconds, re-running the same script will usually fix that problem.

     Also note that if this script breaks, the 'taipy' directory that was
     created by the `fetch_source_files.sh` script may have been moved to the
     `tools` directory. Usually, the script restores that directory.<br/>
     However, if this was not the case, you must manually move it from
     `tools` to the top directory: from the root of the `taipy-doc` checkout,
     run:
        ```
        mv tools/taipy .
        ```

   - Generate the documentation set.<br/>
     You can finally use _MkDocs_ to generate the documentation set when all files
     are copied and generated. You can use any of the three predefined generation
     modes:

     - `mkdocs serve`: This is a great way to let MkDocs generate the documentation
       and locally run a Web server that lets you watch, on the fly, the impact of
       your changes.

     - `mkdocs build`: Generates the documentation set as a whole hierarchy of files
       in `site`). You can copy the resulting directory hierarchy anywhere if you
       need to deploy the complete documentation set.

     - `mkdocs gh-deploy`: Generates and deploys the documentation set as a
       _GitHub Pages_ site to share the result of the documentation build.

# How to contribute

## Code documentation (Reference Manual)

Code is copied from different repositories to be processed.

## User documentation (User Manuals)

## Other manuals

