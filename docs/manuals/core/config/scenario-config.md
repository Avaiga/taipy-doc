A scenario configuration is necessary to instantiate a [Scenario](../concepts/scenario.md). To create a
`ScenarioConfig^` you can use the `Config.configure_scenario()^` method with the following parameters:

- _**id**_: The id of new scenario configuration to be created. This id is **mandatory** and must be a unique and valid
  Python variable name.
- _**pipelines**_: The list of pipeline configs.
- _**frequency**_: The recurrence of the scenarios instantiated from this configuration. Based on this frequency the
  scenarios will be attached to the right cycles.
- _**comparators**_: The list of functions used to compare scenarios. A comparator function is attached to a
  scenario's data node configuration. During the scenario comparison, each comparator is applied to all the data
  nodes instantiated from the data node configuration attached to the comparator.
- _**properties**_: A dictionary of additional properties.

# Scenario configuration from pipelineConfigs
Here is a simple example assuming the pipeline configuration `pipeline_config` has already been created :

```python linenums="1"
from taipy import Config

scenario_config = Config.configure_scenario("multiply_scenario", [pipeline_config])
```

In this example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration already defined.


# Scenario configuration from taskConfigs

When the scenario configuration contains only one single pipeline configuration, we can also create the
`ScenarioConfig^` from the task configurations directly.

```python linenums="1"
from taipy import Config

scenario_config = Config.configure_scenario_from_tasks("multiply_scenario", [task_config])
```

Behind the scenes, a pipeline configuration is created. Its id will be the scenario configuration id with the
`_pipeline` postfix (`multiply_scenario_pipeline` in the example).

!!! Note

    Note that the pipeline id can be configured as an optional parameter as follows:

    ```python linenums="1"
    from taipy import Config

    scenario_config = Config.configure_scenario_from_tasks("multiply_scenario", [task_config], pipeline_id="multiply_pipeline")
    ```

# Recurrent scenario configuration with Cycle

Assuming the pipeline configuration `pipeline_config` has already been created, here is an example of a weekly
scenario configuration :

```python  linenums="1"
from taipy import Config, Frequency

scenario_config = Config.configure_scenario("multiply_scenario", [pipeline_config], Frequency.WEEKLY)
```

In this small example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration with a
`WEEKLY` frequency.


[:material-arrow-right: The next section introduces the global configuration](global-config.md).
