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
    ["csv"](#csv), ["excel"](#excel), ["sql"](#sql), ["in_memory"](#in-memory), or
    ["generic"](#generic).<br/>
    As explained in the following subsections, depending on the _storage_type_, other configuration attributes must
    be provided in the parameter _properties_ parameter.

-   Any other custom attribute can be provided through the parameter _**properties**_, which is
    a dictionary (a description, a tag, etc.)<br/>
    All the properties are given to the data nodes instantiated from this data node configuration.<br/>
    This _properties_ dictionary is also used to configure the parameters specific to each storage type.

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

In lines 5, 6, 7, 8, and 9 we add another data node configuration with the id "model_cfg". _scope_ is
set to `CYCLE`, so the corresponding data nodes will be shared by all the scenarios from
the same cycle. _storage_type_ is "pickle" as well, and two optional custom properties are
added: a _description_ string and an integer _code_. These two properties are propagated to the
data nodes instantiated from this config.

# Storage type

Taipy proposes various predefined _data nodes_ corresponding to the most popular
_storage types_. Thanks to predefined _data nodes_, the Python developer does not need
to spend much time configuring the _storage types_ or the
_query system_. Most of the time, a predefined _data node_ corresponding to a basic and standard use case satisfies
the user's needs like pickle file, csv file, sql table, Excel sheet, etc.

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

-   The _**path**_ parameter represents the file path used by Taipy to read and write the data.
    If the pickle file already exists (in the case of a shared input data node, for instance), it is necessary
    to provide the file path as the _path_ parameter. If no value is provided, Taipy will use an internal path
    in the Taipy storage folder (more details on the Taipy storage folder configuration available on the
    [Global configuration](global-config.md) documentation).

-   If the _**default_data**_ is provided, the data node is automatically written with the corresponding
    value. Any serializable Python object can be used.

```python linenums="1"
from taipy import Config
from datetime import datetime

date_cfg = Config.configure_pickle_data_node(id="date_cfg", default_data=datetime(2022, 1, 25))

model_cfg = Config.configure_pickle_data_node(id="model_cfg", path="path/to/my/model.p",description="The trained model")
```

In line 4, we configure a simple pickle data node with the id "date_cfg". The scope is `SCENARIO`
(default value), and a default data is provided.

In line 6 we add another pickle data node configuration with the id "model_cfg". The default
`SCENARIO` scope is used. Since the data node config corresponds to a pre-existing pickle file, a path
"path/to/my/model.p" is provided. We also added an optional custom description.

!!! Note

    To configure a pickle data node, it is equivalent to use the method `Config.configure_pickle_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="pickle"`.

# Csv

A `CSVDataNode^` data node is a specific data node used to model csv file data. To add a new _csv_ data node
configuration, the `Config.configure_csv_data_node()^` method can be used. In addition to the generic parameters
described in the previous section [Data node configuration](data-node-config.md), one mandatory and two optional
parameters can be provided.

-   The _**path**_ parameter is a mandatory parameter and represents the csv file path used by Taipy to read and write
    the data.

-   The _**has_header**_ parameter represents if the file has a header of not. By default, _has_header_ is True and Taipy
    will use the 1st row in the CSV file as the header.

-   When the _**exposed_type**_ is given as a parameter, if the _exposed_type_ value provided is `numpy`, the
    data node will read the csv file to a numpy array. If the provided value is a custom class, data node
    will create a list of custom object with the given custom class, each object will represent a row in the csv
    file.If _exposed_type_ is not provided, the data node will read the csv file as a pandas DataFrame.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

temp_cfg = Config.configure_csv_data_node(id="historical_temperature",
                                          path="path/hist_temp.csv",
                                          has_header=True,
                                          exposed_type="numpy")

sales_cfg = Config.configure_csv_data_node(id="sale_history",
                                           path="path/sale_history.csv",
                                           exposed_type=SaleRow)
```

In lines 3, 4, and 5 we define a custom class `SaleRow` representing a row of the CSV file.

In lines 7, 8, 9 and 10 we configure a basic csv data node with the id "historical_temperature". Its _scope_ is by
default `SCENARIO`. The path corresponds to the file `path/hist_temp.csv`. The property _has_header_ being True,
representing the csv file has a header.

In lines 12, 13, and 14, we add another csv data node configuration with the id "sale_history". The
default `SCENARIO` scope is used again. Since we have a custom class pre-defined for this csv file (`SaleRow`), we
provide it as the _exposed_type_ parameter.

!!! Note

    To configure a csv data node, it is equivalent to use the method `Config.configure_csv_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="csv"`.

# Excel

An `ExcelDataNode^` is a specific data node used to model xlsx
file data. To add a new _Excel_ data node configuration, the `Config.configure_excel_data_node()^` method can be used.
In addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), a mandatory and three optional parameters can be provided.

-   The _**path**_ is a mandatory parameter that represents the Excel file path used by Taipy to read and write the data.

-   The _**has_header**_ parameter specifies if the file has a header of not. If _has_header_ is True (by default or was
    specified), Taipy will use the 1st row in the Excel file as the header.

-   The _**sheet_name**_ parameter represents which specific sheet in the Excel file to read. If _sheet_name_
    is provided with a list of sheet names, the data node will return a dictionary with the key being the sheet name and
    the value being the data of the corresponding sheet. If a string is provided, the data node will read only the
    data of the corresponding sheet. The default value of _sheet_name_ is None and the data node will return all sheets
    in the provided Excel file when reading it.

-   When the _**exposed_type**_ is given as a parameter, if the _exposed_type_ value provided is `numpy`, the data
    node will read the Excel file to a numpy array. If the provided value is a custom class, data node will
    create a list of custom objects with the given custom class, each object will represent a row in the Excel
    file. If _exposed_type_ is not provided, the data node will read the Excel file as a pandas DataFrame.

```python linenums="1"
from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

hist_temp_cfg = Config.configure_excel_data_node(id="historical_temperature",
                                                 path="path/hist_temp.xlsx",
                                                 exposed_type="numpy")

sales_cfg = Config.configure_excel_data_node(id="sale_history",
                                             path="path/sale_history.xlsx",
                                             sheet_name=["January", "February"],
                                             exposed_type=SaleRow)
```

In lines 3, 4, and 5 we define a custom class `SaleRow` representing a row of the Excel file.

In lines 7, 8, and 9, we configure an Excel data node. The _id_ identifier is "historical_temperature". Its _scope_ is
`SCENARIO` (default value), and the path is the file hist_temp.xlsx. With _has_header_ being True, the
Excel file must have a header. The _sheet_name_ is not provided so Taipy will use the default value "Sheet1".

In lines 10, 11, 12, and 13, we add another excel data node configuration. The _id_ identifier is "sale_history", the
default `SCENARIO` scope is used. Since we have a custom class pre-defined for this Excel file, we will provide it in
the _exposed_type_. We also provide the list of specific sheets we want to use as the _sheet_name_ parameter.

!!! Note

    To configure an Excel data node, it is equivalent to use the method `Config.configure_excel_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="excel"`.

# Sql

A `SQLDataNode^` is a specific data node used to model Sql
data. To add a new _sql_ data node configuration, the `Config.configure_sql_data_node()^` method can be used. In
addition to the generic parameters described in the previous section
[Data node configuration](data-node-config.md), multiple
parameters can be provided.

-   The _**db_username**_ parameter represents the database username that will be used by Taipy to access the database.
-   The _**db_password**_ parameter represents the database user's password that will be used by Taipy to access the
    database.
-   The _**db_name**_ parameter represents the name of the database.
-   The _**db_engine**_ parameter represents the engine of the database.
-   The _**read_query**_ parameter represents the SQL query that will be used by Taipy to read the data from the
    database.
-   The _**write_table**_ parameter represents the name of the table in the database that Taipy will be writing the
    data to.
-   The _**db_port**_ parameter represents the database port that will be used by Taipy to access the database. The
    default value of _db_port_ is 1433.
-   The _**db_host**_ parameter represents the database host that will be used by Taipy to access the database. The
    default value of _db_host_ is "localhost".
-   The _**db_driver**_ parameter represents the database driver that will be used by Taipy. The default value of
    _db_driver_ is "ODBC Driver 17 for SQL Server".

```python linenums="1"
from taipy import Config

forecasts_cfg = Config.configure_sql_data_node(id="forecasts",
                                               db_username="admin",
                                               db_password="password",
                                               db_name="taipy",
                                               db_engine="mssql",
                                               read_query="SELECT * from forecast_table",
                                               write_table= "forecast_table")
```

In the previous example, we configure a _sql_ data node with the id "forecasts". Its scope is the
default value `SCENARIO`. The database username is "admin", the user's password is "password", the database name
is "taipy", and the database engine is `mssql` (short for Microsoft SQL). The read query will be "SELECT \* from
forecast_table", and the table the data will be written to is "forecast_table".

!!! Note

    To configure a sql data node, it is equivalent to use the method `Config.configure_sql_data_node()^` or
    the method `Config.configure_data_node()^` with parameter `storage_type="sql"`.

# Generic

A `GenericDataNode^` is a specific data node used to model generic data types where the read and the write functions
are defined by the user. To add a new _generic_ data node configuration, the `Config.configure_generic_data_node()^`
method can be used. In addition to the parameters described in the previous section
[Data node configuration](data-node-config.md), two optional parameters can be provided.

-   The _**read_fct**_ is a mandatory parameter that represents a Python function provided by the user. It will
    be used to read the data.

-   The _**write_fct**_ is a mandatory parameter that represents a Python function provided by the user. It will
    be used to write the data. The provided function must have at least one parameter,
    dedicated to receive data to be written.

-   The parameter _**read_fct_params**_ represents the parameters that are passed to the _read_fct_ to read the data.
    It must be a `List` type object.

-   The parameter _**write_fct_params**_ represents the parameters that are passed to the _write_fct_ to write the data.
    It must be a `List` type object.


```python linenums="1"
from taipy import Config

def read_data():
    pass

def write_data(path: str):
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
