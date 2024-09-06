# Version management system
When developing, maintaining, or deploying a Taipy application, it is challenging
to keep the Taipy entities (scenarios, tasks, data nodes, etc.) up-to-date when
the core package configuration changes. Taipy provides Version Management to address
these central issues.

Indeed, developers can update the configuration (`Config^`) to implement a new feature,
experiment with an alternative algorithm, fix a bug, create a new data node, etc.
When re-running the application after a change in the configuration, old entities
instantiated before the change are not guaranteed to be compatible with the new
configuration.

Taipy proposes a **version management system** to:

- Create or re-use a version when running a Taipy application.
- Manage the different versions of the configuration across the application runs (see the
[manage versions on Taipy CLI page](../../ecosystem/cli/manage-versions.md) for more details).

## Modes

Taipy requires a *mode* to run. A mode corresponds to how Taipy behaves at runtime regarding old
entities instantiated in previous runs. There are different runtime modes that can be used when running
a Taipy application.

- In development mode (default mode), Taipy drops all old entities before running the application.
  It is made to help users during the application development phase to implement their application
  through successive iterations of configuration changes. For more information, please refer to
  [development mode](development_mode.md).

- In experiment mode, Taipy keeps old entities untouched but filters them out when running the
  application. The application behaves like there are no old entities. Only the entities created
  during the current run are considered by the application. It is designed to help the user improve
  an existing application by experimenting with possible configuration changes, trying new
  algorithms, investigating the impacts of a parameter change, etc. For more information, please refer to
  [experiment mode](experiment_mode.md).

- In production mode, Taipy considers all existing entities, whether they have been instantiated in
  the current run or in a previous one. It is designed to run an application in a production
  environment with existing entities created in previous runs. For more information, please refer to
  [production mode](production_mode.md).

    !!! warning "Available in Taipy Enterprise edition"

        The production mode is relevant only to the Enterprise edition of Taipy.

## Versions

A *version* is basically made of a *mode* and a configuration (`Config^`). The various versions
are used to track the configuration changes with respect to old entities. Each Taipy entity is
assigned a unique version.

At runtime, Taipy uses a version either by creating a new one or retrieving an existing one. It
depends on the runtime mode used to run the application and on the configuration changes. This
runtime version is assigned to new entities created.


## Usage

Taipy uses the Config mechanism (Python or TOML) to configure the version management.
A dedicated `Config` section named `CORE` can be used. Moreover, its attributes can be
dynamically overwritten at runtime with command-line interface (CLI) options.

This section describes the various methods to configure the Taipy version management system.

=== "Using the CLI"

    The versioning management system has many parameters that you can modify to accommodate your
    use-case (such as development or experiment mode). To see a list of all predefined Taipy options,
    you can run the `taipy help run` command. Alternatively, you can use the *--help* or *-h* options
    by running `taipy run --help` or `taipy run -h`.

    Here is the list of the configuration options you can use in the CLI to configure the version management system:

    - *--development* or *-dev*: With the *--development* argument, Taipy runs the
      application in *development* mode using the unique development version. All existing
      entities (from previous runs) attached to the development version are deleted before
      running the Taipy application. This is the default mode.

    - *--experiment [VERSION]*: With the *--experiment* argument, Taipy runs the application
      in *experiment* mode and only considers the entities attached to the version used.
      All other entities attached to different versions are filtered out.
      When the version is provided as a command line argument, a new *experiment* version
      is created using the version name provided. If no version is provided, a random string
      is used.
      If the version provided already exists, Taipy runs the application using the existing
      version only if the current configuration has not changed compared to the existing
      version.

    - *--production [VERSION]*: With the *--production* argument, Taipy runs the application
      in *production* mode with the version provided. All existing entities are accessible.
      If the version provided already exists as an *experiment* version, it is converted
      to a production version.

    - *--force*: With the *--force* argument, Taipy overrides a version even if
      the configuration has changed and runs the application. Default to False.

    !!! note "Configure using both the TOML file and CLI options."
        If you configure the Taipy version management system using the CLI options, the value
        associated with each CLI option will override the one provided in the explicit TOML file.

=== "Using a TOML file"

    You can also provide a TOML file configuration with a specific section named [CORE].

    Here is an example of a TOML file that set the mode to experiment with the version number is "0.1",
    and force overriding the previous experiment version when there is conflicting Configuration.

    ```toml linenums="1" title="config.toml"
    [CORE]
    mode = "experiment"
    version_number = "0.1"
    force = "True:bool"
    ```

    The TOML file can be loaded by Taipy using Python coding as follow.

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    !!! note "Configure using both Taipy Config and a TOML file"
        If you configure the Taipy version management system using a TOML file, the value associated
        with each field in the TOML file will override the one provided in the Taipy Config.

    For more information about how to configure your application using a TOML file, please refer to
    the [Advanced configuration page](../../advanced_features/configuration/advanced-config.md).

=== "Using Python code"

    The first method is configuring the `CoreSection^` with the `Config.configure_core()^` method.
    For more details about the configuration fields, please refer to the
    [Core config](../../advanced_features/configuration/core-config.md) page.

    ```python linenums="1"
    from taipy import Config

    Config.configure_core(mode="experiment", version_number="0.1")
    ```

    In the above example, we configure the version management system by setting the mode to experiment
    with the version number "0.1".
