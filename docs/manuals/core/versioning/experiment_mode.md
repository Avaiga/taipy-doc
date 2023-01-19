On the development process of a Taipy Core application, you may come across a stable version of the application and
you need to store the configuration as well as all entities, so that you can restore and re-run the application latter.

With experiment mode, you can save your application as an experiment and continue with the development process without worrying about lossing the entities.

# Store an experiment

To store your application in experiment mode, you can run with `--experiment` option on the command line interface.

```console
$ python arima_taipy_app.py --experiment
```

An experiment is now stored under an experiment version.

By default, a random number will be used as the version name of your application. You can explicitly define your
experiment name in the command line.

```console
$ python arima_taipy_app.py --experiment "1.0"
```

With `--experiment "1.0"` option, the entities and the configuration of your current application will be stored under
"1.0" version.

# Re-run an experiment

To re-run an older experiment, you can run experiment mode with the name of the experiment.

This will reload the entities of that experiment to run the application.

!!! example "Re-run an experiment"

    ```console
    $ python arima_taipy_app.py --experiment "1.0"
    [2023-01-19 15:38:53,930][Taipy][INFO] job JOB_arima_training_0745e01b-4126-4736-bb87-2cbc77df7ff2 is skipped.
    ```

To run the experiment with a fresh start, you can run experiment mode with `--clean-entities` option.

This will clean all entities of that experiment and run the application again.

!!! example "Re-run an experiment and clean all entities"

    ```console
    $ python arima_taipy_app.py --experiment "1.0" --clean-entities
    [2023-01-19 15:38:50,139][Taipy][INFO] Clean all entities of version "1.0"
    ----- Started training -----
    Epoch 1 ...
    Epoch 2 ...
    [2023-01-19 15:38:53,930][Taipy][INFO] job JOB_arima_training_0745e01b-4126-4736-bb87-2cbc77df7ff2 is completed.
    ```

There is a constrain: when re-run an experiment, the configuration of the application must be one with that experiment.

But don't worry, on the development process, if there was any change to your configuration, Taipy will show an error message that tells you exactly where the differences come from so you can revert your configuration to that state.

!!! example "Re-run an experiment after updating the configuration"

    ```console
    $ python arima_taipy_app.py --experiment "1.0"
    [2023-01-19 15:28:53,168][Taipy][WARNING] The Configuration of version 1.0 is conflict with the current Python Config.
    Modified object:
            DATA_NODE "historical_data_set" has attribute "path" modified: ./daily-min-temperatures.csv -> ./daily-max-temperatures.csv

    To override these changes, run your application with --force option.
    ```

Assume that you have changed the path of data node "historical_data_set", which creates a conflict with version "1.0".
In the example above, when re-run experiment "1.0", Taipy detects the difference so you can update the data node configuration to its original path.

Notice the ouput on the console, you can also run the application with `--force` option to avoid updating the configuration.
This will override the configuration of experiment "1.0" with the current application configuration and re-run the application again.

!!! example "Re-run an experiment with `--force` option"

    ```console
    $ python arima_taipy_app.py --experiment "1.0" --force
    [2023-01-19 15:28:53,168][Taipy][WARNING] The Configuration of version 1.0 is conflict with the current Python Config.
    [2023-01-19 15:38:53,894][Taipy][WARNING] Overriding version 1.0 ...
    ----- Started training -----
    Epoch 1 ...
    Epoch 2 ...
    [2023-01-19 14:45:11,228][Taipy][INFO] job JOB_arima_training_16a095ec-1286-4138-a289-4e7fe07a624d is completed.
    ```

Here, the jobs are run again since you updated the path of the input datanode.
