In this section, we delve into the specifics of configuring *scenarios* for what if analysis
in Taipy.

# Additional data nodes

A scenario configuration `ScenarioConfig^` holds some data node configurations. These
configurations can be added to the scenario configuration using the
`Config.configure_scenario()^` method.

For more details, see the [What-if-analysis](../what-if-analysis/multiple-scenarios.md) page.

# Frequency for cycle management

A `ScenarioConfig^` can also hold a frequency to model recurrent business problem
to solve. When a frequency is provided to a configuration, the scenarios instantiated
from this configuration are automatically attached to the `Cycle^` (a time period)
corresponding to the date of the scenario creation.
For more details, see the [Scopes, scenarios and cycles](../what-if-analysis/scenario-and-cycles.md)
page.

# Adding scenario comparator

A `ScenarioConfig^` can also hold some scenario comparators. A scenario comparator is a
user function used to compare multiple scenarios from the same configuration.
For more details, see the [Scenario comparators](../what-if-analysis/scenario-comparators.md)
page.

# Adding task configurations
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method. This is useful when you
want to orchestrate the execution of tasks for data processing or data transformation.<br>
For more details, see the
[Task orchestration](../task-orchestration/scenario-config.md#from-task-configurations)
page.

# Adding sequence descriptions
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method.
For more details, see the
[Sequence configuration](../task-orchestration/scenario-config.md#adding-sequence-descriptions)
page.
