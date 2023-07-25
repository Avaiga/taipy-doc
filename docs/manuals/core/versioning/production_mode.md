When running a Taipy Core application in `--production` mode, Taipy can access all entities
attached to the current version or another *production* version. It corresponds to the case where
the application is stable and running in a production environment.

In the following, we consider the basic Taipy Core application `main.py` for all our examples:
```python linenums="1" title="main.py"
{%
include-markdown "./code_example/main.py"
comments=false
%}
```

# Convert an experiment version to production

To convert an experiment version to a production, you can run the Taipy application on the CLI with
`--production` option and providing the version name.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
1.0                                    Experiment (latest)    2023-01-25 12:24:19
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --production 1.0
[2023-01-25 13:00:05,333][Taipy][INFO] job JOB_example_algorithm_e25214c4-1047-4136-a5db-c1241a3ddbcf is completed.
nb scenarios: 3

$ taipy manage-versions --list
Version number                         Mode                   Creation date
1.0                                    Production (latest)    2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

In the example above, Taipy converted the version 1.0 to a production version before running it.

Without explicitly providing the version name, the latest version of your application is used.
Here is another example:

```console
$ python main.py --experiment 2.0
[2023-01-25 13:05:17,712][Taipy][INFO] job JOB_example_algorithm_ac79138a-4c3a-4560-bbd4-f4975083bf83 is completed.
nb scenarios: 1

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Experiment (latest)    2023-01-25 13:05:17
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33

$ python main.py --production
[2023-01-25 13:06:00,871][Taipy][INFO] job JOB_example_algorithm_1fcb6feb-cef1-46e0-a818-4ae2e58df57d is completed.
nb scenarios: 5

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Production (latest)    2023-01-25 13:06:00
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

As you can see, we first created an experiment version named 2.0 and there is one scenario is
attached to it. When listing the existing versions, we can see that 2.0 is the latest version used.
Therefore, when running the Taipy application in production mode without providing the version name,
the latest is used and converted to production before running.

Note that once the version is converted to production, the application can access all production
entities, including from older production versions.

# Change config of an existing production version

Similar to experiment mode, to re-run an existing production version, the configuration
of the application must be the same. There must be no breaking change.

Let's assume multiple changes have been made to the configuration in `main.py`.

```python linenums="1" title="main.py"
{%
include-markdown "./code_example/main_with_multiple_changes.py"
comments=false
%}
```

```console
$ python main.py --production 2.0
[2023-01-25 12:52:05,484][Taipy][ERROR] The version 2.0 Configuration is conflicted with the current Configuration:
    DATA_NODE "input" has attribute "path" added: input.pkl
    DATA_NODE "output" has attribute "path" added: output.pkl
    DATA_NODE "input" has attribute "scope" modified: SCENARIO:SCOPE -> GLOBAL:SCOPE
    DATA_NODE "output" has attribute "scope" modified: SCENARIO:SCOPE -> GLOBAL:SCOPE
    TASK "example_algorithm" has attribute "skippable" modified: False:bool -> True:bool

Please add a new production version with migration functions or run your application with --taipy-force option to override the Config of production version 2.0.
```

In the example above, when re-running production version 2.0, Taipy detects and displays all the
changes. As shown in the message, there are 2 options to deal with these changes.

First, you can run the production version with the `--taipy-force` option to force Taipy to update
the configuration of the version before re-running the application.

```console
$ python main.py --production 2.0 --taipy-force
[2023-07-04 10:25:41][Taipy][ERROR] The version 2.0 Configuration is conflicted with the current Configuration:
    DATA_NODE "input" has attribute "path" added: input.pkl
    DATA_NODE "output" has attribute "path" added: output.pkl
    DATA_NODE "input" has attribute "scope" modified: SCENARIO:SCOPE -> GLOBAL:SCOPE
    DATA_NODE "output" has attribute "scope" modified: SCENARIO:SCOPE -> GLOBAL:SCOPE
    TASK "example_algorithm" has attribute "skippable" modified: False:bool -> True:bool
[2023-07-04 10:25:41][Taipy][WARNING] Option --taipy-force is detected, overriding the configuration of version 2.0 ...
[2023-07-04 10:25:41][Taipy][INFO] Version 2.0 is already a production version.
[2023-07-04 10:25:41][Taipy][INFO] job JOB_example_algorithm_7a54227c-159d-4768-99c3-8c19c84a2e61 is completed.
```

As you can see, the application is run successfully after updating the configuration.

!!! Warning

    By forcing the configuration update, you must be aware that old entities instantiated before
    the configuration change may not be compatible.

Second, to avoid overriding the Configuration of that production version, you can create a new
production version and add migration functions to make entities from all production versions
compatible with each other. Let's dive deeper into this topic in the next section.

# Production version with migration functions

To avoid overriding production version 2.0, we can create a new production version named 2.1 with these new changes.

```console
$ python main.py --production 2.1
[2023-07-04 11:35:31][Taipy][INFO] There is no migration function from production version "2.0" to version "2.1".
[2023-07-04 11:35:31][Taipy][INFO] job JOB_example_algorithm_e3f72ec8-86b1-40c7-a382-6f63f04e8b7b is completed.
```

Recall that in the production environment, Taipy can access all entities attached to any production version. However, since there are conflicting changes between version 2.0 and 2.1, accessing an entity from version 2.0 may lead to inconsistent behavior.

It is recommended that when there are conflicting changes between production versions, migration functions should also be provided. These functions accept an entity as the input, and should return the newly migrated entity.

```python
def migrate_datanode_scope(datanode):
    datanode.scope = Scope.GLOBAL
    return datanode

def migrate_skippable_task(task):
    task.skippable = True
    return task
```

In this example, we have 2 migration functions, `migrate_datanode_scope()` and `migrate_skippable_task()`.
Notice that between version 2.0 and 2.1, each data node has its path and scope changed. However, we only migrate the scope because we want to keep the path pointing to the correct pickle file. You can freely modify the migration function as you wish, but be careful with how it may affect the application.

To register the migration functions to Taipy, use the `Config.add_migration_function()^` method. This method requires the following parameters.

- ***target_version*** represents the production version that entities are migrated to.

- ***config*** indicates the configuration or the id of the config that needs to migrate.

- ***migration_fct*** represents the migration function that takes an entity as input and returns a new entity that is compatible with the target production version.

```python
Config.add_migration_function(
    target_version="2.1",
    config="input",
    migration_fct=migrate_datanode_scope,
)

Config.add_migration_function(
    target_version="2.1",
    config="output",
    migration_fct=migrate_datanode_scope,
)

Config.add_migration_function(
    target_version="2.1",
    config="example_algorithm",
    migration_fct=migrate_skippable_task,
)
```



<!-- TODO: Add example on how to get an entity from an old production version, and what would the result looks like -->

# Remove a production version

To remove a production version, you can use the `taipy manage-versions` with the `--delete-production`
option on the Taipy CLI and providing the version name (see the
[Manage versions on Taipy CLI page](../../cli/manage-versions.md) for more details).

```console
$ taipy manage-versions --delete-production 2.0
Successfully delete version 2.0 from production version list.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
2.0                                    Experiment (latest)    2023-01-25 13:06:00
1.0                                    Production             2023-01-25 13:00:05
325d0618-6f9e-459b-9597-48fa93a57a23   Experiment             2023-01-25 12:20:56
26e56e84-9e7e-4a26-93f6-443d9aa541d9   Development            2023-01-25 12:20:33
```

After running the commands above, version 2.0 is an experiment version again. It is no longer a
production version.
