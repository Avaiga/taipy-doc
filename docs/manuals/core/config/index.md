# Taipy's Core configuration

In the previous chapter, the few [Taipy Core concepts](../concepts/index.md) are defined.

Taipy Core is an application builder designed to help data scientists turn their algorithms into an interactive
production-ready data-driven application.

To build such an application, the first step consists in configuring the characteristic and the desired behavior of
your application and its entities.

!!! important "Reminder: Config vs Entities"

    The **data nodes**, **tasks**, **pipelines**, and **scenarios** concepts have two types of Taipy objects
    related to them: configuration objects and runtime objects.

    To differentiate the configuration objects from their runtime counterparts, they are named **_configs_**
    (`DataNodeConfig`, `TaskConfig`, `PipelineConfig`, and `ScenarioConfig`) while the runtime objects
    (`DataNode`, `Task`, `Pipeline`, and `Scenario`) are called **_entities_**.

    One thing to wrap your head around (it may not be very intuitive for everyone at first) is that the **configs**
    are really just configuration objects specifying the characteristics and the behaviors of the concepts they relate
    to. **Configs** can be seen as generators. Indeed, each **entity** is created from a **config**. Note also that
    a same **config** can be used to instantiate multiple **entities**.

More details on the **entities** are available in the [Entities](../entities/index.md) chapter.

This chapter is dedicated to the configuration and focuses on the various **configs** objects. Its sections are
organized as follows:

- [Config](config.md) section introduces the `Config^` singleton class which is the single entrypoint for Taipy Core
  configuration.
- [Data node configs](data-node-config.md) section provides documentation on the data nodes' configurations using
  the python `DataNodeConfig^` class.
- [Task configs](task-config.md) section provides documentation on the tasks' configurations using the python
  `TaskConfig^` class.
- [Pipeline configs](pipeline-config.md) section provides documentation on the pipelines' configurations using the
  python `PipelineConfig^` class.
- [Scenario configs](scenario-config.md) section provides documentation on the scenarios' configurations using the
  python `ScenarioConfig^` class.
- [Global config](global-config.md) section documents the global configuration fields and the python `GlobalAppConfig^`
  class.
- [Job scheduling config](job-config.md) section documents the configuration of the job scheduling using the python
  `JobConfig^` class.
- [Config checker](config-checker.md) section presents the configuration checkers.
- [Advanced configuration](advanced-config.md) section provides details on advanced configuration features, and in
  particular the capacity to overwrite configuration fields with _TOML_ files.

[:material-arrow-right: The next section introduces the Config singleton](config.md).
