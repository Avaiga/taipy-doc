In the following, it is assumed that [`my_config.py`](../my_config.py) module contains a Taipy configuration
already implemented.

Data nodes get created when scenarios or pipelines are created. Please refer to the
[Entities' creation](scenario-creation.md) section for more details.

# Data node attributes

A `DataNode^` entity is identified by a unique identifier `id` that Taipy generates.
A data node also holds various properties and attributes accessible through the entity:

-   _**config_id**_: The id of the data node config.
-   _**scope**_: The scope of this data node (scenario, pipeline, etc.).
-   _**id**_: The unique identifier of this data node.
-   _**name**_: The user-readable name of the data node.
-   _**owner_id**_: The identifier of the owner (pipeline_id, scenario_id, cycle_id) or `None`.
-   _**last_edit_date**_: The date and time of the last modification.
-   _**job_ids**_: The ordered list of jobs that have written on this data node.
-   _**cacheable**_: The Boolean value that indicates if a data node is cacheable.
-   _**validity_period**_: The validity period of a cacheable data node. If _validity_period_ is set to None, the
    data node is always up-to-date.
-   _**edit_in_progress**_: The flag that signals if a task is currently computing this data node.
-   _**properties**_: The dictionary of additional arguments.

# Get data node

The first method to get a **data node** is from its id using the `taipy.get()^` method:

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

The data nodes that are part of a **scenario**, **pipeline** or **task** can be directly accessed as attributes:

!!! Example

    ```python linenums="1"
    import taipy as tp
    import my_config

    # Creating a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Access the data node 'sales_history' from the scenario
    scenario.sales_history

    # Access the pipeline 'sales' from the scenario and then access the data node 'sales_history' from the pipeline
    pipeline = scenario.sales
    pipeline.sales_history

    # Access the task 'training' from the pipeline and then access the data node 'sales_history' from the task
    task = pipeline.training
    task.sales_history
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

    # Access the pipeline 'sales' from the scenario and then access all the data nodes from the pipeline
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

To read the content of a data node you can use the `DataNode.read()^` method. The read method returns the data
stored on the data node according to the type of data node:

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
method takes a data object (string, dictionary, lists, numpy arrays, pandas dataframes, etc. based on the data node type and its exposed type)
as a parameter and writes it on the data node:

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

When read from a Pickle data node, Taipy returns whichever data stored in the pickle file.

Pickle data node can write any data object that can be picked, including but not limited to:

- integers, floating-point numbers.
- strings, bytes, or bytearrays.
- tuples, lists, sets, and dictionaries *containing only picklable objects*.
- functions, classes.
- instances of classes with picklable properties.

Check out [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled) for more details.


## CSV

When read from a CSV data node, Taipy returns the data of the csv file based on _exposed_type_ parameter.
Check out [CSV Data Node configuration](../config/data-node-config.md#csv) for more details on _exposed_type_.

!!! example "path/sale_history.csv"

    ```csv
    date,nb_sales
    12/24/2018,1550
    12/25/2018,2315
    12/26/2018,1832
    ```

!!! example "`data_node.read()` returns"

    The following examples represent the results when read from CSV data node with different _exposed_type_:

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

When write data to a CSV data node, the `CSVDataNode.write()^` method can take several datatype as the input:

- list, numpy array
- dictionary, or list of dictionaries
- pandas dataframes

!!! example "`data_node.write()` examples"

    The following examples will write to the path of the CSV data node:

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
        # write 1 row
        data_node.write(
            {"date": "12/24/2018", "nb_sales": 1550}
        )
        # write multile rows
        data_node.write(
            {
                "date": ["12/24/2018", "12/25/2018", "12/26/2018"],
                "nb_sales": [1550, 2315, 1832]
            }
        )
        # or using a list of dictionaries
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

When read from a Excel data node, Taipy returns the data of the Excel file based on _exposed_type_ parameter.
Check out [Excel Data Node configuration](../config/data-node-config.md#excel) for more details on _exposed_type_.

!!! example "path/sale_history.xlsx"

    | date       | nb_sales |
    |------------|----------|
    | 12/24/2018 | 1550     |
    | 12/25/2018 | 2315     |
    | 12/26/2018 | 1832     |

!!! example "`data_node.read()` returns"

    The following examples represent the results when read from Excel data node with different _exposed_type_:

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

When write data to a Excel data node, the `ExcelDataNode.write()^` method can take several datatype as the input:

- list, numpy array
- dictionary, or list of dictionaries
- pandas dataframes

!!! example "`data_node.write()` examples"

    The following examples will write to the path of the Excel data node:

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
                ["12/24/2018", 2315],
                ["12/24/2018", 1832],
            ])
        )
        ```

    === "dictionary"

        ```python
        # write 1 row
        data_node.write(
            {"date": "12/24/2018", "nb_sales": 1550}
        )
        # write multile rows
        data_node.write(
            {
                "date": ["12/24/2018", "12/25/2018", "12/26/2018"],
                "nb_sales": [1550, 2315, 1832]
            }
        )
        # or using a list of dictionaries
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

SQL table read/write example

## SQL

SQL read/write example

## JSON

When read from a JSON data node, Taipy will return a dictionary or a list based on the format of the JSON file.

When write data to a JSON data node, the `JSONDataNode.write()^` method can take list, dictionary, or list of dictionaries as the input.

In JSON, values must be one of the following data types:

- A string
- A number
- An object (embedded JSON object)
- An array
- A boolean
- `null`

However, the content of a JSON data node can vary. By default, JSON data node can also encode and decode:

- Python [`enum.Enum`](https://docs.python.org/3/library/enum.html).
- A [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) object.
- A [dataclass](https://docs.python.org/3/library/dataclasses.html) object.

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

You can also specify custom JSON _**encoder**_ and _**decoder**_ to handle different data types. Check out [JSON Data Node
configuration](../config/data-node-config.md#json) for more details on how to config custom JSON _**encoder**_ and _**decoder**_.

## Mongo collection

When read from a Mongo collection data node, Taipy will return a list of objects as instances of a document class defined by _**custom_document**_.

When write data to a Mongo collection data node, the `MongoCollectionDataNode.write()^` method takes a list of objects as instances of a document class
defined by _**custom_document**_ as the input.

By default, Mongo collection data node uses `taipy.core.DefaultCustomDocument` as the document class. A `DefaultCustomDocument` can have any attribute,
however, the type of the value should be supported by MongoDB, including but not limited to:

- Boolean, integers, and floating-point numbers.
- String.
- Object (embedded document object).
- Arrays − arrays or list or multiple values.

Check out [MongoDB supported data types](https://www.mongodb.com/docs/manual/reference/bson-types/) for more details.

!!! example "Read and write from a Mongo collection data node using default document class"

    ```python
    from taipy.core import DefaultCustomDocument

    data = [
        DefaultCustomDocument(date="12/24/2018", nb_sales=1550),
        DefaultCustomDocument(date="12/25/2018", nb_sales=2315),
        DefaultCustomDocument(date="12/26/2018", nb_sales=1832),
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

    The read method will return a list of DefaultCustomDocument objects, including "_id" attribute.

You can also specify custom document class to handle specific attribute, encode and decode data when reading and writing to the Mongo collection.

Check out [Mongo collection Data Node configuration](../config/data-node-config.md#mongo-collection) for more details on how to config a custom
document class.

## In memory

In memory read / write example

!!! Warning

    Since the data is stored in memory, it cannot be used in a multiprocess environment. (See
    [Job configuration](job-config.md#standalone) for more details).

## Generic

Generic read / write example


# Filter read results

It is also possible to partially read the contents of data nodes, which comes in handy when dealing with large amounts
of data.
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

    For now , the `DataNode.filter()^` method can only be used with data node that has the exposed type is pandas.DataFrame.

[:material-arrow-right: The next section shows the scheduling and job execution](scheduling-and-job-execution.md).
