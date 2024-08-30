Taipy provides three ways to configure your application:

- A Python code configuration
- An explicit file configuration using TOML format
- A file configuration provided through an environment variable

!!! example

    Here is a typical workflow that shows how to adapt the configuration of a Taipy application at each stage of a
    software project (from initial development to production).

    1. As a developer, I will design my application by configuring all the new entities (data nodes, tasks, scenarios)
    using the Python code configuration with just a few attributes configured. The default configuration is used
    for the other attributes.

    2. Then, I test the application I just built. At this step, I need my application to have a more realistic
    behavior, like real data. For that, I need more configuration. I can specify for my
    specific input dataset what file to use. I am using the Python code configuration for that.

    3. Once I am satisfied with my application running on my local dev environment, I will deploy it to a remote
    environment for testing. It is a dedicated environment made for testing deployment and integration testing.
    I can then use an explicit TOML file configuration. I can now easily update the file when needed to
    debug efficiently without changing the code directly.

    4. Once step 3 is completed, I want to deploy a released and tagged version of my application across
    several remote environments (e.g., pre-production and production). I create one TOML file per remote
    environment with a few values that differ from step 3. For each environment, I set the environment
    variable TAIPY_CONFIG_PATH (see below) to point to the right TOML configuration file.

These methods are described below.

# Python code configuration

The configuration (for all your data nodes, tasks, scenarios, etc.) can be defined directly using Python
code. This configuration can be done using methods from the `Config^` class. This Python configuration is meant to
be used during the application development phase. It overrides the default configuration:
the default configuration applies if some values are not provided.

!!! example "Design of the application to configure"

    ![scenarios](img/scenarios.svg){ align=left }

    Let's imagine we want to configure an application corresponding to the design described in the picture. We use
    the following Python configuration code.

    === "Python configuration"

        Below is the Python code corresponding to the design above.

        ```python linenums="1" title="my_config.py"
        from datetime import datetime
        from my_functions import write_orders_plan, compare, plan, predict, train
        from taipy import Config, Frequency, Scope

        # Configure all six data nodes
        sales_history_cfg = Config.configure_csv_data_node(
            id="sales_history", scope=Scope.GLOBAL, default_path="path/sales.csv"
        )
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
        orders_cfg = Config.configure_sql_data_node(
            id="orders",
            db_username="admin",
            db_password="ENV[PWD]",
            db_name="production_planning",
            db_engine="mssql",
            read_query=("SELECT orders.ID, orders.date, products.price, "
                        "orders.number_of_products FROM orders INNER JOIN "
                        "products ON orders.product_id=products.ID"),
            write_query_builder=write_orders_plan,
            db_driver="ODBC Driver 17 for SQL Server",
        )

        # Configure the three tasks
        training_cfg = Config.configure_task(
            "training",
            train,
            sales_history_cfg,
            [trained_model_cfg])
        predicting_cfg = Config.configure_task(
            id="predicting",
            function=predict,
            input=[trained_model_cfg, current_month_cfg],
            output=sales_predictions_cfg
        )
        planning_cfg = Config.configure_task(
            id="planning",
            function=plan,
            input=[sales_predictions_cfg, capacity_cfg],
            output=[orders_cfg]
        )

        # Configure the scenario
        monthly_scenario_cfg = Config.configure_scenario(
            id="scenario_configuration",
            task_configs=[training_cfg, predicting_cfg, planning_cfg],
            frequency=Frequency.MONTHLY,
            comparators={sales_predictions_cfg.id: compare},
            sequences={"sales": [training_cfg, predicting_cfg], "production": [planning_cfg]}
        )
        ```

        The `train`, `predict`, and `plan` methods used in lines 22, 24, and 28 are the user functions imported in line
        2 from the module `my_functions` that represents a user Python module.

    === "my_functions.py module"

        The following module "my_function" is imported in the Python configuration.

        ```python linenums="1" title="my_functions.py"
        import pandas as pd

        def write_orders_plan(data: pd.DataFrame):
            insert_data = data[["date", "product_id", "number_of_products"]].to_dict("records")
            return [
                "DELETE FROM orders",
                ("INSERT INTO orders VALUES (:date, :product_id, :number_of_products)", insert_data)
            ]

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

<a name="studio"></a>
!!! note "Studio"

    You can use [Taipy Studio](../../ecosystem/studio/index.md) for your Python code configuration. Taipy Studio
    generates a TOML file that you can load using the following code:

    === "Load your Studio config file"

        The _config.toml_ file contains the TOML generated by Studio equivalent to the previous Python code
        configuration.

        ``` py linenums="1"
        from taipy import Config

        Config.load("config.toml")
        ```

    === "config.toml: TOML file generated by Studio"

        The following file is the TOML version of the Python code configuration.

        ```toml linenums="1" title="config.toml"
        [TAIPY]

        [JOB]

        [DATA_NODE.sales_history]
        storage_type = "csv"
        scope = "GLOBAL:SCOPE"
        default_path = "path/sales.csv"
        has_header = "True:bool"
        exposed_type = "pandas"

        [DATA_NODE.trained_model]
        storage_type = "pickle"
        scope = "CYCLE:SCOPE"

        [DATA_NODE.current_month]
        storage_type = "pickle"
        scope = "CYCLE:SCOPE"
        default_data = "2020-01-01T00:00:00:datetime"

        [DATA_NODE.sales_predictions]
        storage_type = "pickle"
        scope = "CYCLE:SCOPE"

        [DATA_NODE.capacity]
        storage_type = "pickle"
        scope = "SCENARIO:SCOPE"

        [DATA_NODE.orders]
        storage_type = "sql"
        scope = "SCENARIO:SCOPE"
        db_username = "admin"
        db_password = "admin_pwd"
        db_name = "production_planning"
        db_host = "localhost"
        db_engine = "mssql"
        db_driver = "ODBC Driver 17 for SQL Server"
        read_query = "SELECT orders.ID, orders.date, products.price, orders.number_of_products FROM orders INNER JOIN products ON orders.product_id=products.ID"
        write_query_builder = "functions.write_orders_plan:function"
        db_port = "1433:int"
        exposed_type = "pandas"

        [TASK.training]
        inputs = [ "sales_history:SECTION",]
        function = "functions.train:function"
        outputs = [ "trained_model:SECTION",]
        skippable = "False:bool"

        [TASK.predicting]
        inputs = [ "trained_model:SECTION", "current_month:SECTION",]
        function = "functions.predict:function"
        outputs = [ "sales_predictions:SECTION",]
        skippable = "False:bool"

        [TASK.planning]
        inputs = [ "sales_predictions:SECTION", "capacity:SECTION",]
        function = "functions.plan:function"
        outputs = [ "orders:SECTION",]
        skippable = "False:bool"

        [SCENARIO.scenario_configuration]
        tasks = [ "training:SECTION", "predicting:SECTION", "planning:SECTION",]
        frequency = "MONTHLY:FREQUENCY"

        [SCENARIO.scenario_configuration.comparators]
        sales_predictions = [ "functions.compare:function",]

        [SCENARIO.scenario_configuration.sequences]
        sales = [ "training:SECTION", "predicting:SECTION",]
        production = [ "planning:SECTION",]
        ```

        Note that the type of the non-string configuration attributes is specified in the TOML file by adding at the
        end of the value (':bool', ':int', or ':float').

!!! warning "Security"

    Note that in line 15 of the Python code, and in line 37 of the TOML export, the password is not exposed. The
    property's value is a template referencing the environment variable _PWD_ that contains the value.
    It must be exported as follows:
    ``` commandline
    export PWD=my_pwd
    ```
    See section [Attribute in an env variable](#attribute-in-an-env-variable) for more details.

# Override using explicit TOML file

Taipy also provides file configuration. Indeed, a TOML file can be explicitly provided by the developer to the Taipy
application using Python coding such as:

```python linenums="1"
from taipy import Config

