# Deploy on Ubuntu

[Ubuntu](https://ubuntu.com/) is a GNU/Linux operating system. Simple and Open Source it is a perfect target for
deploying a Taipy Project.


## Ubuntu version
- 20.04

## Prepare your machine

The following software should be installed on your targeted machine:
- `pip`: for installing Python3 packages.
- `uwsgi`: your Web Application server.
- `gevent`: for accepting Websocket on your Web Application server.
- `nginx`: your Web Server.

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

We put this code in a file named `app.py` then create an `requirements.txt` file with the
following content:
```
taipy
```

On your local machine you can start the application by doing:
```
pip install -r requirements.txt
python app.py
```

Taipy start the Web Application, you can show the application by going on `http://127.0.0.1:5000/` with your browser.


## Prepare the application for deployment

This configuration is great for local development but not enough for deployment.
By default, Taipy application are on the debug mode, before putting your application accessible on the Internet,
you should turn off the this mode by passing the `debug=False` parameter. Then you should inform Taipy that it should
not run the application by itself but delegate the execution by setting the parameter `run_server` to False.
Then, you should expose to the Web Application Server uWSGI the Flask application.

The new content of `app.py` should now be:
```
from taipy import Gui

g = Gui(page="# Getting started with *Taipy*")
g.run(debug=False, run_server=False)
app = g._get_flask_app()
```

Do not forget to upload this code on your targeted machine and install your dependencies with pip.

!!! important
    The entrypoint filename and the app variable name are important in this documentation for the good configuration of
    the Web Application Server. Please, keep them or adapt your configuration.


## uWSGI Application Server

Maybe did you remarque the following message when you start an Taipy Application:
```
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
```
This message is provided by Flask because the ways to expose an application on the Internet and
the way of develop an application is not the same mainly for security reasons.

To be able to expose on the Internet we will first use uWSGI for running our application in place of Flask.
Then, we will use Nginx for exposing your application on the Internet.

uWSGI can be start by command line. But, generally, it's better to start the application automatically when the machine
start. To be able to do that, we will use [systemd](https://systemd.io/) who is by default installed on Ubuntu.

Beside your application code, run the following command for generate an adapted file for systemd:
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
Then move this file in the correct folder by doing `sudo mv app.uwsgi.service /etc/systemd/system/app.uwsgi.service`

Now, we can start automatically your application at the startup time of your machine by doing:
```
sudo systemctl start app.uwsgi.service
sudo systemctl enable app.uwsgi.service
```

The application is now running locally but is not accessible from the Internet.


## Web Server

To be able to access to your application from the Internet, we will use Nginx.
Changing the content of `/etc/nginx/sites-enabled/default` by the following:
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
    This configuration is only for HTTP. For HTTPS access, follow the [Nginx documentation](https://nginx.org/en/docs/http/configuring_https_servers.html).


