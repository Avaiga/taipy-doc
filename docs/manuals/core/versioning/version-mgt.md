# Manage Taipy application versions

## List all versions

To list all versions of your Taipy Core application, you can run with `--list-version` or `-l` option on the command line interface.

```console
$ python arima_taipy_app.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35
```

In the example above, there are 5 versions of the application:

- Development version "d74ec95e-6b98-4612-b50b-d171599fa3e9" which is also the latest version.
- Experiment versions "7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9" and "3.0".
- Production versions "1.0" and "2.0".

## Delete a version

To delete a version, you can run with `--delete-version` or `-d` option with the version name on the command line interface.

```console
$ python arima_taipy_app.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python arima_taipy_app.py --delete-version "1.0"
Successfully delete version 1.0.
$
$ python arima_taipy_app.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
```

## Remove a version from production

To remove a version from production version, you can run with `--delete-production-version` option with the version name on the command line interface.

```console
$ python arima_taipy_app.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python arima_taipy_app.py --delete-production-version "1.0"
Successfully delete version 1.0 from production version list.
$
$ python arima_taipy_app.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Experiment             2023-01-12 09:10:35
```

After run the command above, version "1.0" will be removed from production and will return to an experiment.
