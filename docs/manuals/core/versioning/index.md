# Version management system

When developing, maintaining, or deploying a Taipy application, it is challenging
to keep the Taipy entities (scenarios, tasks, data nodes, etc.) up-to-date when
the Core configuration changes. Taipy provides Version Management to address these
central issues.

Indeed, developers can update the configuration (`Config^`) to implement a new feature,
experiment with an alternative algorithm, fix a bug, create a new data node, etc.
When re-running the application after a change in the configuration, old entities
instantiated before the change are not guaranteed to be compatible with the new
configuration.

Taipy proposes a **version management system** to:

- Create or re-use a version when running a Taipy application.
- Manage the different versions of the configuration across the application runs (see the
[Manage versions on Taipy CLI page](../../cli/manage-versions.md) for more details).

## Modes

Taipy requires a *mode* to run. A mode corresponds to how Taipy behaves at runtime regarding old
entities instantiated in previous runs. There are three runtime modes that can be used when running
a Taipy application.

- In development mode (default mode), Taipy drops all old entities before running the application.
  It is made to help users during the application development phase to implement its application
  through successive iterations of configuration changes. Please refer to the
  [Development mode](./development_mode.md) documentation page for more details.

- In experiment mode, Taipy keeps old entities untouched but filters them out when running the
  application. The application behaves like there are no old entities. Only the entities created
  during the current run are considered by the application. It is designed to help the user improve
  an existing application by experimenting with possible configuration changes, trying new
  algorithms, investigating the impacts of a parameter change, etc. Please refer to the
  [Experiment mode](./experiment_mode.md) documentation page for more details.

- In production mode, Taipy considers all existing entities, whether they have been instantiated in
  the current run or in a previous one. It is designed to run an application in a production
  environment with existing entities created in previous runs. Please refer to the
  [Production mode](./production_mode.md) documentation page for more details.

## Versions

A *version* is basically made of a *mode* and a configuration (`Config^`). The various versions
are used to track the configuration changes with respect to old entities. Each Taipy entity is
assigned a unique version.

At runtime, Taipy uses a version either by creating a new one or retrieving an existing one. It
depends on the runtime mode used to run the application and on the configuration changes. This
runtime version is assigned to new entities created.
