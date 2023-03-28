The **version management system** allows a Taipy user to track and manage various
versions of its application. To use the **version management system**, one needs
to add command line arguments when running a Taipy Core application.

Below is the list of all the optional arguments:

- **--help** or **-h**: With the `--help` argument, running a Taipy Core application
  shows the help message and exits.

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

- **--override**: With the `--override` argument, Taipy overrides a version even if
  the configuration has changed. Default to False.

- **--clean-entities**: With the `--clean-entities` argument, running a Taipy
  Core application cleans all current version entities before running the application.
  Default to False.

- **--list-versions** or **-l**: With the `--list-versions` argument, running a Taipy
  Core application lists all existing versions and exits.

- **--delete-version VERSION** or **-d VERSION**: With the `--delete-version` argument,
  running a Taipy Core application deletes the provided version.

- **--delete-production-version VERSION** or **-dp VERSION**: With the `--delete-production-version`
  argument, running a Taipy Core application converts the provided production version to
  an experiment version.


!!! Note

    In the following, we consider the basic Taipy Core application `main.py`:

    ```python linenums="1"
    {%
    include-markdown "./code_example/main.py"
    comments=false
    %}
    ```

# Help

To display the help with all command line arguments, you can run a Taipy Core application
on your command line interface with the `--help` or `-h` option.

``` console
$ python main.py --help
Usage: main.py [-h] [--development | --experiment [VERSION] | --production [VERSION]]
        [--override] [--clean-entities] [--list-versions] [--delete-version VERSION]
        [--delete-production-version VERSION]

options:
  -h, --help            show this help message and exit

Core:
  Optional arguments for Core service

  --development, -dev   When execute Taipy application in `development` mode, all
                        entities from the previous development version will be deleted
                        before running new Taipy application. This is the default behavior.
  --experiment [VERSION]
                        When execute Taipy application in `experiment` mode, the current
                        Taipy application is saved to a new version. If version name already
                        exists, check for compatibility with current Python Config and run the
                        application. Without being specified, the version number will be a
                        random string.
  --production [VERSION]
                        When execute in `production` mode, the current version is used in
                        production. All production versions should have the same configuration
                        and share all entities. Without being specified, the latest version
                        is used.
  --override, -f           Force override the configuration of the version if existed. Default
                        to False.
  --clean-entities      Clean all current version entities before running the application.
                        Default to False.
  --list-versions, -l   List all existing versions of the Taipy application.
  --delete-version VERSION, -d VERSION
                        Delete a Taipy version by version number.
  --delete-production-version VERSION, -dp VERSION
                        Delete a Taipy version from production by version number. The version
                        is still kept as an experiment version.
```

# List all versions

To list all versions of your Taipy Core application, you can run a Taipy application
on your command line interface with `--list-version` or `-l` option.

```console
$ python main.py --list-version
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35
```

In the example above, there are 5 versions of the application:

- The development version "d74ec95e-6b98-4612-b50b-d171599fa3e9" which is also the latest version used.
- Two experiment versions "7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9" and "3.0".
- Two production versions "1.0" and "2.0".

# Delete a version

To delete a version, you can run a Taipy application on your command line interface
with `--delete-version` or `-d` option.

```console
$ python main.py --list-version
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python main.py --delete-version "1.0"
Successfully delete version 1.0.

$ python main.py --list-version
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
```

# Remove a version from production

To convert a version from production to experiment, you can run a Taipy application
on your command line interface with `--delete-production-version` option.

```console
$ python main.py --list-version
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python main.py --delete-production-version "1.0"
Successfully delete version 1.0 from production version list.

$ python main.py --list-version

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Experiment             2023-01-12 09:10:35
```

After running the command above, production version "1.0" is converted to an experiment version.
