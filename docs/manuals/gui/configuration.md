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
method of your `Gui` instance using the *kwargs* parameter.

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
    be provided with command-line options that Taipy can use to ultimately
    override configuration settings. Not all configuration parameters can be
    overridden with option but when they can, the option is describe in the
    specific configuration parameter entry below.

    To see a list of all predefined Taipy options, you can run any Taipy
    script that runs a `Gui` instance with the *-h* option.

Here is the list of the configuration parameters you can use in
`Gui.run()^` or as an environment setting:

   - *host* (str, default: 127.0.0.1): the hostname of the server.<br/>
     This parameter can be overridden using the *-H* or *--host* option
     when launching your application:<br/>
     *-H,--host &lt;hostname>*
   - *port* (int, default: 5000): the port that the server uses.<br/>
     This parameter can be overridden using the *-P* or *--port* option
     when launching your application:<br/>
     *-P,--port &lt;port>*
   - *title* (str or None, default: "Taipy App"): the string displayed in the browser page
     title bar when navigating your Taipy application.
   - *favicon* (str or None, default is the Avaiga logo): the path to an image file used
     as the page's icon when navigating your Taipy application.
   - *dark_mode* (bool, default: True): whether the application shows in Dark mode (True)
     or Light mode (False).
   - *margin* (str or None, default: "1em"): a CSS dimension value that indicates how far
     from the border of the windows should your interface be. The default value avoids
     elements getting glued to the window borders, improving appearance.
   - *system_notification* (bool, default: True): if True, notifications will be sent by
     the system as well as the browser, should the *system_notification* parameter in the
     call to (notify()^) be set to None. If False, the default behavior is to not use
     system notifications. See the section on [Notifications](notifications.md) for details.
   - *notification_duration* (int, default: 3000): the time, in milliseconds, that
     notifications should remain visible (see [Notifications](notifications.md) for
     details).
   - *debug* (bool, default: True): set to True if you want to be provided with detailed
     debugging information messages from the server.<br/>
     If the debug mode is set, then the *async_mode* parameter of the call to `Gui.run()^`
     is overridden to "threading" to use the Flask built-in development server.<br/>
     To avoid warning from the websocket layer when using the *debug* mode, make sure
     you install the *simple-websocket* optional package.<br/>
     You can force the *debug* mode using the *--debug* option when launching
     your application.<br/>
     Or you can force **not** to use the *debug* mode using the *--no_debug* option
     when launching your application.
   - *theme* (Union[dict[str, any], None]): A dictionary that lets you customize
     the theme of your application. See the [Themes section](styling.md/#themes) for
     details.
   - *light_theme* (Union[dict[str, any], None]): Similar to the *theme* setting,
     but applies to the _light_ theme only.
   - *dark_theme* (Union[dict[str, any], None]): Similar to the *theme* setting,
     but applies to the *dark* theme only.
   - *stylekit* (Union[bool, dict[str, int, float], None]): If True or unspecified, use the
     default [Stylekit](styling/stylekit.md) for this application.<br/>
     If False, do not use the [Stylekit](styling/stylekit.md).<br/>
     If this parameter is set to a dictionary, the keys are used as
     [Stylekit variable](styling/stylekit.md#variables) names, whose values are
     overloaded by the value indicated in the dictionary.
   - *flask_log* (bool, default: False): if set to True, you can get a full, real-time
     log from the Flask server. This may be useful when trying the find the reason why
     a request does not behave as expected.
   - *use_reloader* (bool, default: True): If True, the application watches its Python
     source file while running, and reloads the entire script should the file be
     modified. If False, there is no such watch in place.<br/>
     You can force the *use_reloader* mode using the *--use-reloader* command line when
     launching your application.<br/>
     Or you can force **not** to use the *use_reloader* mode using the *--no-reloader*
     command line option when launching your application.<br/>
     Note that the reloading only takes place if either the *async_mode* parameter of
     `Gui.run()^` is set to "threading" or the *debug* parameter is set to True.
   - *single_client* (bool, default: False): set to True if only a single client can
     connect. False, which is the default value, indicates that multiple clients can
     connect to the server.
   - *propagate* (bool, default: True): the default value that will be used for every
     *propagate* property value, for all controls. Please look at the section on the
     [*propagate* property](viselements/#the-propagate-property) for details).
   - *time_zone* (str, default: "client"): indicates how date and time values should be
     interpreted.<br/>
     You can use a TZ database name (as listed in [Time zones list on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
     or one of the following values:
     - "client" indicates that the time zone to be used is the Web client's.
     - "server" indicates that the time zone to be used is the Web server's.
   - *use_arrow* (bool, default: False): indicates whether or not to use the
     [Apache Arrow](https://arrow.apache.org/) technology to serialize data to Taipy
     clients. This allows for better performance in some situations.
   - *upload_folder* (str or None, default: None): the local path where files are uploaded,
     when using the [`file_selector`](viselements/file_selector.md) control.<br/>
     The default value is the temp directory on the system where the application runs.
   - *data_url_max_size* (int or None): the size below which the upload of file content is
     performed as inline data. If a file content exceeds that size, it will actually create
     a physical file on the server for your application to use. This upload mechanism is
     used by the [`file_download`](viselements/file_download.md) and [`image`](viselements/image.md) controls.<br/>
     The default is 50 kB.
   - *ngrok_token* (str, default: ""): an authtoken, if you need to use Ngrok to expose
     your application to the Internet. See the section on
     [Accessing your app from the Web](#accessing-your-app-from-the-web) for details.

!!! info "Multiple Taipy services"
   To run the Taipy GUI service with some other Taipy services, please refer to the
   [Running Taipy services](../running_services/index.md) section.

## Using an external Web server

Taipy user interfaces can be served by external servers. This happens in situations
where you already have a Web app running, and you want to add the GUI capabilities
of Taipy to it.

What you need to do in this case is use the *flask* parameter of the `Gui^` constructor,
setting it to the instance of the Flask server you are using.

Here is a short code sample that should make this straightforward:

```py linenums="1"
from flask import Flask
from taipy import Gui

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

When *gui* is run (in line 11), Taipy will not create a server of its own.
Instead, it will serve your GUI pages using the *flask_app* server created
in line 4.

## Protect your application files

When the `Gui^` instance runs, it creates a Web server that serves the
registered pages, with the root of the site located where the `__main__`
Python module file is located.<br/>
This allows malicious users to potentially access the files of your
application if those users know their path names: the main file of a Python
application is often called `main.py`, so anyone could request the
`http://<url:port>/main.py` and see your Python source code.<br/>
This can be even more dangerous if your application relies on data files
that are meant to remain private. If a user of your application happens
to discover the path to this file, the application has a security vulnerability
because this file can be directly accessed using the underlying
Web server.

The way to solve that issue is to configure the application server to indicate
which requests are safe and which should be blocked.

Taipy GUI, however, comes with a simple feature that makes this configuration
far simpler: Located next to the main module of your application, you can create
a file called `.taipyignore` that lists files or directories that you want
to protect against a direct request.<br/>
The syntax of this text file is identical to the syntax used by Git
for its [`.gitignore`](https://git-scm.com/docs/gitignore) file.

If a user requests a file whose path matches one that appears in `.taipyignore`
then the Taipy Web server returns an HTTP error 404 (Not Found), protecting
your file from being downloaded without your consent.

## Accessing your app from the Web

[Ngrok](https://ngrok.com/) provides a way to expose your local application
to the public Internet. That allows anyone to access your application
before deploying it in your production environment.

If you want to expose your application using Ngrok, you can follow these
steps:

- Install the `pyngrok` package in your Python environment:
  When installing Taipy GUI:
  ```
  pip install taipy-gui[pyngrok]
  ```
  or independently:
  ```
  pip install pyngrok
  ```
- Create an account on the [Ngrok Web site](https://ngrok.com/).
   - That will drive you to a page where you can install the *ngrok* executable
     on your machine. Behind the scene, Ngrok will also send you a confirmation
     email providing a link that you must click to validate your
     registration and connect to your new account.<br/>
     Connecting to your account will provide you the Ngrok *authtoken*.

- Add the NGrok *authtoken* to the call to `(Gui.)run()^`:
    ```
    ...
    gui=Gui(...)
    ...
    gui.run(ngrok_token="<ngrok_authtoken>")
    ...
    ```
- When you run your Taipy script, the console will print out the public URL that
  allows users to connect to it. This has the form `http://<id>.ngrok.io`.<br/>
  Your Flask server, running locally, will accept and serve connections from all
  around the world.
