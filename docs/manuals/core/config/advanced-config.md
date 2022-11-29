Taipy provides three ways to configure your application :

- A Python configuration
- An explicit file configuration using _TOML_ format
- An environment variable file configuration

!!! example

    Here is a typical workflow that shows how to adapt the configuration of a Taipy application at each stage of a
    software project (from initial development to production).

    1. To get started, as a developer I will be designing my application by configuring all the new entities  (data
    nodes, tasks, pipelines, scenarios) using the Python code configuration with just a minimal number of attributes
    configured. The default configuration is used for the other attributes.

    2. Then, I am testing the application built. At this step, I need my application to have a more realistic
    behavior like real data. For that, I need more configuration. I can specify for my
    specific input dataset what file to use. I am using the Python code configuration for that.

    3. Then, once I am happy with my application running on my local dev environment, I am deploying it to a remote
    environment for testing. This is a dedicated environment made for testing deployment and for integration testing.
    I can then use an explicit TOML file configuration. I can now easily update the file if necessary to be efficient in
    debugging, without changing the code directly.

    4. Once the step 3 is done, I want to be able to deploy a released and tagged version of my application in
    several remote environments (e.g. pre-production, production). I am creating one TOML file per remote environment
    with a few values that differ from step 3, and on each environment, I am setting a different environment
    variable value to point to the right TOML configuration file.

These methods are described below.

# Python code configuration

A code configuration can be done on a Python file directly when designing the pipelines and scenarios. This
configuration can be done using methods from the `Config^` class. This python configuration is meant to be used
during the application development phase. It overrides the default configuration:
if some values are not provided, the default configuration applies.

!!! Example "Design of the application to configure"

    ![scenarios](../pic/scenarios.svg){ align=left }

    Let's imagine we want to configure an application corresponding to the design described in the picture. We use
    the following python configuration code.

    === "Python configuration"

        Below is the python code corresponding to the design above.

        ```py linenums="1" title="my_config.py"
        from datetime import datetime
        from my_functions import plan, predict, train
        from taipy import Config, Frequency, Scope

        # Configure all six data nodes
        sales_history_cfg = Config.configure_csv_data_node(id="sales_history",
                                                           scope=Scope.GLOBAL,
                                                           default_path="my/file/path.csv")
        trained_model_cfg = Config.configure_data_node(
            id="trained_model",
            scope=Scope.CYCLE)
        current_month_cfg = Config.configure_data_node(
            id="current_month",
            scope=Scope.CYCLE,
            default_data=datetime(2020, 1, 1))
        sales_predictions_cfg = Config.configure_data_node(
            id="sales_predictions",
            scope=Scope.CYCLE)
        capacity_cfg = Config.configure_data_node(id="capacity")
        production_orders_cfg = Config.configure_sql_data_node(
            id="production_orders",
            db_username="admin",
            db_password="ENV[PWD]",
            db_name="production_planning",
            db_engine="mssql",
            read_query="SELECT * from production_order",
            write_table="production_order")

        # Configure the three tasks
        training_cfg = Config.configure_task(
            "training",
            train,
            sales_history_cfg,
            [trained_model_cfg])
        predicting_cfg = Config.configure_task(id="predicting",
                                               function=predict,
                                               input=[trained_model_cfg, current_month_cfg],
                                               output=sales_predictions_cfg)
        planning_cfg = Config.configure_task(id="planning",
                                             function=plan,
                                             input=[sales_predictions_cfg, capacity_cfg],
                                             output=[production_orders_cfg])

        # Configure the two pipelines
        sales_pipeline_cfg = Config.configure_pipeline(
            id="sales",
            task_configs=[training_cfg, predicting_cfg])
        production_pipeline_cfg = Config.configure_pipeline(
            id="production",
            task_configs=[planning_cfg])

        # Configure the scenario
        monthly_scenario_cfg = Config.configure_scenario(
            id="scenario_configuration",
            pipeline_configs=[sales_pipeline_cfg, production_pipeline_cfg],
            frequency=Frequency.MONTHLY)
        ```

        The `train`, `predict`, and `plan` methods used in lines 32, 36, and 40 are the user functions imported in
        line 2 from the module `my_functions` that represents a user python module.

    === "my_functions.py module"

        The following module "my_function" is imported in the python configuration.

        ```py linenums="1" title="my_functions.py"
        import pandas as pd

        def train(sales_history: pd.DataFrame):
            print("Running training")
            return "TRAINED_MODEL"

        def predict(model, current_month):
            print("Running predicting")
            return "SALES_PREDICTIONS"

        def plan(sales_predictions, capacity):
            print("Running planning")
            return "PRODUCTION_ORDERS"
        ```

    === "_TOML_ export of the python configuration"

        The following file is the TOML version of the python configuration.

        ```toml linenums="1" title="config.toml"
        [TAIPY]

        [JOB]

        [DATA_NODE.sales_history]
        storage_type = "csv"
        scope = "GLOBAL"
        default_path = "my/file/path.csv"
        has_header = "True:bool"
        cacheable = "False:bool"

        [DATA_NODE.trained_model]
        storage_type = "pickle"
        scope = "CYCLE"
        cacheable = "False:bool"

        [DATA_NODE.current_month]
        storage_type = "pickle"
        scope = "CYCLE"
        default_data = 2020-01-01T00:00:00
        cacheable = "False:bool"

        [DATA_NODE.sales_predictions]
        storage_type = "pickle"
        scope = "CYCLE"
        cacheable = "False:bool"

        [DATA_NODE.capacity]
        storage_type = "pickle"
        scope = "SCENARIO"
        cacheable = "False:bool"

        [DATA_NODE.production_orders]
        storage_type = "sql"
        scope = "SCENARIO"
        db_username = "admin"
        db_password = "ENV[PWD]"
        db_name = "production_planning"
        db_host = "localhost"
        db_engine = "mssql"
        db_driver = "ODBC Driver 17 for SQL Server"
        read_query = "SELECT * from production_order"
        write_table = "production_order"
        db_port = "1433:int"
        cacheable = "False:bool"

        [TASK.training]
        inputs = [ "sales_history",]
        outputs = [ "trained_model",]

        [TASK.predicting]
        inputs = [ "trained_model", "current_month",]
        outputs = [ "sales_predictions",]

        [TASK.planning]
        inputs = [ "sales_predictions", "capacity",]
        outputs = [ "production_orders",]

        [PIPELINE.sales]
        tasks = [ "training", "predicting",]

        [PIPELINE.production]
        tasks = [ "planning",]

        [SCENARIO.scenario_configuration]
        pipelines = [ "sales", "production",]
        frequency = "MONTHLY"
        ```

        Note that the type of the non-string configuration attributes is specified in the _TOML_ file by adding at the
        end of the value (':bool', ':int', or ':float').

