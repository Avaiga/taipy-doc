In production environment, your Taipy Core application can access entities of multiple experiments.

To push an experiment to production environment, you can run with `--production` option with the version name on the command line interface.

```console
$ python arima_taipy_app.py --production "1.0"
```

In the example above, experiment "1.0" is push to production and now becomes a production version. The application is re-run and can access entities from older productions versions too.

With out explicitly define the version, the latest version of your application is push to production.

To remove a version from production version, you can run with `--delete-production-version` option with the version name on the command line interface.

```console
$ python arima_taipy_app.py --delete-production-version "1.0"
```

After run the command above, version "1.0" will be removed from production and will return to an experiment.
