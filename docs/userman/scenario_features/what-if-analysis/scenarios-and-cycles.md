In this page, we explore the join concepts of data node scope and cycle,
to model business cases where new scenarios are created at regular intervals.

# What is a Cycle?

A `Cycle^` in Taipy is an entity designed to model a time period, such as a day, week,
month, quarter or year. Its main purpose is to organize scenarios and data nodes in a
time-based manner.

Here are the main attributes of a *cycle*:

- `name`: The name or label of the cycle.
- `start_date`: The start date of the time period the cycle represents.
- `end_date`: The end date of the time period the cycle represents.
- `frequency`: The frequency of the cycle, such as `daily`, `weekly`, `monthly`, `quarterly`,
    or `yearly`.

When instantiating a scenario with a *frequency*, the *cycle* corresponding to the scenario's
*creation date* is automatically created if it does not exist. The scenario is then attached
to the cycle.

# What is a Data node Scope?

Taipy uses the `Scope^` concept to manage data nodes efficiently, avoiding duplicating
data when it is not necessary.

The *scope* is an enumeration defined as an attribute of the `DataNodeConfig^` and determines
how the data nodes are shared or reused across scenarios.

- `Scope.GLOBAL`: A single data node instance shared by all scenarios.

- `Scope.CYCLE`: One data node instance per cycle, shared by all scenarios within the same cycle.

- `Scope.SCENARIO`: A unique data node instance for each scenario.

By configuring the *scope* appropriately, you can control how your data nodes are created or
re-used by scenarios.

# Why using scopes and cycles?

Using scenarios with cycles and data node scopes offers several benefits:

- **Time based analysis:** Taipy is ideal for time-based analyses such as daily results,
    weekly reports, monthly forecasts, or yearly planning. Each time period is modeled as
    a cycle, and each scenario is attached to a cycle.

- **Recurring business situations:**
    Scenarios with cycles are perfect for recurrent business cases. For each cycle,
    an end-user can create multiple scenarios to simulate and compare different business
    situations. This is ideal for what-if analysis, A/B testing, and comparing different
    assumptions over specific time periods. Taipy also provides the concept of a _primary_
    scenario, which is unique for a cycle. It represents the main scenario for a cycle.
    For instance, among all the simulations in a cycle, the primary scenario is the one
    to apply in production or to publish to the operational team.

- **Sharing data nodes across scenarios:**
    Thanks to the data node scope, you can share the same
    data nodes across multiple scenarios. This promotes data reuse and efficiency. For instance,
    you can have a data node with a `GLOBAL` scope that is shared across all scenarios, or a data
    node with a `CYCLE` scope that is shared across all scenarios within the same cycle.

# Creating Scenarios and cycles

The creation of cycles and alternative data nodes with different scopes is performed along with
the instantiation of *scenarios*. A `Scenario^` is instantiated from a `ScenarioConfig^`
holding a *frequency* attribute, and encapsulating the `DataNodeConfig^` configurations with their
defined scopes. When a scenario is instantiated, data nodes are created or reused depending on
the scope of their configurations.

To create cycles and alternative data nodes with different scopes, you need to:
1. Configure the data nodes with the desired scopes using the various
    `Config.configure_data_node()^` methods.

2. Configure the scenarios with a *frequency* using the `Config.configure_scenario()^` method.

3. Instantiate multiple scenarios using `create_scenario()^` function to create alternative
    data nodes with different scopes.

# Example

Let's consider a simple example where a company wants to predict its sales for the next month.
The company has a trained model that predicts sales based on the current month and historical
sales data. Based on the sales forecasts, the company wants to plan its production orders.
The company wants to simulate two scenarios every month: one with low capacity and one with
high capacity.

We can have the following:

- One data node for the historical sales with a `GLOBAL` scope.
- Three data nodes with a `CYCLE` scope for the trained model, the current month, and the
    sales predictions.
- Two data nodes with a `SCENARIO` scope for the capacity and the production orders.

The following code snippet shows how to configure the data nodes with different scopes:

```python linenums="1"
{%
include-markdown "./code-example/scenarios-and-cycles/sales-forecasts-and-prod-orders.py"
comments=false
%}
```

The code example above aims at configuring a `ScenarioConfig^` to instantiate scenarios.
As you can see, the various data nodes are configured and passed as parameters to the
`Config.configure_scenario()` method. The scenario configuration is then used to instantiate
three scenarios.

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

The data node configurations are created with the `Config.configure_data_node()^` method.

Pay a particular attention to the *scope* attribute of the data node configurations.
In this example, the historical sales data node is shared across all scenarios, while the
trained model, current month, and sales predictions data nodes are unique to each cycle.
The capacity and production orders data nodes are unique to each scenario.

For more details on how to configure data nodes, see the
[data node configuration](../data-integration/data-node-config.md) page.

## Scenario configuration

Once the data nodes are configured, you can configure a scenario. The `Config.configure_scenario()^`
method allows you to specify the *frequency* attribute and returns the scenario configuration
`ScenarioConfig^`.

??? note "Scenarios with Tasks"

    Note that when scenarios require data processing, you can add task configurations to your
    `ScenarioConfig^`. Configuring scenarios with task configurations automatically
    adds the task's input and output data node configurations.<br>
    For more details, see the [task orchestration](../task-orchestration/scenario-config.md)
    page.

For more details on the various way of creating a scenario configuration, see the
[scenario configuration](../sdm/scenario/scenario-config.md) page.

## Scenario Instantiation

The `create_scenario()^` function is then used to instantiate the scenarios. Three *scenarios*
are created in this example with two *cycles*: two scenarios for the January cycle, and one for
February cycle.

Along with the *scenarios*, a total of thirteen *data nodes* are created:

- one unique sales_history data node,
- two (one per cycle) trained_model, two current_month, and two sales_predictions data nodes,
- three (one per scenario) capacity, and three production_orders data nodes.

This allows you to efficiently model and analyze recurrent scenarios on different time period.
Multiple scenarios can be created on the same cycle or on different cycles. Each scenario is
independent of the others, but share some cycle scoped data nodes with the scenarios from the
same cycle and the global data node with all scenarios.

You can use the utility methods provided by Taipy to access, read, write, compare,
and manage data nodes and scenarios.

For more details, see the [scenario](../sdm/scenario/index.md) and
[data node](../sdm/data-node/index.md) pages.

!!! important "User Interface"

    Note that the scenarios are created and edited programmatically in this example. A Taipy
    user interface is often used to let end-users create their own scenarios, manage their cycles
    and set the data. In particular, the visual elements
    [scenario selector](../../../refmans/gui/viselements/corelements/scenario_selector.md),
    [scenario viewer](../../../refmans/gui/viselements/corelements/scenario.md),
    [data node selector](../../../refmans/gui/viselements/corelements/data_node_selector.md), and
    [data node viewer](../../../refmans/gui/viselements/corelements/data_node.md) are designed to facilitate
    the creation and management of scenarios.
