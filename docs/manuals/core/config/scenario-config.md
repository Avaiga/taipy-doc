A scenario configuration is necessary to instantiate a [Scenario](../concepts/scenario.md). To create a
[`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig) you can use
the `taipy.configure_scenario()` method with the following parameters:

- `name`: The name of new scenario configuration to be created. This name should be unique.
- `pipelines`: The list of pipeline configs.
- `frequency`: The recurrence of the scenarios instantiated from this configuration.
Based on this frequency the scenarios will be attached to the right cycles.
- `comparators`: The list of functions used to compare scenarios.
A comparator function is attached to a scenario's data node configuration. During the scenarios comparison, each
comparator is applied to all the data nodes instantiated from the data node configuration attached to the comparator.
- `properties`: The dictionary of additional properties.

Basic example using the pipeline configuration `pipeline_config` created in the previous example:

```python linenums="1"
import taipy as tp

scenario_config = tp.configure_scenario("multiply_scenario", [pipeline_config])
```

In this example, we create a scenario configuration `ScenarioConfig` which contains the pipeline that was
defined in the previous example.

In the case the scenario configuration contains only one single pipeline configuration, we can also create the
`ScenarioConfig` from the task configurations directly.

```python linenums="1"
import taipy as tp

scenario_config = tp.configure_scenario_from_tasks("multiply_scenario", [task_config])
```

Behind the scenes, a pipeline configuration is created. Its name will be the scenario configuration name with the
`_pipeline` postfix (`multiply_scenario_pipeline` in the previous example).

!!! Note

    Note that the pipeline name can be configured as an optional parameter as follows:

    ```python linenums="1"
    import taipy as tp

    scenario_config = tp.configure_scenario_from_tasks("multiply_scenario", [task_config], pipeline_name="multiply_pipeline")
    ```
[:material-arrow-right: Next section introduces the global and scheduling configuration](global-config.md).
