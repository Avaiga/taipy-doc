The `CoreSection^` holds configuration fields related to the core package, in particular
the fields related to the Taipy repository for entity storage.

Here are the (optional) configurable properties:

- _**root_folder**_: The path of the base folder for the Taipy application, its default value is
    "./taipy/".
- _**storage_folder**_: The folder name used to store Taipy data, its default value is ".data/".
    It is used in conjunction with the root_folder field. That means the default storage path is
    "./taipy/.data/".
- _**read_entity_retry**_: An integer number only used with `filesystem` _**repository_type**_. <br>
    It corresponds to the number of times Taipy retries reading an entity after a failed attempt
    for concurrent access. <br>
    The default value is 1.
- _**repository_type**_: The type of storage that will be used to hold Taipy entities. Available
    options are: `filesystem` and `mongo`. The filesystem will be used as the default
    repository if no repository type is informed.
- _**repository_properties**_: A dictionary of properties that will be used to instantiate the
    chosen repository. Only required if the chosen repository is `mongo`.</br>
    If _**repository_type**_ is set to `filesystem`, Taipy uses _**root_folder**_ and
    _**storage_folder**_ to store entities. In this case, _**repository_properties**_ attribute
    is not required.</br>
    If _**repository_type**_ is set to `mongo`, the possible properties are
    _**mongodb_hostname**_, _**mongodb_user**_, _**mongodb_password**_, _**mongodb_port**_,
    _**application_db**_, _**properties**_. Please refer to
    [MongoDB storage section](core-config.md#mongodb-storage-for-taipy-entities).
- _**mode**_: A string that indicates the mode of the version management system.
    Possible values are *"development"* or *"experiment"*. On Enterprise edition of Taipy,
    *production* mode is also available. Please refer to the
    [Versioning management](../versioning/index.md) documentation page for more details.
- _**version_number**_: The identifier of the version. In development mode, the version number
    is ignored.
- _**force**_: Indicates whether Taipy will override a version even if the configuration has
    changed or not and run the application. Default to False.

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_core(
        root_folder=".taipy_root_folder/",
        storage_folder=".data_folder",
        read_entity_retry=2,
        mode="experiment",
        version_number="1.0.0",
        application_name="my_application",
    )
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"

    [TAIPY]

    [CORE]
    root_folder = ".taipy_root_folder/"
    storage_folder = ".data_folder"
    read_entity_retry = "2:int"
    mode = "experiment"
    version_number = "1.0.0"
    application_name = "my_application"
    ```

In this example, we configure:

  - Custom values for the *root_folder*, *storage_folder*, and *read_entity_retry* parameters.
      Note that most of the time, the default values can be used.
  - The *mode* of the version management system to experiment mode, and the *version_number* is
      set to "1.0.0".</br>
      Please refer to the [Version management configuration](../versioning/index.md)
      documentation page for more details.
  - In lines 9, a custom *application_name* property are specified.

## MongoDB storage for Taipy entities

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

The configuration needed to use a mongo database is described in the lines 6-14.

```python linenums="1"
from taipy import Config

Config.configure_core(
    root_folder=".taipy_root_folder/",
    storage_folder=".data_folder",
    repository_type="mongo",
    repository_properties={
        "mongodb_hostname": "localhost",
        "mongodb_user": "username",
        "mongodb_password": "passwd",
        "mongodb_port": 27017,
        "application_db": "taipy",
    }
)
```

Taipy will create a collection, in the database described in the configuration, for each Taipy
entity (`Cycle^`, `Scenario^`, `DataNode^`, `Task^` and `Job^`), where it will store information
about the Taipy entities.

Here are the configurable properties for the Mongo repository:

  - _**mongodb_hostname**_: The URL for the mongo database.
  - _**mongodb_user**_: The username to access the database.
  - _**mongodb_password**_: The password to access the database.
  - _**mongodb_port**_: The port to access the database. This property is optional and has 27017
      as a default value.
  - _**application_db**_: The database that will hold the taipy collections.
