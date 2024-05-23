A scenario configuration is necessary to instantiate a `Scenario^`. To create a
`ScenarioConfig^`, you can use the `Config.configure_scenario()^` method with the following parameters:

- _**id**_: The id of a new scenario configuration to be created. This id is **mandatory** and must
  be a unique and valid Python identifier.
- _**tasks**_: A list of task configurations.
- _**additional_data_nodes**_: A list of additional data node configurations.
- _**frequency**_: The recurrence of the scenarios instantiated from this configuration. The scenarios
  are attached to the proper cycles based on this frequency.
- _**sequences**_: A dictionary of sequence descriptions.
- _**comparators**_: A list of functions used to compare scenarios. A comparator function is attached to a
  scenario's data node configuration. During the scenario comparison, each comparator is applied to all the data
  nodes instantiated from the data node configuration attached to the comparator.
- _**properties**_: A dictionary of additional properties.

!!! warning "Reserved keys"

    Note that we cannot use the word "_entity_owner" as a key in the properties as it has been reserved for internal use.

# From task configurations

Here is a simple example assuming the task configuration `multiply_task_cfg` has already been created:

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [multiply_task_cfg])
```

In this example, we create a scenario configuration `ScenarioConfig^` from a task configuration from
a defined task configuration. A `ScenarioConfig^` must always be provided with a list of `TaskConfig^`.

# Adding additional data nodes configurations

Here is a simple example assuming the task configuration `multiply_task_cfg` and the data node configuration
`additional_dn_cfg` have already been created:

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [multiply_task_cfg],
                                         [additional_dn_cfg])
```

In this example, we create a scenario configuration `ScenarioConfig^` from a task configuration and
a data node configuration already defined. The provided data node configuration represents additional data.
Additional data node configurations are optional when configuring a `ScenarioConfig^`.


# Adding sequence descriptions

In the scenario configuration, we can describe the sequences to be created with the scenario creation.
Here is a simple example assuming the task configuration `add_task_cfg_1`, `add_task_cfg_2`,
`multiply_task_cfg_1`, `multiply_task_cfg_2` have already been created:

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [add_task_cfg_1, add_task_cfg_2, multiply_task_cfg_1, multiply_task_cfg_2],
                                         sequences={"add_sequence": [add_task_cfg_1, add_task_cfg_2],
                                                    "multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})
```

We can also add sequences to our scenario configuration after we have created our scenario configuration.

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [add_task_cfg_1, add_task_cfg_2, multiply_task_cfg_1, multiply_task_cfg_2])

scenario_cfg.add_sequences({"add_sequence": [add_task_cfg_1, add_task_cfg_2],
                            "multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})

# Or we can add them separately as well
scenario_cfg.add_sequences({"add_sequence": [add_task_cfg_1, add_task_cfg_2]})
scenario_cfg.add_sequences({"multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})

```

We can also remove sequences after providing them in your scenario configuration.

```python linenums="1"
from taipy import Config

scenario_cfg = Config.configure_scenario("multiply_scenario",
                                         [add_task_cfg_1, add_task_cfg_2, multiply_task_cfg_1, multiply_task_cfg_2],
                                         sequences={"add_sequence": [add_task_cfg_1, add_task_cfg_2],
                                                    "multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})

scenario_cfg.remove_sequences(["add_sequence", "multiply_sequence"])

# Or we can remove a single sequence from a ScenarioConfig by passing only a sequence name to
# ScenarioConfig.remove_sequences
scenario_cfg.remove_sequences("add_sequence")

```
In the small examples above, we create a scenario configuration `ScenarioConfig^` from task configurations and
define sequences for that scenario configuration. You can refer back to the sequence concept in
[Sequence concept](../concepts/sequence.md).

When defining a sequence in a `ScenarioConfig^`, you need to provide a dictionary with the sequence name as the key
and a list of task configurations that belong to the sequence as the value. Note that the task configurations of the
sequence must also exist in the tasks of the scenario configuration.

# Using Cycles

Assuming the task configuration `multiply_task_cfg` has already been created, here is an example of a weekly
scenario configuration:

```python linenums="1"
from taipy import Config, Frequency

scenario_cfg = Config.configure_scenario("multiply_scenario", [multiply_task_cfg], frequency=Frequency.WEEKLY)
```

In this small example, we create a scenario configuration `ScenarioConfig^` from a task configuration with a
`WEEKLY` frequency. When scenarios (entities) get instantiated using the scenario configuration above, they will be
associated with a Cycle corresponding to their creation date. See the documentation on
[Scenario and cycle management](../entities/scenario-cycle-mgt.md).

# Using scenario comparators

Let us imagine a typical situation where the task configuration `task_cfg` has been
created using `datanode_cfg` as one of its data node configurations. At the scenario configuration level, you can
define a function that compares the results for the various scenarios (entities) created with this configuration. You
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
    [task_cfg],
    comparators={datanode_cfg.id: compare_function})
```

We created the scenario configuration `scenario_cfg` using the indicated task configuration. We use
_comparators_ parameter to provide a dictionary indicating which data nodes and what function(s) will be
involved in the comparison. In this example we use the function `compare_function()`.

Line 25 indicates that only the data nodes instantiated from `data_node_cfg` are selected for the comparison.

The comments in lines 3-8, gives you an idea of what the `compare_function()` function computes depending
on the given input parameters.

!!! info

    Please refer to the [scenario entity comparison](../entities/scenario-cycle-mgt.md) section to see
    how to compare scenarios using the comparators defined in a `ScenarioConfig^`.

[:material-arrow-right: The next section introduces the Core configuration](core-config.md).
