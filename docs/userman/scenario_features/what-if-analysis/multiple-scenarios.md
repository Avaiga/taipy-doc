This section explains how to create multiple *scenarios* with Taipy.

Supporting multiple scenarios with alternative datasets or parameter sets allows you to:

- **Experiment:** Perform A/B testing or compare model performance across different
    assumptions or conditions.
- **Monitor over time:** Monitor over time your data, results or KPIs.
- **Track Changes:** Keep a history of data for audit and rollback purposes.
- **Facilitate Collaboration:** Enable different teams to work on various datasets
    without interference.

# Creating multiple Scenarios

To instantiate alternative data nodes, you need to use multiple *scenarios*. A `Scenario^` is
instantiated from a `ScenarioConfig^`, which encapsulates `DataNodeConfig^` configurations.
When a scenario is instantiated, data nodes are also created.

To create multiple scenarios with alternative data nodes, you need to:

1. Configure the data nodes using the various `Config.configure_data_node()^` methods.<br>

2. Configure the scenarios with the data node configurations using the
    `Config.configure_scenario()^` method.<br>

    ??? note "Scenarios with Tasks"

        Note that when scenarios require data processing, you can add task configurations to your
        `ScenarioConfig^`. Configuring scenarios with task configurations automatically
        adds the input and output data node configurations.<br>
        For more details, see the [task orchestration](../task-orchestration/scenario-config.md)
        page.

3. Instantiate multiple scenarios using `create_scenario()^` function. The alternative
    data nodes (and tasks) are created along with the new scenarios.


# Example

The code example above aims at configuring a `ScenarioConfig^` to instantiate scenarios.
The scenario configuration is designed to model a business problem where sales
history is used to train a model and make sales forecasts. The forecasts are then used
to plan production orders constrained by the available capacity.

```python linenums="1"
{%
include-markdown "./code-example/multiple-scenarios/sales-forecasts-and-prod-orders.py"
comments=false
%}
```

As you can see in the example, the various data nodes are configured and passed as parameters
to the `Config.configure_scenario()` method to create a scenario configuration. The scenario
configuration is then used to instantiate three scenarios.

??? note "Scenario with Tasks"

    To simplify the example, we only have additional data node configurations. No data
    processing is presented in this example.<br>
    However we could have added three data processing functions using task configurations.
    One to train the monthly model based on the historical data, one to predict sales based
    on the current month and the trained model, and one to plan the production orders based
    on the capacity and the predictions.<br>
    For more details, see the [task orchestration](../task-orchestration/scenario-config.md)
    page.

## Data node configuration

The default way of configuring a data node is through the `Config.configure_data_node()^` method.
It returns a `DataNodeConfig^` object. This is the standard way when there is no constraint on
the data storage format. As you can see in the example, some data nodes are configured using
other methods like `Config.configure_csv_data_node()^` or `Config.configure_sql_data_node()^`.
These methods are designed to facilitate the configuration when the data format is constrained.
Most of the time, the format is constraint by a third party component that you need to integrate
with. Many predefined data nodes are available in Taipy. For more details, see the
[data node configuration](../data-integration/data-node-config.md) page.

## Scenario configuration

Once you have all your data nodes configurations `DataNodeConfig`, you can configure your
scenarios. The `Config.configure_scenario()^` method takes the data node configurations as
parameter and returns the scenario configuration `ScenarioConfig^`.

??? note "Configure scenarios from task configurations"

    For simplicity purpose, we only consider scenario configurations made of additional
    data node configurations. Note that you can also add data node configurations along
    with task configurations if your scenario use case require some data processingneeded.<br>
    For more details, see the [task orchestration](../task-orchestration/scenario-config.md)
    page.

For more details on the various way of creating a scenario configuration, see the
[scenario configuration](../sdm/scenario/scenario-config.md) page.

## Scenario Creations

Finally, using a `ScenarioConfig^` object, you can create multiple scenarios and set the data
for each scenario. The `create_scenario()^` function is used to instantiate the scenarios.

The example above demonstrates how to create different scenarios from the same configuration.
Three scenarios are created and different data are set to their data nodes (such as the
current_month and the capacity). This allows you to model and analyze different business
conditions or what-if scenarios. Each scenario is independent of the others. You can use the
utility methods provided by Taipy to access, read, write, compare, and manage data nodes and
scenarios.
For more details, see the [scenario](../sdm/scenario/index.md) and
[data node](../sdm/data-node/index.md) pages.

!!! important "User Interface"

    Note that the scenarios are created and edited programmatically in this example. A Taipy
    user interface is often used to let end-users create their own scenarios and set the data.
    In particular, the visual elements
    [scenario selector](../../../refmans/gui/viselements/corelements/scenario_selector.md),
    [scenario viewer](../../../refmans/gui/viselements/corelements/scenario.md),
    [data node selector](../../../refmans/gui/viselements/corelements/data_node_selector.md), and
    [data node viewer](../../../refmans/gui/viselements/corelements/data_node.md) are designed to facilitate
    the creation and management of scenarios.

