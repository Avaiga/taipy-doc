Taipy uses the Config mechanism (Python or TOML) to configure the version management. A dedicated `Config` section named `CORE` can be used. Moreover, its attributes can be dynamically overwritten at runtime with command-line interface (CLI) options.

This section describes the various methods to configure the Taipy version management system.

# Configure using Core Configuration

The first method is configuring the `CoreSection^` with the `Config.configure_core()^` method.
For more details about the configuration fields, please refer to the [Core config](../config/core-config.md)
documentation
page.

```python linenums="1"
from taipy import Config

Config.configure_core(mode="experiment", version_number="0.1", clean_entities=True)
```

In the above example, we configure the version management system by setting the mode to experiment
with the version number is "0.1", and clean all entities on each run.

# Configure using a TOML file

You can also provide a TOML file configuration with a specific section named [CORE].

Here is an example of a TOML file that set the mode to experiment with the version number is "0.1",
and force overriding the previous experiment version when there is conflicting Configuration.

```toml linenums="1" title="config.toml"
[CORE]
mode = "experiment"
version_number = "0.1"
force = "True:bool"
clean_entities = "False:bool"
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
the [Advanced configuration page](../config/advanced-config.md).

# Configure using the CLI

The versioning management system has many parameters that you can modify to accommodate your
use-case (such as development or experiment mode). To see a list of all predefined Taipy options,
you can run any Taipy script that runs a `Core` instance with the *-h* or *--help* option.

Here is the list of the configuration options you can use in the CLI to
configure the version management system:

- **--development** or **-dev**: With the `--development` argument, Taipy runs the
  application in *development* mode using the unique development version. All existing
  entities (from previous runs) attached to the development version are deleted before
  running the Taipy application. This is the default mode.

- **--experiment [VERSION]**: With the `--experiment` argument, Taipy runs the application
  in *experiment* mode and only considers the entities attached to the version used.
  All other entities attached to different versions are filtered out.
  When the version is provided as a command line argument, a new *experiment* version
  is created using the version name provided. If no version is provided, a random string
  is used.
  If the version provided already exists, Taipy runs the application using the existing
  version only if the current configuration has not changed compared to the existing
  version.

- **--production [VERSION]**: With the `--production` argument, Taipy runs the application
  in *production* mode with the version provided. All existing entities are accessible.
  If the version provided already exists as an *experiment* version, it is converted
  to a production version.

- **--taipy-force**: With the `--taipy-force` argument, Taipy overrides a version even if
  the configuration has changed and run the application. Default to False.

- **--clean-entities**: With the `--clean-entities` argument, running a Taipy
  Core application cleans all current version entities before running the application.
  Default to False.

!!! note "Configure using both TOML file and CLI options"
    If you configure the Taipy version management system using the CLI options, the value
    associated with each CLI option will override the one provided in the explicit TOML file.
