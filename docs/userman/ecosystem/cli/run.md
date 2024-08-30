# Run application in Taipy CLI

Assume that you have a "main.py" file containing your Taipy application.
To start the Taipy application, you can run:

```console
$ taipy run main.py
```

??? note "Using the 'python' command"

    An alternative way to run your application is to use the `python` command, which runs the
    Python interpreter.

    ```console
    $ python main.py
    ```
    However, when working with command-line arguments, Taipy arguments can be confused with
    arguments of other libraries or your application's arguments. To avoid this confusion, we
    recommend using the `taipy run` command, which is more robust in avoiding any command-line
    argument conflict.

## With Taipy arguments

Taipy CLI will parse internal arguments (interpreted by Taipy) and pass the others to your Taipy
application. For specific descriptions and usages of each argument, refer to:

- [Configuring the `Gui` instance](../../advanced_features/configuration/gui-config.md#configuring-the-gui-instance)
- [Configuring version management using the CLI](../../advanced_features/versioning/index.md#usage)

To display the list of available Taipy arguments, you can run the `taipy help run` command.
Alternatively, you can use the *--help* or *-h* options by running `taipy run --help` or
`taipy run -h`.

```console
$ taipy help run
usage: taipy run [-h] [--port [PORT]] [--host [HOST]] [--ngrok-token [NGROK_TOKEN]]
                 [--webapp-path [WEBAPP_PATH]] [--debug | --no-debug]
                 [--use-reloader | --no-reloader] [--development | --experiment [VERSION] |
                 --production [VERSION]] [--force | --no-force]
                 application_main_file {external-args} ...

positional arguments:
  application_main_file

options:
  -h, --help            show this help message and exit
  --port [PORT], -P [PORT]
                        Specify server port
  --host [HOST], -H [HOST]
                        Specify server host
  --ngrok-token [NGROK_TOKEN]
                        Specify NGROK Authtoken
  --webapp-path [WEBAPP_PATH]
                        The path to the web app to be used. The default is the web app directory
                        under gui in the Taipy GUI package directory.
  --debug               Turn on debug
  --no-debug            Turn off debug
  --use-reloader        Auto reload on code changes
  --no-reloader         No reload on code changes
  --development         When executing the Taipy application in `development` mode, all entities from
                        the previous development version will be deleted before running the new Taipy
                        application.
  --experiment [VERSION]
                        When executing the Taipy application in `experiment` mode, the current Taipy
                        application is saved to a new version. If the version name already exists,
                        check for compatibility with the current Python Config and run the
                        application. Without being specified, the version number will be a random
                        string.
  --production [VERSION]
                        When executed in `production` mode, the current version is used in
                        production. All production versions should have the same configuration and
                        share all entities. The latest version is only used if specified.
  --force               Force override the configuration of the version if existed and run the
                        application. Default to False.
  --no-force            Stop the application if any Config conflict exists.

subcommands:
  {external-args}
    external-args       Arguments defined after this keyword will be considered external
                        arguments to be passed to the application.
```

To start your application in the Taipy CLI, you can run:

```console
$ taipy run main.py
```

You can also provide Taipy arguments to the run command.

```console
$ taipy run main.py --port 8080 --experiment "0.1" --debug
```

In this example, your Taipy application will be started in experiment mode with version name "0.1"
with debug on and on the port "8080" of the server.

!!! info

    By providing the arguments to the taipy run command, you are specifying that these arguments are
    Taipy's arguments. Your application and other libraries would not use these arguments. To pass
    arguments to other libraries, please refer to the next section.

## With external arguments for other libraries

Assume that the "main.py" file contains some custom arguments for your application:

- *--host* specify the host of the data server to read from.
- *--port* specify the port of the data server to read from.
- *--debug* turn on debug mode on your data processing pipeline.

In a standard Python CLI, your application arguments will conflict with Taipy arguments.
Passing the host of your data server would also change the host of your Taipy application, which
is not a good problem to have.

To solve this problem, Taipy CLI provides the "external-args" subcommand to pass external arguments
to your application.

```console
$ taipy run main.py --port 8080 external-args --host data.server.com --port 2714 --debug
```

In this example, your Taipy application will be started on *localhost:8080* with *debug* off
since we do not specify *--debug* parameter for Taipy. Meanwhile, your application will run with
*--debug* parameter and read data from *data.server.com:2714*.
