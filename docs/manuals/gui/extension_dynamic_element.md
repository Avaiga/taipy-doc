# Dynamic elements

The [previous section on static elements](extension_static_element.md) exposes
how element libraries and elements are defined. A major limitation with
static elements is that you cannot change their property values at run-time.
In Taipy GUI, you can [bind Python variables or expressions](binding.md)
to properties so that when the application changes the value of a
variable, it can be immediately reflected in the user interface.<br/>

Custom elements that allow for variable binding are called *dynamic elements*
in Taipy GUI.

Dynamic elements use [TypeScript](https://www.typescriptlang.org/) and
[JavaScript](https://www.javascript.com/) code to dynamically generate HTML code to
produce the pages that can be displayed in a browser. Taipy GUI actually relies
on the [React](https://reactjs.org/) JavaScript library to simplify the
development of graphical components.
