Tasks get created when scenarios or pipelines are created. Please refer to the
[Entities' creation](scenario-creation.md) section for more details.

In this section, it is assumed that <a href="./code_example/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented.

# Task attributes
Now that we know how to create a new `Task^`, this section focuses on describing the task's attributes and
utility methods.

A `Task^` entity is identified by a unique identifier `id` Taipy generates.
A task also holds various properties accessible as an attribute of the task:

- _**config_id**_ is the id of the scenario configuration.
- _**input**_ is the list of input data nodes.
- _**output**_ is the list of output data nodes.
- _**function**_ is the Python function associated with the Task config.<br/>
  The _function_ takes as many parameters as there are data nodes in the _input_ attribute. Each parameter corresponds
  to the return value of an input data node `read()` method.<br/>
  The function returns as many parameters as there are data nodes in the _output_ attribute. Each
  _function_'s returned value corresponds to the parameter of an output data node `write()` method.
- _**version**_: The string indicates the application version of the task to instantiate.
  If not provided, the current version is used. Refer to the [version management](../versioning/index.md)
  page for more details.
- _**skippable**_: Boolean attribute indicating if a task execution can be skipped when all output
  data nodes are up-to-date. Default value: `False`.

!!! Example

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

A task can also be retrieved from a scenario or a pipeline, by accessing the task config_id attribute.

```python linenums="1"
task_1 = scenario.predicting
pipeline = scenario.sales
task_2 - pipeline.predicting
# task_1 == task_2
```

All the jobs can be retrieved using the method `taipy.get_tasks()^`.

# Get parent scenarios and pipelines

To access the parent entities of a task (scenarios or pipelines), you can
use either the method `Task.get_parents()^` or the function
`taipy.get_parents()^`. Both return the parents of the task.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a task
    task = scenario.training_cfg

    # Retrieve the parent entities of the task. The returned value is
    # {'scenarios': [Scenario 1], 'pipelines': [Pipeline 1]}
    parent_entities = task.get_parents()

    # Retrieve the parent entities of the task. The return value is
    # {'scenarios': [Scenario 1], 'pipelines': [Pipeline 1]}
    tp.get_parents(task)
    ```

[:material-arrow-right: The next section shows the data node management](data-node-mgt.md).
