The `Config^` class is a singleton object used as the entry point for the Taipy
configuration. It is accessible using the following import:

```python linenums="1"
from taipy import Config
```

# Configuration sections

The `Config^` class behaves like a container that holds all the configuration sections
used to configure the various Taipy components. It is a singleton, meaning that there
is only one instance of the `Config^` class throughout the whole Taipy execution. However,
some configuration sections might have multiple instances, such as the data node configurations,
task configurations, and scenario configurations.

!!! warning

    All configuration objects must be created before running the Orchestrator service.

    Any modification to the configuration objects after the Orchestrator service has been
    started or an entity has been instantiated will raise an error.

The various sections are presented below.

## Data node sections

The data node sections are exposed as a dictionary of data node configurations
`DataNodeConfig^`s:

```python linenums="1"
from taipy import Config

Config.data_nodes
```

For more details on how to configure data nodes, see the
[data node configuration](../../scenario_features/data-integration/data-node-config.md#create-a-data-node-config) section.

## Task sections

The task sections are exposed as a dictionary of task configurations `TaskConfig^`s:

```python linenums="1"
from taipy import Config

Config.tasks
```

For more details on how to configure tasks, see the
[task configuration](../../scenario_features/task-orchestration/scenario-config.md#from-task-configurations) section.

## Scenario sections

The scenario sections are exposed as a dictionary of scenario configurations
`ScenarioConfig^`s:

```python linenums="1"
from taipy import Config

Config.scenarios
```

For more details on how to configure scenarios, see the
[scenario configuration](../../scenario_features/sdm/scenario/scenario-config.md) page.

## Job execution section

The job execution section is exposed as a `JobConfig^`:

```python linenums="1"
from taipy import Config

Config.job_config
```

For more details on how to configure job execution, see the
[job execution configuration](job-config.md) page.

## Core package section

The core package section is exposed as a core configuration `CoreSection^`:

```python linenums="1"
from taipy import Config

Config.core
```

For more details on how to configure the core package features, see the
[core configuration](core-config.md) page.

## Gui service section

The gui service section is exposed as a gui configuration `_GuiSection`:

```python linenums="1"
from taipy import Config

Config.gui
```

For more details on how to configure the gui service, see the
[gui configuration](gui-config.md) page.

## Global configuration

The Global configuration as a `GlobalAppConfig^` allows you to add any custom
configuration that you want to be available throughout the application.

```python linenums="1"
from taipy import Config

Config.global_config
```

# Check configuration

Taipy provides a checking mechanism to validate if your configuration is correct.
The `Config.check()` method returns a collector of issues. Each issue corresponds
to an inconsistency in the configuration attached to an issue level (`INFO`, `WARNING`,
`ERROR`). `Config.check()` raises an exception if at least one issue collected has the
`ERROR` level.

```python linenums="1"
from taipy import Config

Config.check()
```

For more details on the issues that the checker could return, see the
[configuration checker](config-checker.md) page.

# Advanced configuration

By default, one can configure a Taipy application using the `Config^` class with the
Python API. However, Taipy also provides a way to override some configuration
parameters using TOML files, through environment variables, or through command-line
arguments.

For more details, see the [advanced configuration](advanced-config.md) page.
