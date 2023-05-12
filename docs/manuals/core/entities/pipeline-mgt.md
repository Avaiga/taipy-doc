The [Entities' creation](scenario-creation.md) section provides documentation on `Pipeline^` creation. Now
that we know how to create a new `Pipeline^`, this section focuses on describing the pipeline's attributes
and utility methods.

In this section, it is assumed that <a href="./code_example/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented.

# Pipeline attributes

The pipeline creation method returns a `Pipeline^` entity. It is identified by a unique identifier `id` that
Taipy generates. A pipeline also holds various properties accessible as an attribute of the pipeline:

- _config_id_: The id of the pipeline configuration.
- _subscribers_: The list of Tuples (callback, params) representing the subscribers.
- _properties_: The complete dictionary of the pipeline properties. It includes a copy of the properties of
  the pipeline configuration, in addition to the properties provided at the creation and at runtime.
- _tasks_: The dictionary holding the various tasks of the pipeline. The key corresponds to the config_id of the
  task while the value is the task itself.
- _owner_id_: The identifier of the owner, which can be a pipeline, scenario, cycle, or None.
- _**version**_: The string indicates the application version of the pipeline to instantiate. If not provided,
  the current version is used. Refer to the [version management](../versioning/index.md) page for more details.
- Each property of the _properties_ dictionary is also directly exposed as an attribute.
- Each nested entity is also exposed as an attribute of the pipeline. the attribute name corresponds to the
  *config_id* of the nested entity.

!!! Example

    ```python linenums="1"
    import taipy as tp
    from datetime import datetime
    import my_config

    pipeline = tp.create_pipeline(my_config.sales_pipeline_cfg, name="Pipeline for sales prediction")

    # The config_id is an attribute of the pipeline. Here it is "pipeline_configuration"
    pipeline.config_id
    # There was no subscription, so subscribers is an empty list
    pipeline.subscribers # []
    # The properties dictionary equals {"name": "Pipeline for sales prediction"}. It
    # contains all the properties, including the `name` provided at the creation
    pipeline.properties # {"name": "Pipeline for sales prediction"}
    # The `name` property is also exposed directly as an attribute. It
    # equals "Pipeline for sales prediction"
    pipeline.name
    # The training task entity is exposed as an attribute of the pipeline
    training_task = pipeline.training
    # The predicting task entity as well
    predicting_task = pipeline.predicting
    # The data nodes are also exposed as attributes of the pipeline.
    current_month_data_node = pipeline.current_month
    ```

# Get pipeline by id

The method to access a pipeline is from its id by using the `taipy.get()^` method :

```python linenums="1"
import taipy as tp
import my_config

pipeline = tp.create_pipeline(my_config.sales_pipeline_cfg)
pipeline_retrieved = tp.get(pipeline.id)
pipeline == pipeline_retrieved
```

Here the two variables `pipeline` and `pipeline_retrieved` are equal.

# Get pipelines by config id

A pipeline can also be retrieved from a scenario by accessing the pipeline's config_id of the scenario.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get the pipelines by config id
    sales_pipeline = scenario.sales
    production_pipeline = scenario.production
    ```

Pipelines can also be retrieved using `taipy.get_entities_by_config_id()^` providing the config_id.
This method returns the list of all existing pipelines instantiated from the config_id provided as a parameter.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create 2 scenarios, which will also create 2 sales pipelines.
    scenario_1 = tp.create_scenario(my_config.monthly_scenario_cfg)
    scenario_2 = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get all sale pipelines by config id, this will return a list of 2 sales pipelines
    # created alongside the 2 scenarios.
    all_sales_pipeline = tp.get_entities_by_config_id("sales")
    ```

# Get all pipelines

All the pipelines can be retrieved using the method `taipy.get_pipelines()^`. This method returns the list of all
existing pipelines.

# Delete a pipeline

A pipeline can be deleted by using `taipy.delete()^` which takes the pipeline id as a parameter. The deletion is
also propagated to the nested tasks, data nodes, and jobs if they are not shared with any other pipeline.

# Get parent scenarios

To get the parent entities of a pipeline (i.e., scenarios) you can use either the method `DataNode.get_parents()^` or
the function
`taipy.get_parents()^`. Both return the parents of the pipeline.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a pipeline
    pipeline = scenario.sales_pipeline_cfg

    # Retrieve the parent entities of the pipeline
    parent_entities = pipeline.get_parents()  # {'scenarios': [Scenario 1]}

    # Retrieve the parent entities of the pipeline
    tp.get_parents(pipeline)  # {'scenarios': [Scenario 1]}
    ```

[:material-arrow-right: The next sections show the task management](task-mgt.md).
