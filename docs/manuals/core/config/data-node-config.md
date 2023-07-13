# New data node config
To create an instance of a [Data node](../concepts/data-node.md), a data node
configuration must first be provided. `DataNodeConfig^` is used to configure data nodes.
To configure a new `DataNodeConfig^`, one can use the function `Config.configure_data_node()^`.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_simple.py"
comments=false
%}
```

We configured a simple data node in the previous code by providing an identifier
as the string "data_node_cfg". The `Config.configure_data_node()^` method actually
creates a data node configuration, and registers it in the `Config^` singleton.

The attributes available on data nodes are:

- _**id**_ is the string identifier of the data node config.<br/>
    It is the only **mandatory** parameter and must be a unique and valid Python identifier.
- _**scope**_ is a `Scope^`.<br/>
    It corresponds to the [scope](../concepts/scope.md) of the data node that will be instantiated
    from the data node configuration. The **default value** is `Scope.SCENARIO`.
- _**validity_period**_ is a [timedelta object](https://docs.python.org/3/library/datetime.html#timedelta-objects)
    that represents the duration since the last edit date for which the data node can be considered up-to-date.
    Once the validity period has passed, the data node is considered stale and relevant tasks will run even if they are
    skippable (see the [Task configs page](../config/task-config.md) for more details).
    If *validity_period* is set to the default value None, the data node is always up-to-date.
- _**storage_type**_ is an attribute that indicates the storage type of the
    data node.<br/>
    The possible values are ["pickle"](#pickle) (**the default value**), ["csv"](#csv),
    ["excel"](#excel), ["json"](#json), ["mongo_collection"](#mongo-collection),
    ["parquet"](#parquet), ["sql"](#sql), ["sql_table"](#sql_table),
    ["in_memory"](#in-memory), or ["generic"](#generic).<br/>
    As explained in the following subsections, depending on the *storage_type*, other
    configuration attributes must be provided in the *properties* parameter.
- Any other custom attribute can be provided through the parameter _**properties**_,
    a kwargs dictionary accepting any number of custom parameters (a description,
    a label, a tag, etc.) (It is recommended to read
    [doc](https://realpython.com/python-kwargs-and-args/) if you are not familiar with
    **kwargs arguments)
    <br/>
    This *properties* dictionary is used to configure the parameters specific to each
    storage type. It is copied in the dictionary properties of all the data nodes
    instantiated from this data node configuration.<br/>

!!! warning "Reserved keys"

    Note that we cannot use the word "_entity_owner" as a key in the properties as it has been reserved for internal use.

Below are two examples of data node configurations.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_two-examples.py"
comments=false
%}
```

In lines 4-7, we configured a simple data node with the id "date_cfg". The default value for *scope*
is `SCENARIO`. The *storage_type* is set to the default value "pickle".<br/>
An optional custom property called *description* is also added: this property is
propagated to the data nodes instantiated from this config.

In lines 9-16, we add another data node configuration with the id "model_cfg". The *scope* is set to
`CYCLE` so that all the scenarios from the same cycle will share the corresponding data nodes. The
*storage_type* is "pickle". The *validity_period* is set to 2 days, which indicate that the data node
is going to stale after 2 days of being modified. Finally, two optional custom properties are added:
a *description* string and an integer *code*. These two properties are propagated to the data nodes
instantiated from this config.

# Storage type

Taipy proposes predefined *data nodes* corresponding to the most popular
*storage types*. Thanks to predefined *data nodes*, the Python developer
does not need to spend much time configuring the *storage types* or the
*query system*. A predefined data node will often satisfy the user's
required format: pickle, CSV, SQL table, MongoDB collection, Excel sheet,
etc.

The various predefined *storage types* are typically used for input data.
Indeed, the input data is usually provided by external sources, where
the Python developer user does not control the format.

For intermediate or output *data nodes*, the developer often does not have
any particular specifications regarding the *storage type*. In such a case,
using the default *storage type* pickle that does not require any
configuration is recommended.

