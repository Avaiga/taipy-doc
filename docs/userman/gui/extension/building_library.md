# Building the custom library

This section explains how to build the custom extension library.

### Prerequisites

To complete the build of the extension library, we need to following tools:

- Python 3.8 or higher;
- Taipy GUI 2.0 or higher;
- [Node.js](https://nodejs.org/en/) 16.x or higher: a JavaScript runtime.<br/>
  This embeds [npm](https://www.npmjs.com/), the Node Package Manager.

Installing Taipy GUI is usually done in a Python virtual environment.

Create a directory run virtual environment as in the following

- If you are using `pipenv`:
   ```sh
   $ pipenv --python $PYTHON_VERSION
   $ pipenv shell
   $ pipenv install
   ```

- If you are not using `pipenv`:
   ```sh
   $ pip install virtualenv
   $ python -m venv ./venv
   $ source ./venv/bin/activate
   $ pip install taipy-gui
   ```

### Customize the build process {data-source="gui:doc/extension/example_library/front-end/webpack.config.js"}

You will need to adapt some files in this template directory to match your specific
needs. Here are the important settings that you must check:

- `<project_dir>/<package_dir>/frontend/webpack.config.js`: This file is used to compile all the JavaScript
  code into a single JavaScript bundle.<br/>
  Here are the settings that you must check:
- `output.path`: The directory where the JavaScript bundle will be generated.
- `output.filename`: The name of the JavaScript bundle file.<br/>
  If you want to change any of these parameters, you must make sure that the location
  and filename that you have set are reflected in the list of mandatory scripts declared
  by the element library code: in `<package_dir>/example_library.py`, the method
  `get_script()` must return an array where the path to this script is explicitly
  indicated, relative to the element library source file.<br/>
  A new setting of `output.path` must also be reflected in
  `<package_dir>/frontend/tsonfig.js` (see below).
  The default values are set to generate the file `exampleLibrary.js` filename in the `dist` directory
  (located in the `frontend` directory, where the bundle is built)

  - `output.library.name`: Indicates the name of the JavaScript module that holds the code
    for the generated library.</br>
    It must be derived from the name of the element library (the value of the `get_name()`
    method for the custom library in `<package_dir>/example_library.py`): the name of the
    JavaScript object should be a camel case version of the library name.<br/>
    If `get_name()` returns `"the_name_of_the_library"` then this setting should be set
    to `"TheNameOfTheLibrary"`.
  - `plugins`: We must provide `webpack` with the path to a bundle, provided by Taipy GUI,
    that holds all the dependencies that Taipy GUI depends on.<br/>
    You must set the `manifest` argument to
    `<package_dir>/frontend/taipy-gui-deps-manifest.json` where `<package_dir>` is the
    absolute path to the Taipy GUI installation directory, as returned by the script
    `find_taipy_gui_dir.py`.
- `<package_dir>/frontend/tsonfig.json`:
   - `"outDir"`: Must be set to the value of `output.path` in
     `<package_dir>/frontend/webpack.config.js`.
   - `"include"`: Must have the item indicating where the TypeScript source files should
     be located. The default is `"src"`, referencing `<package_dir>/frontend/src`.

### Things to check

The previous section explained what to change and where.
Another way of looking at things is to list the different settings that can be
modified, and check that they all match:

- The element library name: set by overriding `ElementLibrary.get_name()`.<br/>
  This is the prefix that is used in page description texts to find the visual
  element to instantiate.
- The JavaScript module name: Is specified in `webpack.config.js` (setting is
  `output.library.name`).<br/>
  By default, it is a camel case version of the element library name.<br/>
  It can be specified otherwise by overriding `ElementLibrary.get_js_module_name()`.
- The JavaScript bundle path name: Is specified in `webpack.config.js` (settings are
  `output.filename` and `output.path`).<br/>
  This is the path of the file that contains all the JavaScript parts of the library. It
  must appear in the list returned by `ElementLibrary.get_scripts()`.
- The element names: They are declared as keys to the dictionary returned by
  `ElementLibrary.get_elements()`.<br/>
  They are used to find an element in a library when the page description text is
  read.
- The element component names: Are specified as the value of the `react_component`
  argument to the `Element` constructor.<br/>
  These component names must be exported with the exact same name from the JavaScript
  bundle entry point.

### Building the JavaScript bundle

When all configuration files have been properly updated, we can build the
JavaScript bundle:

- Set your directory to `<package_dir>/frontend`
- Install the Taipy GUI JavaScript bundle:<br/>
  You must run the command:
  ```
  npm i $TAIPY_GUI_DIR/webapp
  ```
  (or `npm i %TAIPY_GUI_DIR%/frontend` on Windows machines)

  where the variable TAIPY_GUI_DIR represents the absolute path to the installation
  of Taipy GUI, on your filesystem. You can use the script `find_taipy_gui_dir.py`
  that will find this location.
- You can now build the custom element library JavaScript bundle file:
  ```
  npm run build
  ```
  This generates the bundle `exampleLibrary.js` in the `dist` directory (if you have not changed
  the `output` settings in `webpack.config.js`).

### Testing the custom element library {data-source="gui:doc/extension/example_library/main.py"}

After building the JavaScript bundle, you can test the custom element library by creating a simple application that utilizes it.
In your `<project_dir>`, create a Python file to integrate and use the custom element library.

To execute your application, you can run:
   ```bash
   # With pipenv
   pipenv run python demo-init.py

   # Without pipenv
   python  demo-init.py
   ```

And see the custom label control in action.
