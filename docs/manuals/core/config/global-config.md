The [`GlobalAppConfig`](../../../reference/#taipy.core.config.global_app_config.GlobalAppConfig) holds configuration
fields
related to the global application.

Here are the optional configurable properties:

- `root_folder`: The path of the base folder for the taipy application. Default value is "./taipy/".
- `storage_folder`: The folder name used to store Taipy data. Default value is ".data/".
It is used in conjunction with the root_folder field. That means the storage path is <root_folder><storage_folder>
(Default path is "./taipy/.data/").
- `clean_entities_enabled`: The field to activate/deactivate the clean entities feature. Default value is false.
- `properties`: The dictionary of additional properties.

```python linenums="1"
import taipy as tp

tp.configure_global_app(
    root_folder=".taipy_root_folder/",
    storage_folder=".data_folder",
    clean_entities_enabled=True,
    properties={"custom_property": False}
    )
```

[:material-arrow-right: Next section introduces the job scheduling configuration](job-config.md).
