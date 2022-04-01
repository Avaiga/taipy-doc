# Taipy's Core configuration

Taipy Core is an application builder that converts user algorithms into a back-end application. To build such
an application with the desired behaviors, a few Taipy entities must be configured.

The following sections show how to configure a Taipy application in python. All The taipy configuration methods can
easily be imported from the Taipy main module as follows:

```python
import taipy as tp
```

!!! Note
    Note that you can override the python configuration using _TOML_ files. (More details on the
    [advanced configuration](advanced-config.md)) page.

!!! "Reminder. Config vs Entities"

    Among the concepts described in this section, the **data nodes**, **tasks**, **pipelines**, and **scenarios** have
    two types of Taipy objects related to them: configuration objects and runtime objects.

    To differentiate the configuration objects from their runtime counterparts, they are named **_configs_**
    (`DataNodeConfig`, `TaskConfig`, `PipelineConfig`, and `ScenarioConfig`) while the runtime objects
    (`DataNode`, `Task`, `Pipeline`, and `Scenario`) are called **_entities_**.

    One thing to wrap your head around (it may not be very intuitive for everyone at first) is that the **configs**
    are really just configuration objects specifying the characteristics and the behaviors of the concepts they relate
    to. **Configs** can be seen as generators. Indeed, each **entity** is created from a **config**. Note also that
    a same **config** can be used to instantiate multiple **entities**.

    More details on the **entities** are available in the [entities documentation](../entities/index.md)

[:material-arrow-right: Next section introduces the data node configuration](data-node-config.md).
