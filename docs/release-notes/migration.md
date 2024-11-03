---
title: Migration
---

This documentation page lists the migration paths of Taipy releases as they were published.

# From 3.x to 4.0

Due to changes in Taipy’s package structure in version 4.0, the previous version of the
`taipy-config` package may not be automatically removed when upgrading Taipy from version 3.x to
4.0. This could lead to runtime issues as the system may attempt to reference outdated dependencies.

To ensure a clean installation, please manually  uninstall Taipy 3.x manually and then install a
fresh Taipy 4.0.

# From 2.x to 3.0

1. In Taipy GUI 3.0, the `on_action` callback signature was unified across all controls: the third
    parameter (*action*) was dropped. The *payload* dictionary parameter that used to be in fourth
    place is now in third place and contains an *action* key that is set to the action name if you
    used to use *action*.

2. In Taipy 3.0 we deprecated the **Pipeline** concept in favor of
    [**Sequence**](../userman/scenario_features/sdm/sequence/index.md). This also means that the
    function `configure_pipeline()` was removed from Taipy Config, making it necessary to update
    your config code. Take for instance the following configuration, built for Taipy 2.4:

    ```python title="config.py from Taipy 2.4 edition"
    from taipy import Config

    # Omitting multiply_task_cfg creation

    pipeline_cfg = Config.configure_pipeline(
        "pipeline_1",
        task_configs=[multiply_task_cfg]
    )

    scenario_cfg = Config.configure_scenario(
        "multiply_scenario",
        pipeline_configs=[pipeline_cfg]
    )
    ```

    Now, `configure_scenario()` takes task configs as parameter in place of pipeline configs, so to
    update the config above to Taipy 3.0 is just a matter of:

    ```python title="config.py from Taipy 3.0 edition"
    from taipy import Config

    # Omiting multiply_task_cfg creation

    scenario_cfg = Config.configure_scenario(
        "multiply_scenario",
        task_configs=[multiply_task_cfg]
    )
    ```

    After migrating the code, we recommend that you take advantage of `Taipy CLI`
    [migration tool](../userman/ecosystem/cli/migrate-entities.md).


# From 2.0 to 2.1

In Taipy version 2.1, the version management system has been introduced. For applications
created with a Taipy version &#8804 2.0, the first time it runs with version 2.1 or later,
no version exists, and so legacy entities are not attached to any version. The overall principle
is to create a version the first time the application runs with Taipy 2.1 or later and to assign
all the old entities to this version. Depending on the mode used to run the application,
(Refer to [versioning documentation](../userman/advanced_features/versioning/index.md) for details)
we propose the following migration paths:

## Using default or development mode

Please refer to the [Development mode](../userman/advanced_features/versioning/development_mode.md)
documentation page for more details on how to run Taipy in development mode.

The first time you run the application with Taipy 2.1 or later, if you use the _development_
mode which is the default mode, Taipy automatically creates an _experiment_ version with the
current configuration and assigns all legacy entities to it. The version is named
"LEGACY-VERSION". Depending on how you want to handle legacy entities, you can now manage your
newly created version using the version management system. Please refer to the
[Version management system](../userman/advanced_features/versioning/index.md) documentation page for
more details.

## Using experiment or production mode

Please refer to the [Experiment mode](../userman/advanced_features/versioning/experiment_mode.md) or
[Production mode](../userman/advanced_features/versioning/experiment_mode.md) documentation pages
for more
details on how to run Taipy in experiment or production mode.

The first time you run the application with Taipy 2.1 or later, if you use _experiment_ or
_production_ mode, you can simply provide a version name to create a new version. All legacy
entities are automatically attached to this version. You can now manage your newly created
version using the version management system. Please refer to the
[Version management system](../userman/advanced_features/versioning/index.md) documentation page for
more details.
