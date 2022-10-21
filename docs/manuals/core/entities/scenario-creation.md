# Scenario creation
Scenarios are the most used entities in Taipy. The `taipy.create_scenario()^` function can be used to create a new
scenario.

This function creates and returns a new scenario from the scenario configuration provided as a parameter. The
scenario's creation also triggers the creation of the related entities that do not exist yet. Indeed, if the
scenario has a frequency and there isn’t any corresponding cycle, the cycle will be created. Similarly, the
pipelines, tasks, and data nodes nested in the scenario are created if they do not exist yet.

The simplest way of creating a scenario is to call the `taipy.create_scenario()^` method providing the scenario
configuration as a parameter:

=== "Simple scenario creation without optional parameters"

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    ```

=== "my_config.py module"

    Below is the python configuration imported in the example.

    ```py linenums="1" title="my_config.py"
    from datetime import datetime
    from my_functions import plan, predict, train
    from taipy import Config, Frequency, Scope

    # Configure all six data nodes
    sales_history_cfg = Config.configure_csv_data_node(id="sales_history",
                                                       scope=Scope.GLOBAL,
                                                       default_path="my/file/path.csv")
    trained_model_cfg = Config.configure_data_node(id="trained_model", scope=Scope.CYCLE)
    current_month_cfg = Config.configure_data_node(id="current_month", scope=Scope.CYCLE, default_data=datetime(2020, 1, 1))
    sales_predictions_cfg = Config.configure_data_node(id="sales_predictions", scope=Scope.CYCLE)
    capacity_cfg = Config.configure_data_node(id="capacity")
    production_orders_cfg = Config.configure_sql_data_node(id="production_orders",
                                                           db_username="admin",
                                                           db_password="ENV[PWD]",
                                                           db_name="production_planning",
                                                           db_engine="mssql",
                                                           read_query="SELECT * from production_order",
                                                           write_table="production_order")

    # Configure the three tasks
    training_cfg = Config.configure_task("training", train, sales_history_cfg, [trained_model_cfg])
    predicting_cfg = Config.configure_task(id="predicting",
                                           function=predict,
                                           input=[trained_model_cfg, current_month_cfg],
                                           output=sales_predictions_cfg)
    planning_cfg = Config.configure_task(id="planning",
                                         function=plan,
                                         input=[sales_predictions_cfg, capacity_cfg],
                                         output=[production_orders_cfg])

    # Configure the two pipelines
    sales_pipeline_cfg = Config.configure_pipeline(id="sales", task_configs=[training_cfg, predicting_cfg])
    production_pipeline_cfg = Config.configure_pipeline(id="production", task_configs=[planning_cfg])

    # Configure the scenario
    monthly_scenario_cfg = Config.configure_scenario(id="scenario_configuration",
                                                     pipeline_configs=[sales_pipeline_cfg, production_pipeline_cfg],
                                                     frequency=Frequency.MONTHLY)
    ```

Three parameters can be given to the scenario creation method :

-   `config` is a mandatory parameter of type `ScenarioConfig^`. It corresponds to a scenario configuration (created
    in the module my_config.py)
-   `creation_date` is an optional parameter of type datetime.datetime. It corresponds to the creation date of
    the scenario. If the parameter is not provided, the current date-time is used by default.
-   The `name` parameter is optional as well. Any string can be provided as a `name`. It can be used to display
    the scenario in a user interface.

!!! Example

    === "Scenario creation with parameters"
        Using the [`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py) module, here is an example of how to create a scenario.

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
        * And six data nodes (sales_history, trained_model, current_month, sales_predictions, capacity, production_orders).

    === "my_config.py module"

        Below is the python configuration imported in the example.

        ```py linenums="1" title="my_config.py"
        from datetime import datetime
        from my_functions import plan, predict, train
        from taipy import Config, Frequency, Scope

        # Configure all six data nodes
        sales_history_cfg = Config.configure_csv_data_node(id="sales_history",
                                                           scope=Scope.GLOBAL,
                                                           default_path="my/file/path.csv")
        trained_model_cfg = Config.configure_data_node(id="trained_model", scope=Scope.CYCLE)
        current_month_cfg = Config.configure_data_node(id="current_month", scope=Scope.CYCLE, default_data=datetime(2020, 1, 1))
        sales_predictions_cfg = Config.configure_data_node(id="sales_predictions", scope=Scope.CYCLE)
        capacity_cfg = Config.configure_data_node(id="capacity")
        production_orders_cfg = Config.configure_sql_data_node(id="production_orders",
                                                               db_username="admin",
                                                               db_password="ENV[PWD]",
                                                               db_name="production_planning",
                                                               db_engine="mssql",
                                                               read_query="SELECT * from production_order",
                                                               write_table="production_order")

        # Configure the three tasks
        training_cfg = Config.configure_task("training", train, sales_history_cfg, [trained_model_cfg])
        predicting_cfg = Config.configure_task(id="predicting",
                                               function=predict,
                                               input=[trained_model_cfg, current_month_cfg],
                                               output=sales_predictions_cfg)
        planning_cfg = Config.configure_task(id="planning",
                                             function=plan,
                                             input=[sales_predictions_cfg, capacity_cfg],
                                             output=[production_orders_cfg])

        # Configure the two pipelines
        sales_pipeline_cfg = Config.configure_pipeline(id="sales", task_configs=[training_cfg, predicting_cfg])
        production_pipeline_cfg = Config.configure_pipeline(id="production", task_configs=[planning_cfg])

        # Configure the scenario
        monthly_scenario_cfg = Config.configure_scenario(id="scenario_configuration",
                                                         pipeline_configs=[sales_pipeline_cfg, production_pipeline_cfg],
                                                         frequency=Frequency.MONTHLY)
        ```

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

