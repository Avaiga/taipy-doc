In Taipy, managing multiple alternative data nodes is essential for use cases where
data evolves over time, experiments need to be conducted with different assumptions,
when data needs to be preserved for auditing and comparison purposes.

This functionality is seamlessly integrated into Taipy's data management framework
thanks to *scenarios*.

# Why creating multiple alternative data nodes?
Supporting multiple alternative datasets allows you to:

- **Track Changes:** Keep a history of data for audit and rollback purposes.
- **Experiment:** Perform A/B testing or compare model performance across different
    datasets or different parameter sets.
- **Ensure Consistency:** Maintain data integrity and consistency across different
    scenarios and cycles.
- **Facilitate Collaboration:** Enable different teams to work on various datasets
    without interference.

# What is a Scenario?
A `Scenario^` in Taipy represents an instance of a business problem. Among other features
scenarios own data nodes. Two different scenarios can own two alternative data nodes (from the
same `DataNodeConfig^`), allowing users to evaluate different situations independently
each one based on a different assumption, data version, or parameter set.

For more details on scenarios, please refer to the [Scenario Management](../scenario-mgt/index.md)
page.

# Creating Scenarios and alternative data nodes

To create alternative data nodes, you need to use *scenarios*. A `Scenario^` is
instantiated from a `ScenarioConfig^`, which encapsulates `DataNodeConfig^` configurations.
When a scenario is instantiated, data nodes are also created.

To create alternative data nodes, you need to:
1. Configure the data nodes using the various
    `Config.configure_data_node()^` methods.<br>
    For more details, see the [data node configuration](../data-integration/data-node-config.md) page.

2. Configure the scenarios with the data node configurations as additional data nodes using
    the `Config.configure_scenario()^` method.<br>
    For more details, see the [scenario configuration](../scenario-mgt/scenario-config.md)
    page.

3. Instantiate multiple scenarios using `create_scenario()^` function to create alternative
    data nodes.<br>
    For more details, see the [scenario usage](../scenario-mgt/scenario-mgt.md)
    page.

# Example

TODO: Brief description of the example.

```python linenums="1"
{%
include-markdown "./code-example/data-node-scopes/sales-forecasts-and-prod-orders.py"
comments=false
%}
```

The code example above aims at configuring a `ScenarioConfig^` to instantiate scenarios.

## Data node configuration

The data node configurations are created with the `Config.configure_data_node()^` method.
For more details, see the [data node config](../data-integration/data-node-config.md) page.

TODO: Brief description of all the data node created in the example.

## Scenario configuration

Once the data nodes are configured, you can configure a scenario. The `Config.configure_scenario()^`
returns the scenario configuration `ScenarioConfig^`.

!!! note
    This example only have additional data node configurations. Note that you can also
    add data node configurations along with task configurations if needed.<br>
    For more details, see the [task orchestration](../task-orchestration/scenario-config.md)
    page.

## Multiple scenario Instantiations

TODO:
The `create_scenario()^` function is then used to instantiate multiple scenarios.

By using scenarios, you can manage alternative data nodes efficiently. You can use
the utility methods provided by Taipy to access, read, write, and manage data nodes.
For more details, see the [data node usage](../data-integration/data-node-usage.md) page.
