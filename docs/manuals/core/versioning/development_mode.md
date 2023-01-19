When developing a Taipy Core application, data nodes, tasks, pipelines, ... or the execution flow are constantly changing.

In this mode, all entities of is stored in a development version.
Each time the Core application is run, all entities of the development version are cleaned, which ensure a fresh start
for the new application.

By default, a Taipy Core application is run in development mode. You can also run with explicit `--development` or
`-dev` option on the command line interface.

```console
$ python arima_taipy_app.py
[2023-01-19 14:45:10,139][Taipy][INFO] Development mode: Clean all entities with version d74ec95e-6b98-4612-b50b-d171599fa3e9
----- Started training -----
----- Model is in training -----
----- Model is in training -----
[2023-01-19 14:45:11,228][Taipy][INFO] job JOB_arima_training_16a095ec-1286-4138-a289-4e7fe07a624d is completed.
[2023-01-19 14:45:11,250][Taipy][INFO] job JOB_arima_scoring_341ca8ee-cca5-4f03-bdd1-c6ffd02de2cb is completed.
```

In the example above, `python arima_taipy_app.py` run the application in development mode.

The output on the console indicates that all entities of development version `d74ec95e-6b98-4612-b50b-d171599fa3e9` was cleaned and the application is run.

!!! info "Taipy Core application in Notebook environment."

    In a Notebook environment, development mode is applied by default when the Core service is run.

    This means all entities of the development version are cleaned every time `Core().run()` is invoked in a code cell.
