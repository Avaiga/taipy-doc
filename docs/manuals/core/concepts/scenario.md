We introduce here the important concept of a `Scenario^`. A Taipy Scenario represents an instance of a
business problem to solve on consistent data and parameter sets.

As its name implies, with Taipy scenarios, the users can instantiate different versions of a business
problem with different assumptions. This is extremely useful in a business context where impact analysis
and what-if analysis are essential in the decision process.

After analyzing its first scenario, an end-user may be interested in modifying input
data nodes (not the intermediate nor the output data nodes), re-running the same pipelines, and
comparing the results with the previous run.

For this purpose, he needs to instantiate a second scenario, execute it and compare it with the
first scenario. This process can be repeated across multiple scenarios.


!!! example "In the example"

    Here, our scenario consists of the two pipelines described earlier. The external light blue box in the flowchart
    below represents our scenario that contains both pipelines.

    ![scenarios](../pic/scenarios.svg){ align=left }

A scenario represents one instance of a business problem to solve. Each new business problem instance
is represented by a new scenario. With Taipy, end-users can create, store, edit, and
execute various scenarios within the same application.

!!! example

    We build an application that:

    - first forecast the monthly demand for a plant

    - then, based on that forecast, generate the planning for the production orders.

    The end-user creates the first scenario for January. It must contain everything the end-user needs
    to understand the January case, access input data, compute predictions, visualize our
    forecast algorithm results, make production decisions, and publish the January production orders.

    Then the end-user creates another scenario for February using the new information provided for the
    February period. And so on.

Two _scenarios_ can also represent the same instance of a business problem but with two different sets of
assumptions.

!!! example

    The end-user would like to simulate the impact of our capacity data on production planning for the
    February use case.

    The first scenario can forecast demand and compute production orders assuming a low capacity,
    whereas the second assumes a higher capacity value.

    One can note that data scientists can also use scenarios. This is often referred to as ‘experiments’.
    Scenarios are in fact, a generalization of experiments in such a way that both data sceintists
    and end-users can finally use the same concept: the Scenario.


[:material-arrow-right: The next section introduces the Cycle concept.](cycle.md)
