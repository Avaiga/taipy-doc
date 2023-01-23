# New data node config
For Taipy to instantiate a [Data node](../concepts/data-node.md), a data node
configuration must be provided. `DataNodeConfig^` is used to configure the various
data nodes that Taipy will manipulate. To configure a new `DataNodeConfig^`, one
can use the function `Config.configure_data_node()^`.

```python linenums="1"
from taipy import Config

data_node_cfg = Config.configure_data_node(id="data_node_cfg")
```

In the previous code, we configured a simple data node just providing an identifier
as a string "data_node_cfg".

More optional attributes are available on data nodes, including:

- _**id**_ is the identifier of the data node config.<br/>
    It is a **mandatory** parameter that must be unique. It must be a valid Python
    identifier.

- _**scope**_ is a `Scope^`.<br/>
    It corresponds to the [scope](../concepts/scope.md) of the data node that will
    be instantiated from the data node configuration. The **default value** is
    `Scope.SCENARIO`.

- _**storage_type**_ is an attribute that indicates the type of storage of the
    data node.<br/>
    The possible values are ["pickle"](#pickle) (**the default value**), ["csv"](#csv),
    ["excel"](#excel), ["json"](#json), ["mongo_collection"](#mongo-collection),
    ["parquet"](#parquet), ["sql"](#sql), ["sql_table"](#sql_table),
    ["in_memory"](#in-memory), or ["generic"](#generic).<br/>
    As explained in the following subsections, depending on the _storage_type_, other
    configuration attributes must be provided in the parameter _properties_ parameter.

- _**cacheable**_ is an attribute that indicates if the data node can be cached during
    the execution of the tasks it is connected to.

- Any other custom attribute can be provided through the parameter _**properties**_,
    which is a dictionary (a description, a tag, etc.)<br/>
    This _properties_ dictionary is used to configure the parameters specific to each
    storage type. Note also that all this dictionary _**properties**_ is copied in the
    dictionary properties of all the data nodes instantiated from this data node
    configuration.<br/>

Below are two examples of data node configurations.

```python linenums="1"
from taipy import Config, Scope

date_cfg = Config.configure_data_node(id="date_cfg",
                                      description="The current date of the scenario")

model_cfg = Config.configure_data_node(
    id="model_cfg",
    scope=Scope.CYCLE,
    storage_type="pickle",
    description="Trained model shared by all scenarios",
    code=54)
```

In lines 3-4, we configured a simple data node with the id "date_cfg". The default
value for _scope_ is `SCENARIO`. The _storage_type_ also has the default value
"pickle".<br/>
An optional custom property called _description_ is also added: this property is
propagated to the data nodes instantiated from this config.

In lines 6-11, we add another data node configuration with the id "model_cfg". _scope_ is
set to `CYCLE`, so the corresponding data nodes will be shared by all the scenarios from
the same cycle. _storage_type_ is "pickle" as well, and two optional custom properties are
added: a _description_ string and an integer _code_. These two properties are propagated to the
data nodes instantiated from this config.

# Storage type

Taipy proposes various predefined _data nodes_ corresponding to the most popular
_storage types_. Thanks to predefined _data nodes_, the Python developer does not need
to spend much time configuring the _storage types_ or the
_query system_. Most of the time, a predefined _data node_ corresponding to a basic and
standard use case satisfies the user's needs like pickle file, CSV file, SQL table,
MongoDB collection, Excel sheet, etc.

The various predefined _storage types_ are mainly used for input data. Indeed, the input
data is usually provided by an external component, and the Python developer user does not
control the format.

However, in most cases, particularly for intermediate or output _data nodes_, it is not
relevant to prefer one _storage type_. The end-user wants to manipulate the corresponding
data within the Taipy application. Still, the user does not have any particular specifications
regarding the _storage type_. In such a case, the Python developer is recommended to use the
default _storage type_ pickle that does not require any configuration.

In case a more specific method to store, read and write the data is needed by the user,
Taipy proposes a _Generic data node_ that can be used for any _storage type_ or any kind
of _query system_. The user only needs to provide two python functions, one for reading
and one for writing the data.

Each predefined data node is described in a subsequent section.

## Pickle

A `PickleDataNode^` is a specific data node used to model pickle data.
To add a new _pickle_ data node configuration, the `Config.configure_pickle_data_node()^`
method can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, two optional parameters can be
provided.

- _**default_path**_ represents the default file path used by Taipy to read and write
  the data.<br/>
  If the pickle file already exists (in the case of a shared input data node, for
  instance), it is necessary to provide the default file path as the _default_path_
  parameter.<br/>
  If no value is provided, Taipy will use an internal path in the Taipy storage folder
  (more details on the Taipy storage folder configuration available on the
  [Global configuration](global-config.md) documentation).

- _**default_data**_ indicates data that is automatically written to the data node
  upon creation.<br/> Any serializable Python object can be used. The default value
  is `None`.

```python linenums="1"
from taipy import Config
from datetime import datetime

date_cfg = Config.configure_pickle_data_node(
    id="date_cfg",
    default_data=datetime(2022, 1, 25))

model_cfg = Config.configure_pickle_data_node(
    id="model_cfg",
    default_path="path/to/my/model.p",
    description="The trained model")
```

In lines 4-6, we configure a simple pickle data node with the id "date_cfg".
The scope is `SCENARIO` (default value), and a default data is provided.

In lines 8-11, we add another pickle data node configuration with the id "model_cfg".
The default `SCENARIO` scope is used. Since the data node config corresponds to a
pre-existing pickle file, a default path "path/to/my/model.p" is provided. We also
added an optional custom description.

!!! Note

    To configure a pickle data node, it is equivalent to use the method
    `Config.configure_pickle_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="pickle"`.

## CSV

A `CSVDataNode^` data node is a specific data node used to model CSV file data. To
add a new _CSV_ data node configuration, the `Config.configure_csv_data_node()^` method
can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ is a mandatory parameter and represents the default CSV file path
  used by Taipy to read and write the data.

- _**has_header**_ indicates if the file has a header of not.<br/>
  By default, _has_header_ is True and Taipy will use the 1st row in the CSV file as
  the header.

- _**exposed_type**_ indicates the data type returned when reading the data node (more
  examples of reading from CSV data node with different _exposed_type_ is available on
  [Read / Write a data node](../entities/data-node-mgt.md#csv) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the CSV file
      as a Pandas dataframe (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "modin", the data node reads the CSV
      file as a modin dataframe (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "numpy", the data node reads the CSV
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ value is a custom Python class, the data node creates
      a list of custom objects with the given custom class, each object represents
      a row in the CSV file.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

temp_cfg = Config.configure_csv_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.csv",
    has_header=True,
    exposed_type="numpy")

log_cfg = Config.configure_csv_data_node(
    id="log_history",
    default_path="path/hist_log.csv",
    exposed_type="modin")

sales_history_cfg = Config.configure_csv_data_node(
    id="sales_history",
    default_path="path/sales.csv",
    exposed_type=SaleRow)
```

In lines 3-5, we define a custom class `SaleRow` representing a row of the CSV file.

In lines 7-11, we configure a basic CSV data node with the identifier "historical_temperature".
Its _scope_ is by default `SCENARIO`. The default path corresponds to the file
"path/hist_temp.csv". The property _has_header_ being True, representing the CSV file
has a header.

In lines 13-16, we configure another CSV data node with the identifier "log_history".
It uses the default `SCENARIO` scope again. The default path is the path to the CSV
file "path/hist_log.csv". The _exposed_type_ provided will be "modin" exposed type.

In lines 18-21, we add another CSV data node configuration with the identifier "sales_history".
The default `SCENARIO` scope is used again. Since we have a custom class called `SaleRow`
that is defined for this CSV file, we provide it as the _exposed_type_ parameter.

!!! Note

    To configure a CSV data node, it is equivalent to use the method
    `Config.configure_csv_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="csv"`.

## Excel

An `ExcelDataNode^` is a specific data node used to model xlsx file data. To add a
new _Excel_ data node configuration, the `Config.configure_excel_data_node()^` method
can be used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, a mandatory and three optional
parameters can be provided.

- _**default_path**_ is a mandatory parameter that represents the default Excel file
  path used by Taipy to read and write the data.

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
      file as a Pandas dataframe (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "modin", the data node reads the Excel
      file as a modin dataframe (`modin.pandas.DataFrame`) when executing the
      read method.
    - If the _exposed_type_ value provided is "numpy", the data node reads the
      Excel file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ value is a custom Python class, the data node
      creates a list of custom objects with the given custom class, each object
      represents a row in the Excel file.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

hist_temp_cfg = Config.configure_excel_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.xlsx",
    exposed_type="numpy")

hist_log_cfg = Config.configure_excel_data_node(
    id="log_history",
    default_path="path/hist_log.xlsx",
    exposed_type="modin")

sales_history_cfg = Config.configure_excel_data_node(
    id="sales_history",
    default_path="path/sales.xlsx",
    sheet_name=["January", "February"],
    exposed_type=SaleRow)
```

In lines 3-5, we define a custom class `SaleRow`, representing a row in the Excel
file.

In lines 7-10, we configure an Excel data node. The identifier is "historical_temperature".
Its _scope_ is `SCENARIO` (default value), and the default path is the file hist_temp.xlsx.
With _has_header_ being True, the Excel file must have a header. The _sheet_name_ is not
provided so Taipy will use the default value "Sheet1".

In lines 12-15, we configure a new Excel data node. The identifier is "log_history",
the default `SCENARIO` scope is used, and the default path is "path/hist_log.xlsx".
"modin" will be used as the _exposed_type_.

In lines 17-21, we add another Excel data node configuration. The identifier is
"sales_history", the default `SCENARIO` scope is used. Since we have a custom class
pre-defined for this Excel file, we will provide it in the _exposed_type_. We also provide
the list of specific sheets we want to use as the _sheet_name_ parameter.

!!! Note

    To configure an Excel data node, it is equivalent to use the method
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
      as a Pandas dataframe (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "modin", the data node reads the SQL table
      as a modin dataframe (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "numpy", the data node reads the SQL table
      as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ value is a custom Python class, the data node creates
      a list of custom objects with the given custom class, each object represents
      a record in the SQL table.

```python linenums="1"
from taipy import Config

sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    table_name="sales"
)
```

In the previous example, we configure a _SQL table_ data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password", the database name is "taipy", and the database engine is `mssql`
(short for Microsoft SQL). The table name is "sales".

When the data node is read, it will read all the rows from the table "sales", and when the
data node is written, it will delete all the data in the table and insert the new data.

!!! Note

    To configure a SQL table data node, it is equivalent to use the method
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
      as a Pandas dataframe (`pandas.DataFrame`) when execute the _read_query_.
    - If the _exposed_type_ value provided is "modin", the data node reads the CSV file
      as a modin dataframe (`modin.pandas.DataFrame`) when execute the _read_query_.
    - If the _exposed_type_ value provided is "numpy", the data node reads the CSV file
      as a NumPy array (`numpy.ndarray`) when execute the _read_query_.
    - If the provided _exposed_type_ value is a custom Python class, the data node
      creates a list of custom objects with the given custom class, each object represents
      a record in the table returned by the _read_query_.

```python linenums="1"
from taipy import Config
import pandas as pd

def write_query_builder(data: pd.DataFrame):
    insert_data = list(
        data[["date", "nb_sales"]].itertuples(index=False, name=None))
    return [
        "DELETE FROM sales",
        ("INSERT INTO sales VALUES (?, ?)", insert_data)
    ]

sales_history_cfg = Config.configure_sql_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    read_query="SELECT * from sales",
    write_query_builder=write_query_builder
)
```

In the previous example, we configure a _SQL_ data node with the id "sales_history".
Its scope is the default value `SCENARIO`. The database username is "admin", the user's
password is "password", the database name is "taipy", and the database engine is `mssql`
(short for Microsoft SQL). The read query will be "SELECT \* from sales".

The _write_query_builder_ in this example is a callable function that takes in a
`pandas.DataFrame` and return a list of queries. The first query will delete all the data in
the table "sales", and the second query is a prepared statement that takes in two values, which
is the data from the two columns "date" and "nb_sales" in the `pandas.DataFrame`. Since this is
a prepared statement, it must be passed as a tuple with the first element being the query and
the second element being the data.

The data parameter of _write_query_builder_ is expected to have the same data type
as the return type of the task function whose output is the data node. In this example,
the task function returns a `pandas.DataFrame`, so the data parameter of the
_write_query_builder_ is also expected to be a `pandas.DataFrame`.

!!! Note

    To configure a SQL data node, it is equivalent to use the method
    `Config.configure_sql_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="sql"`.

## JSON

A `JSONDataNode^` is a type of data node used to model JSON file data. To add a new
_JSON_ data node configuration, the `Config.configure_json_data_node_node()^` method can be
used. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, the following parameters can be
provided:

- _**default_path**_ is a mandatory parameter that represents the JSON file path used
  by Taipy to read and write data.

- _**encoder**_ and _**decoder**_ parameters are optional parameters that represent
  the encoder (json.JSONEncoder) and decoder (json.JSONDecoder) used to serialize and
  deserialize JSON data.<br/>
  Check out [JSON Encoders and Decoders](https://docs.python.org/3/library/json.html#encoders-and-decoders)
  documentation for more details.

```python linenums="1"
from taipy import Config

hist_temp_cfg = Config.configure_json_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.json",
)
```

In this example, we configure a JSON data node. The _id_ argument is
"historical_temperature". Its _scope_ is `SCENARIO` (default value), and the path is
the file *hist_temp.json*.

Without specific _**encoder**_ and _**decoder**_ parameters, *hist_temp_cfg* will use
default encoder and decoder provided by Taipy, which have the capability to encode and
decode Python [`enum.Enum`](https://docs.python.org/3/library/enum.html),
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects),
[`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objects),
and [dataclass](https://docs.python.org/3/library/dataclasses.html) object.

```python linenums="1"
from taipy import Config
import json

class SaleRow:
    date: str
    nb_sales: int

class SaleRowEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SaleRow):
            return {
                '__type__': "SaleRow",
                'date': obj.date,
                'nb_sales': obj.nb_sales}
        return json.JSONEncoder.default(self, obj)

class SaleRowDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self,
                                  object_hook=self.object_hook,
                                  *args,
                                  **kwargs)

    def object_hook(self, d):
        if d.get('__type__') == "SaleRow":
            return SaleRow(date=d['date'], nb_sales=d['nb_sales'])
        return d

sales_history_cfg = Config.configure_json_data_node(
    id="sales_history",
    path="path/sales.json",
    encoder=SaleRowEncoder,
    decoder=SaleRowDecoder)
```

In this next example, we config a `JSONDataNode^` with custom JSON _**encoder**_
and _**decoder**_:

- In lines 4-6, we define a custom class `SaleRow`, representing data in a JSON object.

- In line 8-27, we define custom encoder and decoder for the `SaleRow` class.
    - When [writing a JSONDataNode](../entities/data-node-mgt.md#write-data-node),
    the `SaleRowEncoder` encodes a `SaleRow` object to JSON format. For example,
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
    - When reading a JSONDataNode, the `SaleRowDecoder` is used to convert a JSON
    object with the attribute `__type__` into a Python object corresponding to the
    value of the attribute. In this example, the "SaleRow"` data class.

- In lines 29-33, we create a JSON data node configuration. The _id_ identifier is
"sales_history", the default `SCENARIO` scope is used. The encoder and decoder are the
custom encoder and decoder defined above.

!!! Note

    To configure a JSON data node, it is equivalent to use the method
    `Config.configure_json_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="json"`.

## Parquet

A `ParquetDataNode^` data node is a specific data node used to model
[Parquet](https://parquet.apache.org/) file data. To add a new _Parquet_ data node
configuration, the `Config.configure_parquet_data_node()^` method can be used. In
addition to the generic parameters described in [Data node configuration](data-node-config.md)
section, the following parameters can be provided:

- _**default_path**_ is a mandatory parameter and represents the default Parquet path to
  the file or directory used by Taipy to read and write
  the data.

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
    of these methods at the [Data Node Management page](../entities/data-node-mgt.md#parquet).

- _**exposed_type**_ indicates the data type returned when reading the data node (more examples
  of reading from Parquet data node with different _exposed_type_ is available on
  [Read / Write a data node](../entities/data-node-mgt.md#parquet) documentation):
    - By default, _exposed_type_ is "pandas", and the data node reads the Parquet file
      as a Pandas dataframe (`pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "modin", the data node reads the Parquet
      file as a modin dataframe (`modin.pandas.DataFrame`) when executing the read method.
    - If the _exposed_type_ value provided is "numpy", the data node reads the Parquet
      file as a NumPy array (`numpy.ndarray`) when executing the read method.
    - If the provided _exposed_type_ value is a Callable, the data node creates a list of
      objects as returned by the Callable. Each object represents a record in the Parquet
      file. The Parquet file is read as a `pandas.DataFrame`, and each row of the DataFrame
      is passed to the Callable as keyword arguments where the key is the column name and the
      value is the corresponding value for that row.

```python linenums="1"
from taipy import Config

temp_cfg = Config.configure_parquet_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.parquet",
```

In lines 3-5, we configure a basic Parquet data node. The only two required parameters are
_id_ and _default_path_.

```python linenums="1"
from taipy import Config

read_kwargs = {"filters": [("log_level", "in", {"ERROR", "CRITICAL"})]}
write_kwargs = {"partition_cols": ["log_level"], "compression": None}

log_cfg = Config.configure_parquet_data_node(
    id="log_history",
    default_path="path/hist_log.parquet",
    engine="pyarrow", # default
    compression="snappy", # default, but overridden by the key in write_kwargs
    exposed_type="modin",
    read_kwargs=read_kwargs,
    write_kwargs=write_kwargs)
```

In this larger example, we illustrate some specific benefits of using ParquetDataNode for
storing tabular data. This time, we pass the _read_kwargs_ and _write_kwargs_ dictionary
parameters to be passed as keyword arguments to
[`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
respectively.

Here, the dataset is partitioned (using _partition_cols_ on line 4) by the "log_level"
column when being written to disk. Also, filtering is performed (using _filters_ on line 3)
to read only the rows where the "log_level" column value is either "ERROR" or "CRITICAL"
— speeding up the read, especially when dealing with a large amount of data.

Note that even though line 10 specifies the _compression_ as "snappy", because the "compression"
key was also provided in the _write_kwargs_ dictionary on line 4, the latter value will be
used — hence the _compression_ will be `None`.

!!! Note

    To configure a Parquet data node, it is equivalent to use the method
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
- _**custom_document**_ represents the custom class that is used to store, encode, and
  decode data when reading and writing to a Mongo collection. The data returned by the
  read method is a list of custom_document object(s), and the data passed as a parameter
  of the write method is a (list of) custom_document object(s). The custom_document can have:
    - An optional `decoder()` method to decode data in the Mongo collection to a custom object when reading.
    - An optional `encoder()` method to encode the object's properties to the Mongo collection format when writing.
- _**db_username**_ represents the username that will be used by Taipy to access MongoDB.
- _**db_password**_ represents the user's password that will be used by Taipy to access MongoDB.
- _**db_port**_ represents the database port that will be used by Taipy to access MongoDB.<br/>
    The default value of _db_port_ is 27017.
- _**db_host**_ represents the database host that will be used by Taipy to access MongoDB.<br/>
    The default value of _db_host_ is "localhost".

```python linenums="1"
from taipy import Config

historical_data_cfg = Config.configure_mongo_collection_data_node(
    id="historical_data",
    db_username="admin",
    db_password="pa$$w0rd",
    db_name="taipy",
    collection_name="historical_data_set",
)
```

In this example, we configure a *mongo_collection* data node with the id "historical_data":

- Its scope is the default value `SCENARIO`.
- The database username is "admin", the user's password is "pa$$w0rd"
- The database name is "taipy"
- The collection name is "historical_data_set".
- Without being specified, the custom document class is defined as
  `taipy.core.DefaultCustomDocument`.

```python linenums="1"
from taipy import Config
from datetime import datetime

class DailyMinTemp:
    def __init__(self, Date : datetime=None, Temp : float=None):
        self.Date = Date
        self.Temp = Temp

    def encode(self):
        return {
            "date": self.Date.isoformat(),
            "temperature": self.Temp,
        }

    @classmethod
    def decode(cls, data):
        return cls(
            datetime.fromisoformat(data["date"]),
            data["temperature"],
        )

historical_data_cfg = Config.configure_mongo_collection_data_node(
    id="historical_data",
    db_username="admin",
    db_password="pa$$w0rd",
    db_name="taipy",
    collection_name="historical_data_set",
    custom_document=DailyMinTemp,
)
```

In this next example, we configure another *mongo_collection* data node, with the custom
document is defined as `DailyMinTemp` class.

-   The custom encode method encodes `datetime.datetime` to the ISO 8601 string format.
-   The corresponding decode method decodes a ISO 8601 string to `datetime.datetime`.
-   The `_id` of the Mongo document is discarded.

Without this two methods, the default decoder will map the key of each document to
the corresponding property of a `DailyMinTemp` object, and the default encoder will
convert `DailyMinTemp` object's properties to a dictionary, without any special formatting.

!!! Note

    To configure a Mongo collection data node, it is equivalent to use the method
    `Config.configure_mongo_collection_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="mongo_collection"`.

## Generic

A `GenericDataNode^` is a specific data node used to model generic data types where the
read and the write functions are defined by the user. To add a new _generic_ data node
configuration, the `Config.configure_generic_data_node()^` method can be used. In addition
to the parameters described in the [Data node configuration](data-node-config.md) section,
the following parameters can be provided:

- _**read_fct**_ is a mandatory parameter that represents a Python function provided
  by the user. It will be used to read the data. More optional parameters can be passed
  through the _**read_fct_params**_ parameter.

- _**write_fct**_ is a mandatory parameter representing a Python function provided by the
  user. It will be used to write/serialize the data. The provided function must have at least
  one parameter dedicated to receiving data to be written. It must be the first parameter.
  More optional parameters can be passed through the _**write_fct_params**_ parameter.

- _**read_fct_params**_ represents the parameters that are passed to the _read_fct_ to
  read/de-serialize the data. It must be a `List` type object.

- _**write_fct_params**_ represents the parameters that are passed to the _write_fct_ to write
  the data. It must be a `List` type object.


```python linenums="1"
from taipy import Config

def read_text(path: str) -> str:
    with open(path, 'r') as text_reader:
        data = text_reader.read()
    return data

def write_text(data: str, path: str):
    with open(path, 'w') as text_writer:
        text_writer.write(data)

historical_data_cfg = Config.configure_generic_data_node(
    id="historical_data",
    read_fct=read_text,
    write_fct=write_text,
    read_fct_params=["../path/data.txt"]
    write_fct_params=["../path/data.txt"])
```

In this small example, we configure a generic data node with the id "historical_data".

In line 14-15, we provide two Python functions (previously defined) as _read_fct_ and _write_fct_
parameters to read and write the data in a text file. Note that the first parameter of _write_fct_
is mandatory, and it is used to pass the data to write.

In line 16, we provide _read_fct_params_ with a path to let the _read_fct_ know where to read the
data.

In line 17, we provide a list of parameters to _write_fct_params_ with a path to let the _write_fct_
know where to write the data. Note that the data parameter will be automatically passed at runtime
when writing the data.

The generic data node can also be used in situations that require a specific business logic either in
reading or writing data, and that can be easily provided by the user. Follows an example using a
custom delimiter when writing and reading a csv file.

```python linenums="1"
import csv
from typing import List

from taipy import Config

def read_csv(path: str, delimiter: str = ",") -> str:
    with open(path, newline=' ') as csvfile:
        data = csv.reader(csvfile, delimiter=delimiter)
    return data

def write_csv(data: List[str], path: str, delimiter: str = ","):
    headers = ["country_code", "country"]
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

csv_country_data_cfg = Config.configure_generic_data_node(
    id="csv_country_data",
    read_fct=read_csv,
    write_fct=write_csv,
    read_fct_params=["../path/data.csv", ";"]
    write_fct_params=["../path/data.csv", ";"])
```

It is also possible to use a generic data node custom functions to do some data preparation:

```python linenums="1"
from datetime import datetime
from typing import List

import pandas as pd

from taipy import Config

def read_csv(path: str) -> str:
    # reading a csv file, define some column types and parse a string into datetime
    custom_date_parser = lambda x: datetime.strptime(x, "%Y %m %d %H:%M:%S")
    data = pd.read_csv(
        path,
        parse_dates=['date'],
        date_parser=custom_date_parser,
        dtype={
            "name": str,
            "grade": int
        }
    )
    return data

def write_csv(data: pd.DataFrame, path: str):
    # dropping not a number values before writing
    data.dropna().to_csv(path)

student_data = Config.configure_generic_data_node(
    id="student_data",
    read_fct=read_csv,
    write_fct=write_csv,
    read_fct_params=["../path/data.csv"],
    write_fct_params=["../path/data.csv"])
```


!!! Note

    To configure a generic data node, it is equivalent to use the method
    `Config.configure_generic_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="generic"`.

## In memory

An `InMemoryDataNode^` is a specific data node used to model any data in the RAM. The
`Config.configure_in_memory_data_node()^` method can be used to add a new in_memory
data node configuration. In addition to the generic parameters described in the
[Data node configuration](data-node-config.md) section, an optional parameter can be
provided:

- If the _**default_data**_ is given as a parameter, the data node is automatically
  written with the corresponding value (note that any serializable python object can
  be used).

```python linenums="1"
from taipy import Config
from datetime import datetime

date_cfg = Config.configure_in_memory_data_node(
    id="date",
    default_data=datetime(2022, 1, 25))
```

In this example, we configure an in_memory data node with the id "date", the scope
is `SCENARIO` (default value), and a default data is provided.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multiprocess environment.
    (See [Job configuration](job-config.md#standalone) for more details).

!!! Note

    To configure an in_memory data node, it is equivalent to use the method
    `Config.configure_in_memory_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="in_memory"`.

[:material-arrow-right: The next section introduces the task configuration](task-config.md).
