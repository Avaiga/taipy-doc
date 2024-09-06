In this section, we delve into the specifics of configuring *scenarios* for task
orchestration.

# From task configurations

The code below aims at configuring a `ScenarioConfig^` from a single `TaskConfig^`
to instantiate a simple scenario computing the double of a given number.

```python linenums="1"
{%
include-markdown "./code-example/scenario-config/scenario-config-from-task-cfg.py"
comments=false
%}
```

Two data node configurations are created with the `Config.configure_data_node()^` method.
One "input" for the number to double and one "output" for the result. For more details,
see the [data node configuration](../data-integration/data-node-config.md) page.

Then, a task configuration `double_task_cfg` is created using the `Config.configure_task()^`
method. It takes as parameter the input and output data node configurations and the function
`double()` that computes the double of a given number.

Finally, the scenario configuration `double_scenario` is created as a `ScenarioConfig^`
passing the task configuration as parameter.

# Adding sequence descriptions

A `Sequence^` is a subset of scenario tasks that can be executed together, independently of
the other tasks. The sequences can be created directly on scenario instances, at run time,
but they can also be describes in the scenario configurations, so they can be created along
with the scenario creation.

Here is a simple example assuming the task configurations
`add_task_cfg_1`, `add_task_cfg_2`, `multiply_task_cfg_1`, `multiply_task_cfg_2` have
already been created:

```python linenums="1"
{%
include-markdown "./code-example/scenario-config/with-sequences.py"
comments=false
%}
```

An alternative way to add sequences to a scenario configuration is to use the `add_sequences()`
method.

```python linenums="1"
{%
include-markdown "./code-example/scenario-config/alternative-with-sequences.py"
comments=false
%}
```

We can also remove sequences after providing them in your scenario configuration.

```python linenums="1"
{%
include-markdown "./code-example/scenario-config/alternative-with-sequences.py"
comments=false
%}
```

In the small examples above, we create a scenario configuration `ScenarioConfig^`
from task configurations and define sequences for that scenario configuration.

When defining a sequence in a `ScenarioConfig^`, you need to provide a dictionary
with the sequence name as the key and a list of task configurations that belong to
the sequence as the value. Note that the task configurations of the sequence must
also exist in the tasks of the scenario configuration.

# Additional data nodes

In addition to the execution graph made of task and data node configurations,
a scenario configuration `ScenarioConfig^` can also hold some additional data
node configurations that are not connected to the execution graph. These
configurations can be added to the scenario configuration using the
`Config.configure_scenario()^` method.

For more examples, see the [multiple scenarios](../what-if-analysis/multiple-scenarios.md) page.

# Frequency for cycle management

A `ScenarioConfig^` can also hold a frequency to model recurrent business problem
to solve. When a frequency is provided to a configuration, the scenarios instantiated
from this configuration are automatically attached to the `Cycle^` (a time period)
corresponding to the date of the scenario creation.
For more details on cycles see the
[Recurrent Scenarios](../what-if-analysis/scenarios-and-cycles.md) page.

# Adding scenario comparator

A `ScenarioConfig^` can also hold some scenario comparators. A scenario comparator is a
user function used to compare multiple scenarios from the same configuration.
For more details, see the
[scenario comparison](../what-if-analysis/scenario-comparison.md)
page.
