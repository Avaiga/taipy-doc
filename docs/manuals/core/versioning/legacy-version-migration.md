To run an application that was created on Taipy version &#8804 2.0 with the version control system, first you need to update Taipy to version 2.1 or greater.

``` console
$ pip install taipy==2.1
```

or

``` console
$ pip install --upgrade taipy
```

With the same storage folder, you can store all of the entities to an experiment or production version with the name of your choice.

```console
$ python arima_taipy_app.py --experiment "legacy-application"
```

or

```console
$ python arima_taipy_app.py --production "legacy-application"
```

!!! warning "Run legacy application in development mode"

    If you run the application in development mode, all legacy entities will be stored under "LEGACY-VERSION" name with the current Config.
