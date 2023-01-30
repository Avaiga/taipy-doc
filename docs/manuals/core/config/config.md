The `Config^` class is a singleton as the entry point for the Taipy Core configuration. It is accessible
using the following import:

```py linenums="1"
from taipy import Config
```

It exposes all the necessary attributes and methods to manage the configuration. In particular, it holds

- the [data node configurations](data-node-config.md) as a dictionary of `DataNodeConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.data_nodes
    ```
- the [task configurations](task-config.md) as a dictionary of`TaskConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.tasks
    ```
- the [pipeline configurations](pipeline-config.md) as a dictionary of`PipelineConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.pipelines
    ```
- the [scenario configurations](scenario-config.md) as a dictionary of `ScenarioConfig^`s:
    ```python linenums="1"
    from taipy import Config

    Config.scenarios
    ```
- the [job configuration](job-config.md) as a `JobConfig^`:
    ```python linenums="1"
    from taipy import Config

    Confi.job_config
    ```
- the [global configuration](global-config.md) as a `GlobalAppConfig^`:
    ```python linenums="1"
    from taipy import Config

    Confi.global_config
    ```

[:material-arrow-right: The next section introduces the data node configuration](data-node-config.md).
