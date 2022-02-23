This documentation focuses on providing necessary information to use the Taipy core features, and in particular
the capabilities related to scenario management. It is assumed that the reader already knows the [Taipy core
concepts](user_core_concepts.md) described in a previous documentation.

It is also assumed in the next sections that `my_config.py` module contains a Taipy configuration already implemented
with the following python code:

```python linenums="1"
import taipy as tp
from taipy import Frequency
from taipy import Scope
from my_functions import train, predict, plan

# Configure all six data nodes
sales_history_cfg = tp.configure_data_node(name="sales_history", scope=Scope.GLOBAL, storage_type="csv", path="my/file/path.csv")
trained_model_cfg = tp.configure_data_node(name="trained_model", scope=Scope.CYCLE)
current_month_cfg = tp.configure_data_node(name="current_month", scope=Scope.CYCLE, default_data=datetime(2020,1,1))
sales_predictions_cfg = tp.configure_data_node(name="sales_predictions", scope=Scope.CYCLE)
capacity_cfg = tp.configure_data_node(name="capacity", scope=Scope.SCENARIO)
production_orders_cfg = tp.configure_data_node(name="production_orders", scope=Scope.SCENARIO, storage_type="sql",
                                               db_username="admin",
                                               db_password="ENV[PWD]",
                                               db_name="production_planning",
                                               db_engine="mssql",
                                               read_query="SELECT * from production_order",
                                               write_table="production_order")

# Configure the three tasks
training_cfg = tp.configure_task(name="training", inputs=sales_history_cfg, train, outputs=[trained_model_cfg])
predicting_cfg = tp.configure_task(name="predicting", inputs=[trained_model_cfg, current_month_cfg], predict, outputs=sales_predictions_cfg)
planning_cfg = tp.configure_task(name="planning", inputs=[sales_predictions_cfg, capacity], plan, outputs=[production_orders_cfg])

# Configure the two pipelines
sales_pipeline_cfg = tp.configure_pipeline(name="sales", tasks=[training_cfg, predicting_cfg])
production_pipeline_cfg = tp.configure_pipeline(name="production", tasks=[planning_cfg])

# Configure the scenario
monthly_scenario_cfg = tp.configure_scenario(name="scenario_configuration",
                                             pipelines=[sales_pipeline_cfg, production_pipeline_cfg])
                                             frequency=Frequency.MONTHLY)
```

The previous configuration corresponds to the design displayed in the following picture.

![scenarios](scenarios.svg)

Please refer to the [configuration documentation](user_core_configuration.md) to have information
on how to configure a Taipy application.

# Create a Scenario

