Applications created using the `taipy.gui` package can be configured
for different use cases or environments.

This section describes how to configure an application and
explains different deployment scenarios.

# Configuring the `Gui` instance

The `Gui^` instance of your application has many parameters that
you can modify to accommodate your environment (such as development
or deployment context) or tune the user experience.

Configuration parameters can be specified in the call to the `(Gui.)run()^`
method of your `Gui` instance using the *kwargs* parameter.

!!! note "Configuring with a .env file"
    All parameters can also be set to any values and stored as a list of key-value
    pairs in a text file for your `Gui` instance to consume. The name of this file
    is the one provided as the *env_filename* parameter to the
    `Gui.__init__()^`(`Gui` constructor).

    If you have such a configuration file, then the value associated with a
    configuration parameter will override the one provided in the `(Gui.)run()^`
    method of your `Gui` instance.

!!! note "Script options"
    The Python script that you launch to run your application can
    be provided with command-line options that Taipy can use to ultimately
    override configuration settings. Not all configuration parameters can be
    overridden by a command-line option, but when they can, the option is described below
    in the specific configuration parameter entry.

    To see a list of all predefined Taipy options, you can run any Taipy
    script that runs a `Gui` instance with the *-h* option.

Here is the list of the configuration parameters you can use in
`Gui.run()^` or as an environment setting:

- <a name="p-host"></a>*host* (str, default: 127.0.0.1): the hostname of the server.<br/>
  This parameter can be overridden using the *-H* or *--host* option
  when launching your application:<br/>
  *-H,--host &lt;hostname>*
