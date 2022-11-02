For Taipy to instantiate a [Data node](../concepts/data-node.md), a data node configuration must be provided.
`DataNodeConfig^` is used to configure the various data nodes that Taipy will manipulate. To configure a new
`DataNodeConfig^`, one can use the function `Config.configure_data_node()^`.

```python linenums="1"
from taipy import Config

data_node_cfg = Config.configure_data_node(id="data_node_cfg")
```

In the previous code, we configured a simple data node just providing an identifier as a string "data_node_cfg".

More optional attributes are available on data nodes, including:

- _**id**_ is the identifier of the data node config.<br/>
    It is a **mandatory** parameter that must be unique. It must be a valid Python identifier.

-   _**scope**_ is a `Scope^`.<br/>
    It corresponds to the [scope](../concepts/scope.md) of the data node that will be instantiated from the data
    node configuration. The **default value** is `Scope.SCENARIO`.

-   _**storage_type**_ is an attribute that indicates the type of storage of the
    data node.<br/>
    The possible values are ["pickle"](#pickle) (**the default value**),
    ["csv"](#csv), ["excel"](#excel), ["json"](#json), ["mongo_collection"](#mongo-collection),
    ["sql"](#sql), ["sql_table"](#sql_table), ["in_memory"](#in-memory), or ["generic"](#generic).<br/>
    As explained in the following subsections, depending on the _storage_type_, other configuration attributes must
    be provided in the parameter _properties_ parameter.

-   _**cacheable**_ is an attribute that indicates if the data node can be cached during the execution of the tasks
    it is connected to.

-   Any other custom attribute can be provided through the parameter _**properties**_, which is
    a dictionary (a description, a tag, etc.)<br/>
    This _properties_ dictionary is used to configure the parameters specific to each storage type.
    Note also that all this dictionary _**properties**_ is copied in the dictionary properties of all the data
    nodes instantiated from this data node configuration.<br/>

Below are two examples of data node configurations.

```python linenums="1"
from taipy import Config, Scope

date_cfg = Config.configure_data_node(id="date_cfg", description="The current date of the scenario")

model_cfg = Config.configure_data_node(id="model_cfg",
                                       scope=Scope.CYCLE,
                                       storage_type="pickle",
                                       description="The trained model shared by all scenarios",
                                       code=54)
```

In line 3, we configured a simple data node with the id "date_cfg". The default
value for _scope_ is `SCENARIO`. The _storage_type_ also has the default value "pickle".<br/>
An optional custom property called _description_ is also added: this property is propagated
to the data nodes instantiated from this config.

In lines 5-9, we add another data node configuration with the id "model_cfg". _scope_ is
set to `CYCLE`, so the corresponding data nodes will be shared by all the scenarios from
the same cycle. _storage_type_ is "pickle" as well, and two optional custom properties are
added: a _description_ string and an integer _code_. These two properties are propagated to the
data nodes instantiated from this config.

# Storage type

Taipy proposes various predefined _data nodes_ corresponding to the most popular
_storage types_. Thanks to predefined _data nodes_, the Python developer does not need
to spend much time configuring the _storage types_ or the
_query system_. Most of the time, a predefined _data node_ corresponding to a basic and standard use case satisfies
the user's needs like pickle file, CSV file, SQL table, MongoDB collection, Excel sheet, etc.

The various predefined _storage types_ are mainly used for input data. Indeed, the input data is usually provided by an
external component, and the Python developer user does not control the format.

However, in most cases, particularly for intermediate or output _data nodes_, it is not relevant to prefer one _storage
type_. The end-user wants to manipulate the corresponding data within the Taipy application. Still, the user does not
have any particular specifications regarding the _storage type_. In such a case, the Python developer is
recommended to use the default _storage type_ pickle that does not require any configuration.

In case a more specific method to store, read and write the data is needed by the user, Taipy proposes a _Generic data
node_ that can be used for any _storage type_ or any kind of _query system_. The user only needs to provide two python
functions, one for reading and one for writing the data.

Each predefined data node is described in a subsequent section.

# Pickle

A `PickleDataNode^` is a specific data node used to model
pickle data.
To add a new _pickle_ data node configuration, the `Config.configure_pickle_data_node()^` method can be used. In
addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), two optional parameters can be provided.

-   _**default_path**_ represents the default file path used by Taipy to read and write the data.<br/>
    If the pickle file already exists (in the case of a shared input data node, for instance), it is necessary
    to provide the default file path as the _default_path_ parameter.<br/>
    If no value is provided, Taipy will use an internal path in the Taipy storage folder (more details on the
    Taipy storage folder configuration available on the [Global configuration](global-config.md) documentation).

-   _**default_data**_ indicates data that is automatically written to the data node upon creation.<br/>
    Any serializable Python object can be used. The default value is `None`.

```python linenums="1"
from taipy import Config
from datetime import datetime

date_cfg = Config.configure_pickle_data_node(id="date_cfg", default_data=datetime(2022, 1, 25))

model_cfg = Config.configure_pickle_data_node(id="model_cfg", default_path="path/to/my/model.p",description="The trained model")
```

In line 4, we configure a simple pickle data node with the id "date_cfg". The scope is `SCENARIO`
(default value), and a default data is provided.

In line 6, we add another pickle data node configuration with the id "model_cfg". The default
`SCENARIO` scope is used. Since the data node config corresponds to a pre-existing pickle file, a default path
"path/to/my/model.p" is provided. We also added an optional custom description.

!!! Note

    To configure a pickle data node, it is equivalent to use the method `Config.configure_pickle_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="pickle"`.

# CSV

A `CSVDataNode^` data node is a specific data node used to model CSV file data. To add a new _CSV_ data node
configuration, the `Config.configure_csv_data_node()^` method can be used. In addition to the generic parameters
described in the previous section [Data node configuration](data-node-config.md), the following parameters can be provided:

-   _**default_path**_ is a mandatory parameter and represents the default CSV file path used by Taipy to read and write
    the data.

-   _**has_header**_ indicates if the file has a header of not.<br/>
    By default, _has_header_ is True and Taipy will use the 1st row in the CSV file as the header.

-   _**exposed_type**_ indicates the data type returned when reading the data node (more examples of reading from CSV data node with different _exposed_type_ is available on [Read / Write a data node](../entities/data-node-mgt.md#csv) documentation):
    -   By default, _exposed_type_ is `"pandas"`, and the data node will read the CSV file as a `pandas.DataFrame`.
    -   If the _exposed_type_ value provided is `"numpy"`, the data node will read the CSV file to a numpy array.
    -   If the provided _exposed_type_ value is a custom Python class, the data node will create a list of custom
    objects with the given custom class, each object will represent a row in the CSV file.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

temp_cfg = Config.configure_csv_data_node(id="historical_temperature",
                                          default_path="path/hist_temp.csv",
                                          has_header=True,
                                          exposed_type="numpy")

sales_cfg = Config.configure_csv_data_node(id="sale_history",
                                           default_path="path/sale_history.csv",
                                           exposed_type=SaleRow)
```

In lines 3-5, we define a custom class `SaleRow` representing a row of the CSV file.

In lines 7-10, we configure a basic CSV data node with the id "historical_temperature". Its _scope_ is by
default `SCENARIO`. The default path corresponds to the file `path/hist_temp.csv`. The property _has_header_ being True,
representing the CSV file has a header.

In lines 12-14, we add another CSV data node configuration with the id "sale_history". The
default `SCENARIO` scope is used again. Since we have a custom class pre-defined for this CSV file (`SaleRow`), we
provide it as the _exposed_type_ parameter.

!!! Note

    To configure a CSV data node, it is equivalent to use the method `Config.configure_csv_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="csv"`.

# Excel

An `ExcelDataNode^` is a specific data node used to model xlsx
file data. To add a new _Excel_ data node configuration, the `Config.configure_excel_data_node()^` method can be used.
In addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), a mandatory and three optional parameters can be provided.

-   _**default_path**_ is a mandatory parameter that represents the default Excel file path used by Taipy to read and
    write the data.

-   _**has_header**_ indicates if the file has a header of not.<br/>
    By default, _has_header_ is True and Taipy will use the 1st row in the Excel file as the header.

-   _**sheet_name**_ represents which specific sheet in the Excel file to read:
    -   By default, _sheet_name_ is None and the data node will return all sheets in the Excel file when reading it.
    -   If _sheet_name_ is provided as a string, the data node will read only the data of the corresponding sheet.
    -   If _sheet_name_ is provided with a list of sheet names, the data node will return a dictionary with the key
    being the sheet name and the value being the data of the corresponding sheet.

-   _**exposed_type**_ indicates the data type returned when reading the data node (more examples of reading from Excel data node with different _exposed_type_ is available on [Read / Write a data node](../entities/data-node-mgt.md#excel) documentation):
    -   By default, _exposed_type_ is `"pandas"`, and the data node will read the Excel file as a `pandas.DataFrame`.
    -   If the _exposed_type_ value provided is `"numpy"`, the data node will read the Excel file to a numpy array.
    -   If the provided _exposed_type_ value is a custom Python class, the data node will create a list of custom
    objects with the given custom class, each object will represent a row in the Excel file.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

hist_temp_cfg = Config.configure_excel_data_node(id="historical_temperature",
                                                 default_path="path/hist_temp.xlsx",
                                                 exposed_type="numpy")

sales_cfg = Config.configure_excel_data_node(id="sale_history",
                                             default_path="path/sale_history.xlsx",
                                             sheet_name=["January", "February"],
                                             exposed_type=SaleRow)
```

In lines 3-5, we define a custom class `SaleRow`, representing an the Excel file row.

In lines 7-9, we configure an Excel data node. The _id_ identifier is "historical_temperature". Its _scope_ is
`SCENARIO` (default value), and the default path is the file hist_temp.xlsx. With _has_header_ being True, the
Excel file must have a header. The _sheet_name_ is not provided so Taipy will use the default value "Sheet1".

In lines 10-13, we add another Excel data node configuration. The _id_ identifier is "sale_history", the
default `SCENARIO` scope is used. Since we have a custom class pre-defined for this Excel file, we will provide it in
the _exposed_type_. We also provide the list of specific sheets we want to use as the _sheet_name_ parameter.

!!! Note

    To configure an Excel data node, it is equivalent to use the method `Config.configure_excel_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="excel"`.

# SQL Table

!!! Important

    -  To be able to use a `SQLTableDataNode^` with Microsoft SQL Server you need to run internal dependencies with `pip install taipy[mssql]` and install your corresponding [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
    - To be able to use a `SQLTableDataNode^` with MySQL Server you need to run internal dependencies with `pip install taipy[mysql]` and install your corresponding [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
    - To be able to use a `SQLTableDataNode^` with PostgreSQL Server you need to run internal dependencies with `pip install taipy[postgresql]` and install your corresponding [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).


An `SQLTableDataNode^` is a specific data node that models data stored in a single SQL table. To add a new _SQL table_
data node configuration, the `Config.configure_sql_table_data_node()^` method can be used. In addition to the generic
parameters described in the previous section [Data node configuration](data-node-config.md), the following parameters
can be provided:

-   _**db_username**_ represents the database username that will be used by Taipy to access the database.
-   _**db_password**_ represents the database user's password that will be used by Taipy to access the database.
-   _**db_name**_ represents the name of the database.
-   _**db_engine**_ represents the engine of the database.<br/>
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
-   _**table_name**_ represents the name of the table to read from and write into.
-   _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
    The default value of _db_port_ is 1433.
-   _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
    The default value of _db_host_ is "localhost".
-   _**db_driver**_ represents the database driver that will be used by Taipy.<br/>
    The default value of _db_driver_ is "ODBC Driver 17 for SQL Server".

```python linenums="1"
from taipy import Config

forecasts_cfg = Config.configure_sql_table_data_node(id="forecasts",
                                               db_username="admin",
                                               db_password="password",
                                               db_name="taipy",
                                               db_engine="mssql",
                                               table_name="forecast_table")
```

In the previous example, we configure a _SQL table_ data node with the id "forecasts". Its scope is the
default value `SCENARIO`. The database username is "admin", the user's password is "password", the database name
is "taipy", and the database engine is `mssql` (short for Microsoft SQL). The table name is "forecast_table". When the data node is read, it will read all the rows from the table "forecast_table", and when the data node is written, it will delete all the data in the table and insert the new data.

!!! Note

    To configure a SQL table data node, it is equivalent to use the method `Config.configure_sql_table_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="sql_table"`.

# SQL

!!! Important

    -  To be able to use a `SQLTableDataNode^` with Microsoft SQL Server you need to run internal dependencies with `pip install taipy[mssql]` and install your corresponding [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server).
    - To be able to use a `SQLTableDataNode^` with MySQL Server you need to run internal dependencies with `pip install taipy[mysql]` and install your corresponding [MySQL Driver for MySQL](https://pypi.org/project/PyMySQL/).
    - To be able to use a `SQLTableDataNode^` with PostgreSQL Server you need to run internal dependencies with `pip install taipy[postgresql]` and install your corresponding [Postgres JDBC Driver for PostgreSQL](https://www.postgresql.org/docs/7.4/jdbc-use.html).

An `SQLDataNode^` is a specific data node used to model data stored in an SQL Database. To add a new _SQL_ data node
configuration, the `Config.configure_sql_data_node()^` method can be used. In addition to the generic parameters
described in the previous section [Data node configuration](data-node-config.md), the following parameters can be
provided:

-   _**db_username**_ represents the database username that will be used by Taipy to access the database.
-   _**db_password**_ represents the database user's password that will be used by Taipy to access the database.
-   _**db_name**_ represents the name of the database.
-   _**db_engine**_ represents the engine of the database.<br/>
    Possible values are _"sqlite"_, _"mssql"_, _"mysql"_, or _"postgresql"_.
-   _**read_query**_ represents the SQL query that will be used by Taipy to read the data from the database.
-   _**write_query_builder**_ is a callable function that takes in the data as an input parameter and returns a list of
    SQL queries to be executed when the write data node method is called.
-   _**db_port**_ represents the database port that will be used by Taipy to access the database.<br/>
    The default value of _db_port_ is 1433.
-   _**db_host**_ represents the database host that will be used by Taipy to access the database.<br/>
    The default value of _db_host_ is "localhost".
-   _**db_driver**_ represents the database driver that will be used by Taipy.<br/>
    The default value of _db_driver_ is "ODBC Driver 17 for SQL Server".

```python linenums="1"
from taipy import Config
import pandas as pd

def write_query_builder(data: pd.DataFrame){
    insert_data = list(data[["date", "nb_sales"]].itertuples(index=False, name=None))
    return [
        "DELETE FROM forecast_table",
        ("INSERT INTO forecast_table VALUES (?, ?)", insert_data)
    ]
}

forecasts_cfg = Config.configure_sql_data_node(id="forecasts",
                                               db_username="admin",
                                               db_password="password",
                                               db_name="taipy",
                                               db_engine="mssql",
                                               read_query="SELECT * from forecast_table",
                                               write_query_builder= write_query_builder)
```

In the previous example, we configure a _SQL_ data node with the id "forecasts". Its scope is the
default value `SCENARIO`. The database username is "admin", the user's password is "password", the database name
is "taipy", and the database engine is `mssql` (short for Microsoft SQL). The read query will be "SELECT \* from
forecast_table".

The write query builder in this example is a callable function that takes in a dataframe and return a list of queries. The first query will delete all the data in the table "forecast_table", and the second query is a prepared statement that takes in two values, which is the data from the two columns "date" and "nb_sales" in the dataframe. Since this is a prepared statement, it must be passed as a tuple with the first element being the query and the second element being the data.

The data parameter of the write query builder is expected to have the same data type as the return type of the task function whose output is the data node. In this example, the task function returns a dataframe, so the data parameter of the write query builder is also expected to be a dataframe.

!!! Note

    To configure an SQL data node, it is equivalent to use the method `Config.configure_sql_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="sql"`.

# JSON

A `JSONDataNode^` is a type of data node used to model JSON file data. To add a new _JSON_ data node configuration, the
`Config.configure_json_data_node_node()^` method can be used. In addition to the generic parameters described in
[Data node configuration](data-node-config.md) section, the following parameters can be provided:

-   _**default_path**_ is a mandatory parameter that represents the JSON file path used by Taipy to read and write data.

-   _**encoder**_ and _**decoder**_ parameters are optional parameters that represent the encoder (json.JSONEncoder) and
    decoder (json.JSONDecoder) used to serialize and deserialize JSON data.<br/>
    Check out [JSON Encoders and Decoders documentation](https://docs.python.org/3/library/json.html#encoders-and-decoders) for more details.

```python linenums="1"
from taipy import Config

hist_temp_cfg = Config.configure_json_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.json",
)
```

In this example, we configure a JSON data node. The _id_ argument is "historical_temperature". Its _scope_ is
`SCENARIO` (default value), and the path is the file *hist_temp.json*.

Without specific _**encoder**_ and _**decoder**_ parameters, *hist_temp_cfg* will use default encoder and decoder provided by Taipy,
which have the capability to encode and decode Python [`enum.Enum`](https://docs.python.org/3/library/enum.html),
[`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects), and
[dataclass](https://docs.python.org/3/library/dataclasses.html) object.

```python linenums="1"
from taipy import Config
import json

class SaleRow:
    date: str
    nb_sales: int

class SaleRowEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SaleRow):
            return {'__type__': "SaleRow", 'date': obj.date, 'nb_sales': obj.nb_sales}
        return json.JSONEncoder.default(self, obj)

class SaleRowDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, d):
        if d.get('__type__') == "SaleRow":
            return SaleRow(date=d['date'], nb_sales=d['nb_sales'])
        return d

sales_cfg = Config.configure_json_data_node(id="sale_history",
                                             path="path/sale_history.json",
                                             encoder=SaleRowEncoder,
                                             decoder=SaleRowDecoder)
```

In this next example, we config a `JSONDataNode^` with custom JSON _**encoder**_ and _**decoder**_:

- In lines 4-6, we define a custom class `SaleRow`, representing data in a JSON object.

- In line 8-21, we define custom encoder and decoder for the `SaleRow` class.
    - When [write to JSONDataNode](../entities/data-node-mgt.md#write-data-node), the `SaleRowEncoder` will
    encode a `SaleRow` object to JSON format. For example, after create a scenario,
        ```python
        scenario.sale_history.write(SaleRow("12/24/2018", 1550))
        ```
    will write
        ```json
        {
            "__type__": "SaleRow",
            "date": "12/24/2018",
            "nb_sales": 1550,
        }
        ```
    to the file *path/sale_history.json*.
    - When read a JSONDataNode, the `SaleRowDecoder` will decode any JSON object has `"__type__": "SaleRow"` to a `SaleRow` object.

- In lines 23-26, we create a JSON data node configuration. The _id_ identifier is "sale_history", the
default `SCENARIO` scope is used. The encoder and decoder are the custom encoder and decoder defined above.

!!! Note

    To configure a JSON data node, it is equivalent to use the method `Config.configure_json_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="json"`.

# Mongo Collection

A `MongoCollectionDataNode^` is a specific data node used to model data stored in a Mongo collection. To add a new *mongo_collection* data node configuration, the `Config.configure_mongo_collection_data_node()^` method can be used.
In addition to the generic parameters described in the previous section [Data node configuration](data-node-config.md), multiple parameters can be provided.

-   _**db_name**_ represents the name of the database in MongoDB.
-   _**collection_name**_ represents the name of the data collection in the database.
-   _**custom_document**_ represents the custom class that is used to store, encode, and decode data when reading and writing to a Mongo collection. The data returned by the read method is a list of custom_document object(s), and the data passed as a parameter of the write method is a (list of) custom_document object(s). The custom_document can have:
    -   An otional `decoder()` method to decode data in the Mongo collection to a custom object when reading.
    -   An optional `encoder()` method to encode the object's properties to the Mongo collection format when writing.
-   _**db_username**_ represents the username that will be used by Taipy to access MongoDB.
-   _**db_password**_ represents the user's password that will be used by Taipy to access MongoDB.
-   _**db_port**_ represents the database port that will be used by Taipy to access MongoDB.<br/>
    The default value of _db_port_ is 27017.
-   _**db_host**_ represents the database host that will be used by Taipy to access MongoDB.<br/>
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

-   Its scope is the default value `SCENARIO`.
-   The database username is "admin", the user's password is "pa$$w0rd"
-   The database name is "taipy"
-   The collection name is "historical_data_set".
-   Without being specified, the custom document class is defined as `taipy.core.DefaultCustomDocument`.

```python linenums="1"
from taipy import Config
from datetime import datetime

class DailyMinTemp:
    def __init__(self, Date : datetime = None, Temp : float = None):
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

In this next example, we configure another *mongo_collection* data node, with the custom document is defined as DailyMinTemp class.

-   The custom encode method encodes `datetime.datetime` to the ISO 8601 string format.
-   The corresponding decode method decodes a ISO 8601 string to `datetime.datetime`.
-   The `_id` of the Mongo document is discarded.

Without this two methods, the default decoder will map the key of each document to the corresponding property of a DailyMinTemp object,
and the default encoder will convert DailyMinTemp object's properties to a dictionary, without any special formating.

!!! Note

    To configure a Mongo collection data node, it is equivalent to use the method `Config.configure_mongo_collection_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="mongo_collection"`.

# Generic

A `GenericDataNode^` is a specific data node used to model generic data types where the read and the write functions
are defined by the user. To add a new _generic_ data node configuration, the `Config.configure_generic_data_node()^`
method can be used. In addition to the parameters described in the previous section
[Data node configuration](data-node-config.md),  the following parameters can be provided:

-   _**read_fct**_ is a mandatory parameter that represents a Python function provided by the user. It will
    be used to read the data. More optional parameters can be passed through the _**read_fct_params**_ parameter.

-   _**write_fct**_ is a mandatory parameter representing a Python function provided by the user. It will
    be used to write/serialize the data. The provided function must have at least one parameter dedicated to
    receiving data to be written. More optional parameters can be passed through the _**write_fct_params**_ parameter.

-   _**read_fct_params**_ represents the parameters that are passed to the _read_fct_ to read/de-serialize the data.
    It must be a `List` type object.

-   _**write_fct_params**_ represents the parameters that are passed to the _write_fct_ to write the data.
    It must be a `List` type object.


```python linenums="1"
from taipy import Config

def read_data():
    pass

def write_data(data: Any, path: str):
    pass

historical_data_cfg = Config.configure_generic_data_node(id="historical_data",
                                                         read_fct=read_data,
                                                         write_fct=write_data,
                                                         write_fct_params=['../path/'])
```

In this small example, we configure a generic data node with the id "historical_data". We provide two
Python functions (previously defined) as _read_fct_ and _write_fct_ parameters to read and write the data. We also
provided a list object for the _write_fct_params_ with a path to let the _write_fct_ know where to write the data.


!!! Note

    To configure a generic data node, it is equivalent to use the method `Config.configure_generic_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="generic"`.

# In memory

An `InMemoryDataNode^` is a specific data node used to model any data in the RAM. The
`Config.configure_in_memory_data_node()^` method can be used to add a new in_memory data node configuration. In
addition to the generic parameters described in the previous section [Data node configuration](data-node-config.md),
an optional parameter can be provided.

-   If the _**default_data**_ is given as a parameter, the data node is automatically written with the corresponding
    value (note that any python object can be used).

```python linenums="1"
from taipy import Config
from datetime import datetime

date_cfg = Config.configure_in_memory_data_node(id="date", default_data=datetime(2022, 1, 25))
```

In this example, we configure an in_memory data node with the id "date", the scope is `SCENARIO`
(default value), and a default data is provided.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multiprocess environment. (See
    [Job configuration](job-config.md#standalone) for more details).

!!! Note

    To configure an in_memory data node, it is equivalent to use the method `Config.configure_in_memory_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="in_memory"`.

[:material-arrow-right: The next section introduces the task configuration](task-config.md).
