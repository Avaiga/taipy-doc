# User Interface Configuration

Applications created using the `taipy.gui` package can be configured
for different use cases or environments.

This section describes how to configure an application and
explains different deployment scenarios.

## Configuring the `Gui` instance

The `Gui^` instance of your application has many parameters that
you can modify to accommodate your environment (such as development
or deployment context) or tune the user experience.

Configuration parameters can be specified in the call to the `(Gui.)run()^`
method of your `Gui` instance using the _kwargs_ parameter.

!!! note "Configuring with an .env file"
    All parameters can also be set to any values and stored as a list of key-value
    pairs in a text file for your `Gui` instance to consume. The name of this file
    is the one provided as the _env_filename_ parameter to the
    [`Gui` constructor](Gui.__init__()^).

    If you have such a configuration file, then the value associated with a
    configuration parameter will override the one provided in the `(Gui.)run()^`
    method of your `Gui` instance.

!!! note "Script options"
    The Python script that you launch to run your application can
    be provided command-line options that Taipy can use to ultimately
    override configuration settings. Not all configuration parameters can be
    overridden with option but when they can, the option is describe in the
    specific configuration parameter entry below.

    To see a list of all predefined Taipy options, you can run any Taipy
    script that runs a `Gui` instance with the _-h_ option.

Here is the list of the configuration parameters you can use in
`Gui.run()^` or as an environment setting:

   - _host_ (str, default: 127.0.0.1): the hostname of the server.<br/>
     This parameter can be overridden using the _-H_ or _--host_ option
     when launching your application:<br/>
     _-H,--host &lt;hostname>_
   - _port_ (int, default: 5000): the port that the server uses.<br/>
     This parameter can be overridden using the _-P_ or _--port_ option
     when launching your application:<br/>
     _-P,--port &lt;port>_
   - _title_ (str or None, default: "Taipy App"): the string displayed in the browser page
     title bar when navigating your Taipy application.
   - _favicon_ (str or None, default is the Avaiga logo): the path to an image file used
     as the page's icon when navigating your Taipy application.
   - _dark_mode_ (bool, default: True): whether the application shows in Dark mode (True)
     or Light mode (False).
   - _margin_ (str or None, default: "1em"): a CSS dimension value that indicates how far
     from the border of the windows should your interface be. The default value avoids
     elements getting glued to the window borders, improving appearance.
   - _system_notification_ (bool, default: True): if True, notifications will be sent by
     the system as well as the browser, should the _system_notification_ parameter in the
     call to (notify()^) be set to None. If False, the default behavior is to not use
     system notifications. See the section on [Notifications](notifications.md) for details.
   - _notification_duration_ (int, default: 3000): the time, in milliseconds, that notifications
     should remain visible (see [Notifications](notifications.md) for details).
   - _debug_ (bool, default: True): set to True if you want to be provided with detailed
     debugging information messages from the server.<br/>
     You can force the _debug_ mode using the _--debug_ option when launching
     your application.<br/>
     Or you can force **not** to use the _debug_ mode using the _--no_debug_ option
     when launching your application.
   - _flask_log_ (bool, default: False): if set to True, you can get a full, real-time
     log from the Flask server. This may be useful when trying the find the reason why
     a request does not behave as expected.
   - _use_reloader_ (bool, default: True): If True, the application watches its Python
     source file while running, and reloads the entire script should the file be
     modified. If False, there is no such watch in place.<br/>
     You can force the _use_reloader_ mode using the _--use-reloader_ option when
     launching your application.<br/>
     Or you can force **not** to use the _use_reloader_ mode using the _--no-reloader_
     option when launching your application.
   - _single_client_ (bool, default: False): set to True if only a single client can connect.
     False indicates that multiple clients can connect to the server.
   - _propagate_ (bool, default: True): the default value that will be used for every
     _propagate_ property value, for all controls. Please look at the section on the
     [_propagate_ propery](viselements/#the-propagate-property) for details).
   - _time_zone_ (str, default: "client"): indicates how date and time values should be
     interpreted.<br/>
     You can use a TZ database name (as listed in [Time zones list on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
     or one of the following values:
     - _"client"_ indicates that the time zone to be used is the Web client's.
     - _"server"_ indicates that the time zone to be used is the Web server's.
   - _theme_ (t.Union[t.Dict[str, t.Any], None]): A dictionary that lets you customize
     the theme of your application. See the [Themes section](styling.md/#themes) for
     details.
   - _light_theme_ (t.Union[t.Dict[str, t.Any], None]): Similar to the _theme_ setting,
     but applies to the _light_ theme only.
   - _theme[dark]_ (t.Union[t.Dict[str, t.Any], None]):  Similar to the _theme_ setting,
     but applies to the _dark_ theme only.
   - _use_arrow_ (bool, default: False): indicates whether or not to use the
     [Apache Arrow](https://arrow.apache.org/) technology to serialize data to Taipy
     clients. This allows for better performance in some situations.
   - _upload_folder_ (str or None, default: None): the local path where files are uploaded,
     when using the [`file_selector`](viselements/file_selector.md) control.<br/>
     The default value is the temp directory on the system where the application runs.
   - _data_url_max_size_ (int or None): the size below which the upload of file content is
     performed as inline data. If a file content exceeds that size, it will actually create
     a physical file on the server for your application to use. This upload mechanism is
     used by the [`file_selector`](viselements/file_selector.md) control.<br/>
     The default is 50 kB.
   - _ngrok_token_ (str, default: ""): an authtoken, if you need to use Ngrok to expose your
     application to the Internet. See the section on
     [Accessing your app from the Web](#accessing-your-app-from-the-web) for details.
   - _content_security_policy_ (dict or None, default: None): provide an added layer of security
     that helps to mitigate certain types of attacks such as Cross-Site Scripting (XSS)
     and data injection. Visit [Flask-Talisman](https://github.com/GoogleCloudPlatform/flask-talisman#content-security-policy) documentation for more information.
   - _force_https_ (bool, default: False): rewrite all incoming connects to https

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

## Accessing your app from the Web

[Ngrok](https://ngrok.com/) provides a way to expose your local application
to the public Internet. That allows anyone to access your application
before deploying it in your production environment.

If you want to expose your application using Ngrok, you can follow these
steps:

- Install the `pyngrok` package in your Python environment:
  ```
  pip install pyngrok
  ```
- Create an account on the [Ngrok Web site](https://ngrok.com/).
   - That will drive you to a page where you can install the _ngrok_ executable
     on your machine. Behind the scene, Ngrok will also send you a confirmation
     email providing a link that you must click to validate your
     registration and to connect to your new account.<br/>
     Connecting to your account will provide you the Ngrok _authtoken_.

- Add the NGrok _authtoken_ to the call to `(Gui.)run()^`:
    ```
    ...
    gui=Gui(...)
    ...
    gui.run(ngrok_token="<ngrok_authtoken>")
    ...
    ```
- When you run your Taipy script, the console will print out the public URL can
  allows users to connect to it. This has the form `http://<id>.ngrok.io`.<br/>
  Your Flask server, running locally will accept and serve connections from all
  around the world.


