By installing Taipy, you have access to the `taipy` command-line. Several commands are available.

# Get Taipy version
You can check your current version of Taipy by running the `taipy --version` command in a terminal
(Linux, macOS) or command prompt (Windows).

```console
$ taipy --version
Taipy 2.3.0
```

If you don't see a supported version of Taipy, you'll need to either upgrade Taipy or perform a
fresh install, as described in the [Installation page](../installation.md).

# Help
A list of available commands provided by Taipy is shown by running the `taipy`, or `taipy help`,
or `taipy --help` command.

```console
$ taipy
usage: taipy [-v] {manage-versions,create,help} ...

positional arguments:
  {manage-versions,create,help}
    manage-versions     Taipy version control system.
    create              Create a new Taipy application.
    help                Show the Taipy help message.

options:
  -v, --version         Print the current Taipy version and exit.
```

To have more detail about each command, you can run `taipy help <command>` and provide the command
name. For more detail, please refer to each section below.

# Create a Taipy application

Taipy provides a comfortable environment for getting started with Taipy via the create command,
and is the best way to start building a new application with Taipy.

## From the default template
To create a simple Taipy application, you can run `taipy create`, then answer a few questions to
customize your application.
```console
$ taipy create
application_name [taipy_application]: new_application
application_main_file [main.py]: app.py
application_title [Default title]: App Title
$ cd ./new_application
$ python app.py
```
In this example, we scaffold a new application using the default Taipy template, which is a simple
Taipy GUI single-page application. Here, we define the application name as "new_application", the
main Python file of the application as "app.py", and the title of the web page as "App Title". Then
we change directory (`cd`) to our newly created folder and start the application by running
`python app.py`.

!!! Info

    If there is no answer provided, the default value in the square brackets will be applied.

## From a specific template
You can also specify another template using the `--template` option.
```console
$ taipy create --template default
application_name [taipy_application]: new_application
application_main_file [main.py]: app.py
application_title [Default title]: App Title
$ cd ./new_application
$ python app.py
```

## List of templates

You can see the list of supported templates by running `taipy help create` command. Alternatively, you can
use the `--help` or `-h` options. Run `taipy create --help` or `taipy create -h`.
```console
$ taipy help create
usage: taipy create [-h] [--template {default, ...}]

options:
  -h, --help            show this help message and exit
  --template {default, ...}  The Taipy template to create new application.
```

# Manage versions

The `taipy manage-versions` command allows a Taipy user to track and manage various versions of
a Taipy Core application. Please refer to the [Version management](./core/versioning/version-mgt.md)
documentation page for more information on creating or re-using a version.

To use the version management system, one can run the `$ taipy manage-versions`
command in a terminal (Linux, macOS) or command prompt (Windows).

Below is the list of all the optional arguments:

- **--help** or **-h**: Shows the help message and exits.

- **--list** or **-l**: Lists all existing versions of the Taipy application and exits.

- **--rename OLD_VERSION NEW_VERSION**: Rename the provided old version name to the new one.

- **--compare-config VERSION_1 VERSION_2**: Compare the configuration of version 1 and version 2.
  Show the configuration differences and exits.

- **--delete VERSION** or **-d VERSION**: Deletes the provided version and its entities.

- **--delete-production VERSION** or **-dp VERSION**: Converts the provided production version
  to an experiment version.

## List capabilities with the --help option

To display the help with all command line arguments, you can run `taipy help manage-versions`
command. Alternatively, you can use the `--help` or `-h` options.
Alternatively, you can use the `--help` or `-h` options. Run `taipy manage-versions --help`
or `taipy manage-versions -h`.

```console
$ taipy help manage-versions
usage: taipy manage-versions [-h] [-l] [--rename OLD_VERSION NEW_VERSION]
                             [--compare-config VERSION_1 VERSION_2] [-d VERSION] [-dp VERSION]

options:
  -h, --help            show this help message and exit
  -l, --list            List all existing versions of the Taipy application.
  --rename OLD_VERSION NEW_VERSION
                        Rename a Taipy version.
  --compare-config VERSION_1 VERSION_2
                        Compare the Configuration of 2 Taipy versions.
  -d VERSION, --delete VERSION
                        Delete a Taipy version by version number.
  -dp VERSION, --delete-production VERSION
                        Delete a Taipy version from production by version number. The version is
                        still kept as an experiment version.
```

## List all versions
To list all versions of your Taipy Core application, you can run the version management command
with `--list` or `-l` option.

```console
$ taipy manage-versions --list
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

## Rename a version
To rename a version, you can run the version management command with `--rename` option, providing
the current version name and the new desired name.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
2.0                                    Experiment             2023-01-16 15:10:41
1.0                                    Experiment             2023-01-12 09:10:35

$ taipy manage-versions --rename 2.0 1.1
Successfully renamed version '2.0' to '1.1'.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
1.1                                    Experiment             2023-01-16 15:10:41
1.0                                    Experiment             2023-01-12 09:10:35
```

!!! Warning

    You can not use an existing version as the new version name, since it may cause different
    versions to overlap each other.

## Compare configurations

To compare the configuration between 2 versions, you can run the version management command with
`--compare-config` option, providing the two version names.

```console
$ taipy manage-versions --compare-config 1.0 2.0
[2023-01-25 12:52:05,484][Taipy][INFO] Differences between version 1.0 Configuration and version 2.0 Configuration:
Added object:
        DATA_NODE "output" has attribute "description" added: What a description
```
In this example, from the comparison output, we can see that the data node "output" of version 2.0
has a newly added attribute named "description".

## Delete a version

To delete a version, you can run the version management command with `--delete` or `-d` option.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python main.py --delete "1.0"
Successfully delete version 1.0.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
```

## Remove a version from production

To convert a version from production to experiment, you can run the version management command
with `--delete-production` option.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ python main.py --delete-production "1.0"
Successfully delete version 1.0 from the production version list.

$ taipy manage-versions --list

Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Experiment             2023-01-12 09:10:35
```

After running the command above, production version "1.0" is converted to an experiment version.
