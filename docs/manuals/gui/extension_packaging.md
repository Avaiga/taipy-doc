# Packaging your elements library

You can create an autonomous Python package to distribute your Taipy GUI custom extension library.

The following steps must be performed:
- go to your project's root `Pipfile` directory
- Install the build package:
  - If you are using `pipenv`:
  ```bash
   pipenv run pip install build
  ```
- If you are not using `pipenv`:
  ```bash
   pip install build
  ```
- Configure the file `setup.py` to match your settings:

  - The `name` parameter must be set to the package name, which contains the Taipy GUI
    Extension library.<br/>
    Note that before you pick a name for your package, you should make sure that it has not
    already being used. The name of the package is not related to the `import` directive
    in your Python code.
  - The `author` and `author_email` parameters should be set to the package author name
    and email address.
  - The `description` and `long_description` parameters should provide a description of
    this package (short and long versions).
  - The `keywords` parameter should hold relevant keywords exposed by Pypi.
  - The `packages` parameter indicates which directories and files should be included in
    this package.<br/>
    If you have renamed the extension library root directory, you will need to update this,
    replacing "my_custom_lib" with the name of the directory you have created.
  - The `version` parameter should reflect the extension library version you are packaging.
  - Check the `classifiers` and `license` parameters.

- Build the package:
   ```bash
   # With pipenv
   pipenv run python -m build
    
   # Without pipenv
   python -m build
   ```

This generates a Python package that can be uploaded to Pipy or shared with community
members.