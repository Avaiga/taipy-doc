# Taipy Documentation tools

This directory contains the files used by [mkdocs](https://www.mkdocs.org/)
to generate the documentation set.

   - `fetch_source_files.sh`: Locally copies the relevant files from the
     different Taipy repositories to generate the documentation.
   - `setup_generation.py`: Python script that pre-processed Taipy source
      files and visual elements documentation from `taipy-gui` so MkDocs can
      produce structured access to Reference Manual and Visual
      Elements entries.
   - `postprocess.py`: Python post-processor that runs after MkDocs has generated
      the documentation, to create cross-links to the Reference Manual and fix ultimate small issues.
   - `assets`: Stores MkDocs items that are used during the build process.
