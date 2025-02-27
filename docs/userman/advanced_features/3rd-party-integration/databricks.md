# Databricks Integration

!!! note "Available in Taipy Enterprise edition"
    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

## Installation

To use the Databricks integration, you need to install the optional package. You can do
this using pip:

```bash
pip install taipy[databricks]
```

## Overview

The Databricks integration provides the following features:

- **Databricks Task**: A Taipy Task that triggers a Databricks Workflow when submitted for
    execution.
- **Databricks Table Data Node**: A Taipy Data Node that represents a table in Databricks
    Delta Live Tables database.
- **Databricks SQL Data Node**: A Taipy Data Node that represents a SQL query in Databricks
    Delta Live Tables database.

## Databricks Table Data Node

A `DatabricksTableDataNode` is a specific data node used to model Databricks table data. The
usage of a `DatabricksTableDataNode` is similar to a normal data node, allowing user to read,
write and append data from or to Databricks tables seamlessly with `read()`, `write()` and
`append()` functions. To add a new *Databricks Table* data node configuration, the
`Config.configure_databricks_table_data_node()` method can be used. In addition to the
generic parameters described in the
[data node configuration attributes](../../scenario_features/data-integration/data-node-config.md#config-attributes)
section, the following parameters can be provided:

- _**table_name**_ represents the name of the Databricks table used to read and write
    data pointed by the data nodes instantiated from the *Databricks Table* configuration.
    <br/>
    It is used to populate the table name property of the entities (*Databricks Table* data
    nodes) instantiated from the *Databricks Table* data node configuration. That means by
    default all the entities (*Databricks Table* data nodes) instantiated from the same
    *Databricks Table* configuration will inherit/share the same table name provided in
    the table_name. To avoid this, the table name property of a *Databricks Table* data node
    entity can be changed at runtime right after its instantiation.<br/>
- _**profile**_ represents additional options of Databricks credential profile to be used when
    reading and writing to the table.<br/>
- _**conn_string**_ represents the Databricks connection string starting with
    "sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab".
- _**host**_ represents Databricks Workspace URL such as https://foo-workspace.cloud.databricks.com/"
- _**cluster_id**_ represents additional options of the ID of Databricks cluster to be
    used when reading and writing to the table.<br/>
- _**token**_ indicates the Databricks personal access token used to authenticate into
    the cluster and on whose behalf the queries are executed.
- _**exposed_type**_ indicates the data type returned when reading the data node:

    - By default, *exposed_type* is "spark", and the data node reads the Databricks table
        as a Spark DataFrame (`pyspark.sql.dataframe.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "pandas", and the data node reads the Databricks table
        as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "numpy", the data node reads the Databricks table
        as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the *exposed_type* provided is "polars", and the data node reads the Databricks table
        as a Polars DataFrame (`polars.DataFrame`) when executing the read method.

To configure a Databricks SQL data node, use the `configure_databricks_table_data_node` method:

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/data-node-config-table-databricks.py"
    comments=false
    %}
    ```

    In lines 4-10, we configure a basic Databricks Table data node with the id
    "historical_temperature". The data node will point to the Databricks table
    "hist_temp". Its *scope* is by default `SCENARIO`. The profile to be used is
    "default" profile with the cluster id is "0123-456789-dbscluster2". The exposed
    type of this data node will be "pandas".

    In lines 12-17, we configure another Databricks Table data node with the identifier "log_history".
    It uses the `GLOBAL` scope. The Databricks table name is "hist_log". The credential
    to connect to Databricks database is provided through `conn_string` with the string
    `"sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab"`.
    The exposed type of this data node will be the default value "spark".

    In lines 19-21, we create a global data node of from "log_history" data node config.
    We then read from this data node, as it returns a `pyspark.DataDataFrame`, we then called
    `pyspark.DataFrame.show(5)` to display the first 5 rows from the DataFrame.


!!! note

    To configure a Databricks Table data node, it is equivalent to using the method
    `Config.configure_databricks_table_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="databricks_table"`. When configuring a Databricks Table Data Node,
    either the profile parameter, or the conn_string parameter, or a combination of the profile and
    cluster_id, or a combination of the host, token and cluster_id parameters should be specified,
    but not all four. If none of these parameters are provided, the default Databricks profile,
    created with databricks-cli, will be used. The value the host, token and cluster_id parameters
    can also be provided as environment parameters under the name DatabricksToken, DatabricksHost,
    DatabricksClusterId. If multiple combinations are provided, the following order will be prioritized:
    profile with cluster_id, conn_string, host with token and cluster_id.


## Databricks SQL Data Node

A `DatabricksSQLDataNode` data node is a specific data node used to model Databricks SQL data. The usage of  a
`DatabricksSQLDataNode` is similar to a normal data node, allowing user to read, write and append data from or to
Databricks tables seamlessly with `read()`, `write()` and `append()` functions by executing SQL queries provided
by the user. To add a new *Databricks SQL* data node configuration, the `Config.configure_databricks_sql_data_node()`
method can be used. In addition to the generic parameters described in the
[data node configuration attributes](../../scenario_features/data-integration/data-node-config.md#config-attributes)
section, the following parameters can be provided:

- _**read_query**_ represents the SQL query that will be used by Taipy to read the data
    from the Databricks database.
- _**write_query_builder**_ is a callable function that takes in the data as an input
    parameter and returns a list of SQL queries to be executed when the write method is
    called.
- _**append_query_builder**_ is a callable function that takes in the data as an input
    parameter and returns a list of SQL queries to be executed when the append method is
    called.
- _**read_query_parameter**_ represents parameters to be used when executing the read
    query. Default is None
- _**write_query_parameter**_ represents parameters to be used when executing the write
    query. Default is None
- _**append_query_parameter**_ represents parameters to be used when executing the append
    query. Default is None
- _**profile**_ represents additional options of Databricks credential profile to be used
    when reading and writing to the table.<br/>
- _**conn_string**_ represents the Databricks connection string starting with
    "sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab".
- _**host**_ represents Databricks Workspace URL such as
    "https://foo-workspace.cloud.databricks.com/"
- _**cluster_id**_ represents additional options of the ID of Databricks cluster to be
    used when reading and writing to the table.<br/>
- _**token**_ indicates the Databricks personal access token used to authenticate into
    the cluster and on whose behalf the queries are executed.
- _**exposed_type**_ indicates the data type returned when reading the data node:

        - By default, *exposed_type* is "spark", and the data node reads the Databricks table
            as a Spark DataFrame (`pyspark.sql.dataframe.DataFrame`) when executing the read method.
        - If the *exposed_type* provided is "pandas", and the data node reads the Databricks table
            as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
        - If the *exposed_type* provided is "numpy", the data node reads the Databricks table
            as a NumPy array (`numpy.ndarray`) when executing the read method.
        - If the *exposed_type* provided is "polars", and the data node reads the Databricks table
            as a Polars DataFrame (`polars.DataFrame`) when executing the read method.

To configure a Databricks SQL data node, use the `configure_databricks_sql_data_node` method:

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/data-node-config-sql-databricks.py"
    comments=false
    %}
    ```

    In lines 35-44, we configure a basic Databricks SQL data node with the id "historical_temperature".
    The data node will use the query "SELECT * FROM hist_temp" to read data from Databricks database.
    It will use "build_hist_temp_write_query" function and "build_hist_temp_append_query" function
    to build the write and append queries to write and append data to Databricks database.
    Its *scope* is `GLOBAL`. The profile to be used is "default" profile with the cluster id is
    "0123-456789-dbscluster2". The exposed type of this data node will be the default value "spark".

    In lines 46-53, we configure a basic Databricks SQL data node with the id "historical_log". The data node
    will use the query "SELECT * FROM hist_log" to read data from Databricks database. It will use
    "build_hist_log_write_query" function and "build_hist_log_append_query" function to build the write and
    append queries to write and append data to Databricks database. Its *scope* is by default `SCENARIO`.
    The credential to connect to Databricks database is provided through `conn_string` with the string
    `"sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab"`.
    The exposed type of this data node will be the default value "polars".

    In lines 55-57, we create a global data node of from "historical_temperature" data node config.
    We then read from this data node, as it returns a `pyspark.DataDataFrame`, we then called
    `pyspark.DataFrame.show(5)` to display the first 5 rows from the DataFrame.

!!! note

    To configure a Databricks SQL data node, it is equivalent to using the method
    `Config.configure_databricks_sql_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="databricks_sql"`. When configuring a Databricks SQL Data Node,
    either the profile parameter, or the conn_string parameter, or a combination of the profile and
    cluster_id, or a combination of the host, token and cluster_id parameters should be specified,
    but not all four. If none of these parameters are provided, the default Databricks profile,
    created with databricks-cli, will be used. The value the host, token and cluster_id parameters
    can also be provided as environment parameters under the name DatabricksToken, DatabricksHost,
    DatabricksClusterId. If multiple combinations are provided, the following order will be prioritized:
    profile with cluster_id, conn_string, host with token and cluster_id.

## Tasks

A task configuration is necessary to instantiate a Databricks `Task^`. To create a
`TaskConfig^` for Databricks task, you can use the `Config.configure_databricks_task()^` method
with the following parameters:

- _**id**_: The id of the task configuration to be created. This id is **mandatory** and must
    be a unique and valid Python identifier.
- _**job_name**_: The Databricks job in the workflow to be called by Taipy.
- _**inputs**_: The input data nodes referring to the *function*'s parameter(s) data to be
    executed.
- _**outputs**_: The output data nodes referring to the result(s) data of the *function*
    to be executed.
- _**skippable**_: Boolean attribute indicating if the task execution can be skipped if
    all output data nodes are up-to-date (see the *validity_period* attribute in the
    [data node configuration](../../scenario_features/data-integration/data-node-config.md#config-attributes)
    page). The default value of *skippable* is False.
- _**workspace_url**_: The parameters to be passed to the Databricks job. The default is None.
- _**bearer_token**_: The time interval in seconds to fetch the Databricks job status.
    The default is 10 as for 10 seconds.
- _**job_parameters**_: The maximum number of attempts to fetch the Databricks. The default
    is 10.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/task-config-databricks.py"
    comments=false
    %}
    ```

    In the example above, we created a `TaskConfig^` named `run_prediction`.

    In lines 4-37, three data node configurations are created. They will be used
    respectively as input data node and output data node of the tasks created from
    `TaskConfig^ `run_prediction`.

    Finally, on line 40-46, we create the task configuration with the id *run_prediction*.
    It represents the job `simple_linear_regression_job` in the Databricks Workflow.
    On line 45, the Task configuration has been set as `skippable`. That means when
    submitting a Task entity instantiated from this TaskConfig, Taipy will skip its
    execution if its input data nodes haven't changed since the previous execution.

!!! Note

    During the execution of a Databricks task, the input data in input data node will
    not be read and passed to the task for execution. And the output data will not be
    written to the output data node.

## References

For more details, refer to the
[Data Node Configuration](../../scenario_features/data-integration/data-node-config.md),
and [Data Node Usage](../../scenario_features/data-integration/data-node-usage.md) pages.
