# Binding variables

It will often be useful to display information from the application.<br/>
To achieve this goal, Taipy allows [visual elements](viselements/index.md)
to relate directly to application variables, display their values, and
change those variable values.

Consider the following application:

```py linenums="1"
from taipy import Gui

x = 1234

Gui(page="""
# Hello Taipy

The variable `x` contains the value <|{x}|>.
""").run()
```

When this program runs (and a Web browser is directed to the running server), the
root page displays the value of the variable _x_, as it was defined in your code.

## Expressions

Values that you can use in controls and blocks can be more than raw variable values.
You can create complete expressions, just like you would use
in the _f-string_ feature (available since Python 3).

In the code above, you could replace `<|{x}|>` by `<|{x*2}|>`, and the double of _x_
will be displayed on your page.

!!! Note "Arbitrary expressions"
        You can create complex expressions such as `|{x} and {y}|` to concatenate
        two variable values, or whatever your imagination and application requirements are.

!!! Note "Formatting"
        F-string formatting is also available in property value expressions:

        - If you have declared `pi = 3.141592653597`, then `<|Pi is {pi:.4f}|>` will
          display the text:<br/>
          `Pi is 3.1416`.
        - If you have `v = 64177`, then `<|dec:{v}, oct:{v:08o}, hex:{v:X}|>` will result
          in displaying the text:<br/>
          `dec:64177, oct:00175261, hex:FAB1`.

        Note that since HTML text eliminates non-significant white space,
        right-justification format (`{string:>n}`) does not impact the resulting
        display.

## List of values

Some controls (such as [selector](viselements/selector.md) or [tree](viselements/tree.md))
represent one or several values that come from a _list of values_ (or _lov_, for short).
This notion is a way of describing a set of values that a control can show or select.

Each item in a _list of values_  can hold:

- An identifier: an optional string that uniquely identifies an item in the entire
  list;
- A label: a string that is used when displaying the specific item;
- An image: an optional `Icon^` that can be used to display the item as a small
  image. Note that icons can also hold a descriptive string.

A _lov_ can have different types, depending of the use case:

- List of strings: if your items are just a series of string, you can
  create a _lov_ as a List[str] or a single string, where item labels
  are separated by a semicolon (';');

- List with identifier: in situations where items labels may appear
  several times in the same _lov_, you will need a unique identifier to
  specify which item is represented.<br/>
  In this situation, the _lov_ will be a list of tuples where each tuple
  will contain:

   - A unique identifier as the first item;
   - A label as the second item.

  The Python type of such a _lov is therefore: List[Tuple[str, str]].
  
- List with images: if you need to represent items with images, you
  will create a _lov_ that is a list of tuples where each tuple
  will contain:

   - A unique identifier as the first item;
   - An `Icon^` as the second item.

  The Python type of such a _lov is: List[Tuple[str, `Icon^`]].

The "selected" value in controls that use _lov_s are handled in their _value_
property. This will be the original value of the selection in the _lov_, unless
your control has set the property _value_by_id_ to True:
in this situation, the selected value will be the unique identifier of the value
in the _lov_.

## Custom _lov_

You can create a _lov_ from any series of objects.

In this situation, you will provide the control with your
list of objects, and an _adapter_ function that transforms
each item of the list into a tuple that the control can
use as a 'regular' _lov_.

An _adapter_ is a Python function that receive each object
of a _lov_, and that must return a tuple similar to the ones
used in 'regular' _lov_s.

!!! example "Example"

    Suppose we want to display a control that represents versions
    of the Python programming language. We want users to be able to select
    a given version.
    
    Our _list of values_ is an ordered list of descriptors:

    ```py
    python_versions=[
      { "name": "0.9.0", "date": 1991 },
      { "name": "1.0",   "date": 1994 },
      { "name": "1.1",   "date": 1994},
      { "name": "1.6",   "date": 2000 },
      { "name": "2.0",   "date": 2000 },
      { "name": "2.2",   "date": 2001 },
      { "name": "2.3",   "date": 2003 },
      { "name": "2.7",   "date": 2010 },
      { "name": "3.0",   "date": 2008 },
      { "name": "3.4",   "date": 2014 },
      { "name": "3.8",   "date": 2019 },
      { "name": "3.9",   "date": 2020 },
      { "name": "3.10",  "date": 2021 }
    ]

    We want to represent each item as: "Version <version name> (<version date>)".
    The identifier for each version will be its name, which is unique.

    The adapter will will need to write would look like:
    ```py
    def python_version_adapter(version):
      return (version["name"], f"Version {version["name"]} ({version["date"]})")
    ```

## _lov_ for trees

The [tree](viselements/tree.md) control needs an additional item in
each value of the _lov_: each element of the _lov_ represent a node
in the tree, and the additional element in each node's tuple holds
the child nodes, as another _lov_.

TODO example

## Tabular values

TODO

## Lambda expressions

Some control properties can be assigned lambda expressions to simplify the
code.

TODO
