Introducing the `Scenario`, a fundamental key concept in Taipy.

A Taipy *Scenario* represents a business problem with consistent data and parameters.

Scenarios are a powerful tool to create different versions of a business problem under different
assumptions. This is especially valuable for what-if analysis in decision-making processes,
enabling users to create, store, edit, and execute multiple scenarios with various
parameters within the same application. 

A scenario contains an executable Directed Acyclic Graph (or DAG). The scenario DAG is a set of tasks connecting
data nodes together. It can also be broken down into smaller graphs for execution by defining a `Sequence^`s.
A sequence is a subset of tasks derived from the scenario's set of tasks, forming a smaller executable DAG that
can be submitted separately from the scenario DAG. A scenario can also contain a set of other data nodes
outside of the scenario DAG to represent additional data related to the scenario but are not executable.

After analyzing its first scenario, an end-user may be interested in modifying input data nodes
(not the intermediate nor the output data nodes), re-running the identical sequences or scenario and
comparing the results with the previous run.

Once an initial scenario has been analyzed, users can modify the input data nodes (excluding
the intermediates and output data nodes), rerun part of its tasks, and compare results.

This involves instantiating a second scenario, changing the input data, executing it,
and comparing the outcomes with the first scenario.

This iterative process can be repeated across multiple scenarios, allowing for comprehensive
exploration and analysis of different problem variations.

!!! example "In the example"

    Here, our scenario consists of a graph of data nodes and tasks. The scenario graph can also be split into
    two sequences as subgraphs described earlier. The external light blue box in the flowchart below represents
    our scenario that contains all data nodes, tasks, and sequences.
    # TODO: update the picture

    ![scenarios](../pic/scenarios.svg){ align=left }


Two use-cases arise from the utilization of Taipy scenarios:

### - Use case 1 :
Each *scenario* represents a distinct instance of a business problem.

With Taipy, end-users can create, store, edit, and execute various scenarios within the
same application.

!!! example

    We build an application that:

    - first forecast the monthly demand for a plant

    - then, based on that forecast, generate the planning for the production orders.

    The end-user creates the first scenario for January. It must contain everything the
    end-user needs to understand the January case, access input data, compute predictions,
    visualize our forecast algorithm results, make production decisions, and publish the
    January production orders.

    Then the end-user creates another scenario for February using the new information provided
    for the February period. And so on.

### - Use case 2:
Two *scenarios* represent the same business problem instance, but with different sets of
assumptions.

!!! example

    The end-user wants to simulate how the capacity data affects production planning for
    the February situation.

    In the first scenario, we forecast demand and calculate production orders based on a low
    capacity assumption. In the second scenario, we assume a higher capacity value.

    It's important to note that scenarios are not only useful for end-users, but also for
    data scientists. They can use scenarios as experiments to test different hypotheses.
    Essentially, scenarios provide a common concept that both data scientists and end-users
    can utilize.


[:material-arrow-right: The next section introduces the Cycle concept.](cycle.md)
