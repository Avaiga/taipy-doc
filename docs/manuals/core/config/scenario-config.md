A scenario configuration is necessary to instantiate a [Scenario](../concepts/scenario.md). To create a
`ScenarioConfig^`, you can use the `Config.configure_scenario()^` method with the following parameters:

- _**id**_: The id of a new scenario configuration to be created. This id is **mandatory** and must
  be a unique and valid Python identifier.
- _**pipelines**_: The list of pipeline configs.
- _**frequency**_: The recurrence of the scenarios instantiated from this configuration. The scenarios
  are attached to the proper cycles based on this frequency.
- _**comparators**_: The list of functions used to compare scenarios. A comparator function is attached to a
  scenario's data node configuration. During the scenario comparison, each comparator is applied to all the data
  nodes instantiated from the data node configuration attached to the comparator.
- _**properties**_: A dictionary of additional properties.

# From pipeline configs
Here is a simple example assuming the pipeline configuration `pipeline_cfg` has already been created:

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [pipeline_cfg])
```

In this example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration already defined.


# From task configs

When the scenario configuration contains only one single pipeline configuration, we can also create the
`ScenarioConfig^` from the task configurations directly.

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario_from_tasks("multiply_scenario",
                                                    [task_cfg])
```

Behind the scenes, a pipeline configuration is created. Its id will be the scenario configuration id with the
`_pipeline` postfix (`multiply_scenario_pipeline` in the example).

!!! Note

    Note that the pipeline id can be configured as an optional parameter as follows:

    ```python linenums="1"
    from taipy import Config

    scenario_cfg = Config.configure_scenario_from_tasks(
        "multiply_scenario",
        [task_cfg],
        pipeline_id="multiply_pipeline")
    ```

# Using Cycles

Assuming the pipeline configuration `pipeline_cfg` has already been created, here is an example of a weekly
scenario configuration:

```python  linenums="1"
from taipy import Config, Frequency

scenario_cfg = Config.configure_scenario(
    "multiply_scenario",
    [pipeline_cfg],
    Frequency.WEEKLY)
```

In this small example, we create a scenario configuration `ScenarioConfig^` from a pipeline configuration with a
`WEEKLY` frequency. When scenarios (entities) get instantiated using the scenario configuration above, they will be
associated with a Cycle corresponding to their creation date. See the documentation on
[Scenario and cycle management](../entities/scenario-cycle-mgt.md).

# Using scenario comparators

Let us imagine a typical situation where the pipeline configuration `pipeline_cfg` has been
created using `datanode_cfg` as one of its data node configurations. At the scenario configuration level, you can
define a function that compares the results for the various scenarios (entities) created with this config. You
simply need to define such a function in the comparators field. Here’s an example below:


```python linenums="1"
from taipy import Config

# Calling compare_function(10, 13, 17, 9) returns the following dict
# {
# 0: {0: 0, 1: 3, 2: 7, 3: -1},
# 1: {0: -3, 1: 0, 2: 4, 3: -4},
# 2: {0: -7, 1: -4, 2: 0, 3: -8},
# 3: {0: 1, 1: 4, 2: 8, 3: 0}}
def compare_function(*data_node_results):
    compare_result= {}
    current_res_i = 0
    for current_res in data_node_results:
        compare_result[current_res_i]={}
        next_res_i = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_i} with result {next_res_i}")
            compare_result[current_res_i][next_res_i] = next_res - current_res
            next_res_i += 1
        current_res_i += 1
    return compare_result

scenario_cfg = Config.configure_scenario(
    "multiply_scenario",
    [pipeline_cfg],
    comparators={datanode_cfg.id: compare_function})
```

We created the scenario configuration `scenario_cfg` using the indicated pipeline configuration. We use
_comparators_ parameter to provide a dictionary indicating which data nodes and what function(s) will be
involved in the comparison. In this example we use the function `compare_function()`.

Line 25 indicates that only the data nodes instantiated from `data_node_cfg` are selected for the comparison.

The comments in lines 3-8, gives you an idea of what the `compare_function()` function computes depending
on the given input parameters.

!!! Info

    Please refer to the [scenario entity comparison](../entities/scenario-cycle-mgt.md) section to see
    how to compare scenarios using the comparators defined in a `ScenarioConfig^`.

[:material-arrow-right: The next section introduces the global configuration](global-config.md).
