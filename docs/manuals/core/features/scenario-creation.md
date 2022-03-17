Scenarios are the most used entities in Taipy. The
`taipy.create_scenario^` can be used to create a new scenario.

This function creates and returns a new scenario from the scenario configuration
provided as a parameter. The scenario's creation also triggers the creation of the related entities that
do not exist yet. Indeed, if the scenario has a frequency, the corresponding cycle is created if
it does not exist yet. Similarly, the pipelines, tasks, and data nodes nested in the scenario are created
if they do not exist yet.

The simplest way of creating a scenario is to call the `taipy.create_scenario()^` method providing the scenario
configuration as a parameter:

```python linenums="1"
import taipy as tp
from config import *

tp.create_scenario(monthly_scenario_cfg)
```

Three parameters can be given to the scenario creation method :

-   `config` is a mandatory parameter of type
    `ScenarioConfig^`. It corresponds to a
    scenario
    configuration (created in the config.py module)
-   `creation_date` is an optional parameter of type datetime.datetime. It corresponds to the creation date of
    the scenario. If the parameter is not provided, the current date-time is used by default.
-   The `name` parameter is optional as well. Any string can be provided as a `name`. It can be used to display
    the scenario in a user interface.

!!! Example

    Using the [`my_config.py`](../my_config.py) module here is an example of how to create a scenario.

    ```python linenums="1"
        import taipy as tp
        from my_config import *
        from datetime import datetime

        scenario = tp.create_scenario(monthly_scenario_cfg, creation_date=datetime(2022, 1, 1), name="Scenario for January")
    ```

    On this small example, one scenario for January is instantiated. A `creation_date` and a `name` are provided.

    Behind the scene, the other related entities are also created:

    * The January cycle,
    * Two sales and production pipelines,
    * Three tasks (training, predicting, planning),
    * And six data nodes (sales_history, trained_model, current_month, sales_predictions, capacity, production_orders).

[:material-arrow-right: Next section presents the scenario and cycle management features](scenario-cycle-mgt.md).
