# Running in Notebooks

You can create and run a Taipy Graphical User Interface from a Jupyter Notebook.

In this situation, the Web server that Taipy relies on will run on a separate thread,
so the Notebook works as expected.

## Creating a Taipy GUI application in a new Notebook

Here is a step-by-step approach on hosting a Taipy GUI within your Notebook
and interacting with it.

You will start your Jupyter server the usual way:
```py
jupyter notebook
```
Your browser should open a new window, connected to the Jupyter server, where you can create
and manipulate Notebooks.

!!! Note "Example code"
    You may want to load the [Notebook source](gui_example.ipynb) file directly within
    Jupyter and move from cell to cell instead of entering the code in the following
    steps.

Create a new Notebook by selecting the _New_ > _Python 3 (ipykernel)_ option located
in the upper right corner of the Jupyter interface.<br/>
Then start creating the Notebook content.

Enter the following code into the first Notebook cell:
```py linenums="1"
from taipy.gui import Gui, Markdown

page = Markdown("""
# Taipy in a Notebook

Value: <|{value}|>

Set: <|{value}|slider|>
""")

value = 10

gui = Gui(page)
gui.run()
```

As you can see, we create and run our `Gui^` instance in lines 13 and 14.

Note that we use the `Markdown^` class explicitly (in line 3). That is because
later in our code, we will want to modify the content of the page.

Run the cell. The output shows that a server was started (usually on
_http://127.0.0.1:5000_), hosting the 'Taipy' Flask app.<br/>
A new window is created in your browser, displaying the small
interface we have just created.<br/>
Note that the text control automatically displays _value_ when you move the slider
thumb. That shows that Taipy has successfully bound the variable _value_ to both
the [`text`](viselements/text.md) and the [`slider`](viselements/slider.md)
controls.

You can witness the user interface update when you change a variable
on the fly. In the context of Notebooks, you can directly access the
variables that are bound to the user interface:

## Updating variables

The point of using Notebooks (besides making it possible to provide explanatory
text along with the code in a single document) is to allow for changing variables
on the fly and see the impact of these changes immediately. Let's see how we can
use that feature with Taipy.

Enter the following line into a new cell:
```py
gui.state.value = 50
```
When you run this cell, the new value is reflected both in
the text and the slider.

!!! important "The gui.state property"
    This property is provided **only** in the context of Notebooks, where
    there is a single connection to the server, allowing to access a single
    '_state_'.

## Updating pages

Pages can also be updated on-the-fly.

In another cell, enter the following text:

```py
import math

xrange = range(0, 720)

def compute_data(a):
    return [   a    * math.cos(2 * math.pi * x / 100) +
            (100-a) * math.sin(2 * math.pi * x / 50)
            for x in xrange]

data = compute_data(value)
```

After running this cell, the variable _data_ holds an array of floating-point values
representing some fancy trigonometric function (computed in _compute_data()_) based
on some parameter.

If we want to display these values in a chart, we need to change our page to
add a [`chart`](viselements/chart.md) control to it.<br/>
You can update the page content on the fly by creating a new cell with the following
content:

```py
page.set_content("""
# Taipy in a Notebook

Value: <|{value}|>

Set: <|{value}|slider|>

<|{data}|chart|>
""")
```

If you refresh the page where the interface is displayed, you will see that
the `chart` control appears just like you expected.

A final step we can take is to add some interaction to this application.<br/>
We want the data recomputed when the sider value is modified and
witness the chart reflect that change.

Create a final cell and enter the following:

```py
def on_change(state, var_name, var_value):
  if var_name == "value":
    state.data = compute_data(state.value)
```

The code in this cell updates the data displayed in the user
interface when the variable _value_ changes (that is, when the user
moves the slider thumb).<br/>
However, the `Gui` object was initially created without knowing
this function that it must bind controls to. To reset the Taipy server
and connect to _on_change()_, you must run the final cell:

```py
gui.stop()
gui.run()
```

Go to the Taipy interface page and refresh.<br/>
The slider now controls the chart that is automatically updated when a new
value is set.

!!! note "Restarting the Web server"
    Some Notebook environments are not able to restart the underlying Web server so that
    Taipy GUI can immediately reuse the port number it was communicating with. To cope with this
    problem, in the context of Notebooks only, the port number that is used as part of the
    application URL is a proxy to the real port that is served. Invoking `run()` after `stop()`
    generates a hidden port number that gets used transparently. This behavior is controlled by the
    [*notebook_proxy*](configuration.md#p-notebook_proxy) configuration setting.
