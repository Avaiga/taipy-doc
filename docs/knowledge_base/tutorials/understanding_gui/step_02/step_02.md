> You can download the code for
<a href="./../src/step_02.py" download>Step 2</a>
or all the steps <a href="./../src/src.zip" download>here</a>.

!!! warning "For Notebooks"

    The Notebook is available [here](../tutorial.ipynb). In Taipy GUI,
    the process to execute a Jupyter Notebook is different from executing a Python Script.

# Step 2: Visual elements

You can incorporate various visual elements into the basic code demonstrated in Step 1. In this
step, we will illustrate how to utilize visual elements such as charts, sliders, tables, and
more within the graphical interface.

## Visual elements

When using the Mardown syntax, Taipy augments it with the concept of
**[visual elements](../../../../manuals/gui/viselements/index.md)**. A visual element is a
Taipy graphical object displayed on the client. It can be a
[slider](../../../../manuals/gui/viselements/slider.md), a
[chart](../../../../manuals/gui/viselements/chart.md), a
[table](../../../../manuals/gui/viselements/table.md), an
[input](../../../../manuals/gui/viselements/input.md), a
[menu](../../../../manuals/gui/viselements/menu.md), etc. Check the list
[here](../../../../manuals/gui/viselements/controls.md).

Every visual element follows a similar syntax:

`<|{variable}|visual_element_name|param_1=param_1|param_2=param_2| ... |>`.

For example, a [slider](../../../../manuals/gui/viselements/slider.md) is written this way :

`<|{variable}|slider|min=min_value|max=max_value|>`.

To include each visual element you want in your web page, you should incorporate the syntax
mentioned above within your markdown string, which represents your page.
For example, at the beginning of the page, if you want to display:

- a Python variable *text*

- an input that will "visually" modify the value of __text__.

Here is the overall syntax:

```
<|{text}|>
<|{text}|input|>
```

Here is the combined code:

```python
from taipy.gui import Gui

text = "Original text"

page = """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>
"""

Gui(page).run(debug=True)
```

![Visual Elements](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }
