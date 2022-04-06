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
represent one or several values stored in a _list of values_ (or _LoV_, for short).
This notion is a way of describing a set of values that controls can show and select.

Each item in a _list of values_  can hold:

- An identifier: an optional string that uniquely identifies an item in the entire
  list;
- A label: a string that is used when displaying the specific item;
- An image: an optional `Icon^` that can be used to display the item as a small
  image. Note that icons can also hold a descriptive string.

A _LoV_ can have different types, depending on the use case:

- List of strings: if your items are just a series of strings, you can
  create a _LoV_ as a List[str] or a single string, where item labels
  are separated by a semicolon (';');

- List with identifier: in situations where items labels may appear
  several times in the same _LoV_, you will need a unique identifier to
  specify which item is represented.<br/>
  In this situation, the _LoV_ will be a list of tuples where each tuple
  will contain:

   - A unique identifier as the first item;
   - A label as the second item.

  Therefore, the Python type of such a _LoV_ is List[Tuple[str, str]].
  
- List with images: if you need to represent items with images, you
  will create a _LoV_ that is a list of tuples where each tuple
  will contain:

   - A unique identifier as the first item;
   - An `Icon^` as the second item.

  The Python type of such a _lov is: List[Tuple[str, `Icon^`]].

The "selected" value in controls that use _LoV_s are handled in their _value_
property. This will be the original value of the selection in the _LoV_ unless
your control has set the property _value_by_id_ to True, then the selected value
will be the unique identifier of the value in the _LoV_.

### Custom LoVs

You can create a _LoV_ from any series of objects.

In this situation, you will provide the control with your list of objects in
the property _lov_, and an _adapter_ function that transforms each item of
the list into a tuple that the control can use as a 'regular' _LoV_.

An _adapter_ is a Python function that receives each object
of a _LoV_ and that must return a tuple similar to the ones
used in 'regular' _LoV_s.

!!! example "Example"

    Suppose you want to display a control representing versions
    of the Python programming language. You want to display this list
    in [selector](viselements/selector.md) and let users select
    a given version.
    
    The _list of values_ is an ordered list of descriptors:

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
    ```

    You need to represent each item as: "Version &lt;version name&gt; (&lt;version date&gt;)".
    The identifier for each version will be its name, which is unique.

    The adapter you need to write would look like this:
    ```py
    def python_version_adapter(version):
      return (version["name"], f"Version {version["name"]} ({version["date"]})")
    ```

### _LoV_ for trees

The [tree](viselements/tree.md) control needs an additional item in
each value of the _LoV_: each element of the _LoV_ represents a node
in the tree, and the additional element in each node's tuple must hold
the child nodes as another _LoV_, or None if it does not have any.

Here is an example of how a _LoV_ for trees can be created.

We want to provide a control that allows the selection of a musical instrument
from a tree control where instruments are classified:

```py
selected_intrument = None
intruments = [
  ("c1", "Idiophones", [
    ("t1-1", "Concussion", ["Claves", "Spoons"]),
    ("t1-2", "Percussion", ["Triangle", "Marimba", "Xylophone"]),
    ("t1-3", "Plucked", ["Pizzicato "])
  ]),
  ("c2",  "Membranophones", [
    ("t2-1", "Cylindrical drums", ["Bass drum", "Dohol"]),
    ("t2-2", "Conical drum", ["Timbal"]),
    ("t2-3", "Barrel drum", ["Dholak", "Glong thad"])
  ]),
  ("c3",  "Chordophones", [
    ("t3-1", "Plucked", ["Guitar", "Harp", "Mandolin"]),
    ("t3-2", "Bowed", ["Violin", "Cello", "Jinghu"])
  ]),
  ("c4",  "Aerophones", [
    ("t4-1", "Flute", ["Piccolo", "Bansuri", "Transverse flute"]),
    ("t4-2", "Reed", ["Bassoon", "Oboe", "Clarinet"]),
    ("t4-3", "Brass", ["Trombone", "Trumpet", "Cornett"])
  ])
]
```
The tree items are stored in the variable _instruments_, and _selected_instrument_
will be bound to the tree selection.

The Markdown fragment that would be used in a page would look like this:
```
<|{selected_intrument}|tree|lov={intruments}|>
```

## Tabular values

The [chart](viselements/chart.md) and [table](viselements/table.md) controls
represent tabular data. This data can be provided as a
[Pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html),
a list, a [NumPy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html),
or a dictionary.

When a variable containing such tabular data is bound to a control, it is
internally transformed into a Pandas DataFrame so one can specify
which series of data should be used by a control bound to that data:
for a table, you can indicate which data a column displays. In a chart, you can
have different traces for different series in the same graph.

Note that the Python list comprehension syntax (i.e. expressions such as
`[x for x in range(0, 10)]`) is appropriately handled, as long as the returned
type is one of the supported types. Such expressions can even be inlined
directly in the definition of the properties of your control.

This is how Taipy internally stores the tabular data:

- If the data is a dictionary, Taipy creates a DataFrame directly from it.
- If the data is a list of scalar values, Taipy creates a DataFrame with a single
  column called '0'.
- If the data is a list of lists:
  - If all the lists have the same length, then Taipy creates a DataFrame with
    one column for each list, in the order of the list data.
    The column names are the list index.
  - If the lengths of the lists differ, Taipy creates an internal list of
    DataFrames, that each has one single column. The name of the DataFrame
    column is &lt;index&gt;/0, where &lt;index&gt; is the index of the list
    in the original data list.

!!! note "List of lists in charts"
    To display several traces within the same chart control, you must use a list
    of tabular values.

!!! note "Column names"
    When dealing with a list of tabular data, you need to access the name of
    the data columns to provide them to the controls that use them.

    To select a column for a control, you must provide the name of this column,
    prefixed with the index of the data and a slash character.<br/>
    For example, suppose your data set is defined with the following Python code:
    ```py
    dataframe_1 = pd.DataFrame({'x': [i for i in range(10)],
                                'y': [i for i in range(10)]} )
    dataframe_2 = pd.DataFrame({'x': [i for i in range(10)],
                                'y': [i*i for i in range(10)]})
    data = [ dataframe_1, dataframe_2 ]
    ```
    In controls that are bound to _data_, the name of the 'y' column of the second
    DataFrame must be the string "1/y" .

## Lambda expressions

Some control properties can be assigned lambda expressions to simplify the
code.

You can, for example, bind a lambda function to the _on_action_ property of
a control. Here is how you can do this with Markdown:
```
<|Action|button|on_action={lambda state: ...}|>
```
The lambda expression receives the same parameters as the regular _on_action_
callback function.

Because Python prevents any assignment from being performed in the body of a lambda
expression, you cannot update the _state_ object directly. However, the `State^`
class exposes the method `(State.)assign()^` that allows working around
that limitation. Here is how you can change the value of the variable _toggle_
directly from the Markdown definition of your page, within the body of the
definition of a button:
```
<|Toggle|button|on_action={lambda state: s.assign("toggle", not state.toggle)}|>
```
Pressing the button will toggle the value of the _toggle_ variable.
