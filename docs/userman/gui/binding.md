It will often be useful to display information stored in application data.<br/>
To achieve this goal, Taipy allows [visual elements](../../refmans/gui/viselements/index.md)
to relate directly to application variables, display their values, and
change those variable values.

Consider the following application:

<a name="first-example"></a>

```python linenums="1"
from taipy import Gui

if __name__ == "__main__":
  x = 1234

  Gui(page="""
# Hello Taipy

The variable `x` contains the value <|{x}|>.
  """).run()
```

When this program runs (and a web browser is directed to the running server), the
root page displays the value of the variable *x*, as it was defined in your code.

# Expressions

Values that you can use in controls and blocks can be more than raw variable values.
You can create complete expressions, just like you would use
in the *f-string* feature (available since Python 3).

In the [example code above](#first-example), you could replace `<|{x}|>` by `<|{x*2}|>`,
and the double of *x* will be displayed on your page.

!!! note "Arbitrary expressions"
    You can create complex expressions such as `|{x} and {y}|` (using the Markdown syntax) to
    concatenate two variable values, or whatever your imagination and application requirements are.

!!! note "Formatting"
    F-string formatting is also available in property value expressions:

    - If you have declared `pi = 3.141592653597`, then `<|Pi is {pi:.4f}|>` will
      display the text:<br/>
      `Pi is 3.1416`.
    - If you have `v = 64177`, then `<|dec:{v}, oct:{v:08o}, hex:{v:X}|>` will result
      in displaying the text:<br/>
      `dec:64177, oct:00175261, hex:FAB1`.

    Note that since HTML text eliminates non-significant white space, the
    right-justification format (`{string:>n}`) does not impact the resulting
    display.

# Scope for variable binding

In the tiny example above, the entire application holds a single page.
The bound variable (*x*) is defined in the same, unique module.

In larger applications, we may want to create Python modules that hold
Taipy pages, binding visual elements to local variables. That allows for
a clearer code organization, where application variables used in
only a few pages can sit next to the page definition.

When Taipy finds a variable in a page (that is, in a Python expression set to
a property using the curly braces syntax: *{expression}*), it first tries to locate it
in the module where this page is defined. If the variable can not be found in the page
module, then the variable is sought in the *\_\_main\_\_* module (typically, where the
`Gui^` instance is created).<br/>
We call *page scopes* the context where the variables are located: first, the module
where the page is defined, then the main module.

!!! note "Defining a page scope"
    A page scope, where variables used in a page definition are searched, is the module
    where the page *instance* (an instance of the `Markdown^`, `Html^` or
    `(taipy.)gui.builder.Page^` classes), **not** the text of the page.

This mechanism allows pages to bind to local variables declared on their own module.
These variables may not be exposed to other modules of the application.<br/>
Global variables (the ones declared in the *\_\_main\_\_* module), on the other hand, can
be used in all page content definitions. The module where the page is defined does not need
to import the global variables if they are not used in the Python code for that module.

!!! example "Example"
    Say you want to create a page that represents some evaluation of an expression using two
    variables. The first variable would be global for the application. But, the second variable
    does not need to be exposed to the rest of the application, so we store it as a local
    variable in the module where the page is defined.<br/>
    We create a *pages* package. In this package we create the file `page.py`, which is the module
    file where we would declare the page:

    ```python linenums="1"  title="pages/page.py"
    from taipy.gui import Markdown

    page = Markdown("""# Expression evaluation
    Expression value: <|{base_value + local_value}|>
    """)

    local_value = 0
    ```

    Note that the page definition uses the variable *base_value* (in line 4), which
    is unknown to this module.<br/>
    The page also references the variable *local_value* (line 7), defined locally in
    this module.

    Now, let's create the main module of the application, add a home page, and reuse
    the page we just created above. That would be done in the file `main.py`, defining the
    *\_\_main\_\_* module of our application:

    ```python  linenums="1" title="main.py"
    from taipy.gui import Gui, Markdown
    from pages.page import page

    if __name__ == "__main__":
        navigation = [("/home", "Home"), ("/page", "Expression")]
        root_page="""
    <|navbar|lov={navigation}|>
        """

        home_page="""
    # Home page
    ...
        """

        base_value = 0

        pages={
            "/": Markdown(root_page),
            "home": Markdown(home_page),
            "page": page,
        }

        Gui(pages=pages).run()
    ```

    *page* is imported from `pages.page` (that is the file `pages/page.py`) in
    line 2, then added to the `Gui` instance in line 18.

    When you run the application, you will see that the 'Expression' page can
    evaluate the expression stored in its text element. The local variable
    *local_value* was never exported from the *page* module, and neither was the
    global *base_value* imported in *page*.<br/>
    Nevertheless, the evaluation of the expression is performed properly, using
    those two variables.

## Local callback functions

This principle applies to callback functions as well: when a function name is found
in a page definition, this function is first searched in the page scope (the module where
the page was defined). If the function cannot be located, it is sought in the main
module.

This makes it possible to use the same callback function name in different modules and
rely on page scopes to determine which is invoked when a callback is triggered: Taipy
GUI favors the callback functions that are defined in the module where the page itself is
defined.

!!! note "Global callback functions"
    The way you can define local callback functions does not apply to global callbacks
    such as `on_action()`. There can be only one global callback, defined in the main
    module.

    However, a global callback can call any function in any module where a page would have been
    define, and the *state* will behave as you would expect, letting you access the variables
    from the page scope.

    Here is an example to demonstrate that. Suppose you need to initialize some variables from
    a page defined in a module. The proper way to do this would be to define a function called
    *on_init()* and initialize the state variable. However, because *on_init()* is a global
    callback and would not be invoked in the module (contrary to when it is declared in the
    *\_\_main\_\_* module), you need to declare an initialization function in the page module
    (no matter what its name is) and invoke this function from the global *on_init()* callback.

    The code for the module would look like this:
    ```python title="page.py"

    ...
    my_variable = ""
    ...
    def on_init(state):
        state.my_variable = "The initial value"
    ...
    sub_page=Markdown("""  ... some content referencing {my_variable} ... """)
    ```

    Note that we have called the initialization function *on_init()*, but that's really just
    a way to make the code easier to understand: what we want to do here is exactly what should
    be done in the global `on_init` callback.

    Here is how the main module would invoke this initialization function:
    ```python title="main.py"
    # Create an alias for on_init() in the page module
    from page import on_init as page_on_init

    def on_init(state):
        page_on_init(state)
    ```

    Now when the application is initialized from the main module, the global *on_init()* function
    invokes the page module's *on_init()* function with the received *state*. The access to the
    state in the page module's *on_init()* function will properly impact the variable in the
    correct page scope.

!!! example
    Here is an example of how this local callback binding is done. This example has a main module
    that holds a single page (at the root of the application URL) with a
    [`navbar`](../../refmans/gui/viselements/generic/navbar.md) control that can navigate to the page *sub_page*, imported
    from another module.<br/>
    The root page also has a button that, when pressed, invokes the callback function
    *button_pressed()*:

    ```python title="main.py"
    from taipy.gui import Gui, Markdown
    from page import sub_page

    def button_pressed(state):
        ...

    if __name__ == "__main__":
        navigation = [("/sub_page", "Page")]

        root_page="""
    # Application
    <|navbar|lov={navigation}|>

    <|Press for action|button|on_action=button_pressed|>
        """

        Gui(pages={
                "/": Markdown(root_page),
                "sub_page": sub_page
            }).run()
    ```

    Here is the code for the *page* module, where *sub_page* is defined:
    ```python title="page.py"
    from taipy.gui import Markdown

    def button_pressed(state):
        ....

    sub_page=Markdown("""# Sub-Page
        <|Press for action|button|on_action=button_pressed|>""")
    ```

    All this module does is define the (local) function *button_pressed()*, and the
    *sub_page* page that the main module imports.

    Now both the root page **and** the sub-page have a button, defined so they would invoke a
    callback function called *button_pressed()* when activated.<br/>
    The Taipy GUI implementation is such that if you press the button from the root page (defined
    in the main module), then it is the global function *button_pressed()* that gets called. If
    you press the button from the sub page (defined in the *page* module). then it is the function
    *button_pressed()* defined in the *page* module that gets called.

## Page scope in callbacks

All callback functions are invoked with a state object as their first parameter.<br/>
From that state, one can access the variables of the application. However, the state
interprets the access to variables depending on the page scope: if a callback is defined
in a module, then local variables will be available directly, scoped to the appropriate
module.

In the example above, we have defined two different callback functions called *button_pressed()*.
Suppose we had defined two variables called *x* in both the main module and the sub-page module,
then used *x* in both the root page and the sub-page, then when invoked, the state received
in the callback functions would behave slightly differently, enforcing the use of the page
scope:

- When the *button_pressed()* defined in the main module is invoked, then `state.x` would
  return the value of the *x* variable, in the main module.
- When the *button_pressed()* defined in the sub-page module is invoked, then `state.x` would
  return the value of the *x* variable, in the sub-page module.

This makes it very obvious to focus on the variable at hand in a given module where a page
is defined.

!!! note "Crossing page scopes"
    The state received in callbacks has a mechanism that lets you access variables from other
    modules.<br/>
    The way this works is to use the state object as a collection, indexed by the name of the
    module where the variable is defined (and used in a page definition).

    In the situation described above, no matter which *button_pressed()* callback function is
    invoked, you can always explicitly reference the *x* variable defined in the sub-page module
    using the syntax: *state["page"].x*. The indexed syntax avoids confusion.<br/>
    Similarly, *state["\_\_main\_\_"].x* always refers to the global *x* variable, defined in the
    main module.

# Sharing variables across clients

Your application can share a variable across all the connected users (identified as a new
connection to the application).<br/>
The `State^` object that all callbacks receive holds the value of all the bound variables for a
specific client. If you change that value, it does not impact the other clients' pages.

However, variables declared in the main module of the Python script can be *shared* among all the
connected users by declaring them as *shared variables*.<br/>
You can call the function `Gui.add_shared_variable(<variable-name>)^` to achieve that. When you do
this, modifying the value of `state.<variable-name>` is automatically propagated to every client.

Another way to achieve the same result is to use:
```
gui.broadcast_change("<variable-name>", new_value)
```
instead of
```
state.<variable-name> =  new_value
```

Using the `Gui.broadcast_change()^` function propagates a new value for a variable to the states of
every connected user.

The function `Gui.broadcast_changes()^` acts in a similar manner, for multiple variables and values.

# List of values

Some controls (such as [selector](../../refmans/gui/viselements/generic/selector.md) or
[tree](../../refmans/gui/viselements/generic/tree.md)) represent one or several values
stored in a *list of values* (or *LoV*, for short). This notion is a way of describing
a set of values that controls can show and select.

Each item in a *list of values*  can hold:

- **An identifier**: an optional string that uniquely identifies an item in the entire
  list;
- **A label**: a string that is used when displaying the specific item;
- **An image**: an optional `Icon^` that can be used to display the item as a small
  image. Note that icons can also hold a descriptive string.
- **A member** of an enumeration class.

A *LoV* can have different types, depending on the use case:

- **List of strings**: if your items are just a series of strings, you can
  create a *LoV* as a List[str] or a single string, where item labels
  are separated by a semicolon (';');

- **List with identifier**: in situations where items labels may appear
  several times in the same *LoV*, you will need a unique identifier to
  specify which item is represented.<br/>
  In this situation, the *LoV* will be a list of tuples where each tuple
  will contain:

    - A unique identifier as the first item;
    - A label as the second item.

    Therefore, the Python type of such a *LoV* is List[Tuple[str, str]].

- **List with images**: if you need to represent items with images, you
  will create a *LoV* that is a list of tuples where each tuple
  will contain:

    - A unique identifier as the first item;
    - An `Icon^` as the second item.

    The Python type of such a *lov* is: List[Tuple[str, `Icon^`]].

- **An enumeration class** (i.e. a class that inherits from `Enum`).
  
    You can set a *lov* directly from an enumeration class, as detailed in the
    ["LoVs as enumerations"](#lovs-as-enumeration) below.

The "selected" value in controls that use *LoV*s are handled in their *value*
property. This will be the original value of the selection in the *LoV* unless
your control has set the property *value_by_id* to True, then the selected value
will be the unique identifier of the value in the *LoV*.

## LoVs as enumeration {data-source="gui:doc/examples/binding_lov_is_enum"}

An enumeration class can be used to define a set of predefined values for a control. You can
assign the *lov* (List of Values) property of the control to the enumerated class you want to
use.

For example, consider the following enumeration class definition:
```python
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

color = Color.RED
```
In the code above, we also define and initialize the *color* variable, which can then be bound
to a control’s main value. You can directly use this class as the *lov* value in your
control.<br/>

You can directly use this class as a LoV value in you control.<br/>
Here is how you can use the *Color* enumeration class in a
[`toggle`](../../refmans/gui/viselements/generic/toggle.md) control:
!!! example "Enum as LoV"

    === "Markdown"

        ```
        <|{color}|toggle|lov={Color}|>
        ```

    === "HTML"

        ```html
        <taipy:toggle lov="{Color}">{color}</taipy:toggle>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.toggle("{color}", lov="{Color}")
        ```

        You can assign the enumeration class itself directly to the *lov* property
        ```python
        tgb.toggle("{color}", lov=Color)
        ```
        In this case, the *color* variable will hold the enumeration member's value (e.g., 0, 1, 2)
        instead of the enumeration member (e.g., the object `Color.RED`).

When this control is used on a page, the *color* variable will be updated to reflect the selected
member from the *Color* enumeration class.<br/>
If you're using the Page Builder API and have set the *lov* property to the enumeration class
directly, the variable will hold the member value (e.g., 0, 1, 2), otherwise, it will hold the
enumeration member itself (e.g., Color.RED).

## Custom LoVs

You can create a *LoV* from any series of objects.

In this situation, you will provide the control with your list of objects in
the property *lov*, and an *adapter* function that transforms each item of
the list into a tuple that the control can use as a 'regular' *LoV*.

An *adapter* is a Python function that receives each object
of a *LoV* and that must return a tuple similar to the ones
used in 'regular' *LoV*s.

!!! example "Example"

    Suppose you want to display a control representing versions
    of the Python programming language. You want to display this list
    in [selector](../../refmans/gui/viselements/generic/selector.md) and let users select
    a given version.

    The *list of values* is an ordered list of descriptors:

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
      { "name": "3.10",  "date": 2021 },
      { "name": "3.11",  "date": 2022 }
    ]
    ```

    You need to represent each item as: "Version &lt;version name&gt; (&lt;version date&gt;)".
    The identifier for each version will be its name, which is unique.

    The adapter you need to write would look like this:
    ```py
    def python_version_adapter(version):
      return (version["name"], f"Version {version["name"]} ({version["date"]})")
    ```

## *LoV* for trees

The [tree](../../refmans/gui/viselements/generic/tree.md) control needs an additional item in
each value of the *LoV*: each element of the *LoV* represents a node
in the tree, and the additional element in each node's tuple must hold
the child nodes as another *LoV*, or None if it does not have any.

Here is an example of how a *LoV* for trees can be created.

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
The tree items are stored in the variable *instruments*, and *selected_instrument*
will be bound to the tree selection.

The Markdown fragment that would be used in a page would look like this:
```
<|{selected_intrument}|tree|lov={intruments}|>
```

# Non-literal values

When a value whose type is not a literal type (i.e. a dictionary, a list, ...), assigning a new
value by simply calling `state.variable = <new_value>` will not propagate to the page.<br/>
The reason is that it would be too costly to find and communicate to the front-end just the values,
stored within potentially complex object structures, that actually require updates.

When you are in such a situation, you must call `(State.)refresh()^` method explicitly for a
refresh to happen: i.e. `state.refresh("variable")`.

# Tabular values

The [chart](../../refmans/gui/viselements/generic/chart.md) and
[table](../../refmans/gui/viselements/generic/table.md) controls
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

- If the data is a dictionary, Taipy creates a Pandas DataFrame directly from it.
- If the data is a list of scalar values, Taipy creates a Pandas DataFrame with a single
  column called '0'.
- If the data is a list of lists:
  - If all the lists have the same length, then Taipy creates a Pandas DataFrame with
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
    For example, suppose you have defined a data set with the following Python code:
    ```python
    dataframe_1 = pd.DataFrame({'x': [i for i in range(10)],
                                'y': [i for i in range(10)]} )
    dataframe_2 = pd.DataFrame({'x': [i for i in range(10)],
                                'y': [i*i for i in range(10)]})
    data = [ dataframe_1, dataframe_2 ]
    ```
    In controls that are bound to *data*, the name of the 'y' column of the second
    DataFrame must be the string "1/y".

# Lambda expressions

Some control properties can be assigned lambda expressions to simplify the
code.

You can, for example, bind a lambda function to the *on_action* property of
a control. Here is how you can do this with Markdown:
```
<|Action|button|on_action={lambda state: ...}|>
```
The lambda expression receives the same parameters as the regular *on_action*
callback function.

Because Python prevents any assignment from being performed in the body of a lambda
expression, you cannot update the *state* object directly. However, the `State^`
class exposes the method `(State.)assign()^` that allows working around
that limitation.<br/>
Here is how you can change the value of the variable *toggle* directly from the Markdown definition
of your page, within the body of the definition of a button:
```
<|Toggle|button|on_action={lambda state: s.assign("toggle", not state.toggle)}|>
```
Pressing the button will toggle the value of the *toggle* variable.
