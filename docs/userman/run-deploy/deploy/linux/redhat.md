# Deploy your application with uWSGI and Nginx on Red Hat Enterprise Linux

[Red Hat](https://www.redhat.com/) is an Open Source leader providing an GNU/Linux operating system
named [*RHEL*](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) that can run
the Web Application Server [*uWSGI*](https://uwsgi-docs.readthedocs.io/en/latest/) and the web
server [*Nginx*](https://nginx.org).


## Upgrading Python

Most *RHEL* editions are delivered with a Python version older than 3.9 which is the oldest Python
version supported by Taipy.<br/>
If you are in that case, please install Python 3.9 (or newer):
```shell title="Installing Python 3.9.12"
$ sudo dnf install -y gcc openssl-devel bzip2-devel libffi-devel make
$ wget https://www.python.org/ftp/python/3.9.12/Python-3.9.12.tgz
$ tar xzf Python-3.9.12.tgz
$ rm -rf Python-3.9.12.tgz
$ cd Python-3.9.12
$ sudo ./configure --enable-optimizations
$ sudo make altinstall
$ cd ..
$ sudo rm -r Python-3.9.12
```

!!! info "Running Python"
    This tutorial specifies the Python version for each command. If your default version is
    different, you must replace `python3.9` with `python`.

## Prepare your machine

The following software should be installed on your target machine:

- `pip`: for installing Python3 packages.
- `uwsgi` and `gevent`: the web application server and its workers that will run the Taipy
  application.
- `nginx`: the web server for the Internet exposition.

You can install all of these packages by running the following command:
```shell title="Installing the mandatory packages"
$ sudo dnf install -y nginx
$ python3.9 -m pip install uwsgi gevent
$ sudo mv `pwd`/.local/bin/uwsgi /usr/bin/uwsgi
$ sudo restorecon /usr/bin/uwsgi
```

!!! note

    If you are using a SQL database based on Microsoft SQL Server, you need to install your
    corresponding
    [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).


## Run the application locally

If you want to deploy the following application:
```python
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run()
```

This would be placed in a file called _app.py_.<br/>
You need to create a *requirements.txt* file containing:
```
taipy
```

On your local machine, start the application by doing:
```shell title="Running the Taipy application"
$ python3.9 -m pip install -r requirements.txt
Collecting taipy
...
Successfully installed taipy
$ python3.9 app.py
 * Server starting on http://127.0.0.1:5000
 * Serving Flask app 'Taipy' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
...
```

The application is running locally, you can access it with the browser on the URL:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/).

!!! note
    The message:
    ```
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    ```
    is issued by Flask because the way of exposing an application on the Internet and
    developing an application locally is not the same, mainly for security and reliability reasons.
    This message will disappear when using the web server.

## Prepare the application for deployment

Deploying your application on a remote environment needs a little bit of configuration.

Before deploying your application to the Internet, make sure you turn off the Debug mode by setting
the *debug* parameter or the `(Gui.)run()^` to False (which is the default setting).<br/>
You must also inform Taipy not to run the application server on its own but rather delegate the
execution by setting the *run_server* parameter of `Gui.run()` to False.<br/>
The name of the variable where the web application is stored is used in the *uWSGI* configuration:
this allows the web server to load the web application:
```python
from taipy import Gui

gui_service = Gui(page="# Getting started with *Taipy*")
web_app = gui_service.run(debug=False, run_server=False)
```
In our example, we store this application in the variable _web_app_ (see line 3)

Make sure you upload this code on your targeted machine and install your dependencies with _pip_.

!!! note
    The entry point filename and the app variable name are important for the proper configuration of
    the *uWSGI* web application server. Please, keep them as is or adapt the configuration.


## uWSGI application server

To expose your application over the Internet, you must use _uWSGI_ instead of Flask as the
application server. You would then leverage Nginx to expose the application.

*uWSGI* can be started manually. But, generally, it's better to start the application automatically
when the machine starts. To order to do that, you should use [Systemd](https://systemd.io/) which is
installed by default on *RHEL*.

From the directory where *app.py* is located, run the following command to generate an adapted file
for *Systemd*:
```shell
$ echo """
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
""" >app.uwsgi.service
```
Then transfer this file to the correct folder by doing:
```shell
$ sudo mv app.uwsgi.service /etc/systemd/system/app.uwsgi.service
```

Now, you can start your application automatically on startup time of your machine by doing:
```shell
$ sudo restorecon /etc/systemd/system/app.uwsgi.service
$ sudo systemctl daemon-reload
$ sudo systemctl start app.uwsgi.service
$ sudo systemctl enable app.uwsgi.service
```
The application is now running locally but is not accessible yet from the Internet.

## Exposing to the Internet

To expose your application on the Internet, you should use *Nginx*.
Replace the content of `/etc/nginx/nginx.conf` by [this file content](./nginx.conf).<br/>
The configuration file can also be copied from the Taipy documentation:
```shell title="Download the Nginx configuration file"
sudo wget https://docs.taipy.io/en/latest/userman/run-deploy/deploy/linux/nginx.conf -O /etc/nginx/nginx.conf
```

Allow the communication between *Nginx* and *uWSGI*:
```shell
sudo setsebool -P httpd_can_network_connect 1
```
Then restart *Nginx*:
```shell
sudo systemctl restart nginx
```

!!! note
    This configuration is only for HTTP. If you need an HTTPS connection, please read the
    [Nginx documentation](https://nginx.org/en/docs/http/configuring_https_servers.html).

## Open the firewall

Your application is ready to receive traffic from the Internet, but your firewall still blocks the
communication.<br/>
Open the *HTTP* port (e.g. port *80*):
```shell
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --reload
```

Your application is now accessible over the Internet!
