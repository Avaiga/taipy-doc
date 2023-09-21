> You can download the code for
<a href="./../src/step_02.py" download>Step 2</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 

!!! warning "For Notebooks"

    The "Getting Started" Notebook is available [here](../../../../getting_started/getting-started-gui/getting_started.ipynb). In Taipy GUI, the process to execute a Jupyter Notebook is different from executing a Python Script.

# Step 2: Visual elements

Many visual elements can be added to the basic code viewed in Step 1. This Step shows how to use visual elements 
like charts, sliders, tables, etc., inside the graphical interface.

## Visual elements

Taipy GUI can be considered as an **augmented** Markdown; it adds the concept of 
**[Visual elements](../../../../manuals/gui/viselements/index.md)** on top of all the Markdown syntax. A visual 
element is a Taipy graphical object displayed on the client. It can be a 
[slider](../../../../manuals/gui/viselements/slider.md_template), a 
[chart](../../../../manuals/gui/viselements/chart.md_template), a 
[table](../../../../manuals/gui/viselements/table.md_template), an 
[input](../../../../manuals/gui/viselements/input.md_template), a 
[menu](../../../../manuals/gui/viselements/menu.md_template), etc. Check the list 
[here]( ../../../../manuals/gui/viselements/controls.md_template).

Every visual element follows a similar syntax:

`<|{variable}|visual_element_name|param_1=param_1|param_2=param_2| ... |>`.

For example, a [slider](../../../../manuals/gui/viselements/slider.md_template) is written this way :

`<|{variable}|slider|min=min_value|max=max_value|>`.

For each visual element you wish to add to your web page, you must include the above-mentioned syntax inside your markdown 
string (representing your page). Example: at the beginning of the page, let's display:

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

Gui(page).run()
```

![Visual Elements](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }
