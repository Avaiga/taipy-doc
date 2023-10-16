---
title: Migration
hide:
  - navigation
---

This documentation page lists the migration paths of Taipy releases as they
were published.

# From 2.x to 3.0

In Taipy Core 3.0 we deprecated the `pipeline` concept in favor of [sequence](./manuals/core/entities/sequence-mgt.md). This also means that `configure_pipeline` from Taipy Config was removed, making it necessary to update your config code. Take for instance the following config on `Taipy 2.4`:

```python linenums="1"
from taipy import Config

# Omiting multiply_task_cfg creation

pipeline_cfg = Config.configure_pipeline(
  "pipeline_1",
  task_configs=[multiply_task_cfg]
)

scenario_cfg = Config.configure_scenario(
  "multiply_scenario",
  pipeline_configs=[pipeline_cfg]
)
```

Now, `configure_scenario` takes task configs as parameter in place of pipeline configs, so to update the config above to `Taipy 3.0` is just a matter of:

```python linenums="1"
from taipy import Config

# Omiting multiply_task_cfg creation
scenario_cfg = Config.configure_scenario(
  "multiply_scenario",
  task_configs=[pipeline_cfg]
)
```

After migrating the code config, we recommend that you take advantage of `Taipy CLI`
[migration tool](./manuals/cli/migrate-entities.md).

In Taipy GUI 3.0, the `on_action` callback signature was unified across all controls: the third
parameter (*action*) was dropped. The *payload* dictionary parameter that used to be in fourth
place is now in third place and contains an *action* key that is set to the action name if you used
to use *action*.

# From 2.0 to 2.1

In Taipy version 2.1, the version management system has been introduced. For
applications created with a Taipy Core version &#8804 2.0, the first time it
runs with version 2.1 or later, no version exists, and so legacy entities are not
attached to any version. The overall principle is to create a version the first
time the application runs with Taipy 2.1 or later and to assign all the old entities
to this version. Depending on the mode used to run the application,
(Refer to [versioning documentation](manuals/core/versioning/index.md)
for details) we propose the following migration paths:

## Using default or development mode

Please refer to the [Development mode](manuals/core/versioning/development_mode.md)
documentation page for more details on how to run Taipy in development mode.

The first time you run the application with Taipy 2.1 or later, if you use the
_development_ mode which is the default mode, Taipy automatically creates an
_experiment_ version with the current configuration and assigns all legacy
entities to it. The version is named "LEGACY-VERSION". Depending on how you
want to handle legacy entities, you can now manage your newly created version
using the version management system. Please refer to the
[Version management system](manuals/core/versioning/index.md) documentation page
for more details.

## Using experiment or production mode

Please refer to the [Experiment mode](manuals/core/versioning/experiment_mode.md) or
[Production mode](manuals/core/versioning/experiment_mode.md) documentation pages
for more details on how to run Taipy in experiment or production mode.

The first time you run the application with Taipy 2.1 or later, if you use
_experiment_ or _production_ mode, you can simply provide a version name to create
a new version. All legacy entities are automatically attached to this version.
You can now manage your newly created version using the version management system.
Please refer to the [Version management system](manuals/core/versioning/index.md)
documentation page for more details.
