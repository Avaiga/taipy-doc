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

# From pipeline configs
Here is a simple example assuming the pipeline configuration `pipeline_config` has already been created :

```python linenums="1"
from taipy import Config

scenario_config = Config.configure_scenario("multiply_scenario", [pipeline_config])
```

In this example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration already defined.


# From task configs

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

    scenario_config = Config.configure_scenario_from_tasks(
        "multiply_scenario", [task_config], pipeline_id="multiply_pipeline")
    ```

# Using Cycles

Assuming the pipeline configuration `pipeline_config` has already been created, here is an example of a weekly
scenario configuration :

```python  linenums="1"
from taipy import Config, Frequency

scenario_config = Config.configure_scenario(
    "multiply_scenario", [pipeline_config], Frequency.WEEKLY)
```

In this small example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration with a
`WEEKLY` frequency. When scenarios (entities) do get created using the scenario configuration above, they will be
associated to a Cycle corresponding to their creation date. See documentation on
[Scenario and cycle management](../entities/scenario-cycle-mgt.md).

[:material-arrow-right: The next section introduces the global configuration](global-config.md).

# Using scenario comparators

Let us imagine a common situation where the pipeline configuration `pipeline_config` has been created with
`datanode_config` as one of the data node configuration for this the pipeline configuration. The function
`compare_function` is also defined as followed:

```python
from taipy import Config

# Calling compare_function(10, 13, 17, 9) returns the following dict
# {
# 0: {0: 0, 1: 3, 2: 7, 3: -1},
# 1: {0: -3, 1: 0, 2: 4, 3: -4},
# 2: {0: -7, 1: -4, 2: 0, 3: -8},
# 3: {0: 1, 1: 4, 2: 8, 3: 0}}
def compare_function(*data_node_results):
    compare_result= {}
    current_res_index = 0
    for current_res in data_node_results:
        compare_result[current_res_index]={}
        next_res_index = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_index} with result {next_res_index}")
            compare_result[current_res_index][next_res_index] = next_res - current_res
            next_res_index += 1
        current_res_index += 1
    return compare_result

scenario_config = Config.configure_scenario("multiply_scenario", [pipeline_config],
                                            comparators={datanode_config.id: compare_function})
```

We created the scenario configuration `scenario_config` using the indicated pipeline configuration. We use the
`comparators` parameter to provide a dictionary indicating which data node need to be compared and with what function.
