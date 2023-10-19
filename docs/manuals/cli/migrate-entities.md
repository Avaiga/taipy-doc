# Migrate entities from earlier versions to Taipy 3.0

Taipy 3.0 provides a CLI option to update entities from older Taipy versions to `3.0`. It
is recommended to update the Taipy application code to Taipy 3.0 before executing the entity 
migration.

!!! note "Supported Taipy versions"

    The migration supports **Taipy 2.0** or newer.

## Migration arguments

The 'migrate' CLI has one argument, `--repository-type` that accepts 3 values: `filesystem`,
`sql`, and `mongo`. Each repository type must be succeeded of additional arguments, as described 
below:

- *filesystem* must be succeeded by the path to the filesystem folder that holds your Taipy
    application data. It corresponds to the `storage_folder` attribute in the configuration `CORE`
    section. If it has not been changed explicitly the value is `.data` inside the application root
    directory if it has not been provided explicitly.
- *sql* must be succeeded by the path to the sqlite file that holds your Taipy Application data.
- *mongo* must be succeeded by the credentials to access the mongo database that holds
    your Taipy Application data. The credentials must follow the order: `host`, `port`, `username`, 
    and `password`.

To display the help section of `taipy migrate` CLI, you can run the `taipy help migrate` command.
Alternatively, you can use the *--help* or *-h* options by running `taipy migrate --help` or 
`taipy migrate -h`.

```console
$ taipy help migrate
usage: taipy migrate [-h] [--repository-type {filesystem,sql,mongo} [{filesystem,sql,mongo} ...]]

optional arguments:
  -h, --help            show this help message and exit
  --repository-type {filesystem,sql,mongo} [{filesystem,sql,mongo} ...]
                        The type of repository to migrate. If filesystem or sql, a path to the database folder/.sqlite file should be informed. In
                        case of mongo host, port, user and password must be informed, if left empty it is assumed default values
```

To migrate the entities of a Taipy application with a filesystem repository. We can run the 
following command:

```console
$ taipy migrate --repository-type filesystem .data
``` 

Where `.data` is the path to the directory that holds the Taipy application data.

To migrate the entities of a Taipy application with a sqlite repository. We can run the 
following command:

```console
$ taipy migrate --repository-type filesystem ~/taipy.sqlite3
```

Where  `~/taipy.sqlite3` is the path to the sqlite file that holds the Taipy application data.

To migrate the entities of a Taipy application with a sqlite repository. We can run the 
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