- <a name="p-port"></a>*port* (int or "auto", default: 5000): the port that the server will
  use.<br/>
  When set to "auto", the server will attempt to run on a free port by checking the range of port
  numbers defined in the [*port_auto_ranges*](#p-port_auto_ranges) configuration parameter.<br/>
  This parameter can be overridden using the *-P* or *--port* option
  when launching the application:<br/>
  *-P,--port &lt;port>*
- <a name="p-debug"></a>*debug* (bool, default: False): set this parameter to True if you want
  to be provided with detailed debugging information messages from the server.<br/>
  If the debug mode is set, then the *async_mode* parameter of the call to `Gui.run()^`
  is overridden to "threading" to use the Flask built-in development server.<br/>
  To avoid warnings from the web socket layer when using the *debug* mode, make sure
  you install the *simple-websocket* optional package.<br/>
  If *debug* is set to True, exceptions in user code will show the stack trace in the
  application's console.<br/>
  You can force the *debug* mode using the *--debug* option when launching
  your application.<br/>
  Or you can force **not** to use the *debug* mode using the *--no_debug* option
  when launching your application.<br/>
  To avoid warning messages from Flask, setting this parameter to True forces the value
  of the [*allow_unsafe_werkzeug*](#p-allow_unsafe_werkzeug) parameter to True.
- <a name="p-title"></a>*title* (str or None, default: "Taipy App"): the string displayed in the
  browser page title bar when navigating your Taipy application.
- <a name="p-dark_mode"></a>*dark_mode* (bool, default: True): whether the application shows in
  *Dark* mode (True) or *Light* mode (False).
- <a name="p-favicon"></a>*favicon* (str or None, default is the Taipy logo): the path to an
  image file used as the page's icon when navigating your Taipy application.
- <a name="p-run_browser"></a>*run_browser* (bool, default: True): when `Gui.run()^` is invoked,
  Taipy GUI automatically runs the system's browser and opens a new page to display the
  application interface, unless this parameter is set to False.
- <a name="p-margin"></a>*margin* (str or None, default: "1em"): a CSS dimension value that
  indicates how far from the border of the windows should your interface be. The default value
  avoids elements getting glued to the window borders, improving appearance.
- <a name="p-system_notification"></a>*system_notification* (bool, default: True): if True,
  notifications will be sent by the system as well as the browser, should the
  *system_notification* parameter in the call to (`notify()^`) be set to None. If False, the
  default behavior is to not use system notifications.<br/>
  See the section on [Notifications](../../gui/notifications.md) for details.
- <a name="p-notification_duration"></a>*notification_duration* (int, default: 3000): the time,
  in milliseconds, that notifications should remain visible.<br/>
  See the section on [Notifications](../../gui/notifications.md) for details.
- <a name="p-watermark"></a>*watermark* (str, default: "Taipy inside"): a faint text appearing
  on top of all application pages.
- <a name="p-stylekit"></a>*stylekit* (Union[bool, dict[str, int, float], None]): If True or
  unspecified, use the default [Stylekit](../../gui/styling/stylekit.md) for this application.<br/>
  If False, do not use the [Stylekit](../../gui/styling/stylekit.md).<br/>
  If this parameter is set to a dictionary, the keys are used as
  [Stylekit variable](../../gui/styling/stylekit.md#variables) names, whose values are
  overloaded by the value indicated in the dictionary.
- <a name="p-theme"></a>*theme* (dict[str, any] or None): A dictionary that lets you
  customize the theme of your application.<br/>
  See the [Themes section](../../gui/styling/index.md#themes) for details.
- <a name="p-light_theme"></a>*light_theme* (Union[dict[str, any], None]): Similar to the
  [*theme*](#p-theme) setting, but applies to the *light* theme only.
- <a name="p-dark_theme"></a>*dark_theme* (Union[dict[str, any], None]): Similar to the
  [*theme*](#p-theme) setting, but applies to the *dark* theme only.
- <a name="p-data_url_max_size"></a>*data_url_max_size* (int or None): the size in bytes below
  which the upload of file content is performed as inline data. If a file content exceeds that
  size, it will create a physical file on the server so the application can read it. This upload
  mechanism is used by the [`file_download`](../../../refmans/gui/viselements/generic/file_download.md)
  and the [`image`](../../../refmans/gui/viselements/generic/image.md) controls.<br/>
  The default value is 50 kB.
- <a name="p-use_reloader"></a>*use_reloader* (bool, default: False): If True, the application
  watches its Python source file while running and reloads the entire script should the file be
  modified. If False, there is no such watch in place.<br/>
  You can force the *use_reloader* mode using the *--use-reloader* command line when
  launching your application.<br/>
  Or you can force **not** to use the *use_reloader* mode using the *--no-reloader*
  command line option when launching your application.<br/>
  Note that setting this to True forces the [*debug*](#p-debug) parameter to True, and
  the [*async_mode*](#p-async_mode) parameter to "threading".</br>
  This setting is irrelevant in the context of Notebooks.
- <a name="p-ngrok_token"></a>*ngrok_token* (str, default: ""): an authtoken, if you need to use
  [Ngrok](https://ngrok.com/) to expose your application to the Internet. See the section on
  [Accessing your app from the Web](#accessing-your-app-from-the-web) for details.
- <a name="p-change_delay"></a>*change_delay* (int, default: None): the delay, in milliseconds,
  used by some controls (namely [`slider`](../../../refmans/gui/viselements/generic/slider.md),
  [`input`](../../../refmans/gui/viselements/generic/input.md), and
  [`number`](../../../refmans/gui/viselements/generic/number.md)) before the user
  actions are sent to the backend server for further processing. This can be used when there is
  a significant network latency: user actions would then get stacked up on the front-end before
  the back-end had a chance to receive them, resulting in a poor user experience. This value
  should be less than 300 to ensure a smooth interaction with the control.<br/>
  The default value of None indicates that Taipy GUI does not use any delay.
- <a name="p-propagate"></a>*propagate* (bool, default: True): the default value that is used
  for every *propagate* property value, for all controls. Please look at the section on the
  [*propagate* property](../../gui/viselements/introduction.md#the-propagate-property) for details.
- <a name="p-time_zone"></a>*time_zone* (str, default: "client"): indicates how date and time
  values should be interpreted.<br/>
  You can use a TZ database name (as listed in
  [Time zones list on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
  or one of the following values:
  - "client" indicates that the time zone to be used is the web client's.
  - "server" indicates that the time zone to be used is the web server's.
- <a name="p-upload_folder"></a>*upload_folder* (str or None, default: None): the local path
  where files are uploaded when using the [`file_selector`](../../../refmans/gui/viselements/generic/file_selector.md)
  control.<br/>
  The default value is the temp directory on the system where the application runs.
- <a name="p-webapp_path"></a>*webapp_path* (str, None): when working with the Taipy GUI
  source code, it may be helpful to indicate where to find the "webapp" directory that holds
  the client side of the package. You can use this setting to indicate where on your filesystem
  this directory should be searched.<br/>
  The default uses the path to the "webapp" directory within the installed Taipy GUI package.
- <a name="p-chart_dark_template"></a>*chart_dark_template* (dict[str, any] or None, default:
  None): a template for styling charts in dark mode. The full documentation for this object
  can be found in the documentation section for
  [Plotly's layout template](https://plotly.com/javascript/reference/layout/#layout-template).
- <a name="p-extended_status"></a>*extended_status* (bool, default: False): if set to True, the
  [status page](../../gui/pages/advanced/index.md#status-page) output is augmented with additional information.
- <a name="p-flask_log"></a>*flask_log* (bool, default: False): if set to True, you can get a
  complete, real-time log from the Flask server. This may be useful when trying to find out why
  a request does not behave as expected.
- <a name="p-notebook_proxy"></a>*notebook_proxy* (bool, default: True): this setting only
  matters when running Taipy GUI in the context of Notebooks. If set to True, which is the
  default, the exposed port number (the one set in the [*port*](#p-port) parameter) is just a
  proxy port to a dynamically generated port so that the user can stop and restart the server
  without depending on how quickly the kernel can clean up its resources.<br/>
  See the section on [running Taipy GUI in Notebooks](../../run-deploy/notebooks.md) for more details.
- <a name="p-single_client"></a>*single_client* (bool, default: False): set to True if only a
  single client can connect. False, which is the default value, indicates that multiple clients
  can connect to the server.<br/>
  Note that this setting is forced to True when running in a Notebook context.
- <a name="p-port_auto_ranges"></a>*port_auto_ranges* (list[tuple[int,int]]), default:
  [(49152, 65535)]: defines the ranges of port numbers to be used when the [*port*](#p-port)
  configuration parameter is set to "auto".<br/>
  This parameter must be a list of tuples, each containing two integers that specify the start
  and end of a port range.
- <a name="p-async_mode"></a>*async_mode* (str or None, default: "gevent"): specifies the
  [deployment strategy for SocketIO](https://python-socketio.readthedocs.io/en/latest/server.html#deployment-strategies),
  that Taipy GUI depends on.<br/>
  This parameter is forced to "threading" if [*debug*](#p-debug) or
  [*use_reloader*](#p-use_reloader) is set to True.
- <a name="p-server_config"></a>*server_config* (dict[str, any], default: None): allows for
  fine-tuning the configuration of the underlying web server. The keys and types of values that
  you can set in this dictionary are the following:
   - *flask* (dict[str, any]): lets you specify the parameters to the Flask application object,
     as explained in the
     [Flask Server Configuration](https://flask.palletsprojects.com/en/2.3.x/api/#flask.Flask)
     documentation page. Each key/value pair is used when calling the Flask constructor.
   - *cors* (Union[bool, dict[str, any]]): if True, this indicates that you are using
     [Flask CORS](https://flask-cors.readthedocs.io/en/latest/).<br/>
     If this entry holds a dictionary, then the key/value pairs of the dictionary are used
     to configure Flask CORS. All the details can be found in the
     [Flask CORS Configuration](https://flask-cors.readthedocs.io/en/latest/configuration.html#configuration-options)
     documentation section.
   - *socketio*: (dict[str, any]): lets you specify the parameters to the Flask-SocketIO server
     that Taipy GUI creates. You can find all the documentation for all relevant key/value pairs
     in the
     [Flask-SocketIO configuration](https://flask-socketio.readthedocs.io/en/latest/api.html)
     documentation page.
   - *ssl_context" (str|tuple[str, str]): the value set when running the underlying SocketIO
     instance for SSL support.<br/>
     This will work for a Flask development server, for testing purposes but not when using
     "eventlet" or "gevent" [*async_mode*](#p-async_mode). You will need to rely on your web
     server's documentation to learn how to enable SSL support and configure the server with
     a real TLS certificate.
- <a name="p-run_in_thread"></a>*run_in_thread* (bool, default: False): if set to True, the
  underlying web server runs in a separate thread. In a Notebook context, this parameter
  is forced to True.
- <a name="p-run_server"></a>*run_server* (bool, default: True): must be set to False if you
  if you want to run this GUI application on an external server. Then Taipy GUI will not create
  or run the server, and it is up to the programmer to use the Flask instance returned by
  `Gui.run()^` or `Gui.get_flask_app()^` so it is served by the target web server.
- <a name="p-base_url"></a>*base_url* (str or None, default: "/"): a string used as a prefix to
    the path part of the exposed URL, so one can deploy a Taipy GUI application in a path
    different from the root of the web site.<br/>
    If you need to expose the application under the prefix "*my_application*", you can set this
    path to the *base_url* parameter of the `Gui.run()^` method:
    ```python
    Gui(pages=...).run(base_url="/my_application")
    ```
    The application prefix must also be handled at the web server level, to properly proxy the
    requests.

    !!! example "Ngnix configuration"
        Here is an example using [**ngnix**](https://nginx.org/): the server is configured as a proxy
        server, serving port 8080 and redirecting the traffic to the Taipy application that is
        running locally on port 5000.<br/>
        Here is what could be indicated in the web server configuration file:
        ```
        server {
          listen 8080;

          location /my_application {
            rewrite /my_application/(.*) /$1 break;
            rewrite /my_application / break;
            proxy_pass http://127.0.0.1:5000;
          }

          location /my_application/socket.io {
            proxy_http_version 1.1;
            proxy_buffering off;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_pass http://127.0.0.1:5000/socket.io;
          }
        }
        ```
        Note that web socket redirection needs to be setup also.

        With this configuration, a user can connect to and use the Taipy application from the URL:
        `http://<server-url>/my_application`.

- <a name="p-allow_unsafe_werkzeug"></a>*allow_unsafe_werkzeug* (bool, default: False): hides
  some [Flask-SocketIO](https://pypi.org/project/Flask-SocketIO/) runtime errors in some
  debugging scenarios. This is set to True when [*debug*](#p-debug) is set to True.
- <a name="p-use_arrow"></a>*use_arrow* (bool, default: False): indicates whether or not to use
  the [Apache Arrow](https://arrow.apache.org/) technology to serialize data to Taipy
  clients. This allows for better performance in some situations.

!!! info "Multiple Taipy services"
   To run the Taipy GUI service with some other Taipy services, please refer to the
   [Running Taipy services](../../run-deploy/run/running_services.md) section.

# Using an external web server

Taipy user interfaces can be served by external servers. This happens when
you already have a web application running and want to add the GUI capabilities
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

The Flask server is created in line 4. Routes and such would be declared
as usual (like in lines 6 to 8).

Note how we use the Flask instance to use it in the `Gui^` constructor in
line 10.

When *gui* is run (in line 11), Taipy will not create a server of its own.
Instead, it will serve your GUI pages using the *flask_app* server created
in line 4.

# Protect your application files

When the `Gui^` instance runs, it creates a web server that serves the
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
then the Taipy web server returns an HTTP error 404 (Not Found), protecting
your file from being downloaded without your consent.

# Accessing your app from the Web

[Ngrok](https://ngrok.com/) provides a way to expose your local application
to the public Internet. This allows anyone to access your application
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
- Create an account on the [Ngrok web site](https://ngrok.com/).
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
- When you run your Taipy script, the console will print out the public URL,
  allowing users to connect to it. This has the form `http://<id>.ngrok.io`.<br/>
  Your Flask server, running locally, will accept and serve connections from all
  around the world.
