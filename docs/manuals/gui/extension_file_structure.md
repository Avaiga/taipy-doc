# File Structure

## Project Structure

```
- demo_lib
  - frontend
    - src --> this is where our react elements are stored
      - index.ts --> this is where we export our taipy components
    - webpack.config.js
  - __init__.py
  - demo_library.py
- demo-init.py
```
- `demo_lib` is the directory where the whole extension library is located
  - `demo_library.py` is the main library class that is used to define our elements
  - `__init__.py` is used to shorten the import path
  ```py
  # __init__.py
  from .demo_library import DemoLibrary
  ```
  - `frontend` is our react frontend code that is compiled into a bundle and served.
    - `package.json`: JavaScript dependency file used by npm.<br/>
          This file is updated when you manually install Taipy GUI.
     - `webpack.config.js`: This file is used for building the JavaScript bundle that
          holds the Web components code that is used in the generated pages.
    - `tsconfig.json`: We are using [TypeScript](https://www.typescriptlang.org/)
          as a more productive language, compared to JavaScript, to create the Web
          components that are rendered on the generated pages. The TypeScript
          transpiler (the program that transforms TypeScript code to vanilla JavaScript)
          needs this file to drive its execution.
    - `src` is where our react components are stored. Whenever you want to create new taipy component that is defined in `demo_library.py` you have to create it inside this folder
    
      - `index.ts` is where all react elements gets exported with the name that matches with our `demo_library.py` elements' name.
    ```ts
      // index.ts
      import DemoLabel from "./DemoLabel"
      export { DemoLabel } // this is the name that will be used in demo_library.py
      ```
      ```py
      # demo_library.py
      class DemoLibrary(ElementLibrary):
        elts = {
            "label": Element(
                "value",
                {"value": ElementProperty(PropertyType.dynamic_string)},
                react_component="DemoLabel", # this is the name that matches with the exported name in index.ts
            ),
        }

        def get_name(self) -> str:
            return "demo_library"

        def get_elements(self) -> dict:
            return DemoLibrary.elts

        def get_scripts(self) -> list[str]:
            # Only one JavaScript bundle for this library.
            return ["demo_lib/frontend/dist/demo.js"]
    ```
- `demo-init.py` is the entry point for our library. This is where we use our taipy elements
```py
# demo-init.py example
import random
import string

value = "a"

page = """
# Dynamic Elements

<|{value}|demo_library.label|>

<|Add a character|button|>
"""


def on_action(state):
    state.value = state.value + random.choice(string.ascii_letters)

gui = Gui(page)
gui.add_library(DemoLibrary())
gui.run(use_reloader=False)
```

- `Pipfile` Lists the Python package dependencies used by [`pipenv`](https://pypi.org/project/pipenv/).
  
- `find_taipy_gui_dir.py`: Locates the absolute path of the installation directory for
  Taipy GUI. This is used to customize the build of the JavaScript bundle
- `setup.py`: A Python script that is used to package the extension library, if
  needed.<br/>
  See the [section on Packaging](extension_packaging.md) for more information.