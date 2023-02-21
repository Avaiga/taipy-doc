# Extension Libraries

Although Taipy GUI comes with a set of visual elements that lets users create comprehensive
user interfaces, there are situations where applications may need to provide a particular
kind of element with capabilities that one cannot find in Taipy GUI out-of-the-box.

Taipy GUI has an extension mechanism that allows developers to add their own
visual elements so they can be accessed by Taipy GUI when defining page content.<br/>
This mechanism is known as "Taipy GUI Extension".

## Introduction

Taipy GUI lets developers create and use custom visual elements to address specific use
cases or integrate third-party Web components. One can expand the functionality
offered by the base Taipy GUI package to create custom components that can be
effortlessly used in pages and shared with the community.

Custom visual elements are grouped into *Element Libraries*, where each element is identified
by its name. An element name must be unique in the context of its library.<br/>
Each library also has a name. To insert a custom visual element in a page, you will use
the full name of the element:

- `<library_name>.<element_name>` in a Markdown page
- `<library_name>:<element_name>` in an HTML page

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
from taipy.gui.extension import ElementLibrary

class MyCustomLibrary(ElementLibrary):
    def get_name(self) -> str:
        return "library_name"

    def get_elements(self) -> dict:
        return ({
          "element1_name": Element(...),
          "element2_name": Element(...),
          })
```

Other methods can be overridden if necessary, which will be discussed later in the manual.

## Declaring Elements

As we have seen, custom visual element descriptors are associated with the name of
the element as it appears on pages in the `(ElementLibrary.)get_elements()^` method.

The [`Element` constructor](Element.__init__()^) needs a description of all the properties
that this element holds, as well as how this element is rendered.

```py
Element("<default_property_name>",
       {
           "<property_1_name>": ElementProperty(<property_1_type>, ...),
           "<property_2_name>": ElementProperty(<property_2_type>, ...),
           ...
        },
        <rendering_arguments>)
```

An element property descriptor (handled by the `ElementProperty^` class) must
indicate its type (one of the `PropertyType^` values) and potentially a default
value.

All elements must indicate what their default property name is. That is used in Markdown
pages as the first fragment of the `<|...|>` construct or the value located in the
text part of an element tag in HTML pages.

Of course, *default_property_name* must be one of the keys of the properties dictionary
provided to the [`Element` constructor](Element.__init__()^).

## Rendering Elements

The Taipy GUI Extension package provides two different ways to implement the rendering
of the element and its interactions. Both approaches deliver HTML fragments that are
inserted into the page when it is requested.

- Static elements.<br/>
  A static visual element cannot interact with the underlying application.
  It can be used just like any other element in a page, but its properties are not
  bound to application variables: if a variable value is modified, it does not
  impact the representation of the element on the page.<br/>
  Static elements are implemented by creating a string that holds the XHTML text (that is,
  HTML that respects the XML syntax, where all tags must be closed) that is inserted in
  the page displayed by the browser.<br/>
  Please go to the [Static Elements Example](extension_static_element.md) page for
  a complete description of how to implement your own static custom elements.

- Dynamic elements.<br/>
  Dynamic elements provide the binding functionality of Taipy GUI: if a property value
  depends on an application variable (and if the property type is *dynamic*), then the
  page automatically updates when the variable value changes.<br/>
  In Taipy GUI, dynamic visual elements are implemented using the
  [React](https://reactjs.org/) JavaScript library and the
  [TypeScript](https://www.typescriptlang.org/) programming language (that builds on
  JavaScript).

## Prerequisites

To create and use custom visual elements, you need to install the following:

- Taipy GUI 2.0 or higher (included in Taipy and Taipy Enterprise).
- Python 3.8 or higher.
- [Node.js](https://nodejs.org) (version 18 or above) if you need to create dynamic custom visual
  elements. Note that this comes with `npm`, the Node Package Manager.

Basic knowledge of React (that we use with TypeScript) is welcome.

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
<project_dir>
├── pyproject.toml
├── MANIFEST.in
└── <package_dir>/
    ├── __init__.py
    ├── library.py
    └── frontend/
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
  an extension library. See the [section on packaging](../extension_packaging.md) for more
  details.
- `MANIFEST.in`: Commands to be executed when the Python package is built as a source distribution.
  The [section on packaging](../extension_packaging.md) explains what this file should contain.
- `<package_dir>/`: The root directory for the extension library. This contains all the Python
  (and potentially TypeScript/JavaScript code) needed to build the extension library.<br/>
  The name of this directory is used as the name of the root directory for the Python package.
- `<package_dir>/__init__.py`: Required to make `<package_dir>` a valid Python package directory.</br>
  It is also the right place to import the library class because it is easier from the developer's
  standpoint when a Taipy GUI application imports the extension library.
- `<package_dir>/library.py`: The implementation file for the extension library.<br/>
  This is where you typically will define the subclass of `ElementLibrary^` that implements
  your extension library.
- `<package_dir>/frontend/`: If you create an extension library containing dynamic
  elements, we strongly encourage storing all the front-end-specific code in this
  dedicated directory.<br/>
  This should contain all the TypeScript/JavaScript code for the React components and
  what it takes to build the JavaScript bundle that the extension library uses.
- `<package_dir>/frontend/package.json`: The meta-data for the Node project that holds
  the components implementing the front-end side of the dynamic elements of your extension
  library.
- `<package_dir>/frontend/tsconfig.json`: The TypeScript compilation options.
- `<package_dir>/frontend/webpack.config.js`: The configuration to build the JavaScript
  bundle of the extension library.
- `<package_dir>/frontend/src/`: The source file for the front-end components.<br/>
  Grouping all the TypeScript/JavaScript in the same place makes finding and bundling with them easier.
- `<package_dir>/frontend/src/index.ts`: The entry point of the JavaScript bundle.<br/>
  This file must export the React components of the bundle.
- `<package_dir>/frontend/src/<component>.ts`: The implementation file for a React
  component used by a dynamic element. Each component typically has its own
  implementation file.

## Going forward

A complete example of a custom extension library that holds both a static element and
dynamic elements is accessible with its entire source code and build process in
the `doc/extension` directory under the root directory of the Taipy GUI installation.<br/>
You can also take a look at this extension library example directly on
[GitHub](https://github.com/Avaiga/taipy-gui/tree/[BRANCH]/doc/extension).

Here are examples of custom elements you can build with a complete explanation of what
part of the Taipy GUI Extension API is used.

Each example addresses specific areas of the extension API. You should be able to
make your way from one example to the next.

- [Custom static elements](extension_static_element.md)
- [Custom dynamic elements](extension_dynamic_element.md)
- [Using scalar values](extension_scalar_values.md)
- [Using List of Values](extension_list_of_values.md)
- [Using tabular data](extension_data.md)
- [Accessing assets](extension_assets.md)
- [Packaging an element library](extension_packaging.md)
