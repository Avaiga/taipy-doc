With *experiment* mode, you can save and name your application as an experiment version.
When running an experiment version in experiment mode, Taipy only considers the entities attached
to this version. It filters out all other entities from different versions, so you can continue your development process without worrying about losing entities of your other versions.

!!! note "Use case"

    The experiment mode is handy in the process of improving a stable
    version of a Taipy application. In that case, you need to run one or multiple
    experiments like tuning algorithm parameters, updating configuration by adding
    KPI data nodes, testing new algorithms, etc. These require some configuration
    changes so that each experiment has its own configuration. Each run of an experiment
    must be analyzed, evaluated, and eventually compared to others.

    In that case, you want to keep your experiments in a dedicated version with the
    corresponding configuration and entities. You also need to be able to re-run the
    application eventually with some configuration changes without deleting the
    experiment's entities.

In the following, we consider a basic Taipy application `main.py`:

```python linenums="1" title="main.py"
{%
include-markdown "./code-example/main.py"
comments=false
%}
```

# Create a version

To create an experiment version, you can run your Taipy application with *--experiment* option on the CLI.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development (latest)   2023-01-25 12:20:33

$ taipy run main.py --experiment
[2023-01-25 12:20:56,474][Taipy][INFO] job JOB_example_algorithm_e1c49bdb-9284-40c5-a096-db0235697cb3 is completed.
Number of scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment (latest)    2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

As indicated by the output of `taipy manage-versions --list` command, a new experiment version is
created and stored. As you can see, the number of scenarios displayed is 1. That means Taipy only
considers the scenarios of the experiment version, and filters out the entities of the other
development version.

By default, a random name is used to identify the version of your application.

# Name a version

You can explicitly define the name of an experiment version by providing the name in the CLI.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment (latest)    2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ taipy run main.py --experiment 0.1
[2023-01-25 12:24:19,613][Taipy][INFO] job JOB_example_algorithm_9b6232f9-601e-4a85-852e-2ada7bc1e459 is completed.
Number of scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
0.1                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

With the *--experiment 0.1* option, an experiment version is created and stored with the name "0.1".

In this example, you can see the number of scenarios displayed is still 1. Taipy only considered
the scenarios version "0.1", and filters out the entities of other versions.

# Run an existing version

To run an existing experiment version, there **must not** be any breaking change in
the configuration of the application. Any change on the configuration is considered
breaking change, except for:
- Changes in the job execution configuration.
- Changes in the GUI configuration.
- Changes in the core package configuration.

You can run a Taipy application on the CLI with *--experiment* option and following by the name of
the existing version.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
0.1                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ taipy run main.py --experiment 0.1
[2023-01-25 12:28:54,963][Taipy][INFO] job JOB_example_algorithm_2133dc18-643b-4351-872b-aedfc2c65c9c is completed.
Number of scenarios: 2
```

As you can see, this time, the number of scenarios displayed is 2. Indeed, we run the "0.1" version
twice, so we have two scenarios attached to it.

# Change config of an existing version

As explained before, there is a constraint when re-running an existing version. The configuration
of the application must be the same. There must be no breaking change.

But don't worry; if there is any change to your configuration, Taipy will show
a warning message before exiting.

Let's assume a small change has been made to the configuration in `main.py`. A custom property
(`description`) has been added to the output data node config. Here is the new configuration:

```python linenums="1" title="main.py"
{%
include-markdown "./code-example/main_with_small_change.py"
comments=false
%}
```

```console
$ taipy run main.py --experiment 0.1
[2023-01-25 12:52:05,484][Taipy][ERROR] The configuration for version 0.1 conflicts with the current configuration:
    DATA_NODE "my_output" has attribute "description" added: What a description

To force running the application with the changes, run your application with --force option.
```

In the example above, when re-running version 0.1, Taipy detects and displays all the differences,
so you precisely know what has been changed and can decide what to do. Either you revert your
configuration changes, or you can run the application with the *--force* option to force
Taipy to update the configuration of the provided version before re-running the application.

```console
$ taipy run main.py --experiment 0.1 --force
[2023-01-25 12:55:05,484][Taipy][ERROR] The configuration for version 0.1 conflicts with the current Python Config.
    DATA_NODE "my_output" has attribute "description" added: What a description
[2023-01-25 12:52:05,692][Taipy][WARNING] Option --force is detected, overriding the configuration of version  0.1 ...
[2023-01-25 12:52:05,890][Taipy][INFO] job JOB_example_algorithm_96ed74ed-183b-4dff-86c9-3b733d4d9bd9 is completed.
Number of scenarios: 2
```

As you can see on the previous example, the application run correctly after updating
the configuration. A new scenario has been created.

!!! warning

    By forcing the configuration update, you must be aware that old entities instantiated before
    the configuration change may not be compatible.

    On the previous example, note that two scenarios are attached to version "0.1", and two `output`
    data nodes as well. One has been instantiated before the configuration update and one after.
    That means the `description` property only exists for one of the two `output` data nodes.
    It is your responsibility to handle the changes.

    Hint: You can migrate your old entities to become compatible with the new configuration or
    ensure your code is compatible with both versions of data nodes.

# Delete a version

To delete an experiment version, you can use the `taipy manage-versions` with the *--delete*
option on the Taipy CLI and provide the version name (see the
[Manage versions on Taipy CLI page](../../ecosystem/cli/manage-versions.md) for more details).

```console
$ taipy manage-versions --delete 0.1
Successfully delete version 0.1.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment  (latest)   2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

After running the commands above, version 0.1 and all its entities are deleted.
