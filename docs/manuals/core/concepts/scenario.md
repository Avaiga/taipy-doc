A [Scenario](../../../reference/#taipy.core.scenario.scenario.Scenario) is made to model a business concept.
It represents an instance of a business problem to solve on consistent data and parameter sets. In other words,
when an end user select a _scenario_, he/she should have access to all the information and data needed to
understand the business case he/she is working on and to make the right decisions.

!!! example "In the example"

    In our example, we want our scenario to have the two pipelines described before. The external blue frame represents
    my scenario that contains both pipelines.

    ![scenarios](../scenarios.svg){ align=left }

A scenario represents one instance of a business problem to solve. In other words, each new business problem instance
is represented by a new scenario. The end user can manage the various multiple scenarios in the same Taipy application.
He or she can retrieve, edit and execute the various existing scenarios.

!!! example

    Suppose we want to build an application to predict demand every month and compute production orders.
    In that case, we can create the first scenario for January. It must contain everything we need to understand
    the January case, access input data, compute predictions, visualize our forecast algorithm
    results, make production decisions, and publish January production orders.

    Then we can create another scenario for the February production planning. And so on.

Two _scenarios_ can also be used to represent the same instance of a business problem but with two different
assumptions.

!!! example

    Now, we want to perform some simulation on the impact of our capacity data on our production planning.
    We want to create two scenarios for the same February use case.

    The first scenario can forecast demand and compute production orders with a low capacity.

    In contrast, the second scenario assumes a high capacity value.


[:material-arrow-right: Next section introduces the Cycle concept.](cycle.md)
