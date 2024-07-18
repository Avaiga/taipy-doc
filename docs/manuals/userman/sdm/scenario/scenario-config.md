In this section, we delve into the specifics of configuring *scenarios* for what if analysis
in Taipy.

A scenario configuration is necessary to instantiate a `Scenario^`. To create a
`ScenarioConfig^`, you can use the `Config.configure_scenario()^` method with the following
parameters:

- _**id**_: The id of a new scenario configuration to be created. This id is **mandatory**
    and must be a unique and valid Python identifier.
- _**tasks**_: A list of task configurations.
- _**additional_data_nodes**_: A list of additional data node configurations.
- _**frequency**_: The recurrence of the scenarios instantiated from this configuration.
    The scenarios are attached to the proper cycles based on this frequency.
- _**sequences**_: A dictionary of sequence descriptions.
- _**comparators**_: A list of functions used to compare scenarios. A comparator function
    is attached to a scenario's data node configuration. During the scenario comparison,
    each comparator is applied to all the data nodes instantiated from the data node
    configuration attached to the comparator.
- _**properties**_: A dictionary of additional properties.

!!! warning "Reserved keys"

    Note that we cannot use the word "_entity_owner" as a key in the properties as it has
    been reserved for internal use.

# Additional data nodes

A scenario configuration `ScenarioConfig^` holds some data node configurations. These
configurations can be added to the scenario configuration using the
`Config.configure_scenario()^` method.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-config/additional-datanodes.py"
    comments=false
     %}
    ```

    In this example, we have a scenario configuration `scenario_config` containing
    one single data node configuration `data_node_cfg`. This data node configuration
    is added to the scenario configuration as an additional data node configuration.,
    which means that the data node configuration is not part of any task, or any
    execution graph.

A more realistic example is available in the
[multiple scenario](../../what-if-analysis/multiple-scenarios.md#example) section.

# Frequency for cycle management

A `ScenarioConfig^` can also hold a *frequency* to model recurrent business problem
to solve. When a frequency is provided to a configuration, the scenarios instantiated
from this configuration are automatically attached to the `Cycle^` (a time period)
corresponding to the date of the scenario creation.

!!! example

    In the example below, we have a scenario configuration `scenario_config` with a weekly
    frequency. Each scenario instantiated from this configuration will be attached to
    a cycle corresponding to the week of the creation date of the scenario.

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-config/frequency.py"
    comments=false
     %}
    ```

    Three data node configurations are added to the scenario configuration as additional
    data node configurations (a global data node configuration, a cycle data node
    configuration, and a scenario data node configuration).
    When a scenario is created, the global data node configuration is instantiated
    once and shared by all the scenarios. The cycle data node configuration is
    instantiated once per cycle and shared by all the scenarios attached to the same
    cycle. The scenario data node configuration is instantiated once per scenario.


For more details, on scopes and cycles see the
[recurrent Scenarios](../../what-if-analysis/scenarios-and-cycles.md) page.

# Adding scenario comparator

A `ScenarioConfig^` can also hold some scenario comparators. A scenario comparator is a
user function used to compare multiple scenarios from the same configuration.

!!! example

    In the example below, we have a scenario configuration `scenario_config` with a
    scenario comparator `compare_kpis`. This comparator is used to compare
    the kpi data nodes of the compared scenarios.

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-config/comparator.py"
    comments=false
     %}
    ```

    The `compare_kpis` function compares the kpi data (the result of the `DataNode.read()`
    method) and returns the max value as a comparison result.

For more details and examples, see the
[scenario comparison](../../what-if-analysis/scenario-comparison.md) page.

# Adding task configurations
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method. This is useful when you
want to orchestrate the execution of tasks for data processing or data transformation.<br>
For more details, see the
[task orchestration](../../task-orchestration/scenario-config.md#from-task-configurations)
page.

# Adding sequence descriptions
In addition to the data nodes configurations, a scenario configuration `ScenarioConfig^`
can also hold some task configurations connecting data node configurations together and
forming an execution graph. These task configurations can be added to the scenario
configuration using the `Config.configure_scenario()^` method.
For more details, see the
[Sequence configuration](../../task-orchestration/scenario-config.md#adding-sequence-descriptions)
page.