If a more specific method to store, read and write the data is needed, Taipy
provides a Generic data node that can be used for any storage type (or any
kind of query system). The developer only needs to provide two Python
functions, one for reading and one for writing the data. Please refer to the
[generic data node config section](#generic) for more details on generic data
node.

All predefined data nodes are described in the subsequent sections.

## Pickle

A `PickleDataNode^` is a specific data node used to model *pickle* data.
The `Config.configure_pickle_data_node()^` method configures a new *pickle*
data node configuration. In addition to the generic parameters described in
the [Data node configuration](data-node-config.md) section, two optional
parameters can be provided.

- _**default_path**_ represents the default file path used to read and write
  the data of the data nodes instantiated from the *pickle* configuration.<br/>
  It is used to populate the path property of the entities (*pickle* data nodes)
  instantiated from the *pickle* data node configuration. That means by default
  all the entities (*pickle* data nodes) instantiated from the same *pickle*
  configuration will inherit/share the same *pickle* file provided in the
  default_path. To avoid this, the path property of a *pickle* data node entity
  can be changed at runtime right after its instantiation.<br/>
  If no value is provided, Taipy will use an internal path in the Taipy storage folder
  (more details on the Taipy storage folder configuration are available in the
  [Global configuration](global-config.md) documentation).

- _**default_data**_ indicates data automatically written to the data node
  *pickle* upon creation.<br/>
  Any serializable Python object can be used. The default value is None.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_pickle.py"
comments=false
%}
```

In lines 4-6, we configure a simple pickle data node with the id "date_cfg".
The scope is `SCENARIO` (default value), and default data is provided.

In lines 8-11, we add another pickle data node configuration with the id "model_cfg".
The default `SCENARIO` scope is used. Since the data node config corresponds to a
pre-existing pickle file, a default path "path/to/my/model.p" is provided. We also
added an optional custom description.

!!! Note

    To configure a pickle data node, it is equivalent to using the method
    `Config.configure_pickle_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="pickle"`.

## CSV

A `CSVDataNode^` data node is a specific data node used to model CSV file data. To
add a new *CSV* data node configuration, the `Config.configure_csv_data_node()^` method
can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the *csv* configuration.<br/>
  It is used to populate the path property of the entities (*csv* data nodes)
  instantiated from the *csv* data node configuration. That means by default
  all the entities (*csv* data nodes) instantiated from the same *csv*
  configuration will inherit/share the same *csv* file provided in the
  default_path. To avoid this, the path property of a *csv* data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**has_header**_ indicates if the file has a header of not.<br/>
  By default, *has_header* is True and Taipy will use the 1st row in the CSV file as
  the header.

- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from a CSV data node with different *exposed_type* are available
  in the [Read / Write a data node](../entities/data-node-mgt.md#csv) documentation):
    - By default, *exposed_type* is "pandas", and the data node reads the CSV file
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "modin", the data node reads the CSV
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "numpy", the data node reads the CSV
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided *exposed_type* is a custom Python class, the data node creates
      a list of custom objects with the given custom class. Each object represents
      a row in the CSV file.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_csv.py"
comments=false
%}
```

In lines 3-5, we define a custom class `SaleRow` representing a row of the CSV file.

In lines 7-11, we configure a basic CSV data node with the identifier "historical_temperature".
Its *scope* is by default `SCENARIO`. The default path points to the file
"path/hist_temp.csv". The property *has_header* is set to True.

In lines 13-16, we configure another CSV data node with the identifier "log_history".
It uses the default `SCENARIO` scope again. The default path points to "path/hist_log.csv".
The *exposed_type* provided is "modin".

In lines 18-21, we add another CSV data node configuration with the identifier "sales_history".
The default `SCENARIO` scope is used again. Since we have a custom class called `SaleRow`
that is defined for this CSV file, we provide it as the *exposed_type* parameter.

!!! Note

    To configure a CSV data node, it is equivalent to using the method
    `Config.configure_csv_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="csv"`.

## Excel

An `ExcelDataNode^` is a specific data node used to model xlsx file data. To add a
new _Excel_ data node configuration, the `Config.configure_excel_data_node()^` method
can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, a mandatory and three optional
parameters are provided.

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the *Excel* configuration.<br/>
  It is used to populate the path property of the entities (*Excel* data nodes)
  instantiated from the *Excel* data node configuration. That means by default
  all the entities (*Excel* data nodes) instantiated from the same *Excel*
  configuration will inherit/share the same *Excel* file provided in the
  default_path. To avoid this, the path property of a *Excel* data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**has_header**_ indicates if the file has a header of not.<br/>
  By default, *has_header* is True and Taipy will use the 1st row in the Excel file
  as the header.

- _**sheet_name**_ represents which specific sheet in the Excel file to read:
    - By default, *sheet_name* is None and the data node will return all sheets in
      the Excel file when reading it.
    - If *sheet_name* is provided as a string, the data node will read only the data
      of the corresponding sheet.
    - If *sheet_name* is provided with a list of sheet names, the data node will return
      a dictionary with the key being the sheet name and the value being the data of
      the corresponding sheet.

- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from an Excel data node with different *exposed_type* are available
  in the [Read / Write a data node](../entities/data-node-mgt.md#excel) documentation):
    - By default, *exposed_type* is "pandas", and the data node reads the Excel
      file as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "modin", the data node reads the Excel
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the
      read method.
    - If the *exposed_type* provided is "numpy", the data node reads the
      Excel file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided *exposed_type* is a custom Python class, the data node
      creates a list of custom objects with the given custom class. Each object
      represents a row in the Excel file.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_excel.py"
comments=false
%}
```

In lines 3-5, we define a custom class `SaleRow`, representing a row in the Excel
file.

In lines 7-10, we configure an Excel data node. The identifier is "historical_temperature".
Its *scope* is `SCENARIO` (default value), and the default path is the file hist_temp.xlsx.
*has_header* is set to True, the Excel file must have a header. The *sheet_name* is not
provided so Taipy uses the default value "Sheet1".

In lines 12-15, we configure a new Excel data node. The identifier is "log_history",
the default `SCENARIO` scope is used, and the default path is "path/hist_log.xlsx".
"modin" is used as the exposed_type**.

In lines 17-21, we add another Excel data node configuration. The identifier is
"sales_history", the default `SCENARIO` scope is used. Since we have a custom class
pre-defined for this Excel file, we provide it in the exposed_type**. We also provide
the list of specific sheets we want to use as the *sheet_name* parameter.

!!! Note

    To configure an Excel data node, it is equivalent to using the method
    `Config.configure_excel_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="excel"`.

## SQL Table

!!! Important

    - To be able to use a `SQLTableDataNode^` with Microsoft SQL Server you need to run
    internal dependencies with `pip install taipy[mssql]` and install your corresponding
    [Microsoft ODBC Driver for SQLServer](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
    - To be able to use a `SQLTableDataNode^` with MySQL Server you need to run internal
    dependencies with `pip install taipy[mysql]` and install your corresponding
    [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
    - To be able to use a `SQLTableDataNode^` with PostgreSQL Server you need to run
    internal dependencies with `pip install taipy[postgresql]` and install your corresponding
    [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).


A `SQLTableDataNode^` is a specific data node that models data stored in a single SQL
table. To add a new *SQL table* data node configuration, the
`Config.configure_sql_table_data_node()^` method can be used. In addition to the generic
parameters described in the [Data node configuration](data-node-config.md) section, the
following parameters can be provided:

- _**db_name**_ represents the name of the database.
- _**db_engine**_ represents the engine of the database.<br/>
    Possible values are *"sqlite"*, *"mssql"*, *"mysql"*, or *"postgresql"*.
- _**table_name**_ represents the name of the table to read from and write into.
- _**db_username**_ represents the database username that will be used by Taipy to
  access the database. Required by *"mssql"*, *"mysql"*, and *"postgresql"* engines.
- _**db_password**_ represents the database user's password that will be used by Taipy to
  access the database. Required by *"mssql"*, *"mysql"*, and *"postgresql"* engines.
- _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
    The default value of *db_host* is "localhost".
- _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
  The default value of *db_port* is 1433.
- _**db_driver**_ represents the database driver that will be used by Taipy.
- _**sqlite_folder_path**_ represents the path to the folder that contains the SQLite database file. The default value of *sqlite_folder_path* is the current working folder.
- _**sqlite_file_extension**_ represents the file extension of the SQLite database file. The default value of *sqlite_file_extension* is ".db".
- _**db_extra_args**_ is a dictionary of additional arguments that need to be passed into the database connection string.
- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from a SQL table data node with different *exposed_type* are available
  in the [Read / Write a data node](../entities/data-node-mgt.md#sql-table) documentation):
    - By default, *exposed_type* is "pandas", and the data node reads the SQL table
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "modin", the data node reads the SQL table
      as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "numpy", the data node reads the SQL table
      as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided *exposed_type* is a custom Python class, the data node creates
      a list of custom objects with the given custom class. Each object represents
      a record in the SQL table.

### Example with a Microsoft SQL database table

First, let's take a look at an example on how to configure a *SQL table* data node with the
database engine is `mssql` (short for Microsoft SQL).

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql-table_with_mssql_engine.py"
comments=false
%}
```

In this example, we configure a *SQL table* data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password" (refer to [advance configuration](./advanced-config.md) to pass
password as an environment variable), the database name is "taipy". The table name is "sales".
To ensure secure connection with the SQL server, "TrustServerCertificate" is defined as "yes"
in the *db_extra_args*.

### Example with a SQLite database table

In the next example, we configure a *SQL table* data node with the database engine is `sqlite`.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql-table_with_sqlite_engine.py"
comments=false
%}
```

Here, the database username and password are unnecessary. The folder containing SQLite database
file is "database", with the file extension is ".sqlite3". Since the database name is "taipy",
this SQL table data node will read and write to the SQLite database stored at "database/taipy.sqlite3".

When the data node is read, it reads all the rows from the table "sales", and when the
data node is written, it deletes all the data in the table and insert the new data.

!!! Note

    To configure a SQL table data node, it is equivalent to using the method
    `Config.configure_sql_table_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="sql_table"`.

## SQL

!!! Important

    - To be able to use a `SQLDataNode^` with Microsoft SQL Server you need to install
    internal dependencies with `pip install taipy[mssql]` and install your corresponding
    [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
    - To be able to use a `SQLDataNode^` with MySQL Server you need to install internal
    dependencies with `pip install taipy[mysql]` and install your corresponding
    [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
    - To be able to use a `SQLDataNode^` with PostgreSQL Server you need to install
    internal dependencies with `pip install taipy[postgresql]` and install your corresponding
    [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).

A `SQLDataNode^` is a specific data node used to model data stored in a SQL Database. To
add a new *SQL* data node configuration, the `Config.configure_sql_data_node()^` method can
be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**db_name**_ represents the name of the database.
- _**db_engine**_ represents the engine of the database.<br/>
    Possible values are *"sqlite"*, *"mssql"*, *"mysql"*, or *"postgresql"*.
- _**read_query**_ represents the SQL query that will be used by Taipy to read the data
  from the database.
- _**write_query_builder**_ is a callable function that takes in the data as an input
  parameter and returns a list of SQL queries to be executed when the write method is
  called.
- _**db_username**_ represents the database username that will be used by Taipy to access
  the database. Required by *"mssql"*, *"mysql"*, and *"postgresql"* engines.
- _**db_password**_ represents the database user's password that will be used by Taipy to
  access the database. Required by *"mssql"*, *"mysql"*, and *"postgresql"* engines.
- _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
  The default value of *db_host* is "localhost".
- _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
  The default value of *db_port* is 1433.
- _**db_driver**_ represents the database driver that will be used by Taipy.
- _**sqlite_folder_path**_ represents the path to the folder that contains the SQLite database file. The default value of *sqlite_folder_path* is the current working folder.
- _**sqlite_file_extension**_ represents the file extension of the SQLite database file. The default value of *sqlite_file_extension* is ".db".
- _**db_extra_args**_ is a dictionary of additional arguments that need to be passed into the database connection string.
- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from a SQL data node with different *exposed_type* are available
  in the [Read / Write a data node](../entities/data-node-mgt.md#sql) documentation):
    - By default, *exposed_type* is "pandas", and the data node reads the data
      as a Pandas DataFrame (`pandas.DataFrame`) when execute the *read_query*.
    - If the *exposed_type* provided is "modin", the data node reads the CSV file
      as a Modin DataFrame (`modin.pandas.DataFrame`) when execute the *read_query*.
    - If the *exposed_type* provided is "numpy", the data node reads the CSV file
      as a NumPy array (`numpy.ndarray`) when execute the *read_query*.
    - If the provided *exposed_type* is a custom Python class, the data node
      creates a list of custom objects with the given custom class. Each object represents
      a record in the table returned by the *read_query*.

### Example with a Microsoft SQL database table

First, let's take a look at an example on how to configure a *SQL table* data node with the
database engine is `mssql` (short for Microsoft SQL).

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql_with_mssql_engine.py"
comments=false
%}
```

In this example, we configure a *SQL* data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password" (refer to [advance configuration](./advanced-config.md) to pass
password as an environment variable), and the database name is "taipy". The read query
will be "SELECT \* from sales".

The *write_query_builder* is a callable function that takes in a `pandas.DataFrame` and
return a list of queries. The first query will delete all the data in the table "sales",
and the second query is a prepared statement that takes in two values, which is the data
from the two columns "date" and "nb_sales" in the `pandas.DataFrame`. Since this is a
prepared statement, it must be passed as a tuple with the first element being the query
and the second element being the data.

The very first parameter of *write_query_builder* (i.e. data) is expected to have the same
type as the return type of the task function whose output is the data node. In this example,
the task function must return a `pandas.DataFrame`, since the data parameter of the
*write_query_builder* is a `pandas.DataFrame`.


### Example with a SQLite database table

In the next example, we configure a *SQL table* data node with the database engine is `sqlite`.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql_with_sqlite_engine.py"
comments=false
%}
```

Here, the database username and password are unnecessary. The folder containing SQLite database
file is "database", with the file extension is ".sqlite3". Since the database name is "taipy", this
SQL table data node will read and write to the SQLite database stored at "database/taipy.sqlite3".

!!! Note

    To configure a SQL data node, it is equivalent to using the method
    `Config.configure_sql_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="sql"`.

## JSON

A `JSONDataNode^` is a predefined data node that models JSON file data. The
`Config.configure_json_data_node()^` method adds a new *JSON* data node configuration.
In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the *json* configuration.<br/>
  It is used to populate the path property of the entities (*json* data nodes)
  instantiated from the *json* data node configuration. That means by default
  all the entities (*json* data nodes) instantiated from the same *json*
  configuration will inherit/share the same *json* file provided in the
  default_path. To avoid this, the path property of a *json* data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**encoder**_ and _**decoder**_ parameters are optional parameters representing
  the encoder (json.JSONEncoder) and decoder (json.JSONDecoder) used to serialize and
  deserialize JSON data.<br/>
  Check out [JSON Encoders and Decoders](https://docs.python.org/3/library/json.html#encoders-and-decoders)
  documentation for more details.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_json.py"
comments=false
%}
```

In this example, we configure a JSON data node. The *id* argument is
"historical_temperature". Its *scope* is `SCENARIO` (default value), and the path
points to *hist_temp.json* file.

Without specific *encoder* and *decoder* parameters, *hist_temp_cfg* will use
default encoder and decoder provided by Taipy, which can encode and
decode Python [`enum.Enum`](https://docs.python.org/3/library/enum.html),
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects),
[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects),
and [dataclass](https://docs.python.org/3/library/dataclasses.html) object.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_json-with-encoder.py"
comments=false
%}
```

In this next example, we configure a `JSONDataNode^` with a custom JSON *encoder*
and *decoder*:

- In lines 5-7, we define a custom class `SaleRow`, representing data in a JSON object.

- In lines 9-30, we define a custom encoder and decoder for the `SaleRow` class.
    - When [writing a JSONDataNode](../entities/data-node-mgt.md#write-data-node),
    the `SaleRowEncoder` encodes a `SaleRow` object in JSON format. For example,
    after the creation of the scenario `scenario`,
        ```python
        scenario.sales_history.write(SaleRow("12/24/2018", 1550))
        ```
    the previous code writes the following object
        ```json
        {
            "__type__": "SaleRow",
            "date": "12/24/2018",
            "nb_sales": 1550,
        }
        ```
    to the file *path/sales.json*.
    - When reading a JSONDataNode, the `SaleRowDecoder` converts a JSON
    object with the attribute `__type__` into a Python object corresponding to the
    attribute's value. In this example, the "SaleRow"` data class.

- In lines 33-37, we create a JSON data node configuration. The *id* identifier is
"sales_history". The default `SCENARIO` scope is used. The encoder and decoder are the
custom encoder and decoder defined above.

!!! Note

    To configure a JSON data node, it is equivalent to using the method
    `Config.configure_json_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="json"`.

## Parquet

A `ParquetDataNode^` data node is a specific data node used to model
[Parquet](https://parquet.apache.org/) file data. The `Config.configure_parquet_data_node()^`
adds a new *Parquet* data node configuration. In addition to the generic
parameters described in the [Data node configuration](data-node-config.md)
section, the following parameters can be provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the *Parquet* configuration.<br/>
  It is used to populate the path property of the entities (*Parquet* data nodes)
  instantiated from the *Parquet* data node configuration. That means by default
  all the entities (*Parquet* data nodes) instantiated from the same *Parquet*
  configuration will inherit/share the same *Parquet* file provided in the
  default_path. To avoid this, the path property of a *Parquet* data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**engine**_ represents the Parquet library to use.<br/>
  Possible values are *"fastparquet"* or *"pyarrow"*. The default value is *"pyarrow"*.<br/>
  Using the *"fastparquet"* engine requires installation with `pip install taipy[fastparquet]`.

- _**compression**_ is the name of the compression to use.<br/>
  Possible values are *"snappy"*, *"gzip"*, *"brotli"* and None. The default value is
  *"snappy"*. Use None for no compression.

- _**read_kwargs**_ is a dictionary of additional parameters passed to the
  [`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
  method.

- _**write_kwargs**_ is a dictionary of additional parameters passed to the
  [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
  method.<br/>
  The parameters *read_kwargs* and *write_kwargs* have a **higher precedence** than the
  top-level parameters (*engine* and *compression*) which are also passed to Pandas. Passing
  `read_kwargs= {"engine": "fastparquet", "compression": "gzip"}` will override the *engine* and
  *compression* properties of the data node.

!!! Tip

    The `ParquetDataNode.read_with_kwargs^` and `ParquetDataNode.write_with_kwargs^`
    methods provide an alternative for specifying keyword arguments at runtime. See examples
    of these methods on the [Data Node Management page](../entities/data-node-mgt.md#parquet).

- _**exposed_type**_ indicates the data type returned when reading the data node (more examples
  of reading from Parquet data node with different *exposed_type* are available on
  [Read / Write a data node](../entities/data-node-mgt.md#parquet) documentation):
    - By default, *exposed_type* is "pandas", and the data node reads the Parquet file
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "modin", the data node reads the Parquet
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the *exposed_type* provided is "numpy", the data node reads the Parquet
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided *exposed_type* is a `Callable`, the data node creates a list of
      objects as returned by the `Callable`. Each object represents a record in the Parquet
      file. The Parquet file is read as a `pandas.DataFrame` and each row of the DataFrame
      is passed to the Callable as keyword arguments where the key is the column name, and
      the value is the corresponding value for that row.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_parquet-simple.py"
comments=false
%}
```

In lines 3-5, we configure a basic Parquet data node. The only two required parameters are
*id* and *default_path*.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_parquet-complete.py"
comments=false
%}
```

In this larger example, we illustrate some specific benefits of using ParquetDataNode for
storing tabular data. This time, we provide the *read_kwargs* and *write_kwargs* dictionary
parameters to be passed as keyword arguments to
[`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
respectively.

Here, the dataset is partitioned (using _partition_cols_ on line 4) by the "log_level"
column when written to disk. Also, filtering is performed (using _filters_ on line 3)
to read only the rows where the "log_level" column value is either "ERROR" or "CRITICAL",
speeding up the read, especially when dealing with a large amount of data.

Note that even though line 10 specifies the *compression* as "snappy", since the "compression"
key was also provided in the _write_kwargs_ dictionary on line 4, the last value is used, hence
the *compression* is None.

!!! Note

    To configure a Parquet data node, it is equivalent to using the method
    `Config.configure_parquet_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="parquet"`.

!!! Info

    Taipy ParquetDataNode wraps
    [`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
    and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
    methods for reading and writing Parquet data, respectively.

## Mongo Collection

A `MongoCollectionDataNode^` is a specific data node used to model data stored in a
Mongo collection. To add a new *mongo_collection* data node configuration, the
`Config.configure_mongo_collection_data_node()^` method can be used. In addition to
the generic parameters described in the [Data node configuration](data-node-config.md)
section, multiple parameters can be provided.

- _**db_name**_ represents the name of the database in MongoDB.
- _**collection_name**_ represents the name of the data collection in the database.
- _**custom_document**_ represents the custom class used to store, encode, and
  decode data when reading and writing to a Mongo collection. The data returned by the
  read method is a list of custom_document object(s), and the data passed as a parameter
  of the write method is a (list of) custom_document object(s). The custom_document can have:
    - An optional `decoder()` method to decode data in the Mongo collection to a custom object when reading.
    - An optional `encoder()` method to encode the object's properties to the Mongo collection format when writing.
- _**db_username**_ represents the username to be used to access MongoDB.
- _**db_password**_ represents the user's password to be used by Taipy to access MongoDB.
- _**db_port**_ represents the database port to be used to access MongoDB.<br/>
    The default value of *db_port* is 27017.
- _**db_host**_ represents the database host to be used to access MongoDB.<br/>
    The default value of *db_host* is "localhost".

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_mongo-collection.py"
comments=false
%}
```

In this example, we configure a *mongo_collection* data node with the id "historical_data":

- Its scope is the default value `SCENARIO`.
- The database username is "admin", the user's password is "pa$$w0rd"
- The database name is "taipy"
- The collection name is "historical_data_set".
- Without being specified, the custom document class is defined as
  `taipy.core.MongoDefaultDocument`.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_mongo-complete.py"
comments=false
%}
```

In this next example, we configure another *mongo_collection* data node, with the custom
document is defined as `DailyMinTemp` class.

-   The custom *encode* method encodes `datetime.datetime` to the ISO 8601 string format.
-   The corresponding *decode* method decodes an ISO 8601 string to `datetime.datetime`.
-   The `_id` of the Mongo document is discarded.

Without these two methods, the default decoder will map the key of each document to
the corresponding property of a `DailyMinTemp` object, and the default encoder will
convert `DailyMinTemp` object's properties to a dictionary without any special formatting.

!!! Note

    To configure a Mongo collection data node, it is equivalent to using the method
    `Config.configure_mongo_collection_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="mongo_collection"`.

## Generic

A `GenericDataNode^` is a specific data node used to model generic data types where the
user defines the read and the write functions. The `Config.configure_generic_data_node()^`
method adds a new *generic* data node configuration. In addition to the parameters described
in the [Data node configuration](data-node-config.md) section, the following parameters
can be provided:

- _**read_fct**_ represents a Python function, which is used to read the data.
  More optional parameters can be passed through the _**read_fct_args**_ parameter.

- _**write_fct**_ represents a Python function, which is used to write/serialize the data.
  The provided function must have at least one parameter to receive data to be written.
  It must be the first parameter. More optional parameters can be passed through the
  _**write_fct_args**_ parameter.

- _**read_fct_args**_ represents the parameters passed to the *read_fct* to
  read/de-serialize the data. It must be a `List` type object.

- _**write_fct_args**_ represents the parameters passed to the *write_fct* to write
  the data. It must be a `List` type object.

!!! Note

    At least one of the *read_fct* or *write_fct* is required to configure a generic data node.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_generic-text.py"
comments=false
%}
```

In this small example is configured a generic data node with the id "historical_data".

In lines 17-18, we provide two Python functions (previously defined) as *read_fct* and *write_fct*
parameters to read and write the data in a text file. Note that the first parameter of *write_fct*
is mandatory and is used to pass the data on writing.

In line 19, we provide *read_fct_args* with a path to let the *read_fct* know where to read the
data.

In line 20, we provide a list of parameters to *write_fct_args* with a path to let the *write_fct*
know where to write the data. Note that the data parameter will be automatically passed at runtime
when writing the data.

The generic data node can also be used in situations requiring a specific business logic in
reading or writing data, and the user can easily provide that. Follows an example using a
custom delimiter when writing and reading a CSV file.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_generic-csv.py"
comments=false
%}
```

It is also possible to use a generic data node custom functions to perform some data
preparation:

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_generic-data-prep.py"
comments=false
%}
```

!!! Note

    To configure a generic data node, it is equivalent to using the method
    `Config.configure_generic_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="generic"`.

## In memory

An `InMemoryDataNode^` is a specific data node used to model any data in the RAM. The
`Config.configure_in_memory_data_node()^` method is used to add a new in_memory
data node configuration. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, an optional parameter can be
provided:

- If the _**default_data**_ is given as a parameter of the data node configuration,
  the data node entity is automatically written with the corresponding value (note
  that any serializable Python object can be used) upon its instantiation.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_memory.py"
comments=false
%}
```

In this example, we configure an *in_memory* data node with the id "date".
The scope is `SCENARIO` (default value), and default data is provided.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multi-process environment.
    (See [Job configuration](job-config.md#standalone) for more details).

!!! Note

    To configure an in_memory data node, it is equivalent to using the method
    `Config.configure_in_memory_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="in_memory"`.

# Default data node configuration

By default, if there is no information provided when configuring a datanode (except for the mandatory _**id**_), the `Config.configure_data_node()^` method will return a *pickle* data node configuration with the `Scope^` is set to `SCENARIO`.

To override the default data node configuration, one can use the `Config.set_default_data_node_configuration()^` method.
Then, a new data node configuration will:

- have the same properties as the default data node configuration if the _**storage_type**_ is the same as the default one.
- ignore the default data node configuration if the _**storage_type**_ is different from the default one.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_default.py"
comments=false
%}
```

We override the default data node configuration by a SQL table data node configuration in the previous code example, providing all necessary properties for a SQL table data node in lines 3-14.

Then we configure 5 data nodes:

- Line 16 configures a SQL Table data node `products_data_cfg`. By providing only the _**id**_, `products_data_cfg` has the exact same properties as the default data node configuration as above, which reads and writes to the "products" table.
- Line 17 configures a SQL Table data node `users_data_cfg`. By also providing `table_name="users"`, this data node reads and writes to the "users" table.
- Lines 18 and 19 configure 2 SQL Table data nodes, one using `Config.configure_data_node()^` with `storage_type="sql_table"`, one using `Config.configure_sql_table_data_node()^`. Since both have the same _**storage_type**_ as the default data node configuration, both have the same properties except for the table name.
- Line 21 configures a CSV data node `forecast_data_cfg`. Since the _**storage_type**_ is `"csv"`, which is different from the `"sql_table"` configured in line 9, the default data node configuration is ignored. Therefore, the scope of `forecast_data_cfg` is `SCENARIO` by default.

[:material-arrow-right: The next section introduces the task configuration](task-config.md).
