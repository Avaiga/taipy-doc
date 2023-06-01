The **Taipy version management system** allows a Taipy user to track and manage various versions
of its application. When running, Taipy creates or re-uses a version identified with a name
depending on some command-line arguments. (Please refer to the [Command-line interface](../../cli.md)
documentation page for more details on managing existing versions.)

- **--development** or **-dev**: With the `--development` argument, Taipy runs the
  application in _development_ mode using the unique development version. All existing
  entities (from previous runs) attached to the development version are deleted before
  running the Taipy application. This is the default mode.

- **--experiment [VERSION]**: With the `--experiment` argument, Taipy runs the application
  in _experiment_ mode and only considers the entities attached to the version used.
  All other entities attached to different versions are filtered out.
  When the version is provided as a command line argument, a new _experiment_ version
  is created using the version name provided. If no version is provided, a random string
  is used.
  If the version provided already exists, Taipy runs the application using the existing
  version only if the current configuration has not changed compared to the existing
  version.

- **--production [VERSION]**: With the `--production` argument, Taipy runs the application
  in _production_ mode with the version provided. All existing entities are accessible.
  If the version provided already exists as an _experiment_ version, it is converted
  to a production version.

- **--taipy-force**: With the `--taipy-force` argument, Taipy overrides a version even if
  the configuration has changed and run the application. Default to False.

- **--clean-entities**: With the `--clean-entities` argument, running a Taipy
  Core application cleans all current version entities before running the application.
  Default to False.
