# Configuration

The `Config^` class is a singleton as the entry point for the Taipy configuration. It is accessible
using the following import:

```python linenums="1"
from taipy import Config
```

!!! note "Reminder: Config vs Entities"

    Throughout the documentation, configuration objects are named **_configs_** (`DataNodeConfig^`, `TaskConfig^`,
    and `ScenarioConfig^`), while runtime objects (`DataNode^`, `Task^`, `Sequence^`, and `Scenario^`) are called
    entities.

    One thing to wrap your head around (it may not be very intuitive for everyone at first) is that
    the **configs** are really just configuration objects specifying the characteristics and behaviors
    of the runtime concepts they relate to. **Configs** can be seen as generators. Indeed, each
    **entity** is instantiated from a **config**. Note also that the same **config** can be used to
    instantiate multiple **entities**.

    More details on the **entities** are available in the [Entities](../entities/index.md) chapter.

!!! warning

    All configuration objects must be created before instantiating any entity or running the Core service.

    Any modification to the configuration objects after the Core service has been started or an entity has been
    instantiated will raise an error.

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