Scenarios are the most used entities in Taipy. The [`taipy.create_scenario`](../../reference/#taipy.create_scenario)
can be used to create a new scenario.

This function creates and returns a new scenario from the scenario configuration
provided as a parameter. The scenario's creation also triggers the creation of the related entities that
do not exist yet. Indeed, if the scenario has a frequency, the corresponding cycle is created if
it does not exist yet. Similarly, the pipelines, tasks, and data nodes nested in the scenario are created
if they do not exist yet.

The simplest way of creating a scenario is to call the `create_scenario` methods providing the scenario
configuration as a parameter:

```python linenums="1"
import taipy as tp
from config import *

tp.create_scenario(monthly_scenario_cfg)
```

Three parameters can be given to the scenario creation method :

-   `config` is a mandatory parameter of type
    [`ScenarioConfig`](../../reference/#taipy.config.scenario_config.ScenarioConfig). It corresponds to a scenario
    configuration (created in the config.py module)
-   `creation_date` is an optional parameter of type datetime.datetime. It corresponds to the creation date of
    the scenario. If the parameter is not provided, the current date-time is used by default.
-   The `name` parameter is optional as well. Any string can be provided as a `name`. It can be used to display
    the scenario in a user interface.

!!! Example

Using the config.py module here is an example of how to create a scenario.

```python linenums="1"
    import taipy as tp
    from config import *
    from datetime import datetime

    scenario = tp.create_scenario(monthly_scenario_cfg, creation_date=datetime(2022, 1, 1), name="Scenario for January")
```

On this small example, one scenario for January is instantiated. Behind the scene, the other related entities are
also created:

-   The January cycle,
-   Two sales and production pipelines,
-   Three tasks (training, predicting, planning),
-   And six data nodes (sales_history, trained_model, current_month, sales_predictions, capacity, production_orders).

# Scenario and cycle Management

## Scenario attributes

The scenario creation method returns a [`Scenario`](../../reference/#taipy.Scenario) entity. It is identified by
a unique identifier named `id` that is generated by Taipy.
A scenario also holds various properties accessible as an attribute of the scenario:

-   `scenario.config_name` is the name of the scenario configuration.
-   `scenario.creation_date` corresponds to the date-time provided at the creation.
-   `scenario.is_master` equals True if it is a master scenario. False otherwise.
-   `scenario.subscribers` is the list of callbacks representing the subscribers.
-   `scenario.properties` is the complete dictionary of the scenario properties. It includes a copy of
    the properties of the scenario configuration, in addition to the properties provided at the creation and at runtime.
-   `scenario.cycle` is the cycle of the scenario.
-   `scenario.pipelines` is a dictionary holding the various pipelines of the scenario. The key corresponds
    to the config_name of the pipeline while the value is the pipeline itself.
-   Each property of the `scenario.properties` dictionary is also directly exposed as an attribute.
-   Each nested entity is also exposed as an attribute of the scenario. the attribute name corresponds to the config_name
    of the nested entity.

!!! Example

```python linenums="1"
    import taipy as tp
    from datetime import datetime
    from config import *

    scenario = tp.create_scenario(monthly_scenario_cfg, creation_date=datetime(2022, 1, 1), name="Scenario for January")

    # the config_name is an attribute of the scenario and equals "scenario_configuration"
    scenario.config_name
    # The creation date is the date-time provided at the creation. It equals datetime(2022, 1, 1)
    scenario.creation_date
    # Is_master property equals `True` since it is the only scenario of the cycle.
    scenario.is_master
    # There was no subscription, so subscribers is an empty list
    scenario.subscribers # []
    # The properties dictionary equals {"name": "Scenario for January"}. It contains all the properties,
    # including the `name` provided at the creation
    scenario.properties # {"name": "Scenario for January"}
    # The `name` property is also exposed directly as an attribute. It equals "Scenario for January"
    scenario.name
    # the sales pipeline entity is exposed as an attribute of the scenario
    sales_pipeline = scenario.sales
    # the production pipeline entity as well
    production_pipeline = scenario.production
    # All the tasks are also exposed as attributes, including the training task entity
    training_task = scenario.training
    # The six data nodes are also exposed as attributes of the scenario.
    current_month_data_node = scenario.current_month
```

Taipy exposes multiple methods to manage the various scenarios.

## Get scenario by id

The first method to get a scenario is from its id by using the [`taipy.get`](../../reference/#taipy.get) method :

```python linenums="1"
import taipy as tp
from config import *

scenario = tp.create_scenario(monthly_scenario_cfg)
scenario_retrieved = tp.get(scenario.id)
scenario == scenario_retrieved
```

On the previous code, the two variables `scenario` and `scenario_retrieved` are equals.

## Get all scenarios

All the scenarios can be retrieved using the method [`taipy.get_scenarios`](../../reference/#taipy.get_scenarios).
This method returns the list of all existing scenarios. If a cycle is given as parameter, the list contains all the
existing scenarios of the cycle.

## Get master scenarios

[`taipy.get_master`](../../reference/#taipy.get_master) method returns the master scenario of the cycle given as
parameter.

[`taipy.get_all_masters`](../../reference/#taipy.get_all_masters) returns the master scenarios for all the existing
cycles.

## Promote a scenario as master

To set a scenario as master, the [`taipy.set_master`](../../reference/#taipy.set_master) method must be used. It
promotes the scenario given as parameter to the master scenario of its cycle. If the cycle already had a master
scenario it will be demoted, and it will no longer be master for the cycle.

## Delete a scenario

A scenario can be deleted by using [`taipy.delete_scenario`](../../reference/#taipy.delete_scenario) which takes the scenario id as a parameter. The deletion is also propagated to the nested pipelines, tasks, data nodes, and jobs if they are not shared with any other scenario.

# Pipeline Management

## Pipeline attributes

The pipeline creation method returns a [`Pipeline`](../../reference/#taipy.Pipeline) entity. It is identified by
a unique identifier named `id` that is generated by Taipy.
A pipeline also holds various properties accessible as an attribute of the pipeline:

-   `pipeline.config_name` is the name of the pipeline configuration.
-   `pipeline.subscribers` is the list of callbacks representing the subscribers.
-   `pipeline.properties` is the complete dictionary of the pipeline properties. It includes a copy of the properties of the pipeline configuration, in addition to the properties provided at the creation and at runtime.
-   `pipeline.tasks` is a dictionary holding the various tasks of the pipeline. The key corresponds to the config_name of the task while the value is the task itself.
-   `pipeline.parent_id` is the identifier of the parent, which can be a pipeline, scenario, cycle or None.
-   Each property of the `pipeline.properties` dictionary is also directly exposed as an attribute.
-   Each nested entity is also exposed as an attribute of the pipeline. the attribute name corresponds to the config_name
    of the nested entity.

!!! Example

```python linenums="1"
    import taipy as tp
    from datetime import datetime
    from config import *

    pipeline = tp.create_pipeline(sales_pipeline_cfg,name="Pipeline for sales prediction")

    # the config_name is an attribute of the pipeline and equals "pipeline_configuration"
    pipeline.config_name
    # There was no subscription, so subscribers is an empty list
    pipeline.subscribers # []
    # The properties dictionary equals {"name": "Pipeline for sales prediction"}. It contains all the properties,
    # including the `name` provided at the creation
    pipeline.properties # {"name": "Pipeline for sales prediction"}
    # The `name` property is also exposed directly as an attribute. It equals "Pipeline for sales prediction"
    pipeline.name
    # the training task entity is exposed as an attribute of the pipeline
    training_task = pipeline.training
    # the predicting task entity as well
    predicting_task = pipeline.predicting
    # All the tasks are also exposed as attributes, including the training task entity
    training_task = pipeline.training
    # The data nodes are also exposed as attributes of the pipeline.
    current_month_data_node = pipeline.current_month
```

## Get pipeline by id

The method to get a pipeline is from its id by using the [`taipy.get`](../../reference/#taipy.get) method :

```python linenums="1"
import taipy as tp
from config import *

pipeline = tp.create_pipeline(sales_pipeline_cfg)
pipeline_retrieved = tp.get(pipeline.id)
pipeline == pipeline_retrieved
```

On the previous code, the two variables `pipeline` and `pipeline_retrieved` are equals.

## Get pipeline by config name

A pipeline can also be retrieved from a scenario by accessing the pipeline {config_name} of the scenario.

```python linenums="1"
# Configure the two pipelines
sales_pipeline_cfg = tp.configure_pipeline(name="sales", tasks=[training_cfg, predicting_cfg])
production_pipeline_cfg = tp.configure_pipeline(name="production", tasks=[planning_cfg])

# Configure and create the scenario
monthly_scenario_cfg = tp.configure_scenario(name="scenario_configuration",             pipelines=[sales_pipeline_cfg, production_pipeline_cfg]))
scenario = tp.create_scenario(monthly_scenario_cfg)

# Get the pipelines by config name
sales_pipeline = scenario.sales
production_pipeline = scenario.production
```

## Get all pipelines

All the pipelines can be retrieved using the method [`taipy.get_pipelines`](../../reference/#taipy.get_pipelines).
This method returns the list of all existing pipelines.

## Delete a pipeline

A pipeline can be deleted by using [`taipy.delete_pipeline`](../../reference/#taipy.delete_pipeline) which takes the pipeline id as a parameter. The deletion is also propagated to the nested tasks, data nodes, and jobs if they are not shared with any other pipeline.

# Scheduling and execution

## Submit a scenario or pipeline

=> tp.submit

## Jobs attributes

=> all attributes and properties

## Subscribe a scenario or pipeline

=> tp.subscribe_scenario

=> tp.subscribe_pipeline

=> tp.unsubscribe_scenario

=> tp.unsubscribe_pipeline

## Get jobs

The first method to get a job is from its id by using the [`taipy.get`](../../reference/#taipy.get) method :

```python linenums="1"
import taipy as tp
from config import *

job = tp.get(job_id)
# job == job_retrieved
```

On the previous code, the two variables `job` and `job_retrieved` are equals.

All the jobs can be retrieved using the method [`taipy.get_jobs`](../../reference/#taipy.get_jobs).

The latest job of a task can be retrieved using the method [`taipy.get_latest_job`](../../reference/#taipy.get_latest_job).

## Delete jobs

A job can be deleted using the method [`taipy.delete_job`](../../reference/#taipy.delete_job). If the job is not finished, an exception will be thrown. Setting the "force" parameter to True will force the deletion of the job.

All jobs can be deleted using the method [`taipy.delete_jobs`](../../reference/#taipy.delete_jobs). The deletion is forced by default.

# Task Management

## Task attributes

The task creation method returns a [`Task`](../../reference/#taipy.Task) entity. It is identified by a unique identifier named `id` that is generated by Taipy.
A task also holds various properties accessible as an attribute of the task:

-   `task.config_name` is the name of the scenario configuration.
-   `task.function` is the function that will take data from input data nodes and return data that should go inside of the output data nodes .
-   `task.input` is the list of input data nodes.
-   `task.output` is the list of output data nodes.

!!! Example

```python linenums="1"
import taipy as tp
from config import *

scenario = tp.create_scenario(monthly_scenario_cfg)
task = scenario.predicting

# the config_name is an attribute of the task and equals "task_configuration"
task.config_name

# the function which is going to be executed with input data nodes and return value on output data nodes.
task.function # predict

# input is the list of input data nodes of the task
task.input # [trained_model_cfg, current_month_cfg]

# output is the list of input data nodes of the task
task.output # [trained_model_cfg]

# the current_month data node entity is exposed as an attribute of the task
current_month_data_node = task.current_month
```

Taipy exposes multiple methods to manage the various tasks.

## Get Tasks

The first method to get a job is from its id by using the [`taipy.get`](../../reference/#taipy.get) method

```python linenums="1"
import taipy as tp
from taipy.core.scheduler.scheduler import Scheduler
from config import *

scenario = tp.create_scenario(monthly_scenario_cfg)
task = scenario.predicting
task_retrieved = tp.get(task)
# task == task_retrieved
```

On the previous code, the two variables `task` and `task_retrieved` are equals.

A task can also be retrieved from a scenario or a pipeline, by accessing the task config_name attribute.

```python linenums="1"
    task_1 = scenario.predicting
    pipeline = scenario.sales
    task_2 - pipeline.predicting
    # task_1 == task_2
```

All the jobs can be retrieved using the method [`taipy.get_tasks`](../../reference/#taipy.get_tasks).

# Data node Management

## Data node attributes

The data node creation method returns a [`Data Node`](../../reference/#taipy.DataNode) entity. It is identified by
a unique identifier named `id` that is generated by Taipy.
A pipeline also holds various properties and attributes that are accessible through the entity:
-   `datanode.config_name` is the name that identifies the data node.
-   `datanode.scope` the scope of this datanode (scenario, pipeline, etc)
-   `datanode.id` the unique identifier of this datanode
-   `datanode.name` the user-readable name if the data node
-   `datanode.parent_id` identifier of the parent (pipeline_id, scenario_id, cycle_id) or `None`
-   `datanode.last_edition_date` date and time of the last edition
-   `datanode.job_ids` ordered list of jobs that have written on this datanode
-   `datanode.validity_days` number of days to be added to the data node validity duration
-   `datanode.validity_hours` number of hours to be added to the data node validity duration
-   `datanode.validity_minutes` number of minutes to be added to the data node validity duration
-   `datanode.edition_in_progress` flag that signals if a task is currently computing this data node
-   `datanode.properties` dict of additional arguments


## Get data node

The first method to get a **datanode** is from its id using the `taipy.get` method:

!!! Example
```python linenums="1"
import taipy as tp


# Retrieve a datanode by its id
datanode = tp.get(datanode_id)

```

The datanodes that are part of a **scenario** or **pipeline** can be directly accessed on their levels:

!!! Example
```python linenums="1"
import taipy as tp
from config import *

# Creating a scenario from a config 
scenario = tp.create_scenario(monthly_scenario_cfg)

# Access the datanode from a scenario
scenario.sales_history

# Access the pipeline from a scenario
scenario.sales

# Access the datanode from a pipeline
scenario.sales.sales_history

```


All the datanodes can be retrieved using the method `taipy.get_data_nodes`. This methdod returns a list of all existing datanodes.

!!! Example
```python linenums="1"
import taipy as tp


# Retrieve a datanode by its id
datanodes = tp.get_data_nodes()

datanodes #[DataNode 1, DataNode 2, ..., DataNode N]

```

## Read data node

To read the content of a datanode you can use the `datanode.read()` method. The read method returns the data stored on the datanode according to the type of datanode:

!!! Example
```python linenums="1"
import taipy as tp


# Retrieve a datanode by its id
datanode = tp.get(datanode_id)

# Returns the content stored on the datanode
datanode.read()
```


Is also possible to read partially the contents of datanode, usefull when dealing with large ammounts of data. This can be achieve using the `datanode.filter()` method:

```python linenums="1"
datanode.filter([('field_name_like_temperature', 14, Operator.EQUAL), ('field_name_like_temperature', 10, Operator.EQUAL)], JoinOperator.OR))
```
Is also posible to use pandas style filtering:

```python linenums="1"
temp_data = datanode['field_name_like_temperature']
temp_data[(temp_data == 14) | (temp_data == 10)]
```

## Write data node

To write some data on the datanode, like the output of a task, you can use the `datanode.write()` method. The method takes an data object (string, dictionary, lists, numpy arrays, pandas dataframes, etc) as a parameter and writes it on the datanode:

!!! Example
```python linenums="1"
import taipy as tp


# Retrieve a datanode by its id
datanode = tp.get(datanode_id)

data = [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]

# Writes the dictionary on the datanode
datanode.write(data)

# returns the new data stored on the datanode
datanode.read()
```