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

!!! abstract "TODO: fix PyPI package or version link"

# Taipy Documentation

The Taipy documentation set uses [MkDocs](https://www.mkdocs.org/) to generate its entire
content.

## Building the documentation

There are three steps to follow if you want to generate the full content of the
Taipy documentation:

   - Locally copy the mandatory files from other repositories.<br/>
     Because sources files (where the Reference Manual information is stored) are
     spread among different directories, you need to copy those files locally 
     before you run MkDocs.<br/>
     This can be done quickly and safely using the shell script `fetch_source_files.sh`
     located in the `tools` directory. Run the script when your current directory is the
     root of the `taipy-doc` checkout:
        ```
        sh tools/fetch_source_files.sh
        ```
     You will notice that two new directories are created in the root directory: `taipy` and
     `gui`. There are where mandatory files are copied. Git ignores these two directories, and
     you should not bother with them.

   - Generate the Reference Manual and Visual Elements documentation files.<br/>
     The Reference Manual and the documentation for the Visual Elements of the `taipy-gui` module are
     generated from source files copied from the `taipy-core` and `taipy-gui` repositories.<br/>
     To generate all mandatory files, execute the Python script `setup_generation.py` located
     in the `tools` directory. Run the script when your current directory is the root
     of the `taipy-doc` checkout:
        ```
        python tools/setup_generation.py
        ```

   - Generate the documentation set.<br/>
     When all files are copied and generated, you can finally use MkDocs to generate the
     documentation set. You can use any of the three predefined generation modes:

      - `mkdocs serve`: This is a great way to let MkDocs generate the documentation and
        locally run a Web server that lets you watch, on the fly, the impact of your changes.

      - `mkdocs build`: Generates the documentation set as a whole hierarchy of files (in
        `site`). These files can be copied wherever you need to deploy them.

      - `mkdocs gh-deploy`: Generates and deploys the documentation set as a _GitHub Pages_
         site to publish the result of the documentation build.

# How to contribute

## Code documentation (Reference Manual)

Code is copied from different repositories to be processed.

## User documentation (User Manuals)

## Other manuals

