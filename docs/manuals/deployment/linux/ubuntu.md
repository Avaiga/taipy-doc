# Deploy your application with uWSGI and Nginx on Ubuntu

[Ubuntu](https://ubuntu.com/) is a GNU/Linux operating system on witch we can execute the Web Application Server
[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and the Web Server [Nginx](https://nginx.org).


## For Ubuntu version before 20.04

Before Ubuntu 20.04 the pre-installed Python version is older than Python3.8 that is the older Python version
supported by Taipy. If you are in that case, please install at least Python3.8 and use it with this documentation.

## Prepare your machine

The following software should be installed on your targeted machine:
- _pip_: for installing Python3 packages.
- _uwsgi_ and _gevent_: the web application server and its worker that will run the Taipy application.
- _nginx_: the web server for the Internet exposition.

You can install all of this packages by running the following command:
```
sudo apt update -y &&\
sudo apt install -y python3-pip nginx &&\
sudo pip install uwsgi gevent &&\
sudo ln -s `pwd`/.local/bin/uwsgi /usr/bin/uwsgi
```

## The application

We want to deploy the following application:
```
from taipy import Gui

Gui(page="# Getting started with *Taipy*").run()
```

We put this code in a file named _app.py_ then create an _requirements.txt_ file with the
following content:
```
taipy
```

On your local machine you can start the application by doing:
```
pip install -r requirements.txt
python app.py
```

The application is running locally, you can access to it with the browser on the URL _http://127.0.0.1:5000/_.


## Prepare the application for deployment

This configuration is great for local development but not enough for deployment.
By default, Taipy application are on the debug mode. Before putting your application accessible on the Internet,
you should turn off this mode by passing the _debug_ parameter with the value False. Then you should inform Taipy that
it should not run the application by itself but delegate the execution by setting the parameter _run_server_ to False.
Then, you should expose to the Web Application Server uWSGI the Flask application by using `(Gui)._get_flask_app()^`.

The new content of _app.py_ should now be:
```
from taipy import Gui

g = Gui(page="# Getting started with *Taipy*")
g.run(debug=False, run_server=False)
app = g._get_flask_app()
```

Do not forget to upload this code on your targeted machine and install your dependencies with pip.

!!! important
    The entrypoint filename and the app variable name are important for the good configuration of
    the web application server uWSGI. Please, keep them as or adapt the configuration.


## uWSGI application server

Maybe did you remarque the following message when you start a Taipy Application:
```
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
```
This message is provided by Flask because the way to expose an application on the Internet and
the way of develop an application is not the same mainly for security and reliability.

To be able to expose on the Internet we will first use uWSGI for running our application in place of Flask.
Then, we will use Nginx for exposing your application on the Internet.

uWSGI can be start by command line. But, generally, it's better to start the application automatically when the machine
starts. To be able to do that, we will use [Systemd](https://systemd.io/) who is by default installed on Ubuntu.

Beside your application code, run the following command for generate an adapted file for Systemd:
```
echo """
[Unit]
Description=App
After=syslog.target

[Service]
ExecStart=uwsgi --http 127.0.0.1:5000 --gevent 1000 --http-websockets --module app:app
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
Then move this file in the correct folder by doing `sudo mv app.uwsgi.service /etc/systemd/system/app.uwsgi.service`.

Now, we can start automatically your application at the startup time of your machine by doing:
```
sudo systemctl start app.uwsgi.service
sudo systemctl enable app.uwsgi.service
```

The application is now running locally but is not accessible yet from the Internet.


## Web Server

To be able to access to your application from the Internet, we will use Nginx.
Changing the content of `/etc/nginx/sites-enabled/default` with the following:
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
Then restart Nginx by doing `sudo systemctl restart nginx`.

The application is now accessible through the Internet !

!!! Note
    This configuration is only for HTTP. If you need an HTTPS connection, follow the [Nginx documentation](https://nginx.org/en/docs/http/configuring_https_servers.html).


