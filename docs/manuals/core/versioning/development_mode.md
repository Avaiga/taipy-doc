Developing an application in Taipy often requires changing the configuration multiple times.
Data from a previous run are incompatible with the configuration changes. They should then be
deleted to try the new configuration version.

In _development_ mode, Taipy automatically deletes old entities attached to a previous development
version before running the application. This ensures a fresh start for the application. When running
an application in _development mode_, a development version is created.

In the following, we consider the basic Taipy Core application `main.py`:

```python linenums="1"
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

By default, a Taipy Core application runs in _development_ mode, but you can also run a
Taipy application on your command line interface with `--development` or `-dev` option.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
9b01399c-67e4-41a4-83d3-121f7210d4e7   Development (latest)   2023-01-23 23:44:04

$ python main.py
[2023-01-24 23:46:29,468][Taipy][INFO] Development mode: Clean all entities of version 9b01399c-67e4-41a4-83d3-121f7210d4e7
[2023-01-24 23:46:29,615][Taipy][INFO] job JOB_my_print_algo_9d75018a-1803-4358-8530-e62641e00ed8 is completed.
nb scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
9b01399c-67e4-41a4-83d3-121f7210d4e7   Development (latest)   2023-01-23 23:46:29
```

In the example above, `python main.py` command runs the application in development mode.

The output on the console indicates that all entities of the development version
`9b01399c-67e4-41a4-83d3-121f7210d4e7` are deleted before running the application.

!!! info "Taipy Core application in Notebook environment."

    In a Notebook environment, development mode is applied by default when the run method of
    the Core service is called.

    This means all entities of the development version are cleaned every time `Core().run()` is invoked
    in a code cell.
