# Introduction to dynamic elements

The [previous section on static elements](../static_element.md) exposes
how element libraries and elements are defined. A major limitation with
static elements is that you cannot change their property values at runtime.
In Taipy GUI, you can [bind Python variables or expressions](../../binding.md)
to properties so that the user interface is immediately updated should the application
modify the value of a variable.

Custom elements that allow for variable binding are called *dynamic elements*
in Taipy GUI.<br/>
As we have seen in the previous section, every custom element must declare
the properties that it relies on. Doing so means that every property must indicate
the type it supports. This is handled by the `PropertyType^` class.<br/>
Every custom element that wants to use a property with a *dynamic* type
must be defined as a *dynamic element*.<br/>
Although a custom element might not have any *dynamic property* (that is, a property
with a type that is dynamic), it can be implemented as a *dynamic element* nevertheless
to leverage the expressivity of how these elements are implemented.

Dynamic elements use [TypeScript](https://www.typescriptlang.org/) and
[JavaScript](https://www.javascript.com/) code to dynamically generate HTML code to
produce the pages that can be displayed in a browser. Taipy GUI relies
on the [React](https://reactjs.org/) JavaScript library to simplify the
development of graphical components.

!!! warning "Minimal knowledge"
    The following sections contain code samples written in TypeScript that leverage
    the React library. This manual is in no way a beginner's guide on either technology.

    To create your custom dynamic elements, you need to know about React functional
    components and hooks and how to create simple components.<br/>
    You also need to know the basics about packaging React components using
    [webpack](https://webpack.js.org/) that bundles the JavaScript modules into
    a JavaScript library that element libraries can load to implement the front-end
    part of the custom elements.

## Declaring a dynamic element

The declaration of a dynamic element looks very similar to the declaration of a static
element.<br/>
The fundamental change is that if the *render_xhtml* argument of the
`Element.__init__()^`(`Element` constructor) is not set or is not a function
then the element is considered *dynamic*. That is, implemented using a React
component. You can specify the name of the component using the *react_component*
argument. If you don't, Taipy GUI will use a capitalized camel case transformation
of the element name as the target React component name.

Here is how a custom element library containing a dynamic element would be declared:

```py
from taipy.gui.extension import ElementLibrary, Element, ElementProperty

class CustomLibrary(ElementLibrary):

    def __init__(self) -> None:
        self.elements = {
              ...
              "<element1 name>": Element("<default property name>", {
                  "<property1 name>": ElementProperty(<property1 type>, ...),
                  ...
              },
              # This is optional and can be omitted if the component name can be inferred
              # from the element name
              react_component="<element1 component name>"),
              ...
        }

    def get_name(self) -> str:
        return "<library name>"

    def get_elements(self) -> dict:
        return self.elements

    def get_scripts(self) -> list[str]:
        return ["<javascript module pathname>"]
```

There are two significant differences to spot compared to a custom element
library that has only static elements:

- A dynamic element is created using the *react_component* parameter, indicating
  that it is implemented using a React component. The value of this parameter
  must be the name of the React component, as exported by the JavaScript module
  where this component is defined;
- The method `(ElementLibrary.)get_scripts()^` must be overloaded to return
  the path to the JavaScript bundle file that contains the definition for the
  React components of the dynamic elements. The code above assumes that the custom
  element library needs only one file.

## Implementing a dynamic element

The front-end side of dynamic elements is implemented as standard React components.<br/>
We recommend defining each component in its own source file for a clear code
organization. In this manual, we will exclusively use TypeScript to enjoy better type
checking and make the code more readable. The
[custom element library template](https://github.com/Avaiga/guiext-template) repository
provides the skeleton of an
[extension library project structure](../index.md#extension-library-project-structure).

Here are the key things to know when creating a React component that implements the
front-end for a custom visual element:

- The component name should be one used when the element is declared, using the
  *react_component* argument of the `Element.__init__()^`(`Element` constructor).<br/>
  If this parameter is not used, Taipy GUI uses a camel case transformation of the element
  name.
- All component source files are bundled in a JavaScript library. We are using
  [*webpack*](https://webpack.js.org/) for this purpose.
- Components must be exported by the JavaScript library with the same name as the one
  used in the `Element.__init__()^`(`Element` constructor).
- Property names must be valid Python identifiers.
- The camel case transformation of the property names, with a lowercase initial letter, are
  used to name the keys of the *props* argument for the React component.<br/>
  We recommend that we declare a TypeScript interface that provides better typing
  for this argument: each property of the interface should have the transformed name
  of the element property.<br/>
  Note that you can overwrite the name of the property in the React component by using
  the *js_name* argument of the  `ElementProperty.__init__()^`(`ElementProperty` constructor).
- Dynamic properties use two keys in the functional component *props* argument:

    - The (transformed) property name as described above;
    - A similar camel case-transformed version of the property name as if it had been
      prefixed by 'default_'.<br/>
      This slot in the *props* is used to render the component before the Taipy GUI back-end
      has submitted any update (which is then handled by the other slot).

To illustrate this, let's assume we want to create a dynamic custom element called
*sizable_label*. This element has two dynamic properties:

- *label*, the default property, stores a string that the element should display;
- *size* is a numeric property that stores how large the label should be rendered.

The element declaration would look like this in the definition of the dictionary that
holds all the element declarations:

```py
"sizable_label": Element("label", {
                   "label": ElementProperty(PropertyType.dynamic_string),
                   "size": ElementProperty(PropertyType.dynamic_number)
                 }
```

The default name for the React component would be "SizableLabel", and its properties
will be named after the element's property names.<br/>
Here is how the definition for the React component will look like (typically, this code
will be stored in a file called "SizableLabel.tsx", in the directory
"&lt;project dir&gt;/&lt;package dir&gt;/front-end/src"):

```ts
interface SizableLabelProps {
    label?: string;
    defaultLabel: string;
    size?: number;
    defaultSize: number;
}

const SizableLabel = (props: SizableLabelProps) => {
    ...
}
```

When the component is entirely defined, it must be exported by the JavaScript library.<br/>
This is done by adding the *export* directive in the file
"&lt;project dir&gt;/&lt;package dir&gt;/front-end/src/index.ts".

For our example, this would be the content of this file:
```ts
import SizableLabel from "./SizableLabel";

export { SizableLabel };
```

## Building the front-end module

To build the JavaScript module that Taipy GUI can load on the user's browser, there are three
steps to take:

- Convert the TypeScript code to JavaScript;
- Resolve the dependency in the Taipy GUI JavaScript module;
- Bundle all JavaScript code into the extension library JavaScript module.

All the steps are handled by the `package.json` file located at the root of the front-end
NPM project (that is, in the `<package dir>/front-end` directory in our examples).<br/>
The commands declared in this file heavily rely on [*webpack*](https://webpack.js.org/)
to handle the build process: the "scripts" property of the `package.json` content defines
the "build" entry as invoking "webpack".<br/>
The `webpack.config.js` configuration file should sit next to `package.json`. This
file contains all the configuration parameters that we will discuss in the rest of this
section.

### Converting TypeScript

TypeScript is a language that is transformed into JavaScript before it can be packaged
in a JavaScript bundle. This process is known as '*transpilation*'.<br/>
Here is how the project must be set up in order to use TypeScript and support the React
JSX syntax (used in `.tsx` source files):

- To transpile TypeScript, you need to install the NPM modules "typescript" and
   "ts-loader":
   ```
   npm install --save-dev typescript ts-loader
   ```

    Note that in the `package.json` provided with Taipy GUI, these two modules already appear
    in the "devDependencies" property.

- A file called `tsconfig.json` must exist next to the file `webpack.config.js`. This file
  contains the configuration to support JSX and convert TypeScript to vanilla JavaScript.<br/>
  Here is an excerpt of the `tsconfig.json` file we use in the dynamic library examples. We
  do not explain all the settings that appear in the file we provide and let the reader take
  a peek at the [TSConfig documentation](https://www.typescriptlang.org/tsconfig) for a
  complete description of the `tsconfig.json` file content:

    ```json hl_lines="4 10"
    {
      "compilerOptions": {
        "target": "es5",
        "outDir": "./dist/",
        "module": "esnext",
        "moduleResolution": "node",
        "jsx": "react-jsx",
        "allowJs": true,
      },
      "include": [ "src" ]
    }
    ```
    Note that you must make sure that the directory where TypeScript files are located
    (the "include" property) and the output directory (the "outDir" property) are set
    according to your project structure.

- `webpack` must be configured so it can transpile TypeScript code.<br/>
  The two essential settings in the `webpack.config.js` file are shown here:

    ```json
    resolve: { extensions: [".ts", ".tsx"] },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: "ts-loader",
          exclude: /node_modules/
        }
      ]
    },
    ```

   The settings of the *resolve* and *rules* properties make `webpack` look for TypeScript
   files (`.ts` and `.tsx`) and process those files using the "ts-loader" TypeScript
   transpiler loader.

### Resolve Taipy GUI dependency

As you can see in the implementation code for React components, we depend on a
JavaScript library that Taipy GUI provides.<br/>
In the source code for the components, you will find directives similar to the
following:
```js
import { ... } from "taipy-gui";
```

The "taipy-gui" module is provided by Taipy GUI, where it has been installed.<br/>
You can query where Taipy GUI was installed by issuing the command:
```
pip show taipy-gui
```

To simplify the understanding of the rest of this section, let's assume that you store
the directory path returned by this command in the environment variable 'TAIPY_GUI_DIR'.<br/>

To install the Taipy GUI JavaScript module, you need to run the following command:
```title="Unix"
npm i $TAIPY_GUI_DIR/taipy/gui/webapp
```
```title="Windows"
npm i %TAIPY_GUI_DIR%\taipy\gui\webapp
```
Note that in the `package.json` file that is installed in Taipy GUI (in
`$TAIPY_GUI_DIR/taipy/doc/extension/example_library/front-end`), there is an entry
called "install" in the "scripts" section that invokes an NPM script to perform
this task.

This dependency must be explicitly declared for `webpack` to use as an external
library.<br/>
In the `webpack.config.js` file you can find the following lines, that assumes
that the environment variable "TAIPY_GUI_DIR" was set as indicated above:

```js
  externals: {"taipy-gui": "TaipyGui"},

  plugins: [
    new webpack.DllReferencePlugin({
      manifest: path.resolve(
        __dirname,
        `${process.env.TAIPY_GUI_DIR}/taipy/gui/webapp/taipy-gui-deps-manifest.json`
      ),
      name: "TaipyGuiDependencies"
    }),
  ]
```
These two settings ensure that the Taipy GUI JavaScript module is accessible for
resolving the symbols it exposes and that this module is not bundled itself in the
generated custom extension library JavaScript module.

### Bundle the JavaScript code

`webpack` must be configured to indicate where the front-end JavsScript is produced.<br/>
This is done by setting the *output* property in `webpack.config.js`:
```js
    output: {
      filename: "extensionLibrary.js",
      path: path.resolve(__dirname, "dist"),
      library: {
        // Camel case transformation of the library name
        name: "MyExtensionLibrary",
        type: "umd"
      },
    },
```
This indicates that all the source files should be bundled in a single module file
called 'extensionLibrary.js', located in the 'dist' directory.

When the different configuration files are up-to-date, building the extension library
bundle is just a matter of running:

```
npm run build
```

!!! note "Debug mode"
    To debug your front-end code in the browser, you will want to use the command:
    ```
    npm run build:dev
    ```
    instead.<br/>
    This preserves the symbols in the module file and generates a map file next to it,
    allowing for stepping in your TypeScript source code even after transpilation.

With the settings listed above, the result of this command should be a file called
`extensionLibrary.js` under the `dist` directory.<br/>
This path, relative to the Python file where the element library is defined, must
appear in the value returned by the method `(ElementLibrary.)get_scripts()^` of
the `ElementLibrary^` subclass.

## Property types

Elements properties are what control the rendering and the behavior of front-end
components.<br/>
The Taipy GUI Extension API exposes functions that allow components to consume
data coming from the application and send messages to the Python code that
can then handle user interactions.

The API depends on the type of the properties you need to implement.<br/>
Here are the sections that address the different use cases that your custom
element may need:

- [Scalar properties](scalar_props.md)
- [Tabular data properties](../tabular_data.md)

