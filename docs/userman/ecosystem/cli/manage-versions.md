# Manage versions

The `taipy manage-versions` command allows a Taipy user to track and manage various versions of
an application using scenario and data management. Please refer to the
[Version management](../../advanced_features/versioning/index.md)
documentation page for more information on creating or re-using a version.

To use the version management system, one can run the `$ taipy manage-versions`
command in a terminal (Linux, macOS) or command prompt (Windows).

Below is the list of all the optional arguments:

- *--help* or *-h*: Shows the help message and exits.

- *--list* or *-l*: Lists all existing versions of the Taipy application and exits.

- *--rename OLD_VERSION NEW_VERSION*: Rename the provided old version name to the new one.

- *--compare-config VERSION_1 VERSION_2*: Compare the configuration of version 1 and version 2.
  Show the configuration differences and exits.

- *--delete VERSION* or *-d VERSION*: Deletes the provided version and its entities.

- *--delete-production VERSION* or *-dp VERSION*: Converts the provided production version
  to an experiment version.

!!! warning "Available in Taipy Enterprise edition"

    The *--delete-production* option is relevant only to the Enterprise edition of Taipy.

## List capabilities with the --help option

To display the help message of the `manage-version` command, you can run
`taipy help manage-versions` command. Alternatively, you can use the *--help* or *-h* options by
running `taipy manage-versions --help` or `taipy manage-versions -h`.

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
To list all versions of your Taipy application, you can run the version management command
with *--list* or *-l* option.

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

- The development version "d74ec95e-6b98-4612-b50b-d171599fa3e9" which is also the latest
    version used.
- Two experiment versions "7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9" and "3.0".
- Two production versions "1.0" and "2.0".

## Rename a version
To rename a version, you can run the version management command with *--rename* option, providing
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

!!! warning

    You can not use an existing version as the new version name, since it may cause different
    versions to overlap each other.

## Compare configurations

To compare the configuration between 2 versions, you can run the version management command with
*--compare-config* option, providing the two version names.

```console
$ taipy manage-versions --compare-config 1.0 2.0
[2023-01-25 12:52:05,484][Taipy][INFO] Differences between version 1.0 Configuration and version 2.0 Configuration:
Added object:
        DATA_NODE "my_output" has attribute "description" added: What a description
```
In this example, from the comparison output, we can see that the data node "my_output" of version 2.0
has a newly added attribute named "description".

## Delete a version

To delete a version, you can run the version management command with *--delete* or *-d* option.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ taipy manage-versions --delete "1.0"
Successfully delete version 1.0.

$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
```

## Remove a version from production

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

To convert a version from production to experiment, you can run the version management command
with *--delete-production* option.

```console
$ taipy manage-versions --list
Version number                         Mode                   Creation date
d74ec95e-6b98-4612-b50b-d171599fa3e9   Development (latest)   2023-01-19 14:45:10
3.0                                    Experiment             2023-01-18 12:10:55
2.0                                    Production             2023-01-16 15:10:41
7a24dbb8-bdf6-4c84-9ddf-7b921abc5df9   Experiment             2023-01-16 17:10:15
1.0                                    Production             2023-01-12 09:10:35

$ taipy manage-versions --delete-production "1.0"
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
