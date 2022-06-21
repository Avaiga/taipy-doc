# Prepare your application for deployment

Development and production do not imply the same security, reliability and performance level.
These requirements imply specific tools that will impact the code structure.

## A basic application as an example

Create a file _main.py_ and put the following content inside:
```python
import taipy as tp

gui = Gui(page="# Getting started with *Taipy*")

tp.run(gui, title="Taipy Demo")
```

You can run this application with `python main.py` and obtain the following output:
```
* Server starting on http://127.0.0.1:5000
* Serving Flask app ‘Taipy’ (lazy loading)
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Server starting on http://127.0.0.1:5000
```

[Flask](https://flask.palletsprojects.com/en/2.1.x/) generates this warning because it is a development and not
a production server.

## Gunicorn

Following the [recommendation of _Flask_](https://flask.palletsprojects.com/en/2.1.x/deploying/) we will use
[Gunicorn](https://gunicorn.org/) for production. _Gunicorn_ will run your application differently than _Python_
does. Due to that condition, you should update the application to:
```python
import taipy as tp

gui = Gui(page="# Getting started with *Taipy*")

# Here we are defining the `app` variable.
# _Gunicorn_ will use this variable to serve your application.
app = tp.run(gui, title="Taipy Demo", run_server=False)
```

The application is now ready to be served by _Gunicorn_.

!!! Note
    Click [here](../reference/taipy.gui.Gui/#taipy.gui.gui.Gui.run) to obtain more information on the `run_server`
    parameters.

## Running the application with Gunicorn

First, install _Gunicorn_ and [Gevent](http://www.gevent.org/). _Gevent_ will be used by _Gunicorn_ as a worker:
```
pip install gunicorn gevent
```

!!! Note
    If you want more information about running _Gunicorn_ with _Gevent_, have a look at the
    [official documentation](https://flask-socketio.readthedocs.io/en/latest/deployment.html).

Now start _Gunicorn_ by running:
```
gunicorn -k gevent -w 1 --bind=0.0.0.0 --timeout 1800 main:app
```

Your application is now responding, and you can access it from your [browser](http://localhost:8000).

## Using the same code in development and production

Debugging with _Gunicorn_ is not as easy as debugging with the `python` command. To be able to switch
from debugging to ready to production, you should follow this structure:
```python
import taipy as tp

gui = Gui(page="# Getting started with *Taipy*")

if __name__ == '__main__':
    # Execute by the _Python_ interpretor, for debug only.
    tp.run(gui, title="Taipy Demo")
else:
    # Execute by _Gunicorn_, for production environment.
    app = tp.run(gui, title="Taipy Demo", run_server=False)
```

You can now run your application with both commands.

For production:
```
gunicorn -k gevent -w 1 --bind=0.0.0.0 --timeout 1800 main:app
```

For development:
```
python main.py
```