Config.override("config.toml")
```

This file configuration overrides the attributes in the code configuration (and the default configuration).
Here is an example of a TOML file overriding the code configuration provided above as an example:

```toml linenums="1" title="folder/config.toml"
[JOB]
mode = "standalone"
max_nb_of_workers = 5

[DATA_NODE.sales_history]
storage_type="csv"
default_path="./path/to/my/file.csv"
```

Two behaviors occur if the previous TOML file is used as file configuration. First, the Taipy application now has
five workers (By default, the number of workers is 2). Then, the sales_history data node now is a CSV data node
pointing to the file `./path/to/my/file.csv`. All other configuration fields remain unchanged.

# Override with file in env variable

Finally, if the environment variable `TAIPY_CONFIG_PATH` is defined with the path of a TOML config, Taipy will
automatically load the file and override the previous configurations (explicit file configuration, code
configuration, and default configuration).

This functionality can be handy for changing the configuration of a Taipy application without having to restart it.

# Attribute in an env variable

Configuration can be set dynamically using environment variables with the syntax `ENV[MY_VARIABLE]`. This syntax can
be used both in Python configuration or TOML configuration. At runtime, Taipy will search for `MY_VARIABLE` among the
environment variables and then use it.

It can be used to set a different configuration field value depending on the application's environment. It is
also especially useful if you want to use secret strings such as host names, usernames or passwords.
For example, you can hide a password from the configuration file using an environment variable.

Let's take an example with two environment variables. One string password and one integer value. You can export the
`PWD` and `NB_USERS` variables with the following command lines

```commandline linenums="1"
    export PWD=MySeCrEtPaSsWoRd
    export NB_USERS=4
```

and refer to it with the following Taipy configuration:

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_global_app(password="ENV[PWD]", max_nb_users="ENV[NB_USERS]")
    ```

=== "TOML configuration"

    ```toml linenums="1"
    [JOB]
    password = "ENV[PWD]"
    max_nb_users = "ENV[NB_USERS]:int"
    ```

    Note that if the type of the configuration attribute is not a string, it must be specified in the TOML file
    (':bool', ':int', ':float').

# Loading and exporting configuration

Taipy provides some APIs to export and load its configurations.

## Load
!!! note

    Changed in version 2.1. Now it only replaces the Python code configuration.

Load a configuration file and replace the Python code configuration.

```python linenums="1"
from taipy import Config

Config.load("config.toml")
```

## Export
!!! note

    Changed in version 2.1. Now it only exports the Python code configuration.

Export the Python code configuration:

```python linenums="1"
from taipy import Config

Config.export("config.toml")
```


## Backup
!!! note

    New in version 2.1.

Backup the applied configuration:

```python linenums="1"
from taipy import Config

Config.backup("config.toml")
```

## Restore
!!! note

    New in version 2.1.

Load a configuration file and replace the applied configuration.

```python linenums="1"
from taipy import Config

Config.restore("config.toml")
```

## Override
!!! note

    New in version 2.1.

Load a configuration file, replace the current file configuration and triggers a re-computation of the applied
configuration.

```python linenums="1"
from taipy import Config

Config.override("config.toml")
```
