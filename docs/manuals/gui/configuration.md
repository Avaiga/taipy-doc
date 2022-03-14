# User Interface configuration

You can configure the User Interface part of your application using
these settings:

   - _port_ (int, default: 5000): the port that the server uses.
   - _dark_mode_ (bool, default: True): whether the application shows in Dark mode (True), or light mode (False).
   - _debug_ (bool, default: True): set to True if you want detailled debugging information messages from the server.
   - _host_ (str, default: 127.0.0.1): the host name of the server.
   - _use_reloader_ (bool, default: True):
   - _time_zone_ (str, default: "client"): indicates how date and time values should be interpreted.<br/>
     You can use a TZ database name (as listed in [Time zones list on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones))
     or one of the following values:
      - _"client"_ indicates that the time zone to be used is the one of the Web client.
      - _"server"_ indicates that the time zone to be used is the one of the Web server.
   - _propagate_ (bool, default: True):
   - _client_url_ (str, default: "http://127.0.0.1:5000"):
   - _favicon_ (str or None, default is the Avaiga logo): the path to an image file what will be used as the page's
      icon when navigating your Taipy application.
   - _title_ (str or None, default: "Taipy App"): the string displayed in the browser page title bar when navigating your Taipy application.
   - _theme_ (t.Union[t.Dict[str, t.Any], None]):
   - _theme[light]_ (t.Union[t.Dict[str, t.Any], None]):
   - _theme[dark]_ (t.Union[t.Dict[str, t.Any], None]):
   - _use_arrow_ (bool, default: False): indicates, when True, that you want to use the
      [Apache Arrow](https://arrow.apache.org/) technology to serialize data to Taipy clients.
      This allows for better performance in some situations.
   - _browser_notification_ (bool, default: True):
   - _notification_duration_ (int, default: 3000): the time, in milliseconds, that notifications
     should remain visible (see [Notifications](notifications.md) for details).
   - _single_client_ (bool, default: False): set to True if only a single client can connect. False indicates that multiple clients
     can connect to the server.
   - _ngrok_token_ (str, default: ""):
   - _upload_folder_ (str or None, default: None):
   - _data_url_max_size_ (t.Union[int, None]):
   - _flask_log_ (bool, default: False):
   - _margin_ (str or None, default: "1em"): 
