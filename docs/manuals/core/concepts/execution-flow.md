# Execution flow

!!! important "Reminder: Config vs Entities"

    The **data nodes**, **tasks**, and **scenarios** concepts have two types of Taipy objects related to them:
    **configs** and runtime **entities**. **Sequences** also has its configuration object that is provided through
    **scenarios config** Taipy objects. It also has its own runtime **entities**

    Remember that each **entity** is created from a **config** (e.g. a Data node is created from a Data node config, a
    Task from a Task Config, a Scenarios from a Scenario config, etc). Remember also that the same **config** can be used
    to instantiate multiple **entities** (e.g., a scenario configuration can be used to instantiate two different scenarios).

Let's take some scenario entity use cases to illustrate the logic behind the execution flow. For this purpose,
we will use the configuration graph below.
# TODO: update this image

![Configuration Graph ](../pic/execution_flow_configs.svg)

The picture above represents the graph of **configs** objects (`DataNodeConfig` and `TaskConfig` objects).

# Single Scenario Execution

Let’s assume we instantiate a new scenario entity from the scenario configuration above (see the previous configuration
graph). Let’s call it **Scenario 1**. All the entities of **Scenario 1** will be instantiated from the various
configuration objects.

**Scenario 1** can also be represented as the entity graph below:

![Scenario 1 Graph ](../pic/execution_flow_entities.svg)

Thanks to this graph representation, Taipy automatically understand the execution precedence constraints. When a
scenario/sequence is submitted for execution, the tasks are smartly orchestrated and executed in the correct sequence.

Taipy also optimizes the execution of sequences and scenarios by not recomputing tasks that do not need to be
re-executed. This is the concept of _caching_.

Let’s assume that **scenario 1** has already been executed. If the end-user decides to re-execute the same scenario,
then only three situations can occur:

- <u>Situation 1</u>: Taipy re-executes all the tasks. This is the default behavior.
- <u>Situation 2</u>: None of the data nodes have been modified since the last run. The data nodes _**sales
  predictions**_ and _**production orders**_ are cached, then they don't need to be re-executed. Taipy does not
  re-execute the tasks. (Please refer to `DataNodeConfig^` documentation to activate the "cacheable" feature).
- <u>Situation 3</u>: If at least one of the input data nodes has been modified since the last run, Taipy only
  executes the "appropriate" tasks. It implies that:
      * If the _**predict**_ task entity has any of its two input data nodes (_**trained model**_ or _**current
        month**_) changed since the last run, then in the second run, Taipy re-executes both the _**predict**_
        and the _**planning**_ tasks.
      * If _**trained model**_ and _**current month**_ have not been modified but _**capacity**_ has, then Taipy
        only re-executes the _**planning**_ task.

# Multiple Scenario Execution

Let’s continue with the previous example by creating a second scenario from the same config. Let’s call it
**Scenario 2**. In the case of two scenarios instantiated from the same configuration, what could be the impact
of executing **scenario 1** over the execution of **scenario 2**.

Two options are possible with Taipy:

- <u> Option 1 </u>:
Taipy assumes that the entities of each scenario are "local" to each scenario and are not shared with other scenarios.
Similar to the first scenario, the following entity graph is created for **Scenario 2**.

![Scenario 2 Graph option 1](../pic/execution_flow_entities_2.svg)

Note that even if both scenarios share the same configuration graph, all their data nodes and tasks are separate
instances. **Scenario 2**'s data nodes and tasks are separate instances and are prefixed by `2`.

- <u> Option 2 </u>:
Taipy assumes that some entities of the scenarios are "global" and are shared among scenarios. For instance, let's
assume that _**current month**_ can be shared by **Scenario 1** and **Scenario 2**. In this second option, the
following entity graph is created for **Scenario 2**.

![Scenario 2 Graph option 2 ](../pic/execution_flow_entities_2_global_month.svg)

To illustrate the difference between the two options, let’s assume that:

- First, **Scenario 1** has been executed with its **current month** entity set to "_January_".
- Then, the **current month** data node entity of **Scenario 2** has been set to "_February_".

If Option 1 applies, when the end-user re-executes **Scenario 1**, Taipy produces the same execution
as before (or does not re-execute the tasks if the "cacheable" feature is activated).

If Option 2 applies, **current month** and **current month 2** data nodes are the same entity. When the end–user
re-execute **Scenario 1**, Taipy detects that the **current month** data node entity has changed. Then re-executing
**Scenario 1**, runs the entity graph with the **current month** set to "_February_".

To enable the difference in behavior, Taipy introduces the concept of Scope. In Taipy, Option 1 corresponds to the
by-default behavior: the _SCOPE_ default value is `SCENARIO`. While Option 2 corresponds to setting the
scope to a level above `SCENARIO` (either `CYCLE` or `GLOBAL`).

[:material-arrow-right: The next section introduces the Scope concept.](scope.md)
