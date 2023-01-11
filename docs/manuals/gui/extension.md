Although Taipy GUI comes with a set of visual elements that lets users create comprehensive
user interfaces, there are situations where applications may need to provide a very specific
kind of element with capabilities that one cannot find in Taipy GUI out-of-the-box.

# Adding custom visual elements

Taipy GUI lets developers create and use custom visual elements to address specific use
cases or integrate third-party Web components. One can expand the functionality
offered by the base Taipy GUI package to create custom components that can be
effortlessly used in pages and shared with the community.

Custom visual elements are grouped into *Element Libraries*, where each element is identified
by its name. An element name must be unique in the context of its library.<br/>
Each library also as a name. To insert a custom visual element in a page, you will use
the full name of the element:

- `<library_name>.<element_name>` in a Markdown page
- `<library_name>:<element_name>` in an HTML page

## Element Libraries and Custom Elements

An Element Library  holds the information necessary to refer to and instantiate custom visual elements. Element libraries can hold several visual element descriptors, and can be packaged
into a standalone Python package that a Taipy GUI application can import or that can be
deployed.

Here are important things you need to know about element libraries:

- An element library is a Python object that derives from the `ElementLibrary^` class. 
- Element libraries have a name (returned by `ElementLibrary.get_name()^`) that is
  used to refer to visual elements in page definitions.
- Element libraries hold the set of the elements it holds, as returned by
  `ElementLibrary.get_elements()^`.

You can create an element library by simply instantiating the `ElementLibrary^`, and override the methods that are required. The two mandatory methods to override are
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
the element as it appears in pages, in the `(ElementLibrary.)get_elements()^` method.

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

All elements must indicate what is its default property name. That is used in Markdown
page as the first fragment of the `<|...|>` construct, or the value located in the
text part of an element tag in HTML pages.

Of course *default_property_name* must be one of the keys of the properties dictionary
provided to the [`Element` constructor](Element.__init__()^).

## Rendering Elements

The Taipy GUI Extension package provides two different ways to implement the rendering
of the element and its interactions. Both approaches deliver HTML fragments that are
inserted in the page when it is requested.

- Static elements.<br/>
  A static visual element is one that cannot interact with the underlying application.
  It can be used just like any other element in a page, but its properties are not
  bound to the application variable: if the variable value is modified, it does not
  modify the representation of the element on the page.<br/>
  Static elements are implemented by creating a string that holds the XHTML text (that is,
  HTML that respects the XML syntax, where all tags must be closed) that is inserted in
  the page displayed by the browser.<br/>
  Please go to the [Static Elements Example](extension_static_element.md) page for
  a complete description of how to implement your own static custom elements.

- Dynamic elements.<br/>
  Dynamic elements provide the binding functionality of Taipy GUI: if a property value
  depends on an application variable (and if the property type is *dynamic*) then the
  page automatically updates when the variable value changes.<br/>
  In Taipy GUI, dynamic visual element are implemented using the
  [React](https://reactjs.org/) JavaScript library, and the
  [TypeScript](https://www.typescriptlang.org/) programming language (that builds on
  JavaScript).

## Prerequisites

In order to create and use custom visual elements, you need to install:

- Taipy GUI 2.0 or higher (included in Taipy and Taipy Enterprise).
- Python 3.8 or higher.
- NodeJS (and NPM) if you plan to create dynamic custom visual elements.

A basic knowledge of React (that we use with TypeScript) is welcome.

## Examples

A full example of a custom dynamic visual element is provided with the entire
source code and build process in the `doc/extension` directory under the root
directory of the Taipy GUI installation. You can also take a look at this
example directly on
[GitHub](https://github.com/Avaiga/taipy-gui/tree/develop/doc/extension).

Here are examples of custom element libraries that you can build with the
complete explanation of what part of the Extension API is used.

Each example addresses specific areas of the extension API. You should be able to
make you way from one example to the next.

- [File Structure](extension_file_structure.md)
- [Custom static element](extension_static_element.md)
- [Accessing assets](extension_assets.md)
- [Custom dynamic element](extension_dynamic_element.md)
- [Using List of Values](extension_list_of_values.md)
- [Using tabular data](extension_data.md)
- [Packaging an element library](extension_packaging.md)
