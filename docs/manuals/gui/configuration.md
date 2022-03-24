# User Interface Configuration

The user interfaces 

## Configuring the `Gui` instance

You can configure the User Interface part of your application using
these settings:

   - _host_ (str, default: 127.0.0.1): the hostname of the server.
   - _port_ (int, default: 5000): the port that the server uses.
   - _dark_mode_ (bool, default: True): whether the application shows in Dark mode (True)
     or light mode (False).
   - _debug_ (bool, default: True): set to True if you want to be provided with detailed
     debugging information messages from the server.
   - _margin_ (str or None, default: "1em"): a CSS dimension value that indicates how far
     from the border of the windows should your interface be. The default value avoids
     elements getting glued to the window borders, making it nicer to look at.
   - _use_reloader_ (bool, default: True):
   - _time_zone_ (str, default: "client"): indicates how date and time values should be
     interpreted.<br/>
     You can use a TZ database name (as listed in [Time zones list on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
     or one of the following values:
      - _"client"_ indicates that the time zone to be used is the Web client's.
      - _"server"_ indicates that the time zone to be used is the Web server's.
   - _propagate_ (bool, default: True):
   - _favicon_ (str or None, default is the Avaiga logo): the path to an image file used
     as the page's icon when navigating your Taipy application.
   - _title_ (str or None, default: "Taipy App"): the string displayed in the browser page
     title bar when navigating your Taipy application.
   - _theme_ (t.Union[t.Dict[str, t.Any], None]):
   - _theme[light]_ (t.Union[t.Dict[str, t.Any], None]):
   - _theme[dark]_ (t.Union[t.Dict[str, t.Any], None]):
   - _use_arrow_ (bool, default: False): indicates, when True, that you want to use the
      [Apache Arrow](https://arrow.apache.org/) technology to serialize data to Taipy
      clients. This allows for better performance in some situations.
   - _browser_notification_ (bool, default: True):
   - _notification_duration_ (int, default: 3000): the time, in milliseconds, that notifications
     should remain visible (see [Notifications](notifications.md) for details).
   - _single_client_ (bool, default: False): set to True if only a single client can connect.
     False indicates that multiple clients can connect to the server.
   - _ngrok_token_ (str, default: ""):
   - _upload_folder_ (str or None, default: None):
   - _data_url_max_size_ (t.Union[int, None]):
   - _flask_log_ (bool, default: False):

## Running in Notebooks

You can create and run a Taipy Graphical User Interface from a Jupyter Notebook.

In this situation, the Web server that Taipy relies on will run on a separate thread,
so the Notebook works as expected.

### Creating a new Notebook and create a Taipy GUI

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
And you can start creating the Notebook content.

Enter the following code into the first Notebook cell:

```py linenums="1"
from taipy.gui import Gui, Markdown

page=Markdown("""
# Taipy in a Notebook

Value: <|{value}|>

Set: <|{value}|slider|>
""")

value = 10

gui=Gui(page)
gui.run()
```

As you can see, we create and run our `Gui^` instance in lines 13 and 14.

Run the cell. The output shows that a server was started (usually on
_http://127.0.0.1:5000_), hosting the 'Taipy' Flask app.<br/>
You can now connect a new browser window to this server and see the small
interface we have just created.<br/>
Note that the text control automatically displays _value_ when you move the slider
thumb. That shows that Taipy has successfully bound the variable _value_ to both
the [`text`](viselements/text.md) and the [`slider`](viselements/slider.md)`
controls.

### Updating pages

The point of using Notebooks (besides making it possible to provide explanatory
text along with the code in a single document) is to allow for changing variables
on the fly and see the impact of these changes immediately. Let's see how we can
use that feature with Taipy.

In a second cell, enter the following text:

```py
import math

xrange= range(0, 720)

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

## Using an external Web server

Taipy user interfaces can be served by external servers. This happens in situations
where you already have a Web app running, and you want to add the GUI capabilities
of Taipy to it.

What you need to do in this case is use the _flask_ parameter of the `Gui^` constructor,
setting it to the instance of the Flask server you are using.

Here is a short code sample that should make this straightforward:

```py linenums="1"
from flask import Flask
from taipy.gui import Gui

flask_app = Flask(__name__)

@flask_app.route("/home")
def home_page():
    return "The home page."

gui = Gui(page="# Taipy application", flask=flask_app)
gui.run()
```

The Flask server is created in line 4. Routes and such would be declared
as usual (like in lines 6 to 8).

Note how we use the Flask instance to use it in the `Gui^` constructor in
line 10.

When _gui_ is run (in line 11), Taipy will not create a server of its own.
Instead, it will serve your GUI pages using the _flask_app_ server created
in line 4.

