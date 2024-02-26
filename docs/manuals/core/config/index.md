# Taipy's Core configuration

In the previous chapter, the main [Taipy Core concepts](../concepts/index.md) are defined.

Taipy Core is an application builder designed to help Python developers efficiently turn
their algorithms into an interactive production-ready data-driven application.

To build such an application, the first step consists in configuring the characteristics and the desired behavior of
your application and its entities.

!!! note "Reminder: Config vs Entities"

    Throughout the documentation, configuration objects are named **_configs_** (`DataNodeConfig^`, `TaskConfig^`,
    and `ScenarioConfig^`), while runtime objects (`DataNode^`, `Task^`, `Sequence^`, and `Scenario^`) are called entities.

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

This chapter is dedicated to the configuration and focuses on the various **configs** objects. Its sections are
organized as follows:

- [Config](config.md) section introduces the `Config^` singleton class, the single entry
  point for Taipy Core configuration.
- [Data node configs](data-node-config.md) section describes the data nodes' configurations using
  the `DataNodeConfig^` class.
- [Task configs](task-config.md) section describes the tasks' configurations using the
  `TaskConfig^` class.
- [Scenario configs](scenario-config.md) section describes the scenarios' configurations using the
  `ScenarioConfig^` class.
- [Core config](core-config.md) section documents the Core configuration fields and the
  `CoreSection^` class.
- [Job orchestration config](job-config.md) section documents the configuration of the job orchestration
  using the `JobConfig^` class.
- [Config checker](config-checker.md) section presents the configuration checkers.
- [Advanced configuration](advanced-config.md) section provides details on advanced configuration
  features, particularly the capacity to overwrite configuration fields with _TOML_ files.

[:material-arrow-right: The next section introduces the Config singleton](config.md).
