> You can download the code for this step [here](../src/step_00.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started/tree/develop/src).

!!! warning "For Notebooks"

    The "Getting Started" Notebook is available [here](https://docs.taipy.io/en/latest/getting_started/getting-started/getting_started.ipynb).

# Step 0: First web page

To create your first Taipy web page, you only need one line of code. Create a `Gui` object with a String and run it. 
A client link will be displayed in the console. Enter it in a web browser to open your first Taipy web client!

```python
from taipy import Gui

# A dark mode is available in Taipy
# However, we will use the light mode for the Getting Started
Gui(page="# Getting started with *Taipy*").run(dark_mode=False)
```

If you want to run multiple servers at the same time, you can change the server port number (5000 by default) in the `.run()` method. For example, `Gui(...).run(port=xxxx)`.


Note that you can style the text. Taipy uses the Markdown syntax to style your text and more. Therefore, `#` creates 
a title, `##` makes a subtitle. Put your text in `*` for *italics* or in `**` to have it in **bold**.


![First Web Page](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }
