---
hide:
  - toc
---
Taipy user interfaces can be served by external servers. This happens in situations
where you already have a web application running, and you want to add the GUI capabilities
of Taipy to it.

What you need to do in this case is use the *flask* parameter of the `Gui^` constructor,
setting it to the instance of the Flask server you are using.

Here is a short code sample that should make this straightforward:

```python linenums="1"
from flask import Flask
from taipy import Gui

flask_app = Flask(__name__)

@flask_app.route("/home")
def home_page():
    return "The home page."

gui = Gui(page="# Taipy application", flask=flask_app)
gui.run()
```

The Flask server is created in line 3. Routes and such would be declared
as usual (like in lines 6 to 8).

Note how we use the Flask instance to use it in the `Gui^` constructor in
line 10.

When *gui* is run (in line 11), Taipy will not create a server of its own.
Instead, it will serve your GUI pages using the *flask_app* server created
in line 4.
