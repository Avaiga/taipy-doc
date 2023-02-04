In this section, it is assumed that <a href="./code_example/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented.

# Scenario creation
Scenarios are the most used entities in Taipy. The `taipy.create_scenario()^` function can be used to create a new
scenario.

This function creates and returns a new scenario from the scenario configuration provided as a parameter. The
scenario's creation also triggers the creation of the related entities that do not exist yet. Indeed, if the
scenario has a frequency and there isn’t any corresponding cycle, the cycle will be created. Similarly, the
pipelines, tasks, and data nodes nested in the scenario are created if they do not exist yet.

The simplest way of creating a scenario is to call the `taipy.create_scenario()^` method providing the scenario
configuration as a parameter:

=== "Scenario creation"

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    ```

=== "Graph representation of the scenario"

    ![scenarios](../pic/scenarios.svg)


Three parameters can be given to the scenario creation method :

-   `config` is a mandatory parameter of type `ScenarioConfig^`. It corresponds to a scenario configuration (created
    in the module my_config.py)
-   `creation_date` is an optional parameter of type datetime.datetime. It corresponds to the creation date of
    the scenario. If the parameter is not provided, the current date-time is used by default.
-   The `name` parameter is optional as well. Any string can be provided as a `name`. It can be used to display
    the scenario in a user interface.

!!! Example

    === "Scenario creation with parameters"
        Using the [`my_config.py`](./code_example/my_config.py) module, here is an example of how to create a scenario.

        ```python  linenums="1"
            import taipy as tp
            import my_config
            from datetime import datetime

            scenario = tp.create_scenario(config=my_config.monthly_scenario_cfg,
                                          creation_date=datetime(2022, 1, 1),
                                          name="Scenario for January")
        ```

        In this small example, one scenario for January 2022 is instantiated. A `creation_date` and a `name` are
        provided.

        Note that the _**monthly_scenario_cfg**_ has set the frequency to monthly. Therefore, scenario will be assigned
        to the cycle corresponding to its creation date (ie the month of January).

        Behind the scene, the other related entities are also created:

        * The January cycle, since the _**monthly_scenario_cfg**_ has set the frequency to MONTHLY. So scenario will
        be assigned to the cycle corresponding to its creation date (ie the month of January).
        * Two sales and production pipelines,
        * Three tasks (training, predicting, planning),
        * And six data nodes (sales_history, trained_model, current_month, sales_predictions, capacity, orders).

    === "Graph representation of the scenario"

        ![scenarios](../pic/scenarios.svg)

# Pipeline creation
Pipelines can be created separately from scenarios using `taipy.create_pipeline()^` function.

This function creates and returns a new pipeline from the pipeline configuration provided as a parameter. The
pipeline's creation also triggers the creation of the related entities that do not exist yet. Indeed, tasks and data
nodes nested in the pipeline are created if they do not exist yet.

=== "Simple pipeline creation"

    ```python linenums="1"
    import taipy as tp
    import my_config

    pipeline = tp.create_pipeline(my_config.sales_pipeline_cfg)
    ```

=== "Graph representation of the scenario"

    ![scenarios](../pic/scenarios.svg)


[:material-arrow-right: The next section presents the scenario and cycle management](scenario-cycle-mgt.md).
