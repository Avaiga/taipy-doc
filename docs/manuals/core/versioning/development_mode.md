Developing an application in Taipy often requires changing the configuration multiple times.
Data from a previous run are incompatible with the configuration changes. They should then be
deleted to try the new configuration version.

In *development* mode, Taipy automatically deletes old entities attached to a previous development
version before running the application. This ensures a fresh start for the application. When running
an application in development mode, a development version is created.

In the following, we consider a basic Taipy Core application `main.py`:

```python linenums="1" title="main.py"
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

By default, a Taipy Core application runs in development mode. You can also explicitly define the
development mode by running your Taipy application with `--development` or `-dev` option on the CLI.

```console
$ python main.py
[2023-01-24 23:46:29,468][Taipy][INFO] Development mode: Clean all entities of version 9b01399c-67e4-41a4-83d3-121f7210d4e7
[2023-01-24 23:46:29,615][Taipy][INFO] job JOB_my_print_algo_9d75018a-1803-4358-8530-e62641e00ed8 is completed.
nb scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
9b01399c-67e4-41a4-83d3-121f7210d4e7   Development (latest)   2023-01-23 23:46:29
```

In the example above, `python main.py` command runs the application in development mode. The
command `taipy manage-versions --list` lists all versions of your current Taipy Core application
(see the [Manage versions on Taipy CLI page](../../cli/manage-versions.md) for more details).

The output on the console indicates that all entities of the development version
`9b01399c-67e4-41a4-83d3-121f7210d4e7` are deleted before running the application.

!!! info "Taipy Core application in Notebook environment."

    In a Notebook environment, development mode is applied by default when the run method of
    the Core service is called.

    This means all entities of the development version are cleaned every time `Core().run()` is invoked
    in a code cell.
