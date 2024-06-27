In this section, we explore how to use *Scenarios* for What-if-analysis in Taipy.
What-if analysis is all about exploring different scenarios to see how variable
changes affect outcomes. It's essentially asking "What if?" questions and examining
the results.

# What is a Scenario?
A `Scenario^` in Taipy represents an instance of a business problem. Among other features
scenarios own data nodes. Two different scenarios can own two alternative data nodes
(from the same `DataNodeConfig^`). This is particularly handy when you want to represent
different situation, assumption or condition, and compare the data between them.

In addition to holding data nodes, *scenarios* can be attached to a `Cycle^` to manage
recurring business cases. This is ideal for time-based analyses like monthly forecasts,
weekly results, daily reports, etc.

For more details on scenarios, please refer to the
[Scenario and Data Management](../sdm/index.md) page.

# Why use Scenarios?

The main advantages of using *scenarios* for what-if analysis are:

- **Informed Decision-Making**: Understand the implications of different situations.
    Instantiating multiple scenarios with alternative data nodes from the same
    `DataNodeConfig` allows you to manage different versions of the same dataset
    or parameter set. It is essential for use cases where experiments need to be
    conducted with different assumptions, or when data needs to be preserved for
    auditing and comparison purposes.<br>
    For more details, see the [Multiple scenarios](multiple-scenarios.md) page.

- **Temporal Analysis**: Use cycles for recurring business cases, ideal for time-based
    analyses like weekly forecasts, monthly planning, etc.<br>
    For more details, see the [Scopes, scenarios and cycles](scenario-and-cycles.md) page.

- **Easy to use**: Easily manage and compare multiple scenarios for various business situations.
    <br>
    For more details, see the [Scenario comparators](scenario-comparators.md) page.

# How to use Scenarios?

What-if analysis in Taipy involves configuring *data nodes*, setting up *scenario* configurations,
and instantiating new *scenarios* at runtime. Each *scenario* holding an alternative data node,
represents a different situation, assumption or condition, and as an end-user you can compare
the different scenarios to understand the impact of various decisions, or events on your data.

Here is the main principle:

1. **Configuring data nodes**: The first step consist in configuring the data nodes that will be
    instantiated along with the scenarios. *Data nodes* are the building blocks of *scenarios*.
    They represent any data such as input datasets, parameters, intermediate data, kpis, results
    or output dataset. They are instantiated from `DataNodeConfig` objects.
    <br>
    For more details on *data nodes*, see the [Data integration](../data-integration/index.md)
    page.

2. **Configuring Scenarios**: A `ScenarioConfig` is a configuration object used to instantiate
    *scenarios*. It encapsulates scenario-specific settings such as data node configurations,
    *task* configurations, scenario comparators, or frequency for cycle management.<br>
    For more details on how to configure scenarios, see the
    [scenario configuration](../sdm/scenario/scenario-config.md) page.

3. **Instantiating multiple scenarios with alternative data nodes**: At runtime, an end-user
    can create as many new *scenarios* as he/she wants from the same `ScenarioConfig`. Each
    one contains its own set of *data nodes*. This allows an end user to compare the
    scenarios' data.<br>
    For more details, see the [multiple scenarios](multiple-scenarios.md) and
    [scenario comparators](scenario-comparators.md) pages.


