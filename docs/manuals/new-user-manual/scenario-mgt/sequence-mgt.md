The [Entities' creation](scenario-creation.md) section provides documentation on `Sequence^` creation. Now
that we know how to create a new `Sequence^`, this section focuses on describing the sequence's attributes
and utility methods.

In this section, it is assumed that the <a href="../code-example/my_config.py" download>`my_config.py`</a>
module contains an already implemented configuration.

# Sequence attributes

A sequence is identified by a unique identifier `id` that Taipy generates. A sequence also holds
various properties accessible as an attribute of the sequence:

add data_nodes, parent_ids

- _**subscribers**_: The list of Tuples (callback, params) representing the subscribers.
- _**properties**_: The complete dictionary of the sequence properties. It includes a copy of the properties of
  the sequence configuration, in addition to the properties provided at the creation and runtime.
- _**tasks**_: The dictionary holds the sequence's various tasks. The key corresponds to the config_id of the
  task while the value is the task itself.
- _**data_nodes**_: The dictionary holding the various data nodes of the sequence. The key corresponds to the
    data node's _config_id_ (while the value is the data node itself).
- _**owner_id**_: The identifier of the owner, which can be a scenario, cycle, or None.
- _**version**_: The string indicates the application version of the sequence to instantiate. If not provided,
  the current version is used. For more details, refer to [version management](../versioning/index.md).
- Each property of the _**properties**_ dictionary is also directly exposed as an attribute.
- Each nested entity is also exposed as an attribute of the sequence. The attribute name corresponds to the
  *config_id* of the nested entity.

!!! example

    ```python linenums="1"
    import taipy as tp
    from datetime import datetime
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg, name="Monthly scenario")
    sales_sequence = scenario.sales_sequence
    sales_sequence.name = "Sequence for sales prediction"

    # There was no subscription, so subscribers is an empty list
    sequence.subscribers # []
    # The properties dictionary equals {"name": "Sequence for sales prediction"}. It
    # contains all the properties, including the `name` provided at the creation
    sequence.properties # {"name": "Sequence for sales prediction"}
    # The `name` property is also exposed directly as an attribute. It
    # equals "Sequence for sales prediction"
    sequence.name
    # The training task entity is exposed as an attribute of the sequence
    training_task = sequence.training
    # The predicting task entity as well
    predicting_task = sequence.predicting
    # The data nodes are also exposed as attributes of the sequence.
    current_month_data_node = sequence.current_month
    ```

# Get a sequence

There are two ways to retrieve a sequence:

The first method is by getting it from its parent scenario, using the sequence name as an attribute.
The second method to access a sequence is from its id using the `taipy.get()^` method.

```python linenums="1"
import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
sequence = scenario.sales_sequence

sequence_retrieved = tp.get(sequence.id)
sequence == sequence_retrieved
```

Here the two variables `sequence` and `sequence_retrieved` are equal.

# Get all sequences

All the sequences can be retrieved using the method `taipy.get_sequences()^`. This method returns the list of all
existing sequences.

# Delete a sequence

A sequence can be deleted by using `taipy.delete()^` which takes the sequence id as a parameter. The deletion is
also propagated to the nested tasks, data nodes, and jobs if they are not shared with any other sequence.

# Get parent scenarios

To get the parent entities of a sequence (i.e., scenarios) you can use either the method `DataNode.get_parents()^` or
the function
`taipy.get_parents()^`. Both return the parents of the sequence.

!!! example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a sequence
    sequence = scenario.sales_sequence_cfg

    # Retrieve the parent entities of the sequence
    parent_entities = sequence.get_parents()  # {'scenarios': [Scenario 1]}

    # Retrieve the parent entities of the sequence
    tp.get_parents(sequence)  # {'scenarios': [Scenario 1]}
    ```

[:material-arrow-right: The next sections show the task management](task-mgt.md).
