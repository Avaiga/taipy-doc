Business problems are often recurrent. A [Cycle](../../../reference/#taipy.core.cycle.cycle.Cycle)
(or work cycle) represents an iteration of such a recurrent work
pattern. Each _cycle_ has a start date and a duration that depends on the frequency on which a user must publish
a scenario in production. In Taipy, a _cycle_ duration depends on the
[Frequency](../../../reference/#taipy.core.common.frequency.Frequency) of the scenarios, which is among :

- `Frequency.DAILY`
- `Frequency.WEEKLY`
- `Frequency.MONTHLY`
- `Frequency.QUATERLY`
- `Frequency.YEARLY`

Each recurrent scenario is attached to a _cycle_. In other words, each _cycle_ contains multiple scenarios. At the end
of a cycle (start date + duration), only one of the scenarios can be applied in production. This scenario is
called _master scenario_. There is only one _master scenario_ per cycle.

!!! example

    The user must publish production orders every month. Each month is
    modeled as a cycle in Taipy, and each cycle contains one or multiple scenarios.

    Depending on the simulation we ran, we may have one unique scenario (a master one) for the January cycle and two
    scenarios for the February cycle (one with the low capacity assumption and one with the high capacity assumption).
    As a user of the application, I can decide to apply the low capacity scenario in production for February.
    For that, I promote my low capacity scenario as master for the February cycle.

    The tree of entities resulting from the various scenarios created is represented on the following picture.
    ![cycles](../cycles_grey.svg){ width="250" }


The attributes of a scenario (the set of pipelines, the cycle, ... ) are populated based on the scenario configuration
([`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig)) that
must be provided when instantiating a new scenario. (Please refer to the
[`configuration details`](../user_core_configuration.md#scenario-configuration) documentation for more
details on configuration).


[:material-arrow-right: Next section introduces the Scope concept.](scope.md)
