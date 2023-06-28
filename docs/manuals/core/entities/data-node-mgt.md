Data nodes get created when scenarios or pipelines are created. Please refer to the
[Entities' creation](scenario-creation.md) section for more details.

In this section, it is assumed that <a href="./code_example/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented.

# Data node attributes

A `DataNode^` entity is identified by a unique identifier `id` that Taipy generates.
A data node also holds various properties and attributes accessible through the entity:

- _**config_id**_: The id of the data node config.
- _**scope**_: The scope of this data node (scenario, pipeline, etc.).
- _**id**_: The unique identifier of this data node.
- _**name**_: The user-readable name of the data node.
- _**owner_id**_: The identifier of the owner (pipeline_id, scenario_id, cycle_id) or None.
- _**last_edit_date**_: The date and time of the last data modification made through Taipy.
    Note that **only** for file-based data nodes (CSV, Excel, pickle, JSON, Parquet, ...), the
    file's last modification date is used to compute the _**last_edit_date**_ value. That means if a file is modified
    manually or by an external process, the _**last_edit_date**_ value is automatically updated within Taipy.
- _**edits**_: The ordered list of `Edit^`s, representing the successive modifications of the data node.
- _**version**_: The string indicates the application version of the data node to instantiate.
    If not provided, the current version is used.
- _**validity_period**_: The duration since the last edit date for which the data node can be considered up-to-date.
    Once the validity period has passed, the data node is considered stale and relevant tasks will run
    even if they are skippable (see the [Task management page](task-mgt.md) for more details).
    If *validity_period* is set to None, the data node is always up-to-date.
- _**edit_in_progress**_: The boolean flag signals if the data node is locked for modification.
- _**properties**_: The dictionary of additional arguments.

# Get data node

The first method to access a **data node** is by calling the `taipy.get()^` method
passing the data node id as parameter:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    data_node = scenario.sales_history
    data_node_retrieved = scenario.sales_history
    data_node = tp.get(data_node.id)
    # data_node == data_node_retrieved
    ```

# Get data nodes by config_id

The data nodes that are part of a **scenario**, **pipeline** or **task** can be directly accessed as attributes by
using their config_id:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Access the data node 'sales_history' from the scenario
    scenario.sales_history

    # Access the pipeline 'sales' from the scenario and
    # then access the data node 'sales_history' from the pipeline
    pipeline = scenario.sales
    pipeline.sales_history

    # Access the task 'training' from the pipeline and
    # then access the data node 'sales_history' from the task
    task = pipeline.training
    task.sales_history
    ```

Data nodes can be retrieved by using `taipy.get_entities_by_config_id()^` providing the config_id.
This method returns the list of all existing data nodes instantiated from the config_id provided as a parameter.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create 2 scenarios, which will also create 2 trained_model data nodes.
    scenario_1 = tp.create_scenario(my_config.monthly_scenario_cfg)
    scenario_2 = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get all data nodes by config_id, this will return a list of 2 trained_model data nodes
    # created alongside the 2 scenarios.
    all_trained_model_dns = tp.get_entities_by_config_id("trained_model")
    ```

# Get all data nodes

All data nodes that are part of a **scenario** or a **pipeline** can be directly accessed as attributes:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Access all the data nodes from the scenario
    scenario.data_nodes

    # Access the pipeline 'sales' from the scenario and
    # then access all the data nodes from the pipeline
    pipeline = scenario.sales
    pipeline.data_nodes
    ```

All the data nodes can be retrieved using the method `taipy.get_data_nodes()^` which returns a list of all existing
data nodes.

!!! Example

    ```python linenums="1"
    import taipy as tp

    # Retrieve all data nodes
    data_nodes = tp.get_data_nodes()

    data_nodes #[DataNode 1, DataNode 2, ..., DataNode N]
    ```

# Read / Write a data node

To access the content of a data node you can use the `DataNode.read()^` method. The read method returns the data
stored in the data node according to the type of data node:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a data node
    data_node = scenario.sales_history

    # Returns the content stored on the data node
    data_node.read()
    ```

To write some data on the data node, like the output of a task, you can use the `DataNode.write()^` method. The
method takes a data object (string, dictionary, lists, NumPy arrays, Pandas dataframes, etc. based on the data
node type and its exposed type) as a parameter and writes it on the data node:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a data node
    data_node = scenario.sales_history

    data = [{"product": "a", "qty": "2"}, {"product": "b", "qty": "4"}]

    # Writes the dictionary on the data node
    data_node.write(data)

    # returns the new data stored on the data node
    data_retrieved = data_node.read()
    ```

## Pickle

When reading from a Pickle data node, Taipy returns whichever data stored in the pickle file.

Pickle data node can write any data object that can be picked, including but not limited to:

- integers, floating-point numbers.
- strings, bytes, or bytearrays.
- tuples, lists, sets, and dictionaries *containing only picklable objects*.
- functions, classes.
- instances of classes with picklable properties.

Check out
[What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
for more details.


## CSV

When reading from a CSV data node, Taipy returns the data of the CSV file based on the _exposed_type_ parameter.
Check out [CSV Data Node configuration](../config/data-node-config.md#csv) for more details on _exposed_type_.

Assume that the content of the `sales.csv` file is the following.

!!! example "path/sales.csv"

    ```csv
    date,nb_sales
    12/24/2018,1550
    12/25/2018,2315
    12/26/2018,1832
    ```

The following examples represent the results when reading from a CSV data node with different _exposed_type_:

!!! example "`data_node.read()` returns"

    === "exposed_type = "pandas""

        ```python
        pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "modin""

        ```python
        modin.pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "numpy""

        ```python
        numpy.array(
            [
                ["12/24/2018", "1550"],
                ["12/25/2018", "2315"],
                ["12/26/2018", "1832"]
            ],
        )
        ```

    === "exposed_type = SaleRow"
        ```python
        [
            SaleRow("12/24/2018", 1550),
            SaleRow("12/25/2018", 2315),
            SaleRow("12/26/2018", 1832),
        ]
        ```

When writing data to a CSV data node, the `CSVDataNode.write()^` method can take several datatype as the input:

- list, numpy array
- dictionary, or list of dictionaries
- pandas dataframes

The following examples will write to the path of the CSV data node:

!!! example "`data_node.write()` examples"

    === "list"
        When write a list to CSV data node, each element of a list contains 1 row of data.

        ```python
        # write a list
        data_node.write(
            ["12/24/2018", "12/25/2018", "12/26/2018"]
        )
        # or write a list of lists
        data_node.write(
            [
                ["12/24/2018", 1550],
                ["12/25/2018", 2315],
                ["12/26/2018", 1832],
            ]
        )
        ```

    === "numpy array"

        ```python
        data_node.write(
            np.array([
                ["12/24/2018", 1550],
                ["12/24/2018", 2315],
                ["12/24/2018", 1832],
            ])
        )
        ```

    === "dictionary"

        ```python
        # "list" form
        data_node.write(
            {
                "date": ["12/24/2018", "12/25/2018", "12/26/2018"],
                "nb_sales": [1550, 2315, 1832]
            }
        )
        # "records" form
        data_node.write(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/24/2018", "nb_sales": 2315},
                {"date": "12/24/2018", "nb_sales": 1832},
            ]
        )
        ```

    === "pandas dataframes"

        ```python
        data = pandas.DataFrame(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/24/2018", "nb_sales": 2315},
                {"date": "12/24/2018", "nb_sales": 1832},
            ]
        )

        data_node.write(data)
        ```

When write a list or numpy array to CSV data node, the column name will be numbered from 1.
To write with custom column names, use the `CSVDataNode.write_with_column_names()^` method.

!!! example "`CSVDataNode.write_with_column_names()^` examples"

    ```python
    data_node.write(
        [
            ["12/24/2018", 1550],
            ["12/25/2018", 2315],
            ["12/26/2018", 1832],
        ],
        columns=["date", "nb_sales"]
    )
    ```


## Excel

When reading from an Excel data node, Taipy returns the data of the Excel file based on the _exposed_type_ parameter.
Check out [Excel Data Node configuration](../config/data-node-config.md#excel) for more details on _exposed_type_.

For the example in this section, assume that `sales_history_cfg` in [`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py)
is an _Excel_ data node configuration with `default_path="path/sales.xlsx"`.

Assume that the content of the `sales.xlsx` file is the following.

!!! example "path/sales.xlsx"

    | date       | nb_sales |
    |------------|----------|
    | 12/24/2018 | 1550     |
    | 12/25/2018 | 2315     |
    | 12/26/2018 | 1832     |

The following examples represent the results when reading from an Excel data node with different _exposed_type_:

!!! example "`data_node.read()` returns"

    === "exposed_type = "pandas""

        ```python
        pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "modin""

        ```python
        modin.pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "numpy""

        ```python
        numpy.array(
            [
                ["12/24/2018", "1550"],
                ["12/25/2018", "2315"],
                ["12/26/2018", "1832"]
            ],
        )
        ```

    === "exposed_type = SaleRow"
        ```python
        [
            SaleRow("12/24/2018", 1550),
            SaleRow("12/25/2018", 2315),
            SaleRow("12/26/2018", 1832),
        ]
        ```

When writing data to an Excel data node, the `ExcelDataNode.write()^` method can take several datatype as the input:

- list, numpy array
- dictionary, or list of dictionaries
- pandas dataframes

The following examples will write to the path of the Excel data node:

!!! example "`data_node.write()` examples"

    === "list"
        When write a list to Excel data node, each element of a list contains 1 row of data.

        ```python
        # write a list
        data_node.write(
            ["12/24/2018", "12/25/2018", "12/26/2018"]
        )
        # or write a list of lists
        data_node.write(
            [
                ["12/24/2018", 1550],
                ["12/25/2018", 2315],
                ["12/26/2018", 1832],
            ]
        )
        ```

    === "numpy array"

        ```python
        data_node.write(
            np.array([
                ["12/24/2018", 1550],
                ["12/25/2018", 2315],
                ["12/26/2018", 1832],
            ])
        )
        ```

    === "dictionary"

        ```python
        # "list" form
        data_node.write(
            {
                "date": ["12/24/2018", "12/25/2018", "12/26/2018"],
                "nb_sales": [1550, 2315, 1832]
            }
        )
        # "records" form
        data_node.write(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/25/2018", "nb_sales": 2315},
                {"date": "12/26/2018", "nb_sales": 1832},
            ]
        )
        ```

    === "pandas dataframes"

        ```python
        data = pandas.DataFrame(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/25/2018", "nb_sales": 2315},
                {"date": "12/26/2018", "nb_sales": 1832},
            ]
        )

        data_node.write(data)
        ```

When write a list or numpy array to Excel data node, the column name will be numbered from 1.
To write with custom column names, use the `ExcelDataNode.write_with_column_names()^` method.

!!! example "`ExcelDataNode.write_with_column_names()^` examples"

    ```python
    data_node.write(
        [
            ["12/24/2018", 1550],
            ["12/25/2018", 2315],
            ["12/26/2018", 1832],
        ],
        columns=["date", "nb_sales"]
    )
    ```

## SQL Table

When reading from a SQL Table data node, Taipy returns the data of the SQL Table file based on the _exposed_type_ parameter.
Check out [SQL Table Data Node configuration](../config/data-node-config.md#sql-table) for more details on _exposed_type_.

For the example in this section, assume that `sales_history_cfg` in [`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py)
is a _SQL Table_ data node configuration with `table_name="sales"`.

Assume that the content of the `"sales"` table is the following.

!!! example "A selection from the "sales" table"

    | ID | date       | nb_sales |
    |----|------------|----------|
    | 1  | 12/24/2018 | 1550     |
    | 2  | 12/25/2018 | 2315     |
    | 3  | 12/26/2018 | 1832     |

The following examples represent the results when reading from a SQL Table data node with different _exposed_type_:

!!! example "`data_node.read()` returns"

    === "exposed_type = "pandas""

        ```python
        pandas.DataFrame
        (
               ID        date  nb_sales
            0   1  12/24/2018      1550
            1   2  12/25/2018      2315
            2   3  12/26/2018      1832
        )
        ```

    === "exposed_type = "modin""

        ```python
        modin.pandas.DataFrame
        (
               ID        date  nb_sales
            0   1  12/24/2018      1550
            1   2  12/25/2018      2315
            2   3  12/26/2018      1832
        )
        ```

    === "exposed_type = "numpy""

        ```python
        numpy.array(
            [
                ["1", "12/24/2018", "1550"],
                ["2", "12/25/2018", "2315"],
                ["3", "12/26/2018", "1832"]
            ],
        )
        ```

    === "exposed_type = SaleRow"
        ```python
        [
            SaleRow("12/24/2018", 1550),
            SaleRow("12/25/2018", 2315),
            SaleRow("12/26/2018", 1832),
        ]
        ```

When writing data to a SQL Table data node, the `SQLTableDataNode.write()^` method can take several datatype as the input:

- list of lists or list of tuples
- numpy array
- dictionary, or list of dictionaries
- pandas dataframes

Assume that the "ID" column is the auto-increment primary key. The following examples will write to the SQL Table data
node:

!!! example "`data_node.write()` examples"

    === "list"

        ```python
        # write a list of lists
        data_node.write(
            [
                ["12/24/2018", 1550],
                ["12/25/2018", 2315],
                ["12/26/2018", 1832],
            ]
        )

        # or write a list of tuples
        data_node.write(
            [
                ("12/24/2018", 1550),
                ("12/25/2018", 2315),
                ("12/26/2018", 1832),
            ]
        )
        ```

    === "numpy array"

        ```python
        data = np.array(
            [
                ["12/24/2018", 1550],
                ["12/25/2018", 2315],
                ["12/26/2018", 1832],
            ]
        )

        data_node.write(data)
        ```

    === "dictionary"

        ```python
        # write 1 record to the SQL table
        data_node.write(
            {"date": "12/24/2018", "nb_sales": 1550}
        )

        # write multiple records using a list of dictionaries
        data_node.write(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/25/2018", "nb_sales": 2315},
                {"date": "12/26/2018", "nb_sales": 1832},
            ]
        )
        ```

    === "pandas dataframes"

        ```python
        data = pandas.DataFrame(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/25/2018", "nb_sales": 2315},
                {"date": "12/26/2018", "nb_sales": 1832},
            ]
        )

        data_node.write(data)
        ```

## SQL

A SQL data node is designed to give the user more flexibility on how to read and write to SQL table
(or multiple SQL tables).

Let's consider the `orders_cfg` in
[`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py)
which configures a SQL data node.

When reading from a SQL data node, Taipy executes the read query and returns the data of the SQL
file based on the _exposed_type_ parameter:

- The _exposed_type_ parameter of `orders_cfg` is undefined, therefore it takes the default value
  as "pandas".
  Check out [SQL Data Node configuration](../config/data-node-config.md#sql) for more details on
  _exposed_type_.
- The _read_query_ of `orders_cfg` is
    ```sql
    SELECT orders.ID, orders.date, products.price, orders.number_of_products
    FROM orders INNER JOIN products
    ON orders.product_id=products.ID
    ```
- When reading from the SQL data node using `data_node.read()` method, Taipy will execute the above
  query and return a `pandas.DataFrame` represents the "orders" table inner join with the "products" table.

!!! example "A selection from the "orders" table"

    | ID | date       | product_id | number_of_products |
    |----|------------|------------|--------------------|
    | 1  | 01/05/2019 |          2 |                200 |
    | 2  | 01/05/2019 |          3 |                450 |
    | 3  | 01/05/2019 |          5 |                350 |
    | 4  | 01/06/2019 |          1 |                520 |
    | 5  | 01/06/2019 |          3 |                250 |
    | 6  | 01/07/2019 |          2 |                630 |
    | 7  | 01/07/2019 |          4 |                480 |

!!! example "A selection from the "products" table"

    | ID | price | description |
    |----|-------|-------------|
    | 1  |    30 | foo product |
    | 2  |    50 | bar product |
    | 3  |    25 | foo product |
    | 4  |    60 | bar product |
    | 5  |    40 | foo product |

!!! example "`data_node.read()` returns"

    ```python
    pandas.DataFrame
    (
            ID         date   price   number_of_products
        0   1   01/05/2019      50                 200
        1   2   01/05/2019      25                 450
        2   3   01/05/2019      40                 350
        3   4   01/06/2019      30                 520
        4   5   01/06/2019      25                 250
        5   6   01/07/2019      50                 630
        6   7   01/07/2019      60                 480
    )
    ```

When writing to a SQL data node, Taipy will first pass the data to _write_query_builder_ and then
execute a list of queries returned by the query builder:

- The _write_query_builder_ parameter of `orders_cfg` in this example is defined as the
  `write_orders_plan()` method.
- After being called with the write data as a `pd.DataFrame`, the `write_orders_plan()`
  method will return a list of SQL queries.
- The first query deletes all records from "orders" table.
- The following query will insert a list of records to the "orders" table according to the
  data, assume that "ID" column in "orders" table is the auto-increment primary key.

!!! example "`data_node.write()`"

    ```python
    data = pandas.DataFrame(
        [
            {"date": "01/08/2019", "product_id": 1 "number_of_products": 450},
            {"date": "01/08/2019", "product_id": 3 "number_of_products": 320},
            {"date": "01/08/2019", "product_id": 4 "number_of_products": 350},
        ]
    )

    data_node.write(data)
    ```

    The "orders" table after being written:

    | ID | date       | product_id | number_of_products |
    |----|------------|------------|--------------------|
    | 8  | 01/08/2019 |          1 |                450 |
    | 9  | 01/08/2019 |          3 |                320 |
    | 10 | 01/08/2019 |          4 |                350 |

## JSON

When reading from a JSON data node, Taipy will return a dictionary or a list based on the format of the JSON file.

When writing data to a JSON data node, the `JSONDataNode.write()^` method can take a list,
dictionary, or list of dictionaries as the input.

In JSON, values must be one of the following data types:

- A string
- A number
- An object (embedded JSON object)
- An array
- A boolean
- `null`

However, the content of a JSON data node can vary. By default, JSON data node provided by Taipy can
also encode and decode:

- Python [`enum.Enum`](https://docs.python.org/3/library/enum.html).
- A [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) object.
- A [dataclass](https://docs.python.org/3/library/dataclasses.html) object.

For the example in this section, assume that `sales_history_cfg` in
[`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py)
is a _JSON_ data node configuration with `default_path="path/sales.json"`.

!!! example "Read and write from a JSON data node using default _encoder_ and _decoder_"

    === "Write dictionaries"

        ```python
        data = [
            {"date": "12/24/2018", "nb_sales": 1550},
            {"date": "12/25/2018", "nb_sales": 2315},
            {"date": "12/26/2018", "nb_sales": 1832},
        ]
        data_node.write(data)
        ```

        results in:

        ```json
        [
            {"date": "12/24/2018", "nb_sales": 1550},
            {"date": "12/25/2018", "nb_sales": 2315},
            {"date": "12/26/2018", "nb_sales": 1832},
        ]
        ```

    === "Write datetime.datetime"

        ```python
        from datetime import datetime

        data = [
            {"date": datetime.datetime(2018, 12, 24), "nb_sales": 1550},
            {"date": datetime.datetime(2018, 12, 25), "nb_sales": 2315},
            {"date": datetime.datetime(2018, 12, 26), "nb_sales": 1832},
        ]
        data_node.write(data)
        ```

        results in:

        ```json
        [
            {"date": {"__type__": "Datetime", "__value__": "2018-12-24T00:00:00"}, "nb_sales": 1550},
            {"date": {"__type__": "Datetime", "__value__": "2018-12-24T00:00:00"}, "nb_sales": 2315},
            {"date": {"__type__": "Datetime", "__value__": "2018-12-24T00:00:00"}, "nb_sales": 1832},
        ]
        ```

        The read method will return a list of dictionaries, with "date" are `datetime.datetime` as `data` when written.

    === "Write enum.Enum"

        ```python
        from enum import Enum

        class SaleRank(Enum):
            A = 2000
            B = 1800
            C = 1500
            D = 1200
            F = 1000

        data = [
            {"date": "12/24/2018", "nb_sales": SaleRank.C},
            {"date": "12/25/2018", "nb_sales": SaleRank.A},
            {"date": "12/26/2018", "nb_sales": SaleRank.B},
        ]
        data_node.write(data)
        ```

        results in:

        ```json
        [
            {"date": "12/24/2018", "nb_sales": {"__type__": "Enum-SaleRank-C", "__value__": 1500}},
            {"date": "12/25/2018", "nb_sales": {"__type__": "Enum-SaleRank-A", "__value__": 2000}},
            {"date": "12/26/2018", "nb_sales": {"__type__": "Enum-SaleRank-B", "__value__": 1800}},
        ]
        ```

        The read method will return a list of dictionaries, with "nb_sales" are Enum.enum as `data` when written.

    === "Write dataclass object"

        ```python
        from dataclasses import dataclass

        @dataclass
        class SaleRow:
            date: str
            nb_sales: int

        data = [
            SaleRow("12/24/2018", 1550),
            SaleRow("12/25/2018", 2315),
            SaleRow("12/26/2018", 1832),
        ]
        data_node.write(data)
        ```

        results in:

        ```json
        [
            {"__type__": "dataclass-SaleRow", "__value__": {"date": "12/24/2018", "nb_sales": 1550}},
            {"__type__": "dataclass-SaleRow", "__value__": {"date": "12/25/2018", "nb_sales": 2315}},
            {"__type__": "dataclass-SaleRow", "__value__": {"date": "12/26/2018", "nb_sales": 1832}},
        ]
        ```

        The read method will return a list of SaleRow objects as `data` when written.

You can also specify custom JSON _**encoder**_ and _**decoder**_ to handle different data types.
Check out [JSON Data Node configuration](../config/data-node-config.md#json) for more details on
how to config custom JSON _**encoder**_ and _**decoder**_.

## Parquet

When read from a Parquet data node, Taipy returns the data of the Parquet file based on _exposed_type_ parameter.
Check out [Parquet Data Node configuration](../config/data-node-config.md#parquet) for more details on _exposed_type_.

Assume that the content of the `sales.parquet` file populates the following table.

!!! example "path/sales.parquet"

    | date       | nb_sales |
    |------------|----------|
    | 12/24/2018 | 1550     |
    | 12/25/2018 | 2315     |
    | 12/26/2018 | 1832     |

The following examples represent the results when read from Parquet data node with different _exposed_type_:

!!! example "`data_node.read()` returns"

    === "exposed_type = "pandas""

        ```python
        pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "modin""

        ```python
        modin.pandas.DataFrame
        (
                     date  nb_sales
            0  12/24/2018      1550
            1  12/25/2018      2315
            2  12/26/2018      1832
        )
        ```

    === "exposed_type = "numpy""

        ```python
        numpy.array(
            [
                ["12/24/2018", "1550"],
                ["12/25/2018", "2315"],
                ["12/26/2018", "1832"]
            ],
        )
        ```

    === "exposed_type = SaleRow"
        ```python
        [
            SaleRow("12/24/2018", 1550),
            SaleRow("12/25/2018", 2315),
            SaleRow("12/26/2018", 1832),
        ]
        ```

When writing data to a Parquet data node, the `ParquetDataNode.write()^` method can take several
datatype as the input depending on the _exposed type_:

- pandas dataframes
- modin dataframes
- numpy arrays
- any object, which will be passed to the `pd.DataFrame` constructor (e.g., list of dictionaries)

The following examples will write to the path of the Parquet data node:

!!! example "`data_node.write()` examples"

    === "pandas dataframes"

        ```python
        data = pandas.DataFrame(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/24/2018", "nb_sales": 2315},
                {"date": "12/24/2018", "nb_sales": 1832},
            ]
        )

        data_node.write(data)
        ```

    === "dictionary"

        ```python
        # "list" form
        data_node.write(
            {
                "date": ["12/24/2018", "12/25/2018", "12/26/2018"],
                "nb_sales": [1550, 2315, 1832]
            }
        )

        # "records" form
        data_node.write(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/24/2018", "nb_sales": 2315},
                {"date": "12/24/2018", "nb_sales": 1832},
            ]
        )
        ```

    === "modin dataframes"

        ```python
        data = modin.pandas.DataFrame(
            [
                {"date": "12/24/2018", "nb_sales": 1550},
                {"date": "12/24/2018", "nb_sales": 2315},
                {"date": "12/24/2018", "nb_sales": 1832},
            ]
        )

        data_node.write(data)
        ```

Additionally, Parquet data node entities also expose two new methods, namely: `ParquetDataNode.read_with_kwargs^`
and `ParquetDataNode.write_with_kwargs^`. These two methods may be used to pass additional keyword arguments
to the pandas
[`pandas.read_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html)
and [`pandas.DataFrame.to_parquet`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html)
methods, **on top of the arguments which were defined in the
[ParquetDataNode configuration](../config/data-node-config.md#parquet)**.

The following examples demonstrate reading and writing to a Parquet data node with additional keyword arguments:

!!! example "Reading data with `ParquetDataNode.read_with_kwargs^`"

    ```python
    columns = ["nb_sales"]
    data_node.read_with_kwargs(columns=columns)
    ```

Here, the `ParquetDataNode.read_with_kwargs^` method is used to specify a keyword parameter, _"columns"_,
which is the list of column names to be read from the Parquet dataset. In this case, only the "nb_sales"
column will be read.

!!! example "Writing data with `ParquetDataNode.write_with_kwargs^`"

    ```python
    data_node.write_with_kwargs(index=False)
    ```

Here, the `ParquetDataNode.write_with_kwargs^` method is used to specify a keyword parameter, _"index"_,
which is a boolean value determining if the index of the DataFrame should be written. In this case, the
index will not be not written.

## Mongo collection

When reading from a Mongo collection data node, Taipy will return a list of objects as instances of a
document class defined by _**custom_document**_.

When writing data to a Mongo collection data node, the `MongoCollectionDataNode.write()^` method takes
a list of objects as instances of a document class
defined by _**custom_document**_ as the input.

By default, Mongo collection data node uses `taipy.core.MongoDefaultDocument` as the document class.
A `MongoDefaultDocument` can have any attribute, however, the type of the value should be supported by
MongoDB, including but not limited to:

- Boolean, integers, and floating-point numbers.
- String.
- Object (embedded document object).
- Arrays − arrays or list or multiple values.

For the example in this section, assume that `sales_history_cfg` in
[`my_config.py`](https://github.com/Avaiga/taipy-doc/blob/develop/docs/manuals/core/my_config.py)
is a _Mongo collection_ data node configuration.

Check out [MongoDB supported data types](https://www.mongodb.com/docs/manual/reference/bson-types/) for more details.

!!! example "Read and write from a Mongo collection data node using default document class"

    ```python
    from taipy.core import MongoDefaultDocument

    data = [
        MongoDefaultDocument(date="12/24/2018", nb_sales=1550),
        MongoDefaultDocument(date="12/25/2018", nb_sales=2315),
        MongoDefaultDocument(date="12/26/2018", nb_sales=1832),
    ]
    data_node.write(data)
    ```

    will write 3 documents to MongoDB:

    ```json
    [
        {"_id": ObjectId("634cd1b3383279c68cee1c21"), "date": "12/24/2018", "nb_sales": 1550},
        {"_id": ObjectId("634cd1b3383279c68cee1c22"), "date": "12/25/2018", "nb_sales": 2315},
        {"_id": ObjectId("634cd1b3383279c68cee1c23"), "date": "12/26/2018", "nb_sales": 1832},
    ]
    ```

    The read method will return a list of MongoDefaultDocument objects, including "_id" attribute.

You can also specify custom document class to handle specific attribute, encode and decode data when
reading and writing to the Mongo collection.

Check out [Mongo collection Data Node configuration](../config/data-node-config.md#mongo-collection)
for more details on how to config a custom
document class.

## Generic

A _Generic_ data node has the read and the write functions defined by the user:

- When reading from a generic data node, Taipy runs the function defined by *read_fct* with parameters
  defined by *read_fct_args*.
- When writing to a generic data node, Taipy runs the function defined by *write_fct* with parameters
  defined by *write_fct_args*.

## In memory

Since an _In memory_ data node stores data in RAM as a Python variable, the read / write methods are
rather straightforward.

When reading from an In memory data node, Taipy returns whichever data stored in RAM corresponding
to the data node.

Correspondingly, In memory data node can write any data object that is valid data for a Python variable.

!!! Warning

    Since the data is stored in memory, it cannot be used in a multiprocess environment.
    (See [Job configuration](../config/job-config.md#standalone) for more details).


# Filter read results

It is also possible to partially read the contents of data nodes, which comes in handy when dealing
with large amounts of data.
This can be achieved by providing an operator, a Tuple of (*field_name*, *value*, *comparison_operator*),
or a list of operators to the `DataNode.filter()^` method:

```python linenums="1"
data_node.filter(
    [("field_name", 14, Operator.EQUAL), ("field_name", 10, Operator.EQUAL)],
    JoinOperator.OR
)
```

If a list of operators is provided, it is necessary to provide a join operator that will be
used to combine the filtered results from the operators.

It is also possible to use pandas style filtering:

```python linenums="1"
temp_data = data_node["field_name"]
temp_data[(temp_data == 14) | (temp_data == 10)]
```

!!! Warning

    For now, the `DataNode.filter()^` method is only implemented for `CSVDataNode^`, `ExcelDataNode^`,
    `SQLTableDataNode^`, `SQLDataNode` with `"pandas"` as the _**exposed_type**_ value.

# Get parent scenarios, pipelines and tasks

To get the parent entities of a data node (scenarios or pipelines or tasks) you can use either the method
`DataNode.get_parents()^` or the function `taipy.get_parents()^`. Both return the parents of the data node.

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a data node
    data_node = scenario.sales_history

    # Retrieve the parent entities of the data node
    parent_entities = data_node.get_parents()
    # {'scenarios': [Scenario 1], 'pipelines': [Pipeline 1], 'tasks': [Task 1]}

    # Retrieve the parent entities of the data node
    tp.get_parents(data_node)
    # {'scenarios': [Scenario 1], 'pipelines': [Pipeline 1], 'tasks': [Task 1]}
    ```

[:material-arrow-right: The next section shows the job orchestration and execution](orchestrating-and-job-execution.md).
