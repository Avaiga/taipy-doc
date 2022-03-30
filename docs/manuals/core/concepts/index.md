Taipy core is built for data scientists to turn their algorithms into real, customized applications. Taipy core
provides the necessary concepts for modeling, executing, and monitoring such algorithms.


In this section, the following concepts are defined:

- [Data node](data-node.md)
- [Task](task.md)
- [Job](job.md)
- [Pipeline](pipeline.md)
- [Scenario](scenario.md)
- [Cycle](cycle.md)
- [Scope](scope.md)

!!! definition "Config vs Entities"
    Among the previous concepts, data nodes, tasks, pipelines, and scenarios are created by providing configuration
    objects.

    To differentiate the configuration objects from their runtime counterparts, they are named **_configs_**
    (`DataNodeConfig`, `TaskConfig`, `PipelineConfig`, and `ScenarioConfig`) while the runtime objects
    (`DataNode`, `Task`, `Pipeline`, and `Scenario`) are called **_entities_**.

    On this page, we provide information on the entities. More details on the configuration objects are available in
    the [configuration documentation](../config/index.md).


[:material-arrow-right: Next section introduces the data node concept](data-node.md).
