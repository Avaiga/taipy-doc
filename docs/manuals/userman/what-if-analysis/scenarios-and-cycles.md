Introduction of page

# Why using scenario with cycles?

- Motivation and advantages
- Can be used for time-based analyses like monthly forecasts, weekly results, daily reports, etc.
- Ideal for recurring business cases
- Share the same data nodes across multiple scenarios
-
# What is a Scenario?
A `Scenario^` in Taipy represents an instance of a business problem. Among other features
scenarios own data nodes. Two different scenarios can own two alternative data nodes (from the
same `DataNodeConfig^`), allowing users to run and manage different workflows independently
each one based on a different data version.

*Scenarios* can can be used for what-if analysis, A/B testing, and comparing
different business strategies over specific time periods (called `Cycle^`) or conditions.

For more details on scenarios, please refer to the
[Scenario and Data Management](../sdm/index.md)
page.

# What is a Data node Scope?

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

# What is a Cycle?

- Created from the scenario at its instantiation.

- Contains a time period with a start and end date.

- Based on the scenario creation date and its frequency

# Creating Scenarios and cycles

To create alternative data nodes with different scopes, you need to use *scenarios*.
A `Scenario^` is instantiated from a `ScenarioConfig^`, which encapsulates `DataNodeConfig^`
configurations with their defined scopes. When a scenario is instantiated, data nodes are created
or reused depending on the scope of their configurations.

To create alternative data nodes with different scopes, you need to:
1. Configure the data nodes with the desired scopes using the various
    `Config.configure_data_node()^` methods.<br>
    For more details, see the [data node configuration](../data-integration/data-node-config.md) page.

2. Configure the scenarios with the data node configurations as additional data nodes using
    the `Config.configure_scenario()^` method.<br>
    For more details, see the [scenario configuration](../sdm/scenario/scenario-config.md)
    page.

3. Instantiate multiple scenarios using `create_scenario()^` function to create alternative
    data nodes with different scopes.<br>
    For more details, see the [scenario](../sdm/scenario/index.md)
    page.

# Example

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

```python linenums="1"
{%
include-markdown "./code-example/scenarios-and-cycles/sales-forecasts-and-prod-orders.py"
comments=false
%}
```

The code example above aims at configuring a `ScenarioConfig^` to instantiate scenarios.

## Data node configuration

The data node configurations are created with the `Config.configure_data_node()^` method.
For more details, see the [data node config](../data-integration/data-node-config.md) page.

The historical sales data node is shared across all scenarios, while the
trained model, current month, and sales predictions data nodes are unique to each cycle.
The capacity and production orders data nodes are unique to each scenario.

## Scenario configuration

Once the data nodes are configured, you can configure a scenario. The `Config.configure_scenario()^`
method allows you to specify the frequency and returns the scenario configuration `ScenarioConfig^`.

!!! note
    This example only have additional data node configurations. Note that you can also
    add data node configurations along with task configurations if needed.<br>
    For more details, see the [scenario configuration](../sdm/scenario/scenario-config.md)
    page.

## Scenario Instantiation

The `create_scenario()^` function is then used to instantiate the scenarios. Three scenarios are
created in this example with two cycles: two scenarios for the January cycle, and one for February cycle.
Along with the scenarios, a total of thirteen data nodes are created:
- one unique sales_history data node,
- two (one per cycle) trained_model, two current_month, and two sales_predictions data nodes,
- three (one per scenario) capacity, and three production_orders data nodes.

By using scenarios and scopes, you can manage alternative data nodes efficiently. You can use
the utility methods provided by Taipy to access, read, write, and manage data nodes.
For more details, see the [data node usage](../data-integration/data-node-usage.md) page.
