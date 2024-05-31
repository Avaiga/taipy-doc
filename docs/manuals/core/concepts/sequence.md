---
hide:
  - toc
---

A `Sequence^` is designed to model an algorithm. It represents a direct acyclic graph of input, intermediate, and output
data nodes linked together by tasks. A *sequence* is a set of tasks designed to perform functions.

For instance, in a typical machine learning application, we may have several sequences: a sequence dedicated to
preprocessing and preparing data, a sequence for computing a training model, and a sequence dedicated to scoring.

!!! example "In the example"

    We have chosen to model only two sequences corresponding to a manufacturer having first to predict the sales
    forecast, then, based on the sales forecast, plan its production in its plant.

    ![sequences](../pic/sequences.svg){ align=left }

    First, the sales sequence (boxed in green in the picture) contains **training** and **predict** tasks.

    Second, a production sequence (boxed in dark gray in the picture) contains the **planning** task.

    This problem has been modeled in two sequences - one sequence for the forecasting algorithm and one for the
    production planning algorithm. As a consequence, the two algorithms can have two different workflows. They can run
    independently, under different schedules. For example, one on a fixed schedule (e.g. every week) and one on demand,
    interactively triggered by end-users.


Note that the sequences are not necessarily disjoint.

The attributes of a sequence (the set of tasks) are populated based on the sequence configuration provided in the
`ScenarioConfig^` provided when instantiating a new sequence. (Please refer to the
[`configuration details`](../config/scenario-config.md) documentation for more details on configuration).


[:material-arrow-right: The next section introduces the Scenario concept.](scenario.md)
