# Extension Libraries

Although Taipy GUI comes with a set of visual elements that lets users create comprehensive
user interfaces, there are situations where applications may need to provide a particular
kind of element with capabilities that one cannot find in Taipy GUI out-of-the-box.

Taipy GUI has an extension mechanism that allows developers to add their own
visual elements so they can be accessed by Taipy GUI when defining page content.<br/>
This mechanism is known as "Taipy GUI Extension".

## Introduction

Taipy GUI lets developers create and use custom visual elements to address specific use
cases or integrate third-party web components. One can expand the functionality
offered by the base Taipy GUI package to create custom components that can be
effortlessly used in pages and shared with the community.

Custom visual elements are grouped into *Element Libraries*, where each element is identified
by its name. An element name must be unique in the context of its library.<br/>
Each library also has a name. To insert a custom visual element in a page, you will use
the full name of the element:

- `<library name>.<element name>` in a Markdown page
- `<library name>:<element name>` in an HTML page

## Element Libraries and Custom Elements

An Element Library  holds the information necessary to refer to and instantiate custom visual
elements. Element libraries can contain several visual element descriptors and can be packaged
into a standalone Python package that a Taipy GUI application can import or that can be
deployed.

Here are essential points you need to know about element libraries:

- An element library is a Python object that derives from the `ElementLibrary^` class.
- Element libraries have a name (returned by `ElementLibrary.get_name()^`) that is
  used to refer to visual elements in page definitions.
- Element libraries hold the set of their elements, as returned by
  `ElementLibrary.get_elements()^`.

You can create an element library by simply subclassing `ElementLibrary^` and
overriding the required methods. The two mandatory methods to override are
`(ElementLibrary.)get_name()^` and `(ElementLibrary.)get_elements()^`:

```py
from taipy.gui.extension import ElementLibrary, Element

class CustomLibrary(ElementLibrary):
    def __init__(self) -> None:
        self.elements = {
          "<element1 name>": Element(...),
          "<element2 name>": Element(...),
        }

    def get_name(self) -> str:
        return "<library name>"

    def get_elements(self) -> dict:
        return self.elements
```

Note that in order not to reevaluate the dictionary that holds the declaration of
elements, we create it in the class constructor, and store it in a new data member
(`self.elements`). This data member is then returned by `get_elements()`.

Other methods can be overridden if necessary, which will be discussed later in the manual.

## Declaring Elements

As we have seen, custom visual element descriptors are associated with the name of
the element as it appears on pages in the dictionary returned by the
`(ElementLibrary.)get_elements()^` method.

The `Element.__init__^`(`Element` constructor) needs a description of all the properties
that this element holds, as well as how this element is rendered.

```py
Element("<default property name>",
        {
           "<property1 name>": ElementProperty(<property1 type>, ...),
           "<property2 name>": ElementProperty(<property2 type>, ...),
           ...
        },
        <rendering arguments>)
```

An element property descriptor (handled by the `ElementProperty^` class) must
indicate its type (one of the `PropertyType^` values) and potentially a default
value.

All elements must indicate what their default property name is. That is used in Markdown
pages as the first fragment of the `<|...|>` construct or the value located in the
text part of an element tag in HTML pages.<br/>
Of course, *default_property_name* must be one of the keys of the properties dictionary
provided to the `Element.__init__`(`Element` constructor).

## Rendering Elements

The Taipy GUI Extension package provides two different ways to implement the rendering
of the element and its interactions. Both approaches deliver HTML fragments that are
inserted into the page when it is requested.

- Static elements.<br/>
  A static visual element cannot interact with the underlying application.<br/>
  It can be used just like any other element in a page, but its properties are not bound to
  application variables: if a variable value is modified, it does not impact the representation of
  the element on the page.<br/>
  Static elements are implemented by creating a string that holds the XHTML text (that is, HTML
  that respects the XML syntax, where all tags must be closed) that is inserted in the page
  displayed by the browser. This string is computed and returned by the function set to the
  *render_xhtml* parameter of the `Element.__init__^`(`Element` constructor).<br/>
  Please go to the [Static Elements](static_element.md) section for
  a complete description of how to implement your own custom static elements.

