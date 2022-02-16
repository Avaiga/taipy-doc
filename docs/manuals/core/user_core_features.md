This documentation focuses on providing necessary information to use the Taipy core features, and in particular
the capabilities related to scenario management. It is assumed that the reader already knows the [Taipy core
concepts](user_core_concepts.md) described in a previous documentation.

It is also assumed in the next sections that `my_config.py` module contains a Taipy configuration already implemented
with the following python code:

````python linenums="1"
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
````

The previous configuration corresponds to the design displayed in the following picture.

![scenarios](scenarios.svg)

Please refer to the [configuration documentation](user_core_configuration.md) to have information
on how to configure a Taipy application.

# Create a Scenario

Scenarios are the most used entities in Taipy. The [`taipy.create_scenario`](../../reference/#taipy.create_scenario)
can be used to create a new scenario.

This function creates and returns a new scenario from the scenario configuration
provided as a parameter. The scenario's creation also triggers the creation of the related entities that
do not exist yet.  Indeed, if the scenario has a frequency, the corresponding cycle is created if
it does not exist yet. Similarly, the pipelines, tasks, and data nodes nested in the scenario are created
if they do not exist yet.

The simplest way of creating a scenario is to call the `create_scenario` methods providing the scenario
configuration as a parameter:
````python linenums="1"
import taipy as tp
from config import *

tp.create_scenario(monthly_scenario_cfg)
````

Three parameters can be given to the scenario creation method :

- `config` is a mandatory parameter of type
[`ScenarioConfig`](../../reference/#taipy.config.scenario_config.ScenarioConfig). It corresponds to a scenario
configuration (created in the config.py module)
- `creation_date` is an optional parameter of type datetime.datetime. It corresponds to the creation date of
the scenario. If the parameter is not provided, the current date-time is used by default.
- The `name` parameter is optional as well. Any string can be provided as a `name`. It can be used to display
the scenario in a user interface.

!!! Example

    Using the config.py module here is an example of how to create a scenario.

    ````python linenums="1"
    import taipy as tp
    from config import *
    from datetime import datetime

    scenario = tp.create_scenario(monthly_scenario_cfg, creation_date=datetime(2022, 1, 1), name="Scenario for January")
    ````
    On this small example, one scenario for January is instantiated. Behind the scene, the other related entities are
    also created:

    - The January cycle,
    - Two sales and production pipelines,
    - Three tasks (training, predicting, planning),
    - And six data nodes (sales_history, trained_model, current_month, sales_predictions, capacity, production_orders).

# Scenario and cycle Management

## Scenario attributes

The scenario creation method returns a [`Scenario`](../../reference/#taipy.Scenario) entity. It is identified by
a unique identifier named `id` that is generated by Taipy.
A scenario also holds various properties accessible as an attribute of the scenario :

- `scenario.config_name` is the name of the scenario configuration.
- `scenario.creation_date` corresponds to the date-time provided at the creation.
- `scenario.is_master` equals True if it is a master scenario. False otherwise.
- `scenario.subscribers` is the list of callbacks representing the subscribers.
- `scenario.properties` is the complete dictionary of the scenario properties. It includes a copy of
the properties of the scenario configuration, in addition to the properties provided at the creation and at runtime.
- `scenario.cycle` is the cycle of the scenario.
- `scenario.pipelines` is a dictionary holding the various pipelines of the scenario. The key corresponds
to the config_name of the pipeline while the value is the pipeline itself.
- Each property of the `scenario.properties` dictionary is also directly exposed as an attribute.
- Each nested entity is also exposed as an attribute of the scenario. the attribute name corresponds to the config_name
of the nested entity.

!!! Example

    ````python linenums="1"
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
    ````

Taipy exposes multiple methods to manage the various scenarios.

## Get scenario by id
The first method to get a scenario is from its id by using the [`taipy.get`](../../reference/#taipy.get) method :
````python linenums="1"
import taipy as tp
from config import *

scenario = tp.create_scenario(monthly_scenario_cfg)
scenario_retrieved = tp.get(scenario.id)
scenario == scenario_retrieved
````
On the previous code, the two variables `scenario` and `scenario_retrieved` are equals.

## Get all scenarios
All the scenarios can be retrieved using the method [``taipy.get_scenarios``](../../reference/#taipy.get_scenarios).
This method returns the list of all existing scenarios. If a cycle is given as parameter, the list contains all the
existing scenarios of the cycle.

## Get master scenarios
[``taipy.get_master``](../../reference/#taipy.get_master) method returns the master scenario of the cycle given as
parameter.

[``taipy.get_all_masters``](../../reference/#taipy.get_all_masters) returns the master scenarios for all the existing
cycles.

## Promote a scenario as master

To set a scenario as master, the [``taipy.set_master``](../../reference/#taipy.set_master) method must be used. It
promotes the scenario given as parameter to the master scenario of its cycle. If the cycle already had a master
scenario it will be demoted, and it will no longer be master for the cycle.

## Delete a scenario

=> tp.delete_scenario

# Pipeline Management

## Pipeline attributes

=> list attributes and properties like scenario attributes

## Get pipeline

=> tp.get

=> scenario.pipeline_config_name

## Get all pipelines

=> tp.get_pipelines

## delete pipeline

=> tp.delete_pipeline

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

## get jobs

=> tp.get

=> tp.get_jobs

## delete jobs

=> delete_job

# Task Management

## Task attributes

=> list attributes and properties

## Get Task

=> tp.get

=> scenario.task_config_name

=> pipeline.task_config_name

## Get all tasks

=> tp.get_tasks

# Data node Management

## Data node attributes

=> list attributes and properties

## Get data node

=> tp.get

=> scenario.data_node_config_name

=> pipeline.data_node_config_name

## Get all data nodes

=> tp.get_data_nodes

## Read data node

=> data_node.read()

=> data_node.filter()

## Write data node

=> data_node.write()
