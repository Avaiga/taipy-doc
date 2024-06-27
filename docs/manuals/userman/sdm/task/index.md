This page describes the `Task^` management. It explains how to create tasks,
access their attributes, and retrieve them.

# Task Configuration

TODO:
Cross-ref to the
[Task configuration](../../task-orchestration/scenario-config.md#from-task-configurations) section.

# Task Creation
Tasks get created when scenarios are created. For more details, see the
[Scenario creation](../scenario/index.md#scenario-creation) section.


# Task attributes

A `Task^` entity is identified by a unique identifier `id` Taipy generates.
A task also holds various properties accessible as an attribute of the task:

- _**config_id**_ is the id of the scenario configuration.
- _**input**_ is the list of input data nodes.
- _**output**_ is the list of output data nodes.
- _**function**_ is the Python function associated with the Task config.<br/>
  The *function* takes as many parameters as there are data nodes in the *input* attribute. Each parameter corresponds
  to the return value of an input data node `read()` method.<br/>
  The function returns as many parameters as there are data nodes in the *output* attribute. Each
  *function*'s returned value corresponds to the parameter of an output data node `write()` method.
- _**version**_: The string indicates the application version of the task to instantiate.
  If not provided, the current version is used. Refer to the [version management](../../versioning/index.md)
  page for more details.
- _**skippable**_: Boolean attribute indicating if a task execution can be skipped when all output
  data nodes are up-to-date (see the *validity_period* attribute in the
  [Data node management page](../entities/data-node-mgt.md) for more detail). The default value of
  *skippable* is False.

!!! example

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task = scenario.predicting

    # the config_id is an attribute of the task. Here it equals "predicting"
    task.config_id

    # the function to be executed with data from input data
    # nodes and returns value for output data nodes.
    task.function # predict

    # input is the list of input data nodes of the task
    task.input # [trained_model_cfg, current_month_cfg]

    # output is the list of output data nodes of the task
    task.output # [sales_predictions_cfg]

    # the current_month data node entity is exposed as an attribute of the task
    current_month_data_node = task.current_month
    ```

Taipy exposes multiple methods to manage the various tasks.

# Get Tasks

The first method to access a job is from its id by using the `taipy.get()^` method.

```python linenums="1"
import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
task = scenario.training
task_retrieved = tp.get(task.id)
# task == task_retrieved
```

Here, the two variables `task` and `task_retrieved` are equal.

All the jobs can be retrieved using the method `taipy.get_tasks()^`.

# Get tasks by config id

A task can be retrieved from a scenario or a sequence, by accessing the task config_id attribute.

```python linenums="1"
task_1 = scenario.predicting  # "predicting" is the config_id of the predicting Task in the scenario
sequence = scenario.sales
task_2 = sequence.predicting  # "predicting" is the config_id of the predicting Task in the sequence
# task_1 == task_2
```

Tasks can also be retrieved using `taipy.get_entities_by_config_id()^` providing the config_id.
This method returns the list of all existing tasks instantiated from the config_id provided as a parameter.

!!! example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create 2 scenarios, which will also create 2 trainig tasks.
    scenario_1 = tp.create_scenario(my_config.monthly_scenario_cfg)
    scenario_2 = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get all training tasks by config id, this will return a list of 2 training tasks
    # created alongside the 2 scenarios.
    all_training_tasks = tp.get_entities_by_config_id("training")
    ```

# Get parent scenarios and sequences

To access the parent entities of a task (scenarios or sequences), you can
use either the method `Task.get_parents()^` or the function
`taipy.get_parents()^`. Both return the parents of the task.

!!! example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a task
    task = scenario.training_cfg

    # Retrieve the parent entities of the task. The returned value is
    # {'scenarios': [Scenario 1], 'sequences': [Sequence 1]}
    parent_entities = task.get_parents()

    # Retrieve the parent entities of the task. The return value is
    # {'scenarios': [Scenario 1], 'sequences': [Sequence 1]}
    tp.get_parents(task)
    ```

[:material-arrow-right: The next section shows the data node management](data-node-mgt.md).
