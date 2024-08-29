# Migrate entities from earlier versions to Taipy 3.0

Taipy 3.0 provides a CLI option to update entities from older Taipy versions to 3.0. It
is recommended to update the Taipy application code to Taipy 3.0 before executing the entity
migration.

!!! note "Supported Taipy versions"

    The migration supports **Taipy 2.0** or newer.

## Migrate entities

The required argument of the 'migrate' CLI is `--repository-type`, which first accepts one
of the three following values: "filesystem" and "mongo". Each repository type can be
followed by additional arguments:

- *filesystem* can be followed by the path to the filesystem folder that holds your Taipy
  application data. It corresponds to the "storage_folder" attribute in the configuration "CORE"
  section. If not provided explicitly, the default value is ".data" in the application root directory.
- *mongo* can be followed by the credentials to access the mongo database that holds
  your Taipy Application data. The credentials must follow the order: "host", "port", "username",
  and "password". The default values are "localhost", "27017", and no username and password respectively.

To display the help section of `taipy migrate` CLI, you can run the `taipy help migrate` command.
Alternatively, you can use the *--help* or *-h* options by running `taipy migrate --help` or
`taipy migrate -h`.

```console
$ taipy help migrate
usage: taipy migrate [-h] --repository-type REPOSITORY_TYPE [REPOSITORY_TYPE ...] [--skip-backup]
                     [--restore] [--remove-backup]

options:
  -h, --help            show this help message and exit
  --repository-type REPOSITORY_TYPE [REPOSITORY_TYPE ...]
                        The type of repository to migrate. If filesystem, a path to the
                        database folder should be informed. In the case of MongoDB host,
                        port, user, and password must be informed, if left empty it is assumed
                        default values
  --skip-backup         Skip the backup of entities before migration.
  --restore             Restore the migration of entities from the backup folder.
  --remove-backup       Remove the backup of entities. Only use this option if the migration was
                        successful.
```

To migrate the entities of a Taipy application with a filesystem repository. We can run the
following command:

```console
$ taipy migrate --repository-type filesystem .data
```

Where `.data` is the path to the directory that holds the Taipy application data.

To migrate the entities of a Taipy application with a mongo repository. We can run the
following command:

```console
$ taipy migrate --repository-type mongo localhost 27017 username password
```

Where the arguments are the credentials to access the mongo database that holds the Taipy
application data.

!!! info

    Once executed, the structure of all entities in the repository will be changed to follow
    the data model of Taipy 3.0. You should see an informative message when the process is
    done.

## Backup and restore entities

By default, the migration process creates a backup of the entities before migrating them. To
skip the backup process, you can use the `--skip-backup` option.

```console
$ taipy migrate --repository-type filesystem .data --skip-backup
```

However, it is recommended to create the backup and test your application in a Taipy 3.0 environment
so that you can restore the entities later in case of any issues.

To restore the entities from the backup folder, you can use the `--restore` option. This option
will restore the entities from the backup folder and remove the backup folder.

```console
$ taipy migrate --repository-type filesystem .data --restore
```

If your application is fully tested and working in Taipy 3.0, you can remove the backup folder
by using the `--remove-backup` option.

```console
$ taipy migrate --repository-type filesystem .data --remove-backup
```

!!! info

    When using the `--restore` and `--remove-backup` options, the path provided to the repository
    type is the actual data path, not the backup folder path. Taipy will detect the backup folder
    and act accordingly.
