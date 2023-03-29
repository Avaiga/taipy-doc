The `GlobalAppConfig^` holds configuration fields related to the global application.

Here are the (optional) configurable properties:

- _**root_folder**_: The path of the base folder for the taipy application, its default value is "./taipy/".
- _**storage_folder**_: The folder name used to store Taipy data, its default value is ".data/". It is used in
  conjunction with the root_folder field. That means the default storage path is "./taipy/.data/".
- _**clean_entities_enabled**_: The field to activate/deactivate the clean entities feature.
  Its default value is `ENV[TAIPY_CLEAN_ENTITIES_ENABLED]:bool` meaning that the default value is read from the
  `TAIPY_CLEAN_ENTITIES_ENABLED` environment variable. If the environment variable is not set, the default value is
  False. <br>
  Since it is risky to delete all entities on a production environment, Taipy proposes a way to activate this
  feature only on specific environments. That is why the default value points to an environment variable.
- _**read_entity_retry**_: The integer number of retry when reading an entity after a failed attempt (in case of
  concurrent access). The default value is 0.
- _**repository_type**_: The type of storage that will be used to hold Taipy entities. Available options are:
  `filesystem`, `sql` and `mongo`. If no repository type is informed, the filesystem will be used as the default
  repository.
- _**repository_properties**_: A dictionary of properties that will be used to instantiate the chosen repository.
  Only required if the chosen repository is `sql` or `mongo`.</br>
  If _**repository_type**_ is set to `filesystem`, Taipy uses _**root_folder**_ and _**storage_folder**_ to store
  entities. In this case, _**repository_properties**_ attribute is not required.</br>
  If _**repository_type**_ is set to `sql`, the _**db_location**_ attribute is required as the path of a sqlite3
  database file. Please refer to [SQL storage section](global-config.md#sql-storage-for-taipy-entities).</br>
  If _**repository_type**_ is set to `mongo`, the possible properties are _**mongodb_hostname**_, _**mongodb_user**_,
  _**mongodb_password**_, _**mongodb_port**_, _**application_db**_, _**properties**_. Please refer to
  [MongoDB storage section](global-config.md#mongodb-storage-for-taipy-entities).

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_global_app(root_folder=".taipy_root_folder/",
                                storage_folder=".data_folder",
                                clean_entities_enabled=True,
                                read_entity_retry=2,
                                version_name="1.0.0",
                                application_name="my_application",)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"

    [TAIPY]

    root_folder = ".taipy_root_folder/"
    storage_folder = ".data_folder"
    clean_entities_enabled = "True:bool"
    read_entity_retry = "2:int"
    version_name = "1.0.0"
    application_name = "my_application"
    ```

In this example, we set custom values for the _root_folder_, _storage_folder_, _clean_entities_enabled_, and
_read_entity_retry_ parameters. Note that most of the time the default values can be used. In lines 7-8, two custom
properties are specified: a _version_name_ and an _application_name_.

## SQL storage for Taipy entities

The configuration needed to use a SQL database, through sqlite3 engine, is described in the lines 7-8.

```python linenums="1"
from taipy import Config

Config.configure_global_app(
    root_folder=".taipy_root_folder/",
    storage_folder=".data_folder",
    clean_entities_enabled=True,
    read_entity_retry=2,
    repository_type="sql",
    repository_properties={"db_location": "path_to_sqlite_file/database.db"}
    )
```
Taipy creates a table called `taipy_model` in the database described in the configuration, where it stores
information about the taipy entities.


Here are the configurable properties for the SQL repository:
  - _**db_location**_: The path of a sqlite3 database file.

## MongoDB storage for Taipy entities

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

The configuration needed to use a mongo database is described in the lines 7-14.

```python linenums="1"
from taipy import Config

Config.configure_global_app(root_folder=".taipy_root_folder/",
                            storage_folder=".data_folder",
                            clean_entities_enabled=True,
                            read_entity_retry=2,
                            repository_type="mongo",
                            repository_properties={
                              "mongodb_hostname": "localhost",
                              "mongodb_user": "username",
                              "mongodb_password": "passwd",
                              "mongodb_port": 27017,
                              "application_db": "taipy"
                            }
                            )
```

Taipy will create a collection, in the database described in the configuration, for each taipy entity(Cycle,
Scenario, Pipeline, Datanode, Task and Job), where it will store information about the taipy entities.

Here are the configurable properties for the Mongo repository:

  - _**mongodb_hostname**_: The URL for the mongo database.
  - _**mongodb_user**_: The username to access the database.
  - _**mongodb_password**_: The password to access the database.
  - _**mongodb_port**_: The port to access the database. This property is optional and has 27017 as a default value.
  - _**application_db**_: The database that will hold the taipy collections.

[:material-arrow-right: The next section introduces the job orchestration configuration](job-config.md).
