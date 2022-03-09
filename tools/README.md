# Taipy Documentation tools

This directory contains the files that [mkdocs](https://www.mkdocs.org/)
uses to generate the complete documentation set.

   - `fetch_source_files.sh`: Locally copies the relevant files from the
     different Taipy repositories to generate the documentation.
   - `setup_generation.py`: Python script that pre-processed Taipy source
     files and visual elements' documentation from `taipy-gui` so MkDocs can
     produce structured access to Reference Manual and Visual Elements entries.
   - `postprocess.py`: Python post-processor that runs after MkDocs has generated
     the documentation to create cross-links to the Reference Manual and fix ultimate
     minor issues.
   - `assets`: Stores MkDocs items used during the build process.
