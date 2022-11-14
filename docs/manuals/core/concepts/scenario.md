We have introduced within Taipy the important concept of a `Scenario^`. A Taipy Scenario represents an instance of a
business problem to solve on consistent data and parameter sets.

As its name implies, with Taipy scenarios the users can instantiate different versions of a business
problem with different assumptions. This is extremely useful in a business context where impact analysis and what-if
analysis are essential in the decision process.

After having analyzed its first scenario, the users may be very interested in modifying input data nodes (not the
intermediate nor the output data nodes), re-running the same pipelines and comparing the results with the previous run.

For this purpose, it will just need to instantiate a second scenario, execute it and compare it with the first scenario.
This process can be repeated across multiple scenarios.


!!! example "In the example"

    Here, our scenario consists of the two pipelines described earlier. In the flowchart below, the
    external light blue box represents our scenario that contains both pipelines.

    ![scenarios](../pic/scenarios.svg){ align=left }

A scenario represents one instance of a business problem to solve. Each new business problem instance is represented
by a new scenario. Taipy allows us to give the end users the ability to create, store, edit, and execute various
scenarios in the same application.

!!! example

    We want to build an application that first predict the monthly demand of a plant and then generate the
    planning for the production orders. The user can create the first scenario for January. It must contain
    everything we need to understand the January case, access input data, compute predictions, visualize our
    forecast algorithm results, make production decisions, and publish the January production orders.

    Then the user can create another scenario for February using the new information provided for the February
    period. And so on.

Two _scenarios_ can also be used to represent the same instance of a business problem but with two different sets of
assumptions.

!!! example

    The user would like to perform some simulation on the impact of our capacity data on production planning for the
    February use case.

    The first scenario can forecast demand and compute production orders assuming a low capacity, whereas the
    second scenario assumes a higher capacity value.

    One can note that scenarios can also be used by data scientists, this is often referred as ‘experiments’.
    Scenarios are in fact a generalization of experiments in such a way that both data sceintists and end-users
    can finally use the same concept: the Scenario.


[:material-arrow-right: The next section introduces the Cycle concept.](cycle.md)
