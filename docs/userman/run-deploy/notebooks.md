You can create and run a Taipy Graphical User Interface from a Jupyter Notebook.

In this situation, the web server that Taipy relies on will run on a separate thread,
so the Notebook works as expected.

# Creating a Taipy GUI application in a new Notebook

Here is a step-by-step approach to hosting a Taipy GUI within your Notebook
and interacting with it.

You will start your Jupyter server the usual way:
```py
jupyter notebook
```
Your browser should open a new window connected to the Jupyter server, where you can create
and manipulate Notebooks.

!!! note "Example code"
    You may want to load the [Notebook source](../gui/gui_example.ipynb) file directly within
    Jupyter and move from cell to cell instead of entering the code in the following
    steps.

Create a new Notebook by selecting the *New* > *Python 3 (ipykernel)* option located
in the upper right corner of the Jupyter interface.<br/>
Then, start creating the Notebook content.

Enter the following code into the first Notebook cell:
```py title="Cell [1]" linenums="1"
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

Note that we use the `Markdown^` class explicitly (in line 3). That is because, later in our code,
we will want to modify the content of the page.

Run the cell.<br/>
The output shows that a server was started (usually on *http://127.0.0.1:5000*),
hosting the 'Taipy' Flask app.<br/>
A new window is created in your browser, displaying the small interface we have just created.<br/>
Note that the text control automatically displays *value* when you move the slider thumb. That
shows that Taipy has successfully bound the variable *value* to both the
[`text`](../../refmans/gui/viselements/generic/text.md) and the
[`slider`](../../refmans/gui/viselements/generic/slider.md) controls.

You can witness the user interface update when you change a variable on the fly. In the context of
Notebooks, you can directly access the variables that are bound to the user interface:

# Updating pages

Pages can also be updated on-the-fly.

In the case when you do *not* use new variables in the new page content, you can simply use the
`(Page^).set_content()` method of the `Page^` class to update the content of the page.<br/>
In our example, that would mean calling this method on the *page* object.

Enter the following code into a new Notebook cell to test it out:

```py title="Cell [2]"
page.set_content("""
# Taipy in a Notebook

Value: <|{value}|>

Set: <|{value}|slider|>

As a number field: <|{value}|number|>
""")
```

All we did was add a `number` control to the page, bound to the same variable *value*.

Run this cell and refresh the page in the browser to see this control appear, showing the variable
value as it was set before. Changing the value in the number field or the slider will update it in
all three controls.

# Updating variables

The point of using Notebooks (besides making it possible to provide explanatory text along with the
code in a single document) is to allow for changing variables on the fly and see the impact of
these changes immediately. Let's see how we can use that feature with Taipy.

Enter the following line into a new cell:
```py title="Cell [3]"
gui.state.value = 50
```
When you run this cell, the new value is reflected in the text, the slider, and the number field.
There is no need to refresh the application page.

!!! note "The gui.state property"
    This property is provided **only** in the context of Notebooks, where there is a single
    connection to the server, allowing to access a unique '*state*'.

# Adding variable bindings

A more complicated case is where new variables are introduced within the updated content of a page.
In this situation, you must update the content of the page with the `(Page.)set_content()^` method
just like above, then *reload* the application context using the `Gui.reload()^` method on the
*gui* object.

This is an example of where this must be done.<br>
In another cell, enter the following text:

```py title="Cell [4]"
import math

xrange = range(0, 720)

def compute_data(v):
    return [   v    * math.cos(2 * math.pi * x / 100) +
            (100-v) * math.sin(2 * math.pi * x / 50)
            for x in xrange]

data = compute_data(value)
```

After running this cell, the variable *data* holds an array of floating-point values representing
some fancy trigonometric function (computed in *compute_data()*) based on some parameter.

If we want to display these values in a chart, we need to change our page to add a
[`chart`](../../refmans/gui/viselements/generic/chart.md) control to it (and remove the
`number` control).<br/>
You can update the page content on the fly by creating a new cell with the following content:
```py title="Cell [5]"
page.set_content("""
# Taipy in a Notebook

Value: <|{value}|>

Set: <|{value}|slider|>

<|{data}|chart|>
""")
```

Run this cell.<br/>
If you refresh the page where the interface is displayed, you will see that the `chart` control
appears, but with no data. You also get warnings from Taipy indicating that the *data* variable
could not be found.

To make the `Gui` instance aware of the *data* variable, you must *reload* the server.<br/>
You can do that by creating a new cell with the following content:
```py title="Cell [6]"
gui.reload()
```
When you run this cell, your browser displays your application page, with the *data* variable
properly bound to the `chart` control.

Note that `gui.reload()` is equivalent to:
```py
gui.stop()
gui.run()
```

# Adding interaction

A final step we can take is to add some interaction to this application.<br/>
We want the data recomputed when the sider value is modified and witness the chart reflect that
change.

Create another cell and enter the following:

```py title="Cell [7]"
def on_change(state, var_name, var_value):
    if var_name == "value":
        state.data = compute_data(state.value)
```
Then, run this cell.

The code in this cell implements a callback function that gets called when controls on the page
trigger the `on_change` callback. This function updates the data displayed in the user
interface when the variable *value* changes (when the user moves the slider thumb).<br/>
However, the `Gui` object was initially created without knowing about this function that it must
bind controls to. To reset the Taipy server and connect to *on_change()*, you must run the final
cell:

```py title="Cell [8]"
gui.reload()
```

The page appears in your browser. The slider now controls the chart that is automatically updated
when a new value is set.

!!! note "Restarting the web server"
    Some Notebook environments cannot restart the underlying web server so that Taipy GUI
    can immediately reuse the port number it was communicating with. To cope with this problem, in
    the context of Notebooks only, the port number used as part of the application URL is a
    proxy to the real served port. Invoking `run()` after `stop()` generates a hidden port
    number that gets used transparently. This behavior is controlled by the
    [*notebook_proxy*](../advanced_features/configuration/gui-config.md#p-notebook_proxy) configuration setting.
