# Taipy Documentation tools

This directory contains the files used by [mkdocs](https://www.mkdocs.org/)
to generate the documentation set.

   - `fetch_source_files.sh`: Locally copies the relevant files from the
     different Taipy repositories to generate the documentation.
   - `generate_viselements.py`: Python script that translates the visual elements
      documentation from `taipy-gui` to formats that MkDocs can use.
   - `postprocess.py`: Python post-processor that runs after MkDocs has generated
      the documentation, to fix ultimate small issues.
   - `assets`: Stores MkDocs items that are used during the build process.
