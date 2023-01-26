# Version management system

When developing, maintaining, or deploying a Taipy application, it is difficult
to keep the Taipy entities (scenarios, tasks, data nodes, etc.) up-to-date when
the Core configuration changes. Indeed, one can update the configuration
(`Config^`) to create a new feature, experiment with an alternative algorithm, fix a bug,
etc. When re-running the application after a change in the configuration, old entities
instantiated before the change are not guaranteed to be compatible with the new
configuration.

Taipy proposes a **version management system** to:

- manage the different versions of the configuration across the application runs,
- keep track of the old versions used to instantiate old entities,
- choose the runtime mode of Taipy that defines how Taipy handles old entities.

This **version management system** is available using command line arguments when
running a Taipy Core application. Please refer to the
[command line options](./version-mgt.md) documentation page for more details.


## Modes

Taipy requires a _mode_ to run. A _mode_ corresponds to how Taipy behaves at runtime
regarding old entities instantiated in previous runs. Three
runtime modes can be used to run a Taipy application.

- Using the `development` mode (default mode), Taipy drops all old entities before
  running the application.
  It is made to help users during the application development phase to implement its
  application through successive iterations of configuration changes. Please refer to
  the [development mode](./development_mode.md) documentation page for more details.

- Using the `experiment` mode, Taipy keeps old entities untouched but filters them out
  when running the application. The application behaves like there are no old entities.
  Only the entities created during the current run are considered by the application.
  It is designed to help the user improve an existing application by experimenting
  with possible configuration changes, trying new algorithms, investigating the impacts
  of a parameter change, etc. Please refer to the [experiment mode](./experiment_mode.md)
  documentation page for more details.

- Using the `production` mode, Taipy considers all existing entities, whether they have
  been instantiated in the current run or in a previous one.
  It is designed to run an application in a production environment with existing entities
  created in previous runs. Please refer to the [production mode](./production_mode.md)
  documentation page for more details.

## Versions

A _version_ is basically made of a _mode_ and a configuration (`Config^`). The various
_versions_ are used to track the configuration changes with respect to old entities.
Each Taipy entity is assigned to a unique _version_.

At runtime, Taipy uses a _version_ either by creating a new one or retrieving an
existing one. It depends on the runtime _mode_ used to run the application and on the
configuration changes.
This runtime _version_ is assigned to new entities created.
