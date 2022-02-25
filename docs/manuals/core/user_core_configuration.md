Taipy core is an application builder that converts user algorithms into a back-end application. To build such
an application with the desired behaviors, a few Taipy entities must be configured.
The taipy configuration methods can easily be imported from the Taipy main module as follows:

```python
import taipy as tp
```

The following sections show how to configure the Taipy entities in python. Note that you can override the
python configuration using _TOML_ files. (More details on the [toml configuration](user_core_advanced_configuration.md))
page.

# Data node configuration

For Taipy to instantiate a data node, a data node configuration must be provided.
[`DataNodeConfig`](../../reference/#taipy.core.config.data_node_config.DataNodeConfig) is
used to configure the various data nodes Taipy will manipulate. To configure a new `DataNodeConfig`,
here is the list of the configurable attributes :

-   The config `name` corresponds to the identifier of the data node config. It is a **mandatory** parameter
    that must be unique. We strongly recommend using lowercase alphanumeric characters, dash character '-', or
    underscore character '\_' (a name compatible with a python variable name).
-   The `scope` attribute is from type [`Taipy.Scope`](../../reference/#taipy.core.data.scope.Scope).
    It corresponds to the scope of the data node instantiated from the data node configuration.
    The **default value** is `Scope.SCENARIO`.
-   The storage `storage_type` is a parameter that corresponds to the type of storage of the data node. The possible values are ["pickle"](#../../reference/#taipy.core.data.pickle.PickleDataNode) (**the default value**), ["csv"](#../../reference/#taipy.core.data.csv.CSVDataNode), ["excel"](#../../reference/#taipy.core.data.excel.ExcelDataNode), ["generic"](#../../reference/#taipy.core.data.generic.GenericDataNode), ["in_memory"](#../../reference/#taipy.core.data.in_memory.InMemoryDataNode), ["sql"](#../../reference/#taipy.core.data.sql.SQLDataNode).
    As explained in the following subsections, depending on the `storage_type`, other configuration attributes
    will need to be provided in the `properties` parameter.
-   Any other custom attribute can be provided through the `properties` dictionary (a description, a tag, etc.)
    All the properties will be given to the data nodes instantiated from this data node configuration.
    This `properties` dictionary is also used to configure the parameters specific to each storage type.

To configure a new data node into Taipy, you must use the `taipy.configure_data_node()` method.

!!! example

    Here are two examples of data node configurations.

    ```python
    import taipy as tp
    from taipy import Scope

    # We configure a simple data node. The name identifier is "date_cfg",
    # the scope is "SCENARIO" (default value), the storage type is "pickle" (default value),
    # and we added an optional custom description.
    date_cfg = tp.configure_data_node(name="date_cfg", description="The current date of the scenario")

    # We then add another data node configuration. The name identifier is "model_cfg", the scope is "CYCLE"
    # so the corresponding data node will be shared by all the scenarios from the same cycle,
    # the storage_type is "pickle" as well, and an optional custom description is given.
    model_cfg = tp.configure_data_node(name="model_cfg",
                                       scope=Scope.CYCLE,
                                       storage_type="pickle",
                                       description="The trained model shared by all scenarios")
    ```

### Pickle

A pickle data node is a specific data node used to model pickle data. To add a new _pickle_ data node
configuration, the `taipy.configure_pickle_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), two optional
parameters can be provided.

-   The `path` parameter represents the file path used by Taipy to read and write the data.
    If the pickle file already exists (in the case of a shared input data node, for instance), it is necessary
    to provide the file path as the _path_ parameter. If no value is provided, Taipy will use an internal path
    in the Taipy storage folder (more details on the Taipy storage folder configuration available on the
    [Global configuration](user_core_configuration.md#global-configuration) documentation).

-   If the `default_data` is provided, the data node is automatically written with the corresponding
    value. Any serializable Python object can be used.

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple pickle data node. The name identifier is "date_cfg",
    # the scope is "SCENARIO" (default value), and a default data is provided.
    date_cfg = tp.configure_pickle_data_node(name="date_cfg", default_data=datetime(2022, 1, 25))

    # We then add another pickle data node configuration. The name identifier is "model_cfg", the default
    # SCENARIO scope is used. Since the data node corresponds to a pre-existing pickle file, a path
    # "path/to/my/model.p" is provided and we added an optional custom description.
    model_cfg = tp.configure_pickle_data_node(name="model_cfg",
                                              path="path/to/my/model.p",
                                              description="The trained model")
    ```

!!! Note

    To configure a pickle data node, it is equivalent to use the method `taipy.configure_pickle_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="pickle"`.

### Csv

A Csv data node is a specific data node used to model csv file data. To add a new _csv_ data node
configuration, the `taipy.configure_csv_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), one mandatory and two optional parameters can be provided.

-   The `path` parameter is a mandatory parameter and represents the csv file path used by Taipy to read and write the data.
-   The `has_header` parameter represents if the file has a header of not. If `has_header` is `True`, Taipy will use the 1st row in the csv file as the header. By default, `has_header` is `True`.
-   When the `exposed_type` is given as parameter, if the `exposed_type` value provided is `numpy`, the data node will read the csv file to a numpy array. If the provided value is a custom class, data node will create a list of custom object with the given custom class, each object will represent a row in the csv file.If `exposed_type` is not provided, the data node will read the csv file as a pandas DataFrame.

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple csv data node. The name identifier is "historical_temperature",
    # the scope is "SCENARIO" (default value), and the path is the file hist_temp.csv
    # with `has_header` being True, representing the csv file has a header.
    date_cfg = tp.configure_csv_data_node(name="historical_temperature", path="path/hist_temp.csv", has_header=True, exposed_type="numpy")

    # We then add another csv data node configuration. The name identifier is "sale_history", the
    # default SCENARIO scope is used. Since we have a custom class pre-defined for this csv file, we
    # will provide it in the `exposed_type`.
    model_cfg = tp.configure_pickle_data_node(name="sale_history",
                                              path="path/sale_history.csv",
                                              exposed_type=SaleRow)
    ```

!!! Note

    To configure a csv data node, it is equivalent to use the method `taipy.configure_csv_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="csv"`.

### Excel

An Excel data node is a specific data node used to model xlsx file data. To add a new _excel_ data node
configuration, the `taipy.configure_excel_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), a mandatory and three optional parameters can be provided.

-   The `path` is a mandatory parameter that represents the excel file path used by Taipy to read and write the data.
-   The `has_header` parameter represents if the file has a header of not. If `has_header` is `True`, Taipy will use the 1st row in the excel file as the header. By default, `has_header` is `True`.
-   The `sheet_name` parameter represents which specific sheet in the excel file to read. If `sheet_name` is provided with a list of sheet names, it will return a dictionary with the key being the sheet name and the value being the data of the corresponding sheet. If a string is provided, data node will read only the data of the coressponding sheet. The default value of `sheet_name` is "Sheet1"
-   When the `exposed_type` is given as parameter, if the `exposed_type` value provided is `numpy`, the data node will read the excel file to a numpy array. If the provided value is a custom class, data node will create a list of custom object with the given custom class, each object will represent a row in the excel file.If `exposed_type` is not provided, the data node will read the excel file as a pandas DataFrame.

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple excel data node. The name identifier is "historical_temperature",
    # the scope is "SCENARIO" (default value), and the path is the file hist_temp.xlsx
    # with `has_header` being True, representing the exceo file has a header.
    # The sheet_name is not provided so Taipy will use the default value "Sheet1"
    date_cfg = tp.configure_excel_data_node(name="historical_temperature", path="path/hist_temp.xlsx", has_header=True, exposed_type="numpy")

    # We then add another csv data node configuration. The name identifier is "sale_history", the default
    # SCENARIO scope is used. Since we have a custom class pre-defined for this excel file, we will provide it in the `exposed_type`.
    # We will provide the specific sheet names of the sheets we want to read
    model_cfg = tp.configure_excel_data_node(name="sale_history",
                                              path="path/sale_history.xlsx",
                                              sheet_names=["January", "February"]
                                              exposed_type=SaleRow)
    ```

!!! Note

    To configure an excel data node, it is equivalent to use the method `taipy.configure_excel_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="excel"`.

### Generic

An Generic data node is a specific data node used to model generic data type. To add a new _generic_ data node
configuration, the `taipy.configure_generic_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), two mandatory
parameters can be provided.

-   The `read_fct` is a mandatory parameter that represents a python function provided by the user. It will be used to read the data.
-   The `write_fct` is a mandatory parameter that represents a python function provided by the user. It will be used to write the data.

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple generic data node. The name identifier is "historical_data".
    # The `read_fct` and `write_fct` parameters are provided to read and write the data.
    date_cfg = tp.configure_generic_data_node(name="historical_data", read_fct=read_data, write_fct=write_data)
    ```

!!! Note

    To configure a generic data node, it is equivalent to use the method `taipy.configure_generic_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="generic"`.

### In memory

An in*memory data node is a specific data node used to model any data in the RAM. To add a new \_in_memory* data node
configuration, the `taipy.configure_in_memory_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), an optional
parameters can be provided.

-   If the `default_data` is given as parameter, the data node is automatically written with the corresponding
    value. Any python object can be used.

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple in_memory data node. The name identifier is "date_cfg",
    # the scope is "SCENARIO" (default value), and a default data is provided.
    date_cfg = tp.configure_in_memory_data_node(name="date_cfg", default_data=datetime(2022, 1, 25))
    ```

!!! Note

    To configure an in_memory data node, it is equivalent to use the method `taipy.configure_in_memory_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="in_memory"`.

### Sql

A Sql data node is a specific data node used to model Sql data. To add a new _sql_ data node
configuration, the `taipy.configure_sql_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), multiple
parameters can be provided.

-   The `db_username` parameter represents the database username that will be used by Taipy to access the database.
-   The `db_password` parameter represents the database user's password that will be used by Taipy to access the database.
-   The `db_name` parameter represents the name of the database.
-   The `db_engine` parameter represents the engine of the database.
-   The `read_query` parameter represents the SQL query that will be used by Taipy to read the data from the database.
-   The `write_table` parameter represents the name of the table in the database that Taipy will be writing the data to.
-   The `db_port` parameter represents the database port that will be used by Taipy to access the database. The default value of `db_port` is 1433

!!! example

    ```python linenums="1"
    import taipy as tp
    from taipy import Scope

    # We configure a simple sql data node. The name identifier is "historical_temperature",
    # the scope is "SCENARIO" (default value), and the database username is "admin"
    # The user's password is "password", the database name is "taipy". The database engine will # be mssql short for Microsoft SQL. The read query will be "SELECT * from daily_temp"
    # The table the data will be written to is "forecast_table"
    date_cfg = tp.configure_sql_data_node(name="historical_temperature", db_username="admin",
    db_password="password", db_name="taipy", db_engine="mssql",
    read_query="SELECT * from daily_min_example", "write_table"= "forecast_table")
    ```

!!! Note

    To configure a sql data node, it is equivalent to use the method `taipy.configure_sql_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="sql"`.

# Task configuration

Definition of a [Task](user_core_concepts.md#task).

Properties:

-   `name`: The name of this new task configuration. This name should be unique.
-   `inputs`: The inputs of the function.
-   `function`: The function to execute.
-   `outputs`: The function result(s).

Basic example:

```python linenums="1"
import taipy as tp

def double(nb):
    return nb * 2

input_data_node_config = tp.configure_data_node("input", default_value=21)
output_data_node_config = tp.configure_data_node("output")

task_config = tp.configure_task("double_task", double, input_data_node_config, output_data_node_config)
```

On the previous example, we are configuring a [Task](user_core_concepts.md#task) in Taipy to execute:

```python
output = double(21)
```

In lines 3 and 4, we define a function that we want to use in a [Task](user_core_concepts.md#task).
The Task configuration is done in lines 6 and 7. The function argument and result are represented as two data node configurations.
Finally, on line 9, we create the task configuration named 'double_task' that represents the function 'double' that expects the 'input'
data node as an input parameter and that returns the 'output' data node.

Because a Task can have several inputs and outputs, `tp.configure_task` can receive lists of `DataNodeConfig` objects.

We can have the same behavior by doing:

```python
import taipy as tp

def mult_by(nb, by):
    return nb * by

nb_to_multiple = tp.configure_data_node("nb_to_multiple", default_value=21)
multiply_by = tp.configure_data_node("multiply_by", default_value=2)

output_config = tp.configure_data_node("output")

task_config = tp.configure_task("foo", [nb_to_multiple, multiply_by], mult_by, output_config)
```

# Pipeline configuration

Definition of a [Pipeline](concepts.md#pipeline).

Properties:

-   `name`: The name of this new pipeline configuration. This name should be unique.
-   `tasks`: The list of tasks configs.
-   `properties`: The dictionary of additional properties.

Basic example:

```python linenums="1"
pipeline_config = tp.configure_pipeline("multiply_pipeline", [task_config])
```

On this example, we create a pipeline config which is made of a single task, identical to the one in the previous example.

# Scenario configuration

Definition of a [Scenario](user_core_concepts.md#scenario).

Properties:

-   `name`: The name of this new scenario configuration. This name should be unique.
-   `pipelines`: The list of pipeline configs.
-   `frequency`: The recurrence frequency of the scenario.
-   `comparators`: The list of functions to compare data nodes of scenarios shared the same scenario config.
-   `properties`: The dictionary of additional properties.

Basic example:

```python linenums="1"
scenario_config = tp.configure_scenario("multiply_scenario", [pipeline_config])
```

In this example, we create a scenario config which contains the pipeline that was defined in the previous example.

We can also create a new pipeline belonging to this new scenario config and using the two indicated tasks.

```python linenums="1"
scenario_config = tp.configure_scenario_from_tasks("multiply_scenario", [task_config], pipeline_name="multiply_pipeline")
```

# Global configuration
Holds configuration fields related to the global application.

Properties:

- `root_folder`: The path of the base folder for the taipy application. Default value is "./taipy/".
- `storage_folder`: The folder name used to store Taipy data. Default value is ".data/". It is used in conjunction with the root_folder field. That means the storage path is <root_folder><storage_folder> (Default path is "./taipy/.data/").
- `clean_entities_enabled`: The field to activate/deactivate the clean entities feature. Default value is false.
- `properties`: The dictionary of additional properties.

!!!Example
    ```python linenums="1"
        import taipy as tp
    
        tp.configure_global_app(
            root_folder=".taipy_root_folder/",
            storage_folder=".data_folder",
            clean_entities_enabled=True,
            properties={"custom_property": False}
            )
    ```

# Job configuration

The Job configuration allows the user to configure the Taipy behavior regarding the job executions.
Two main modes are available in Taipy : the standalone and the airflow mode (available in the enterprise
version only).

### Standalone

With the _standalone_ mode, Taipy executes the jobs on its own execution context.
You can configure the standalone mode with the following config:

```
[JOB]
mode = "standalone"
```

!!! Note

    Note that if no mode is configured, the standalone mode is used.

By default, Taipy executes each _job_ one by one, in a synchronous manner. You can ensure this behavior by setting:

```
[JOB]
mode = "standalone"
nb_of_workers = 1
```

!!! Note

    If no value is provided in the nb_of_workers setting in the configuration, Taipy will set this value to 1.

To execute the _jobs_ in parallel, you can set the number of workers to a positive integer value greater than 1.

Taipy will use multiple and asynchronous processes, and run each job in a dedicated process. The value of the variable `nb_of_workers` represents the maximum number of processes spawned in parallel. For example,the following configuration allows Taipy to run at most 8 jobs in parallel:

```
[JOB]
mode = "standalone"
nb_of_workers = 8
```

### Using Airflow

With the _airflow_ mode, Taipy delegates the job executions to an Airflow service. You can configure the
_airflow_ mode with the following config :

```
[JOB]
mode = "airflow"
```

#### Start Airflow from Taipy

To let Taipy start the Airflow service, you can use the following configuration:

```
[JOB]
start_airflow = True
```

By default, Airflow creates a local folder `.airflow` to store its dependencies.
You can change this location with the `airflow_folder` config:

```
[JOB]
airflow_folder = "my_custom_path"
```

!!! warning "Production setting"

    Taipy starts Airflow in `standalone` mode. It is an Airflow development mode and not recommended for production.

#### Use an external Airflow

By default, Taipy runs with an external Airflow. You can specify it by setting:

```
[JOB]
start_airflow = False
```

By default, Taipy is connected to Airflow on `localhost:8080`. You can change it:

```
[JOB]
hostname = "my_remote_airflow:port"
```

Taipy _jobs_ are converted in Airflow _DAG_ through the Airflow DAG Folder.
By default, this folder is `.dags`, but you can update it:

```
[JOB]
airflow_dags_folder = "/dags"
```

!!! note "Remote Airflow"

    The Airflow _Dag_ generation can only be accomplished through this folder.
    If Taipy and Airflow are not on the same machine or if Airflow uses remote workers, you must make sure that this folder is mounted in a shared mode.

Airflow can take time before loading _DAGS_.
In order to wait for Airflow to be ready to schedule tasks, Taipy requests the scheduling several times
until the request is actually accepted.
Depending on your Airflow configuration, you can update the number of retries:

```
[JOB]
airflow_api_retry = 10
```

Taipy authentication with Airflow is based on
[basic_auth](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#basic-authentication).
If Airflow is not started by Taipy, you should provide this configuration:

```
[JOB]
airflow_user = "user"
airflow_password = "pass"
```

!!! note "Security"

    To ensure you are not exposing your company's secrets, we recommend using 
    [environment-based configuration](user_core_advanced_configuration.md#attribute-in-an-environment-variable) for `airflow_user` and `airflow_password`.

# Check configuration

Taipy provides a checking mechanism to validate the configuration. 


You can trigger the check by calling:
```python linenums="1"
import taipy as tp

tp.check_configuration()
```

Currently there are 6 checkers implemented in Taipy:

- [`GlobalConfigChecker`](../../reference/#taipy.core.config.checker.checker.GlobalConfigChecker): checks if the `notification` property is populated with a Boolean.
- [`DataNodeConfigChecker`](../../reference/#taipy.core.config.checker.checker.DataNodeConfigChecker): checks if `storage_type` and `scope` properties have been provided. `DataNodeConfigChecker` also checks for specific required properties corresponding to its `storage_type`.
- [`TaskConfigChecker`](../../reference/#taipy.core.config.checker.checker.TaskConfigChecker): checks if `inputs` and `outputs` properties are populated with DataNode objects and a `Callable` function is provided for the `function` property.  
- [`PipelineConfigChecker`](../../reference/#taipy.core.config.checker.checker.PipelineConfigChecker): checks if the `tasks` property is populated correctly with a list of `TaskConfig` objects or a single `TaskConfig` object.
- [`ScenarioConfigChecker`](../../reference/#taipy.core.config.checker.checker.ScenarioConfigChecker): checks if the `pipelines` property is populated correctly with a list of `PipelineConfig` objects or a single `PipelineConfig` object. The `ScenarioConfigChecker` also checks if the `frequency` property is provided and if it is provided with a `Frequency` value. Lastly, it checks if any `comparators` are provided.
- [`JobConfigChecker`](../../reference/#taipy.core.config.checker.checker.JobConfigChecker): checks if multiprocess is turned on, if yes, checks if any `DataNodeConfigs` have the `storage_type` of `in_memory` as multiprocess cannot be used with `InMemoryDataNode`


# More details

For more details on how to override the python configuration, please read the documentation on the
[:material-arrow-right: TOML configuration](user_core_advanced_configuration.md)