!!! warning "Security"

    Note that in line 15 of the python code, and in line 37 of the _TOML_ export, the password is not exposed. The
    property's value is a template referencing the environment variable _PWD_ that contains the value.
    It must be exported as follows:
    ``` commandline
    export PWD=my_pwd
    ```
    See section [environment-based configuration](#attribute-in-an-environment-variable) for more details.

# Explicit TOML file configuration

Taipy also provides file configuration. Indeed, a _TOML_ file can be explicitly provided by the developer to the Taipy
application using Python coding such as :

```py linenums="1"
from taipy import Config

Config.load("folder/config.toml")
```

This file configuration overrides the attributes in the code configuration (and the default configuration).
Here is an example of a _TOML_ file overriding the code configuration provided above as an example :

```toml linenums="1" title="folder/config.toml"
[JOB]
mode = "standalone"
nb_of_workers = 5

[DATA_NODE.sales_history]
storage_type="csv"
default_path="./path/to/my/file.csv"
```

Two behaviors occur if the previous _TOML_ file is used as file configuration. First, the Taipy application now has
five workers (By default, the number of workers is 1). Then, the sales_history data node now is a CSV data node
pointing to the file `./path/to/my/file.csv`. All other configuration fields remain unchanged.

# Environment variable file configuration

Finally, if the environment variable `TAIPY_CONFIG_PATH` is defined with the path of a _TOML_ config, Taipy will
automatically load the file and override the previous configurations (explicit file configuration, code configuration
and default configuration).

This functionality can be handy to change the configuration of a Taipy application without having to restart it.

# Attribute in an environment variable

Configuration can be set dynamically using environment variables with the syntax `ENV[MY_VARIABLE]`. This syntax can
be used both in python configuration or _TOML_ configuration. At runtime, Taipy will search for `MY_VARIABLE` among the
environment variables then use it.

This can be used to set a different configuration field value depending on the environment on which the application
will run. This is also especially useful if you want to use secret strings such as host names, usernames or passwords.
For example, if you are using Airflow as a Taipy scheduler, you can hide the password from the configuration file
using an environment variable.

Let's take an example with two environment variables. One string password and one integer value. You can export the
`PWD` and `NB_WORKERS` variables with the following command lines

```commandline linenums="1"
    export PWD=MySeCrEtPaSsWoRd
    export NB_WORKERS=4
```

and refer to it with the following Taipy configuration:

=== "python configuration"

    ```py linenums="1"
    from taipy import Config

    Config.configure_global_app(password="ENV[PWD]", nb_workers="ENV[NB_WORKERS]")
    ```

=== "_TOML_ configuration"

    ```toml linenums="1"
    [JOB]
    password = "ENV[PWD]"
    nb_workers = "ENV[NB_WORKERS]:int"
    ```

    Note that if the type of the configuration attribute is not a string, it must be specified in the _TOML_ file
    (':bool', ':int', ':float').

# Exporting configuration

Taipy also provides a method to export the compiled configuration applied after the compilation of all the
configurations (default, Python code, explicit file, and environment variable configurations) which is the result of
the overwriting.

```python linenums="1"
from taipy import Config

Config.export("config.toml")
```
