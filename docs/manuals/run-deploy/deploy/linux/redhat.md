# Deploy your application with uWSGI and Nginx on Red Hat Enterprise Linux

[Red Hat](https://www.redhat.com/) is an Open Source leader providing an GNU/Linux operating system named
_[RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)_ that can run the Web Application
Server [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and the Web Server [Nginx](https://nginx.org).


## Upgrading Python

Most _RHEL_ are delivered with a Python version older than 3.8 which is the oldest Python version
supported by Taipy. If you are in that case, please install Python 3.8 (or newer):
```
sudo dnf install -y gcc openssl-devel bzip2-devel libffi-devel make
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
tar xzf Python-3.8.12.tgz
rm -rf Python-3.8.12.tgz
cd Python-3.8.12
sudo ./configure --enable-optimizations
sudo make altinstall
cd ..
sudo rm -r Python-3.8.12
```

!!! info
    This tutorial specifies the Python version for each command. If your default version is different, you must
    replace `python3.8` with `python`.


## Prepare your machine

The following software should be installed on your target machine:

- _pip_: for installing Python3 packages.

- _uwsgi_ and _gevent_: the web application server and its workers that will run the Taipy application.

- _nginx_: the web server for the Internet exposition.

You can install all of these packages by running the following command:
```
sudo dnf install -y nginx
python3.8 -m pip install uwsgi gevent
sudo mv `pwd`/.local/bin/uwsgi /usr/bin/uwsgi
sudo restorecon /usr/bin/uwsgi
```

!!! Note

    If you are using a SQL database based on Microsoft SQL Server, you need to install your corresponding
    [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).


## Run the application locally

If you want to deploy the following application:
```
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run()
```

This would be placed in a file called _app.py_.<br>
You need to create a _requirements.txt_ file that contains:
```
taipy
```

On your local machine, start the application by doing:
```console
$ python3.8 -m pip install -r requirements.txt
Collecting taipy
...
Successfully installed taipy
$ python3.8 app.py
 * Server starting on http://127.0.0.1:5000
 * Serving Flask app 'Taipy' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
...
```

The application is running locally, you can access it with the browser on the URL [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

!!! note
    The message:
    ```
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    ```
    Is provided by Flask because the way of exposing an application on the Internet and
    developping an application locally is not the same, mainly for security and reliability reasons.
    This message will disappear when using the web server.

## Prepare the application for deployment

Deploying your application on a remote environment needs a little bit of configuration.

By default, Taipy applications run in Debug mode. Before deploying your application to the Internet,
you should turn off the Debug mode by setting the _debug_ parameter or the `(Gui.)run()^` to False. <br>
You must also inform Taipy not to run the application server on its own but rather delegate the execution
by setting the parameter _run_server_ to False.<br>
The name of the variable where the web application is stored is used in the _uWSGI_ configuration:
this allows the web server to load the web application:
```
from taipy import Gui

gui_service = Gui(page="# Getting started with *Taipy*")
web_app = gui_service.run(debug=False, run_server=False)
```
In our example, we store this application in the variable _web_app_ (see line 3)

Make sure you upload this code on your targeted machine and install your dependencies with _pip_.

!!! important
    The entry point filename and the app variable name are important for the proper configuration of
    the *uWSGI* web application server. Please, keep them as is or adapt the configuration.


## uWSGI application server

To expose your application over the Internet, you must use _uWSGI_ instead of Flask as the application server.
You would then leverage Nginx to expose the application.

*uWSGI* can be started manually. But, generally, it's better to start the application automatically when the machine
starts. To order to do that, you should use [Systemd](https://systemd.io/) which is installed by default on *RHEL*.

From the directory where *app.py* is located, run the following command to generate an adapted file for *Systemd*:
```
echo """
[Unit]
Description=App
After=syslog.target

[Service]
ExecStart=uwsgi --http 127.0.0.1:5000 --gevent 1000 --http-websockets --module app:web_app
WorkingDirectory=`pwd`
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=`whoami`

[Install]
WantedBy=multi-user.target
""" > app.uwsgi.service
```
Then transfer this file to the correct folder by doing:
```
sudo mv app.uwsgi.service /etc/systemd/system/app.uwsgi.service
```

Now, you can start your application automatically on startup time of your machine by doing:
```
sudo restorecon /etc/systemd/system/app.uwsgi.service
sudo systemctl daemon-reload
sudo systemctl start app.uwsgi.service
sudo systemctl enable app.uwsgi.service
```

The application is now running locally but is not accessible yet from the Internet.


## Exposing to the Internet

To expose your application on the Internet, you should use _Nginx_.
Replace the content of `/etc/nginx/nginx.conf` by the [following](./nginx.conf) or:
```
sudo wget https://docs.taipy.io/en/latest/manuals/deployment/linux/nginx.conf -O /etc/nginx/nginx.conf
```

Allow the communication between _Nginx_ and _uWSGI_:
```
sudo setsebool -P httpd_can_network_connect 1
```
Then restart _Nginx_:
```
sudo systemctl restart nginx
```

!!! Note
    This configuration is only for HTTP. If you need an HTTPS connection, please read the [Nginx documentation](https://nginx.org/en/docs/http/configuring_https_servers.html).


## Open the firewall

Your application is ready to receive traffic from the Internet, but your firewall still blocks the communication.<br/>
Open the *HTTP* port that is (i.e. port *80*):
```
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --reload
```

Your application is now accessible over the Internet!
