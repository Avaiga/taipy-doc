# Deploy your application with uWSGI and Nginx on Red Hat 8.2

[RedHat](https://www.redhat.com/) is an Open Source leader providing an GNU/Linux operating named _RHEL_
that can run the Web Application Server [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and the Web Server
[Nginx](https://nginx.org).


## Installing Python3.8

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

## Prepare your machine

The following software should be installed on your target machine:

- _pip_: for installing Python3 packages.

- _uwsgi_ and _gevent_: the Web application server and its workers that will run the Taipy application.

- _nginx_: the Web server for the Internet exposition.

You can install all of this packages by running the following command:
```
sudo dnf install -y nginx python3-devel && \
sudo python3.8 -m pip install uwsgi gevent && \
sudo ln -s `pwd`/.local/bin/uwsgi /usr/bin/uwsgi
```

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
$python3.8 -m pip install -r requirements.txt
Collecting taipy
<-- Truncate -->
Successfully installed taipy
$python3.8 app.py
 * Server starting on http://127.0.0.1:5000
 * Serving Flask app 'Taipy' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
<-- Truncate -->
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
The name of the variable where the Web application is stored is used in the _uWSGI_ configuration:
this allows the Web server to load the Web application:
```
from taipy import Gui

gui_service = Gui(page="# Getting started with *Taipy*")
web_app = gui_service.run(debug=False, run_server=False)
```
In our example, we store this application in the variable _web_app_ (see line 3)

Make sure you upload this code on your targeted machine and install your dependencies with _pip_.

!!! important
    The entrypoint filename and the app variable name are important for the proper configuration of
    the _uWSGI_ Web application server. Please, keep them as is or adapt the configuration.


## uWSGI application server

To expose your application over the Internet, you must use _uWSGI_ instead of Flask as the application server.
You would then leverage Nginx to expose the application.

_uWSGI_ can be started manually. But, generally, it's better to start the application automatically when the machine
starts. To order to do that, you should use [Systemd](https://systemd.io/) which is installed by default on _Ubuntu_.

Beside your application code, run the following command to generate an adapted file for _Systemd_:
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
Then transfer this file in the correct folder by doing:
```
sudo mv app.uwsgi.service /etc/systemd/system/app.uwsgi.service
```

Now, you can start your application automatically at the startup time of your machine by doing:
```
sudo restorecon /etc/systemd/system/app.uwsgi.service
sudo daemon-reload
sudo systemctl start app.uwsgi.service
sudo systemctl enable app.uwsgi.service
```

The application is now running locally but is not accessible yet from the Internet.


## Exposing to the Internet

To be able to access to your application from the Internet, you should use _Nginx_.
Change the content of `/etc/nginx/sites-enabled/default` with the following:
```
server {
    listen 80;
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Host $host;
    }
}
```
Then restart _Nginx_:
```
sudo systemctl restart nginx
```

Your application is now accessible over the Internet!

!!! Note
    This configuration is only for HTTP. If you need an HTTPS connection, follow the [Nginx documentation](https://nginx.org/en/docs/http/configuring_https_servers.html).
