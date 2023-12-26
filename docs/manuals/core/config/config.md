The `Config^` class is a singleton as the entry point for the Taipy Core configuration. It is accessible
using the following import:

```python linenums="1"
from taipy import Config
```

It exposes all the necessary attributes and methods to manage the configuration. In particular, it holds:

- The [Data node configurations](data-node-config.md) as a dictionary of `DataNodeConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.data_nodes
    ```
- The [Task configurations](task-config.md) as a dictionary of`TaskConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.tasks
    ```
- The [Scenario configurations](scenario-config.md) as a dictionary of `ScenarioConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.scenarios
    ```
- The [Job configuration](job-config.md) as a `JobConfig^`:
    ```python linenums="1"
    from taipy import Config

    Config.job_config
    ```
- The [Core configuration](core-config.md) as a `CoreSection^`:
    ```python linenums="1"
    from taipy import Config

    Config.core
    ```
- The Global configuration as a `GlobalAppConfig^`:
    ```python linenums="1"
    from taipy import Config

    Config.global_config
    ```

[:material-arrow-right: The next section introduces the data node configuration](data-node-config.md).
