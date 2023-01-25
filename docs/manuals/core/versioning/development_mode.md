During a development phase, when creating a new Taipy Core application, we usually implement
the various functionalities in iterative development steps by alternating an implementation
phase with a test phase.
Basically, we code a first version of the application (the configuration particularly) and we
run it for test purpose. Then we re-write the code to improve it creating a new version, and
run it again. And so on and so forth.

The problem is that when we run the application, we do create some entities (data nodes,
tasks, scenarios, etc.). When re-running the application, the old entities instantiated with
an old version of the configuration are most probably not compatible with the new configuration.
During this development phase, between two runs of the application, we typically don't need
to keep the data. On the contrary, we usually prefer to start the application on a clean state.

In _development_ mode, Taipy deletes old entities attached to a previous development version
before running the application. This ensures a fresh start for the application. When running
an application in _development mode_, a development version is created.

In the following, we consider the basic Taipy Core application `main.py`:

```python
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

By default, a Taipy Core application runs in _development_ mode, but you can also run a
Taipy application on your command line interface with `--development` or `-dev` option.

```console
$ python main.py -l
Version number                         Mode                   Creation date
9b01399c-67e4-41a4-83d3-121f7210d4e7   Development (latest)   2023-01-23 23:44:04

$ python main.py
[2023-01-24 23:46:29,468][Taipy][INFO] Development mode: Clean all entities of version 9b01399c-67e4-41a4-83d3-121f7210d4e7
[2023-01-24 23:46:29,615][Taipy][INFO] job JOB_my_print_algo_9d75018a-1803-4358-8530-e62641e00ed8 is completed.
nb scenarios: 1

$ python main.py -l
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
