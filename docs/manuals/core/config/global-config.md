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
- _**properties**_: The dictionary of additional properties.

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

[:material-arrow-right: The next section introduces the job scheduling configuration](job-config.md).