- Dynamic elements.<br/>
  Dynamic elements provide the binding functionality of Taipy GUI: if a property value
  depends on an application variable (and if the property type is *dynamic*), then the
  page automatically updates when the variable value changes.<br/>
  In Taipy GUI, dynamic visual elements are implemented using the
  [React](https://reactjs.org/) JavaScript library and the
  [TypeScript](https://www.typescriptlang.org/) programming language (that builds on
  JavaScript).<br/>
  You indicate that a custom element is dynamic by setting the *react_component* parameter of
  the `Element.__init__^`(`Element` constructor) to the name of the React component that
  must be created to render the element.<br/>
  The section on [Dynamic Elements](dynamic_element/index.md) provides an introduction to
  custom dynamic elements.

## Registering an extension library

An extension library must be exposed to the Taipy GUI application so application pages can use
its elements:

- The Python application must import the library module or package
  so it can be instantiated;
- The library must be instantiated and the instance must be used in the invocation of
  the function `Gui.add_library()^` to expose the extension library to the application.

## Prerequisites

To create and use custom visual elements, you need to install the following:

- Taipy GUI 2.0 or higher (included in Taipy and Taipy Enterprise).
- Python 3.9 or higher.
- If you need to create [dynamic custom visual elements](dynamic_element/index.md), you
  also need to install [Node.js](https://nodejs.org) (version 18 or above).<br/>
  Note that this comes with `npm`, the Node Package Manager.<br/>
  Basic knowledge of React (that we use with TypeScript) and JavaScript is welcome.

## Extension library project structure

Because you might have to work in two different programming languages (Python for
the back-end side of the extension library and static elements, and TypeScript
- or JavaScript - for the front-end part of dynamic elements), we recommend
organizing your extension library projects so that both are clearly separated and easily
built.<br/>
There is a [template repository](https://github.com/Avaiga/guiext-template) hosted
on GitHub that you can copy. This template holds the entire directory structure
allowing for the creation of an extension library with dynamic elements.

Here is what the directory structure of a typical extension library project looks like:

```
<project dir>
├── pyproject.toml
├── MANIFEST.in
└── <package dir>/
    ├── __init__.py
    ├── library.py
    └── front-end/ (only if you need dynamic elements)
        ├── package.json
        ├── tsconfig.json
        ├── webpack.config.js
        └── src/
            ├── index.ts
            └── <component>.ts
```

Each of these entries needs some explanation:

- `pyproject.toml`: Python project settings file for the extension library package.<br/>
  This is used when building a standalone Python package from all the code that makes
  an extension library. See the [section on packaging](extension_packaging.md) for more
  details.
- `MANIFEST.in`: Commands to be executed when the Python package is built as a source distribution.
  The [section on packaging](extension_packaging.md) explains what this file should contain.
- `<package dir>/`: The root directory for the extension library. This contains all the Python
  (and potentially TypeScript/JavaScript code) needed to build the extension library.<br/>
  The name of this directory is used as the name of the root directory for the Python package.
- `<package dir>/__init__.py`: Required to make `<package dir>` a valid Python package
  directory.</br>
  It is also the right place to import the library class because it is easier from the developer's
  standpoint when a Taipy GUI application imports the extension library.
- `<package dir>/library.py`: The implementation file for the extension library.<br/>
  This is where you typically will define the subclass of `ElementLibrary^` that implements
  your extension library.
- `<package dir>/front-end/`: If you create an extension library containing dynamic
  elements, we strongly encourage storing all the front-end-specific code in this
  dedicated directory.<br/>
  This should contain all the TypeScript/JavaScript code for the React components and
  what it takes to build the JavaScript bundle that the extension library uses.
- `<package dir>/front-end/package.json`: The meta-data for the Node project that holds
  the components implementing the front-end side of the dynamic elements of your extension
  library.
- `<package dir>/front-end/tsconfig.json`: The TypeScript compilation options.
- `<package dir>/front-end/webpack.config.js`: The configuration to build the JavaScript
  bundle of the extension library.
- `<package dir>/front-end/src/`: The source file for the front-end components.<br/>
  Grouping all the TypeScript/JavaScript in the same place makes finding and bundling with them easier.
- `<package dir>/front-end/src/index.ts`: The entry point of the JavaScript bundle.<br/>
  This file must export the React components of the bundle.
- `<package dir>/front-end/src/<component>.ts`: The implementation file for a React
  component used by a dynamic element. Each component typically has its own
  implementation file.

## Going forward

A complete example of a custom extension library that holds both a static element and
dynamic elements is accessible with its entire source code and build process in
the `doc/extension` directory under the root directory of the Taipy GUI installation.<br/>
You can also take a look at this extension library example directly on
[GitHub](https://github.com/Avaiga/taipy/tree/[BRANCH]/doc/gui/extension).

This example defines a subclass of `ElementLibrary^` called `ExampleLibrary` that
holds several examples of custom elements.

The following sections demonstrate specific areas of the extension API. You should be able to
make your way from one example to the next.

- [Custom static elements](static_element.md)
- [Custom dynamic elements](dynamic_element/index.md)
- [Using scalar properties](dynamic_element/scalar_props.md)
- [Using List of Values](extension_list_of_values.md)
- [Using tabular data](extension_data.md)
- [Accessing assets](extension_assets.md)
- [Packaging an element library](extension_packaging.md)
