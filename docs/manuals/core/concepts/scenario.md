A `Scenario^` is created to model a business concept. It represents an instance of a business problem to solve on
consistent data and parameter sets. In other words, when an end user selects a _scenario_, he/she should have access
to all the information and data needed to understand the business case he/she is working on and to make the right
decisions.

!!! example "In the example"

    In our example, we want our scenario to have the two pipelines described earlier. In the flowchart below, the
    external light blue box represents my scenario that contains both pipelines.

    ![scenarios](pic/scenarios.svg){ align=left }

A scenario represents one instance of a business problem to solve. Each new business problem instance is represented
by a new scenario. Taipy allows us to give the end users the ability to store, edit, and execute various scenarios
in the same application.

!!! example

    Suppose that we want to build an application to predict the monthly demand of a store and optimize production
    orders. In that case, we can create the first scenario for January. It must contain everything we need to
    understand the January case, access input data, compute predictions, visualize our forecast algorithm results,
    make production decisions, and publish January production orders.

    Then we can create another scenario for February production planning. And so on.

Two _scenarios_ can also be used to represent the same instance of a business problem but with two different sets of
assumptions.

!!! example

    We would like to perform some simulation on the impact of our capacity data on production planning.
    We want to create two scenarios for the February use case.

    The first scenario can forecast demand and compute production orders assuming a low capacity, whereas the
    second scenario assumes a high capacity value.


[:material-arrow-right: The next section introduces the Cycle concept.](cycle.md)
