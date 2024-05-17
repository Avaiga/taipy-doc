In Taipy, managing multiple alternative data nodes is essential for use cases where
data evolves over time, experiments need to be conducted with different datasets or
parameter sets, or when data needs to be preserved for auditing and comparison purposes.

This functionality is seamlessly integrated into Taipy's data management framework
thanks to *scenarios* and data node *scopes*.

# Why creating multiple alternative data nodes?
Supporting multiple alternative datasets allows you to:

- **Track Changes:** Keep a history of data changes for audit and rollback purposes.
- **Experiment:** Perform A/B testing or compare model performance across different
    datasets or different parameter sets.
- **Ensure Consistency:** Maintain data integrity and consistency across different
    scenarios and cycles.
- **Facilitate Collaboration:** Enable different teams to work on various datasets
    without interference.

# What is a Scenario?
A `Scenario^` in Taipy represents an instance of a business problem. Among other features
scenarios own data nodes. Two different scenarios can own two alternative data nodes (from the
same `DataNodeConfig^`), allowing users to run and manage different workflows independently
each one based on a different data version.

*Scenarios* can can be used for what-if analysis, A/B testing, and comparing
different business strategies over specific time periods (called `Cycle^`) or conditions.

For more details on scenarios, please refer to the [Scenario Management](../scenario-mgt)
documentation.

# What is a Scope?

Taipy allows you to instantiate multiple alternative data nodes from the same `DataNodeConfig^`
by leveraging the `Scope^` concept. This approach helps in managing data nodes efficiently
avoiding duplicating data when it is not necessary by re-using existing data nodes or
creating alternative data nodes when needed.

The *scope* is defined as an attribute of the `DataNodeConfig^` and determines how the
data nodes instantiated from the configuration are shared or re-used across different scenarios.
The *scope* can be set to one of the following values:

- `Scope.GLOBAL`: Only one data node instance can be created from a configuration with a `GLOBAL`
    scope. All scenarios share the unique data node. When a new scenario is created, the
    data node is created if and only if it does not exist yet.
- `Scope.CYCLE`: Only one instance of a data node from a `DataNodeConfig^` with a `CYCLE` scope is
    created for each cycle. All scenarios within the same cycle share the same data node. When a
    new scenario is created within a cycle, a new data node is instantiated if and only if it
    does not already exist for the cycle.
- `Scope.SCENARIO`: A data node with a `SCENARIO` scope is unique to a single scenario. Each scenario
    has its own instance of the data node. When creating a new scenario, data nodes with a `SCENARIO`
    scope are created along with the new scenario.

By configuring the scope appropriately, you can control how your data nodes are created or
re-used by scenarios.

# Creating Scenarios and alternative data nodes

To create alternative data nodes with different scopes, you need to use *scenarios*.
A `Scenario^` is instantiated from a `ScenarioConfig^`, which encapsulates `DataNodeConfig^`
configurations with their defined scopes. When a scenario is instantiated, data nodes are created
or reused depending on the scope of their DataNodeConfig.

To create alternative data nodes with different scopes, you need to:
1. Configure the data nodes with the desired scopes using the various `Config.configure_data_node()^` methods.
2. Configure the scenarios with the data node configurations using the `Config.configure_scenario()^` method.
3. Instantiate multiple scenarios using `create_scenario()^` function to create alternative data nodes
    with different scopes.

## Example

Let's consider a simple example where a company wants to predict its sales for the next month.
The company has a trained model that predicts sales based on the current month and historical
sales data. Based on the sales forecasts, the company wants to plan its production orders.
The company wants to simulate two scenarios every month: one with low capacity and one with
high capacity.

We can have the following:

- One data node for the historical sales with a `GLOBAL` scope.
- Three data nodes with a `CYCLE` scope for the trained model, the current month, and the sales predictions.
- Two data nodes with a `SCENARIO` scope for the capacity and the production orders.

The following code snippet shows how to configure the data nodes with different scopes:

```python
from taipy import Config, Frequency, Scope
import taipy as tp
from datetime import datetime

# Configure data nodes with different scopes
hist_cfg = Config.configure_csv_data_node("sales_history", scope=Scope.GLOBAL)
model_cfg = Config.configure_data_node("trained_model", scope=Scope.CYCLE)
month_cfg = Config.configure_data_node("current_month", scope=Scope.CYCLE)
predictions_cfg = Config.configure_data_node("sales_predictions", scope=Scope.CYCLE)
capacity_cfg = Config.configure_data_node("capacity", scope=Scope.SCENARIO)
orders_cfg = Config.configure_sql_data_node("production_orders",
                                            scope=Scope.SCENARIO,
                                            db_name="taipy",
                                            db_engine="sqlite",
                                            table_name="sales")

# Configure scenarios
scenario_cfg = Config.configure_scenario("scenario", frequency=Frequency.MONTHLY, additional_data_node_configs=[
    hist_cfg,
    model_cfg,
    month_cfg,
    predictions_cfg,
    capacity_cfg,
    orders_cfg])

# Instantiate three scenarios
jan_scenario_high = tp.create_scenario(scenario_cfg, creation_date=datetime(2024, 1, 1))
jan_scenario_low = tp.create_scenario(scenario_cfg, creation_date=datetime(2024, 1, 1))
feb_scenario_low = tp.create_scenario(scenario_cfg, creation_date=datetime(2024, 2, 1))
```

In this example, the historical sales data node is shared across all scenarios, while the
trained model, current month, and sales predictions data nodes are unique to each cycle.
The capacity and production orders data nodes are unique to each scenario.

Once the data nodes are configured, you can configure a scenario. The `Config.configure_scenario()^`
method allows you to specify the frequency of the scenario and the data node configurations.

The `create_scenario()^` function is then used to instantiate the scenarios. Three scenarios are
created in this example with two cycles: two scenarios for the January cycle, and one for February cycle.
Along with the scenarios, a total of thirteen data nodes are created:
- one unique sales_history data node,
- two (one per cycle) trained_model, two current_month, and two sales_predictions data nodes,
- three (one per scenario) capacity, and three production_orders data nodes.

By using scenarios and scopes, you can manage alternative data nodes efficiently. You can use
the utility methods provided by Taipy to access, read, write, and manage data nodes.
For more details, see the [data node usage](data-node-usage.md) page.