=== "my_config.py module"

    Below is the python configuration imported in the example.

    ```py linenums="1" title="my_config.py"
    from datetime import datetime
    from my_functions import plan, predict, train
    from taipy import Config, Frequency, Scope

    # Configure all six data nodes
    sales_history_cfg = Config.configure_csv_data_node(id="sales_history",
                                                       scope=Scope.GLOBAL,
                                                       default_path="my/file/path.csv")
    trained_model_cfg = Config.configure_data_node(id="trained_model", scope=Scope.CYCLE)
    current_month_cfg = Config.configure_data_node(id="current_month", scope=Scope.CYCLE, default_data=datetime(2020, 1, 1))
    sales_predictions_cfg = Config.configure_data_node(id="sales_predictions", scope=Scope.CYCLE)
    capacity_cfg = Config.configure_data_node(id="capacity")
    production_orders_cfg = Config.configure_sql_data_node(id="production_orders",
                                                           db_username="admin",
                                                           db_password="ENV[PWD]",
                                                           db_name="production_planning",
                                                           db_engine="mssql",
                                                           read_query="SELECT * from production_order",
                                                           write_table="production_order")

    # Configure the three tasks
    training_cfg = Config.configure_task("training", train, sales_history_cfg, [trained_model_cfg])
    predicting_cfg = Config.configure_task(id="predicting",
                                           function=predict,
                                           input=[trained_model_cfg, current_month_cfg],
                                           output=sales_predictions_cfg)
    planning_cfg = Config.configure_task(id="planning",
                                         function=plan,
                                         input=[sales_predictions_cfg, capacity_cfg],
                                         output=[production_orders_cfg])

    # Configure the two pipelines
    sales_pipeline_cfg = Config.configure_pipeline(id="sales", task_configs=[training_cfg, predicting_cfg])
    production_pipeline_cfg = Config.configure_pipeline(id="production", task_configs=[planning_cfg])

    # Configure the scenario
    monthly_scenario_cfg = Config.configure_scenario(id="scenario_configuration",
                                                     pipeline_configs=[sales_pipeline_cfg, production_pipeline_cfg],
                                                     frequency=Frequency.MONTHLY)

    ```

[:material-arrow-right: The next section presents the scenario and cycle management](scenario-cycle-mgt.md).
