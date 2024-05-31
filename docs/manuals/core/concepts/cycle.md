---
hide:
  - toc
---

Data applications are often used to solve business problems that operate periodically (i.e. in time cycles).

Examples:

- Predictions of sales data for Store X needs to occur weekly
- The master planning of Company A’s supply chain needs to happen monthly
- etc.

For this purpose, Taipy brings the concept of `Cycle^` (or work cycle), which represents a single iteration of such
a time pattern. Each _cycle_ has a start date and a duration depending upon the chosen time frequency of the
scenarios. In Taipy, scenarios may have a `Frequency^` among:

- `Frequency.DAILY`
- `Frequency.WEEKLY`
- `Frequency.MONTHLY`
- `Frequency.QUARTERLY`
- `Frequency.YEARLY`

At its creation, a new scenario is attached to a single cycle, the one that matches its _frequency_ and its
_creation_date_.

!!! example "Example for January cycle"

    ![cycles](../pic/cycles_january_colored.svg){ align=left width="250" }

    In our example, the end-user publishes production orders (i.e., a production plan) every month. During each
    month (the cycle), the end-user will be interested in "playing" with different scenarios untill only one of
    those scenarios is selected as the official production plan to be published. Using Taipy,
    each month is modeled as a cycle, and each Taipy cycle can contain one or more Taipy scenarios.

    The picture on the left shows the tree of entities: Cycles, Scenarios, and their associated Sequence(s). There
    is an existing past cycle for December and a current cycle for January containing a single scenario.

When comes the end of a _cycle_ (start date + duration), only one of the scenarios is applied in production. This
"official" scenario is called the _**primary scenario**_. Only one _**primary scenario**_ per cycle is allowed.

!!! example "Example for February cycle"

    ![cycles](../pic/cycles_colored.svg){ align=left width="250" }
    Now the user starts working on the February work cycle. He or she creates two scenarios for the February cycle (one
    with a low capacity assumption and one with a high capacity assumption).
    The user can then decide to elect the low capacity scenario as the "officilal" scenario for February.
    To accomplish that, he just needs to promote the low capacity scenario as _**primary**_ for the February cycle.

    The tree of entities resulting from the various scenarios created is represented in the picture on the left. The
    underlined scenarios are _**primary**_.

!!! note

    Note that cycles are optional. If a scenario has no Frequency, it will not be attached to any cycle.

The attributes of a scenario (the set of sequences, the cycle, ... ) are populated based on the scenario configuration
`ScenarioConfig^` that must be provided when instantiating a new scenario. (Please refer to the
[`configuration details`](../config/scenario-config.md) documentation for more details on configuration).


[:material-arrow-right: The next section introduces the Job concept.](job.md)
