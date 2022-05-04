In the following, it is assumed that [`my_config.py`](../my_config.py) module contains a Taipy configuration
already implemented.

Data nodes get created when scenarios or pipelines are created. Please refer to the
[Entities' creation](scenario-creation.md) section for more details.

# Data node attributes

A `DataNode^` entity is identified by a unique identifier `id` that Taipy generates.
A data node also holds various properties and attributes accessible through the entity:

-   _**config_id**_: The id of the data node config.
-   _**scope**_: The scope of this data node (scenario, pipeline, etc.).
-   _**id**_: The unique identifier of this data node.
-   _**name**_: The user-readable name of the data node.
-   _**parent_id**_: The identifier of the parent (pipeline_id, scenario_id, cycle_id) or `None`.
-   _**last_edition_date**_: The date and time of the last edition.
-   _**job_ids**_: The ordered list of jobs that have written on this data node.
-   _**validity_period**_: The validity period of a cacheable data node. If _validity_period_ is set to None, the
    data node is always up-to-date.
-   _**edition_in_progress**_: The flag that signals if a task is currently computing this data node.
-   _**properties**_: The dictionary of additional arguments.

# Get data node

The first method to get a **data node** is from its id using the `taipy.get()^` method:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    data_node = scenario.sales_history
    data_node_retrieved = scenario.sales_history
    data_node = tp.get(data_node.id)
    # data_node == data_node_retrieved
    ```

The data nodes that are part of a **scenario**, **pipeline** or **task** can be directly accessed as attributes:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Access the data node 'sales_history' from the scenario
    scenario.sales_history

    # Access the pipeline 'sales' from the scenario and then access the data node 'sales_history' from the pipeline
    pipeline = scenario.sales
    pipeline.sales_history

    # Access the task 'training' from the pipeline and then access the data node 'sales_history' from the task
    task = pipeline.training
    task.sales_history
    ```

All the data nodes can be retrieved using the method `taipy.get_data_nodes()^` which returns a list of all existing
data nodes.

!!! Example

    ```python linenums="1"
    import taipy as tp

    # Retrieve all data nodes
    data_nodes = tp.get_data_nodes()

    data_nodes #[DataNode 1, DataNode 2, ..., DataNode N]
    ```

# Read data node

To read the content of a data node you can use the `DataNode.read()^` method. The read method returns the data
stored on the data node according to the type of data node:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a data node
    data_node = scenario.sales_history

    # Returns the content stored on the data node
    data_node.read()
    ```

It is also possible to partially read the contents of data nodes, which comes in handy when dealing with large amounts
of data.
This can be achieved by providing an operator, a Tuple of (*field_name*, *value*, *comparison_operator*),
or a list of operators to the `DataNode.filter()^` method:

```python linenums="1"
data_node.filter([("field_name", 14, Operator.EQUAL), ("field_name", 10, Operator.EQUAL)], JoinOperator.OR))
```

If a list of operators is provided, it is necessary to provide a join operator that will be
used to combine the filtered results from the operators.

It is also possible to use pandas style filtering:

```python linenums="1"
temp_data = data_node["field_name"]
temp_data[(temp_data == 14) | (temp_data == 10)]
```

# Write data node

To write some data on the data node, like the output of a task, you can use the `DataNode.write()^` method. The
method takes a data object (string, dictionary, lists, numpy arrays, pandas dataframes, etc.) as a parameter and
writes it on the data node:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a data node
    data_node = scenario.sales_history

    data = [{"product": "a", "qty": "2"}, {"product": "b", "qty": "4"}]

    # Writes the dictionary on the data node
    data_node.write(data)

    # returns the new data stored on the data node
    data_retrieved = data_node.read()
    ```

[:material-arrow-right: The next section shows the scheduling and job execution](scheduling-and-job-execution.md).
