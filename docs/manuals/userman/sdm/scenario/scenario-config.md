In this section, we delve into the specifics of configuring *scenarios* for what if analysis
in Taipy.

A scenario configuration is necessary to instantiate a `Scenario^`. To create a
`ScenarioConfig^`, you can use the `Config.configure_scenario()^` method with the following parameters:

- _**id**_: The id of a new scenario configuration to be created. This id is **mandatory** and must
  be a unique and valid Python identifier.
- _**tasks**_: A list of task configurations.
- _**additional_data_nodes**_: A list of additional data node configurations.
- _**frequency**_: The recurrence of the scenarios instantiated from this configuration. The scenarios
  are attached to the proper cycles based on this frequency.
- _**sequences**_: A dictionary of sequence descriptions.
- _**comparators**_: A list of functions used to compare scenarios. A comparator function is attached to a
  scenario's data node configuration. During the scenario comparison, each comparator is applied to all the data
  nodes instantiated from the data node configuration attached to the comparator.
- _**properties**_: A dictionary of additional properties.

!!! warning "Reserved keys"

    Note that we cannot use the word "_entity_owner" as a key in the properties as it has been reserved for internal use.

# Additional data nodes

A scenario configuration `ScenarioConfig^` holds some data node configurations. These
configurations can be added to the scenario configuration using the
`Config.configure_scenario()^` method.

For more details, see the [What-if-analysis](../../what-if-analysis/multiple-scenarios.md) page.

# Frequency for cycle management

A `ScenarioConfig^` can also hold a frequency to model recurrent business problem
to solve. When a frequency is provided to a configuration, the scenarios instantiated
from this configuration are automatically attached to the `Cycle^` (a time period)
corresponding to the date of the scenario creation.
For more details, on scopes and cycles see the
[Recurrent Scenarios](../../what-if-analysis/scenarios-and-cycles.md) page.

# Adding scenario comparator

A `ScenarioConfig^` can also hold some scenario comparators. A scenario comparator is a
user function used to compare multiple scenarios from the same configuration.
For more details, see the [Scenario comparators](../../what-if-analysis/scenario-comparators.md)
page.

# Adding task configurations
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method. This is useful when you
want to orchestrate the execution of tasks for data processing or data transformation.<br>
For more details, see the
[Task orchestration](../../task-orchestration/scenario-config.md#from-task-configurations)
page.

# Adding sequence descriptions
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method.
For more details, see the
[Sequence configuration](../../task-orchestration/scenario-config.md#adding-sequence-descriptions)
page.
