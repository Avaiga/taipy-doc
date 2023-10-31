> You can download the code for
<a href="./../src/step_01.py" download>Step 1</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 


!!! warning "For Notebooks"

    The Notebook is available [here](../getting_started.ipynb). In Taipy GUI,
    the process to execute a Jupyter Notebook is different from executing a Python Script.

# Step 1: First Web page

You only need one line of code to create your first Taipy web page. Just create a `Gui^` object
with a string and run it. 

In the console, you'll find a client link. All you need to do is copy and paste it into your web
browser to open your first Taipy page!


```python
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run() # use_reloader=True
```

By default, the page won't refresh on its own after you make a code modification.

If you want to alter this behavior, you can add `use_reloader=True` in the `.run()` method. This
will cause the application to automatically reload when you make changes to a file in your
application and save it. It's typically used in development mode.

If you wish to run multiple servers concurrently, you can modify the server port number (5000 by
default) in the `run()` method. For example, `Gui(...).run(port=xxxx)`. Other parameters to the
`run()` method can be found
[here](../../../../manuals/gui/configuration.md#configuring-the-gui-instance).


Keep in mind that you have the option to format your text. Taipy uses different ways to create
pages: [Markdown](../../../../manuals/gui/pages/index.md#using-markdown),
[HTML](../../../../manuals/gui/pages/index.md#using-html) or
[Python code](../../../../manuals/gui/page_builder.md). Here is the Markdown syntax to style your
text  and more. Therefore, `#` creates a title, `##` makes a subtitle. Put your text in `*` for
*italics* or in `**` to have it in **bold**.


![First Web Page](result.png){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }
