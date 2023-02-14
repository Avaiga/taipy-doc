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
    It is the only **mandatory** parameter and must be a unique and valid Python
    identifier.
- _**scope**_ is a `Scope^`.<br/>
    It corresponds to the [scope](../concepts/scope.md) of the data node that will
    be instantiated from the data node configuration. The **default value** is
    `Scope.SCENARIO`.
- _**storage_type**_ is an attribute that indicates the storage type of the
    data node.<br/>
    The possible values are ["pickle"](#pickle) (**the default value**), ["csv"](#csv),
    ["excel"](#excel), ["json"](#json), ["mongo_collection"](#mongo-collection),
    ["parquet"](#parquet), ["sql"](#sql), ["sql_table"](#sql_table),
    ["in_memory"](#in-memory), or ["generic"](#generic).<br/>
    As explained in the following subsections, depending on the _storage_type_, other
    configuration attributes must be provided in the _properties_ parameter.
- Any other custom attribute can be provided through the parameter _**properties**_,
    a kwargs dictionary accepting any number of custom parameters (a description,
    a label, a tag, etc.) (It is recommended to read
    [doc](https://realpython.com/python-kwargs-and-args/) if you are not familiar with
    **kwargs arguments)
    <br/>
    This _properties_ dictionary is used to configure the parameters specific to each
    storage type. It is copied in the dictionary properties of all the data nodes
    instantiated from this data node configuration.<br/>

!!! Warning

    Note that we cannot use the word "_entity_owner" as a key in the properties as it has been reserved for internal use.

Below are two examples of data node configurations.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_two-examples.py"
comments=false
%}
```

In lines 3-4, we configured a simple data node with the id "date_cfg". The default
value for _scope_ is `SCENARIO`. The _storage_type_ is set to the default value
"pickle".<br/>
An optional custom property called _description_ is also added: this property is
propagated to the data nodes instantiated from this config.

In lines 6-10, we add another data node configuration with the id "model_cfg". The
_scope_ is set to `CYCLE` so that all the scenarios from the same cycle will share
the corresponding data nodes. The _storage_type_ is "pickle", and two optional custom properties are
added: a _description_ string and an integer _code_. These two properties are propagated to the
data nodes instantiated from this config.

# Storage type

Taipy proposes predefined _data nodes_ corresponding to the most popular
_storage types_. Thanks to predefined _data nodes_, the Python developer
does not need to spend much time configuring the _storage types_ or the
_query system_. A predefined data node will often satisfy the user's
required format: pickle, CSV, SQL table, MongoDB collection, Excel sheet,
etc.

The various predefined _storage types_ are typically used for input data.
Indeed, the input data is usually provided by external sources, where
the Python developer user does not control the format.

For intermediate or output _data nodes_, the developer often does not have
any particular specifications regarding the _storage type_. In such a case,
using the default _storage type_ pickle that does not require any
configuration is recommended.

If a more specific method to store, read and write the data is needed, Taipy
provides a Generic data node that can be used for any storage type (or any
kind of query system). The developer only needs to provide two Python
functions, one for reading and one for writing the data. Please refer to the
[generic data node config section](#generic) for more details on generic data
node.

All predefined data nodes are described in the subsequent sections.

## Pickle

A `PickleDataNode^` is a specific data node used to model _pickle_ data.
The `Config.configure_pickle_data_node()^` method configures a new _pickle_
data node configuration. In addition to the generic parameters described in
the [Data node configuration](data-node-config.md) section, two optional
parameters can be provided.

- _**default_path**_ represents the default file path used to read and write
  the data of the data nodes instantiated from the _pickle_ configuration.<br/>
  It is used to populate the path property of the entities (_pickle_ data nodes)
  instantiated from the _pickle_ data node configuration. That means by default
  all the entities (_pickle_ data nodes) instantiated from the same _pickle_
  configuration will inherit/share the same _pickle_ file provided in the
  default_path. To avoid this, the path property of a _pickle_ data node entity
  can be changed at runtime right after its instantiation.<br/>
  If no value is provided, Taipy will use an internal path in the Taipy storage folder
  (more details on the Taipy storage folder configuration are available in the
  [Global configuration](global-config.md) documentation).

- _**default_data**_ indicates data automatically written to the data node
  _pickle_ upon creation.<br/>
  Any serializable Python object can be used. The default value is `None`.

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
add a new _CSV_ data node configuration, the `Config.configure_csv_data_node()^` method
can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the _csv_ configuration.<br/>
  It is used to populate the path property of the entities (_csv_ data nodes)
  instantiated from the _csv_ data node configuration. That means by default
  all the entities (_csv_ data nodes) instantiated from the same _csv_
  configuration will inherit/share the same _csv_ file provided in the
  default_path. To avoid this, the path property of a _csv_ data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**has_header**_ indicates if the file has a header of not.<br/>
  By default, _has_header_ is True and Taipy will use the 1st row in the CSV file as
  the header.

- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from CSV data node with different _exposed_type_ is available on
  [Read / Write a data node](../entities/data-node-mgt.md#csv) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the CSV file
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "modin", the data node reads the CSV
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "numpy", the data node reads the CSV
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ is a custom Python class, the data node creates
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
Its _scope_ is by default `SCENARIO`. The default path points to the file
"path/hist_temp.csv". The property _has_header_ is set to True.

In lines 13-16, we configure another CSV data node with the identifier "log_history".
It uses the default `SCENARIO` scope again. The default path points to "path/hist_log.csv".
The _exposed_type_ provided is "modin".

In lines 18-21, we add another CSV data node configuration with the identifier "sales_history".
The default `SCENARIO` scope is used again. Since we have a custom class called `SaleRow`
that is defined for this CSV file, we provide it as the _exposed_type_ parameter.

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
  data pointed by the data nodes instantiated from the _Excel_ configuration.<br/>
  It is used to populate the path property of the entities (_Excel_ data nodes)
  instantiated from the _Excel_ data node configuration. That means by default
  all the entities (_Excel_ data nodes) instantiated from the same _Excel_
  configuration will inherit/share the same _Excel_ file provided in the
  default_path. To avoid this, the path property of a _Excel_ data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**has_header**_ indicates if the file has a header of not.<br/>
  By default, _has_header_ is True and Taipy will use the 1st row in the Excel file
  as the header.

- _**sheet_name**_ represents which specific sheet in the Excel file to read:
    - By default, _sheet_name_ is None and the data node will return all sheets in
      the Excel file when reading it.
    - If _sheet_name_ is provided as a string, the data node will read only the data
      of the corresponding sheet.
    - If _sheet_name_ is provided with a list of sheet names, the data node will return
      a dictionary with the key being the sheet name and the value being the data of
      the corresponding sheet.

- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from Excel data node with different _exposed_type_ is available
  on [Read / Write a data node](../entities/data-node-mgt.md#excel) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the Excel
      file as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "modin", the data node reads the Excel
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the
      read method.
    - If the _exposed_type_ provided is "numpy", the data node reads the
      Excel file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ is a custom Python class, the data node
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
Its _scope_ is `SCENARIO` (default value), and the default path is the file hist_temp.xlsx.
_has_header_ is set to True, the Excel file must have a header. The _sheet_name_ is not
provided so Taipy uses the default value "Sheet1".

In lines 12-15, we configure a new Excel data node. The identifier is "log_history",
the default `SCENARIO` scope is used, and the default path is "path/hist_log.xlsx".
"modin" is used as the _exposed_type_.

In lines 17-21, we add another Excel data node configuration. The identifier is
"sales_history", the default `SCENARIO` scope is used. Since we have a custom class
pre-defined for this Excel file, we provide it in the _exposed_type_. We also provide
the list of specific sheets we want to use as the _sheet_name_ parameter.

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
table. To add a new _SQL table_ data node configuration, the
`Config.configure_sql_table_data_node()^` method can be used. In addition to the generic
parameters described in the [Data node configuration](data-node-config.md) section, the
following parameters can be provided:

- _**db_username**_ represents the database username that will be used by Taipy to
  access the database.
- _**db_password**_ represents the database user's password that will be used by Taipy to
  access the database.
- _**db_name**_ represents the name of the database.
- _**db_engine**_ represents the engine of the database.<br/>
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
- _**table_name**_ represents the name of the table to read from and write into.
- _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
  The default value of _db_port_ is 1433.
- _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
    The default value of _db_host_ is "localhost".
- _**db_driver**_ represents the database driver that will be used by Taipy.<br/>
    The default value of _db_driver_ is "ODBC Driver 17 for SQL Server".
- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from SQL Table data node with different _exposed_type_ is available on
  [Read / Write a data node](../entities/data-node-mgt.md#sql-table) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the SQL table
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "modin", the data node reads the SQL table
      as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "numpy", the data node reads the SQL table
      as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ is a custom Python class, the data node creates
      a list of custom objects with the given custom class. Each object represents
      a record in the SQL table.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql-table.py"
comments=false
%}
```

In the previous example, we configure a _SQL table_ data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password" (refer to [advance configuration](./advanced-config.md) to pass
password as an environment variable), the database name is "taipy", and the database
engine is `mssql` (short for Microsoft SQL). The table name is "sales".

When the data node is read, it reads all the rows from the table "sales", and when the
data node is written, it deletes all the data in the table and insert the new data.

!!! Note

    To configure a SQL table data node, it is equivalent to using the method
    `Config.configure_sql_table_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="sql_table"`.

## SQL

!!! Important

    - To be able to use a `SQLTableDataNode^` with Microsoft SQL Server you need to run
    internal dependencies with `pip install taipy[mssql]` and install your corresponding
    [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
    - To be able to use a `SQLTableDataNode^` with MySQL Server you need to run internal
    dependencies with `pip install taipy[mysql]` and install your corresponding
    [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
    - To be able to use a `SQLTableDataNode^` with PostgreSQL Server you need to run
    internal dependencies with `pip install taipy[postgresql]` and install your corresponding
    [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).

A `SQLDataNode^` is a specific data node used to model data stored in a SQL Database. To
add a new _SQL_ data node configuration, the `Config.configure_sql_data_node()^` method can
be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**db_username**_ represents the database username that will be used by Taipy to access
  the database.
- _**db_password**_ represents the database user's password that will be used by Taipy to
  access the database.
- _**db_name**_ represents the name of the database.
- _**db_engine**_ represents the engine of the database.<br/>
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
- _**read_query**_ represents the SQL query that will be used by Taipy to read the data
  from the database.
- _**write_query_builder**_ is a callable function that takes in the data as an input
  parameter and returns a list of SQL queries to be executed when the write method is
  called.
- _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
  The default value of _db_port_ is 1433.
- _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
  The default value of _db_host_ is "localhost".
- _**db_driver**_ represents the database driver that will be used by Taipy.<br/>
  The default value of _db_driver_ is "ODBC Driver 17 for SQL Server".
- _**exposed_type**_ indicates the data type returned when reading the data node:
    - By default, _exposed_type_ is "pandas", and the data node reads the data
      as a Pandas DataFrame (`pandas.DataFrame`) when execute the _read_query_.
    - If the _exposed_type_ provided is "modin", the data node reads the CSV file
      as a Modin DataFrame (`modin.pandas.DataFrame`) when execute the _read_query_.
    - If the _exposed_type_ provided is "numpy", the data node reads the CSV file
      as a NumPy array (`numpy.ndarray`) when execute the _read_query_.
    - If the provided _exposed_type_ is a custom Python class, the data node
      creates a list of custom objects with the given custom class. Each object represents
      a record in the table returned by the _read_query_.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_sql.py"
comments=false
%}
```

In the previous example, we configure a _SQL_ data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password", the database name is "taipy", and the database engine is `mssql`
(short for Microsoft SQL). The read query will be "SELECT \* from sales".

The _write_query_builder_ is a callable function that takes in a `pandas.DataFrame` and
return a list of queries. The first query will delete all the data in the table "sales",
and the second query is a prepared statement that takes in two values, which is the data
from the two columns "date" and "nb_sales" in the `pandas.DataFrame`. Since this is a
prepared statement, it must be passed as a tuple with the first element being the query
and the second element being the data.

The very first parameter of _write_query_builder_ (i.e. data) is expected to have the same
type as the return type of the task function whose output is the data node. In this example,
the task function must return a `pandas.DataFrame`, since the data parameter of the
_write_query_builder_ is a `pandas.DataFrame`.

!!! Note

    To configure a SQL data node, it is equivalent to using the method
    `Config.configure_sql_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="sql"`.

## JSON

A `JSONDataNode^` is a predefined data node that models JSON file data. The
`Config.configure_json_data_node()^` method adds a new _JSON_ data node configuration.
In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the _json_ configuration.<br/>
  It is used to populate the path property of the entities (_json_ data nodes)
  instantiated from the _json_ data node configuration. That means by default
  all the entities (_json_ data nodes) instantiated from the same _json_
  configuration will inherit/share the same _json_ file provided in the
  default_path. To avoid this, the path property of a _json_ data node entity
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

In this example, we configure a JSON data node. The _id_ argument is
"historical_temperature". Its _scope_ is `SCENARIO` (default value), and the path
points to *hist_temp.json* file.

Without specific _**encoder**_ and _**decoder**_ parameters, *hist_temp_cfg* will use
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

In this next example, we configure a `JSONDataNode^` with a custom JSON _**encoder**_
and _**decoder**_:

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

- In lines 33-37, we create a JSON data node configuration. The _id_ identifier is
"sales_history". The default `SCENARIO` scope is used. The encoder and decoder are the
custom encoder and decoder defined above.

!!! Note

    To configure a JSON data node, it is equivalent to using the method
    `Config.configure_json_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="json"`.

## Parquet

A `ParquetDataNode^` data node is a specific data node used to model
[Parquet](https://parquet.apache.org/) file data. The `Config.configure_parquet_data_node()^`
adds a new _Parquet_ data node configuration. In addition to the generic
parameters described in the [Data node configuration](data-node-config.md)
section, the following parameters can be provided:

- _**default_path**_ represents the default file path used to read and write
  data pointed by the data nodes instantiated from the _Parquet_ configuration.<br/>
  It is used to populate the path property of the entities (_Parquet_ data nodes)
  instantiated from the _Parquet_ data node configuration. That means by default
  all the entities (_Parquet_ data nodes) instantiated from the same _Parquet_
  configuration will inherit/share the same _Parquet_ file provided in the
  default_path. To avoid this, the path property of a _Parquet_ data node entity
  can be changed at runtime right after its instantiation.<br/>

- _**engine**_ represents the Parquet library to use.<br/>
  Possible values are _"fastparquet"_ or _"pyarrow"_. The default value is _"pyarrow"_.<br/>
  Using the _"fastparquet"_ engine requires installation with `pip install taipy[fastparquet]`.

- _**compression**_ is the name of the compression to use.<br/>
  Possible values are _"snappy"_, _"gzip"_, _"brotli"_ and `None`. The default value is
  _"snappy"_. Use None for no compression.

- _**read_kwargs**_ is a dictionary of additional parameters passed to the
  [`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
  method.

- _**write_kwargs**_ is a dictionary of additional parameters passed to the
  [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
  method.<br/>
  The parameters in _"read_kwargs"_ and _"write_kwargs"_ have a **higher precedence** than the
  top-level parameters (**engine** and **compression**) which are also passed to Pandas. Passing
  `read_kwargs= {"engine": "fastparquet", "compression": "gzip"}` will override the **engine** and
  **compression** properties of the data node.

!!! Tip

    The `ParquetDataNode.read_with_kwargs^` and `ParquetDataNode.write_with_kwargs^`
    methods provide an alternative for specifying keyword arguments at runtime. See examples
    of these methods on the [Data Node Management page](../entities/data-node-mgt.md#parquet).

- _**exposed_type**_ indicates the data type returned when reading the data node (more examples
  of reading from Parquet data node with different _exposed_type_ are available on
  [Read / Write a data node](../entities/data-node-mgt.md#parquet) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the Parquet file
      as a Pandas DataFrame (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "modin", the data node reads the Parquet
      file as a Modin DataFrame (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ provided is "numpy", the data node reads the Parquet
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ is a `Callable`, the data node creates a list of
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
_id_ and _default_path_.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_parquet-complete.py"
comments=false
%}
```

In this larger example, we illustrate some specific benefits of using ParquetDataNode for
storing tabular data. This time, we provide the _read_kwargs_ and _write_kwargs_ dictionary
parameters to be passed as keyword arguments to
[`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
respectively.

Here, the dataset is partitioned (using _partition_cols_ on line 4) by the "log_level"
column when written to disk. Also, filtering is performed (using _filters_ on line 3)
to read only the rows where the "log_level" column value is either "ERROR" or "CRITICAL",
speeding up the read, especially when dealing with a large amount of data.

Note that even though line 10 specifies the _compression_ as "snappy", since the "compression"
key was also provided in the _write_kwargs_ dictionary on line 4, the last value is used, hence
the _compression_ is `None`.

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
    The default value of _db_port_ is 27017.
- _**db_host**_ represents the database host to be used to access MongoDB.<br/>
    The default value of _db_host_ is "localhost".

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
  `taipy.core.DefaultCustomDocument`.

```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_mongo-complete.py"
comments=false
%}
```

In this next example, we configure another *mongo_collection* data node, with the custom
document is defined as `DailyMinTemp` class.

-   The custom _encode_ method encodes `datetime.datetime` to the ISO 8601 string format.
-   The corresponding _decode_ method decodes an ISO 8601 string to `datetime.datetime`.
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
method adds a new _generic_ data node configuration. In addition to the parameters described
in the [Data node configuration](data-node-config.md) section, the following parameters
can be provided:

- _**read_fct**_ is a mandatory parameter representing a Python function provided
  by the user. It is used to read the data. More optional parameters can be passed
  through the _**read_fct_params**_ parameter.

- _**write_fct**_ is a mandatory parameter representing a Python function provided by the
  user. It is used to write/serialize the data. The provided function must have at least
  one parameter to receive data to be written. It must be the first parameter.
  More optional parameters can be passed through the _**write_fct_params**_ parameter.

- _**read_fct_params**_ represents the parameters passed to the _read_fct_ to
  read/de-serialize the data. It must be a `List` type object.

- _**write_fct_params**_ represents the parameters passed to the _write_fct_ to write
  the data. It must be a `List` type object.


```python linenums="1"
{%
include-markdown "./code_example/data_node_cfg/data-node-config_generic-text.py"
comments=false
%}
```

In this small example is configured a generic data node with the id "historical_data".

In lines 17-18, we provide two Python functions (previously defined) as _read_fct_ and _write_fct_
parameters to read and write the data in a text file. Note that the first parameter of _write_fct_
is mandatory and is used to pass the data on writing.

In line 19, we provide _read_fct_params_ with a path to let the _read_fct_ know where to read the
data.

In line 20, we provide a list of parameters to _write_fct_params_ with a path to let the _write_fct_
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

In this example, we configure an _in_memory_ data node with the id "date".
The scope is `SCENARIO` (default value), and default data is provided.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multi-process environment.
    (See [Job configuration](job-config.md#standalone) for more details).

!!! Note

    To configure an in_memory data node, it is equivalent to using the method
    `Config.configure_in_memory_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="in_memory"`.

[:material-arrow-right: The next section introduces the task configuration](task-config.md).
