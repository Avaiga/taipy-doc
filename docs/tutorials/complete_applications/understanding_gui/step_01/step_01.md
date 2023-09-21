> You can download the code for this step [here](../src/step_01.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started-gui/tree/develop/src).

!!! warning "For Notebooks"

    The "Getting Started" Notebook is available [here](https://docs.taipy.io/en/latest/getting_started/getting-started-gui/getting_started.ipynb). In Taipy GUI, the process to execute a Jupyter Notebook is different from executing a Python Script.

# Step 1: First Web page

You only need one line of code to create your first Taipy web page. Create a `Gui` object with a String and run it.

You will see a client link in the console. Simply copy and paste it into a web browser to open your first Taipy web client!


```python
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run() # use_reloader=True
```

By default, the page won't automatically reload itself after making a code change.

To change this behavior, putting `use_reloader=True` in the `.run()` will reload the application when you modify a file in your application and save it. It can be used as a development mode.

If you want to run multiple servers simultaneously, you can change the server port number (5000 by default) in the `.run()` method. For example, `Gui(...).run(port=xxxx)`. Other options of the `.run()` can be found [here](https://docs.taipy.io/en/latest/manuals/gui/configuration/#configuring-the-gui-instance).


Note that you can style the text. Taipy uses the Markdown syntax to style your text and more. Therefore, `#` creates 
a title, `##` makes a subtitle. Put your text in `*` for *italics* or in `**` to have it in **bold**.


![First Web Page](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }
