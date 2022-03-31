The `GlobalAppConfig^` holds configuration
fields
related to the global application.

Here are the (optional) configurable properties:

- _**root_folder**_: The path of the base folder for the taipy application, its default value is "./taipy/".
- _**storage_folder**_: The folder name used to store Taipy data, its default value is ".data/". It is used in
  conjunction with the root_folder field. That means the default storage path is "./taipy/.data/".
- _**clean_entities_enabled**_: The field to activate/deactivate the clean entities feature, its default value
  is `ENV[TAIPY_CLEAN_ENTITIES_ENABLED]:bool` meaning that the value is read from the `TAIPY_CLEAN_ENTITIES_ENABLED`
  environment variable. If the environment variable is not set, the value is False.
- _**properties**_: The dictionary of additional properties.

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_global_app(root_folder=".taipy_root_folder/",
                                storage_folder=".data_folder",
                                clean_entities_enabled=True,
                                version_name="1.0.0",
                                application_name="my_application")
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
    version_name = "1.0.0"
    application_name = "my_application"
    ```

In this example, we set custom values for the _root_folder_, _storage_folder_, and _clean_entities_enabled_ parameters.
Note that most of the time the default values can be used. In line 6 and 7, two custom properties are specified: a
_version_name_ and an _application_name_.

[:material-arrow-right: The next section introduces the job scheduling configuration](job-config.md).
