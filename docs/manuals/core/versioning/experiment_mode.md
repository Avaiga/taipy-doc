In the process of improving a stable version of a Taipy application, you want to run
one or multiple experiments like tuning algorithm parameters, updating configuration to
add KPI data nodes, testing new algorithms, etc. These require some configuration changes
so that each experiment has its own configuration. Each run of an experiment
must be analyzed, evaluated, and eventually compared to others.

In that case, you want to keep your experiments in a dedicated version with the
corresponding configuration and entities. You also need to be able to re-run the
application eventually with some configuration changes without deleting the experiment's
entities.

With _experiment_ mode, you can save and name your application as an _experiment_ version.
When running an _experiment_ version in _experiment_ mode, Taipy only considers the
entities attached to this version. It filters out all other entities from different
versions, so you can continue your development process without worrying about losing
entities of your other experiments or your stable versions.

In the following, we consider the basic Taipy Core application `main.py`:

```python
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

# Create an experiment version

To create an _experiment_ version you can run a Taipy application on your command line
interface with `--experiment` option.

```console
$ python main.py -l
Version number                         Mode                   Creation date
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development (latest)   2023-01-25 12:20:33

$ python main.py --experiment
[2023-01-25 12:20:56,474][Taipy][INFO] job JOB_my_print_algo_e1c49bdb-9284-40c5-a096-db0235697cb3 is completed.
nb scenarios: 1

$ python main.py -l
Version number                         Mode                   Creation date
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment (latest)    2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

An _experiment_ version is created and stored. As you can see the number of scenarios
displayed is 1. That means Taipy only considers the scenarios of the _experiment_
version, and filters out the entities of the other development version. By default,
a random name is used to identify the version of your application.

# Name a version

You can explicitly define the name of an _experiment_ version by providing the name
in the command line.

```console
$ python main.py -l
Version number                         Mode                   Creation date
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment (latest)    2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --experiment 1.0
[2023-01-25 12:24:19,613][Taipy][INFO] job JOB_my_print_algo_9b6232f9-601e-4a85-852e-2ada7bc1e459 is completed.
nb scenarios: 1

$ python main.py -l
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

With `--experiment 1.0` option, an _experiment_ version is created and stored under
the name "1.0".

In this example, you can see the number of scenarios displayed is still 1. Taipy
only considered the scenarios of the 1.0 version, and filters out the entities of
other versions.

# Run an existing version

To run an existing _experiment_ version, the configuration of the application must
be the same. No change must be done. You can run a Taipy application on your
command line interface with `--experiment VERSION` option and the name of the existing version.

```console
$ python main.py -l
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --experiment 1.0
[2023-01-25 12:28:54,963][Taipy][INFO] job JOB_my_print_algo_2133dc18-643b-4351-872b-aedfc2c65c9c is completed.
nb scenarios: 2

$ python main.py -l
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

As you can see, this time the number of scenarios displayed is 2. Indeed, we run
twice the 1.0 version, so we have two scenarios attached to it. Scenarios from other
versions are filtered out.

# Clean entities of an existing version

To run the _experiment_ version with a fresh start, you can run using _experiment_
mode with `--clean-entities` option. Taipy deletes the entities of the version
provided before running the application again.

```console
$ python main.py -l
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --experiment 1.0 --clean-entities
[2023-01-25 12:36:05,598][Taipy][INFO] Clean all entities of version 1.0
[2023-01-25 12:36:05,777][Taipy][INFO] job JOB_my_print_algo_494bf4a7-afa2-4916-9221-fabd8de1738a is completed.
nb scenarios: 1

$ python main.py -l
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

As you can see in the previous example the number of scenarios became 1 again. Indeed,
Taipy cleaned all entities of that _experiment_ version before running it again (which
created a new scenario).
Scenarios from other versions are not deleted and still filtered out.

# Change config of an existing version

As explained before, there is a constraint when re-running an existing version.
The configuration of the application must be the same. No change must be made.

But don't worry; if there is any change to your configuration, Taipy will show
a warning message before exiting.

Let's assume a change has been made in the configuration in `main.py`. A custom
property (`description`) has been added to the output data node config. Here is
the new configuration.

```python
{%
include-markdown "./code_example/main_with_changes.py"
comments=false
%}
```

```console
$ python main.py --experiment 1.0
[2023-01-25 12:52:05,484][Taipy][WARNING] The Configuration of version 1.0 is conflict with the current Python Config.
Added object:
        DATA_NODE "output" has attribute "description" added: What a description

To override these changes, run your application with --force option.
```

In the example above, when re-running version 1.0, Taipy detects and displays all
the differences, so you precisely know what has been changed and can decide what
to do. Either you revert your configuration changes, or you can run the application
with the `--force` option to force Taipy to update the configuration of the provided
version before re-running the application.

```console
$ python main.py --experiment 1.0 --force
[2023-01-25 12:55:05,484][Taipy][WARNING] The Configuration of version 1.0 is conflict with the current Python Config.
[2023-01-25 12:52:05,692][Taipy][WARNING] Overriding version 1.0 ...
[2023-01-25 12:52:05,890][Taipy][INFO] job JOB_my_print_algo_96ed74ed-183b-4dff-86c9-3b733d4d9bd9 is completed.
nb scenarios: 2
```

As you can see on the previous example, the application run correctly after updating
the configuration. A new scenario has been created submitted.

!!! Warning

    By forcing the configuration update, you must be aware that old entities
    instantiated before the configuration change may not be compatible.

    On the previous example, note that two scenarios are attached to version
    1.0. Similarly, two `output` data nodes as well. One has been instantiated
    before the configuration update and one after. That means the `description`
    property only exists for one of the two `output` data nodes. It is your
    responsibility to handle the changes.

    Hint: you can migrate your old entities so they become compatible with the
    new configuration or you can ensure your code is compatible with both versions
    of data nodes.
