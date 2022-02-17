# Taipy Documentation tools

This directory contains the files used by [mkdocs](https://www.mkdocs.org/)
to generate the documentation set.

   - `assets`: stores MkDocs items that are used during the build process.
   - `generate_viselements.py`: Python script that translates the visual elements
      documentation from `taipy-gui` to formats that MkDocs can use.
   - `postprocess.py`: Python post-processor that runs after MkDocs has generated
      the documentation, to fix ultimate small issues.
