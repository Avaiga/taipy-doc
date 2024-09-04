In this section, we explore how to integrate data into your Taipy application using *data nodes*.
A `DataNode^` is the cornerstone of Taipy's data management capabilities, providing a flexible
and consistent way to handle data from various sources. Whether your data resides in files,
in databases, in custom data stores, or on local or remote environments, *data nodes* simplify
the process of accessing, processing, and managing your data.

# What is a Data Node?
A *data node* in Taipy is an abstraction that represents some data. It provides a uniform
interface for reading and writing data, regardless of the underlying storage mechanism.
This abstraction allows you to focus on your application's logic without worrying about the
intricacies of data management.

A *data node* does not contain the data itself but holds all the necessary information to
read and write the actual data. It can be seen as a dataset descriptor or data reference.
It is design to model data:

- For any format: a built-in Python object (e.g. an integer, a string, a dictionary
    or list of parameters, etc.) or a more complex object (e.g. a file, a machine learning
    model, a list of custom objects, the result of a database query, etc.).

- For any type: internal or external data, local or remote data, historical data, a parameter
    or a parameter set, a trained model, etc.

- For any usage: independent data or data related to others through data processing pipelines
    or scenarios.

To create a data node, you first need to define a data node configuration using a
`DataNodeConfig^` object. This configuration is used to instantiate one (or multiple)
*data node(s)* with the desired properties.

# Why use Data Nodes?
The main advantages of using data nodes in a Taipy project are:

1. **Easy to configure**:
    Thanks to the various predefined data nodes, many types of data can be easily integrated.
    For more details, see the [data node configuration](data-node-config.md) page.

2. **Easy to use**:
    Taipy already implements the necessary utility methods to create, get, read, write, filter,
    or append data nodes. For more details, see the [data node usage](data-node-usage.md) page.

3. **Taipy visual elements**:
    Benefit from smart visual elements to empower end users just in one line of code.
    Manage, display, and edit data nodes in a user-friendly graphical interface.
    For more details, see the [data node selector](data-node-vizelmts.md#data-node-selector) or
    the [data node viewer](data-node-vizelmts.md#data-node-viewer) pages.

4. **Data history and validity period**:
    Keep track of the data editing history, and monitor the data validity.
    For more information, see the [data node history](data-node-history.md) page.

5. **Seamless integration with Task orchestration and Scenario management**:
    Data pipelines in Taipy are modeled as execution graphs within *scenarios* connecting
    data nodes through *tasks*. Task orchestration and scenario management are key features of
    Taipy. For more information, see the [task orchestration](../task-orchestration/index.md)
    or [scenario and data management](../../scenario_features/sdm/index.md) pages.

6. **Support multiple alternative datasets for What-if analysis**:
    Easily manage alternative data nodes as different versions or variations of your dataset
    within the same application. This is particularly useful for What-if analysis.
    For more information, see the [what-if analysis](../what-if-analysis/index.md) page.

# How to use Data Nodes?

A `DataNode^` is instantiated from a `DataNodeConfig^` object. It encapsulates the necessary
information to create the data node (e.g. the data source, the data format, the data type, the
way to read and write the data).

To integrate a data node into your Taipy application, you need to follow these steps:

1. **Define a DataNodeConfig**:
    Create a global `DataNodeConfig` object using the various predefined methods available
    in Taipy such as `Config.configure_data_node()`, `Config.configure_csv_data_node()`,
   `Config.configure_json_data_node()`, etc. <br>
    For more details, see the [data node configuration](data-node-config.md) page.

2. **Instantiate a DataNode**:
    Once you have defined the data node configuration, you can instantiate your `DataNode`.
    Use the `tp.create_global_data_node()` method.<br>
    For more details, see the [data node usage](data-node-usage.md#create-a-data-node) page.

3. **Access or visualize your Data**:
    You can now retrieve your `DataNode^`, Read, write, filter, or append data as needed.
    For more details, see the [data node usage](data-node-usage.md) page. <br>
    You can also use the Taipy visual elements to manage, display, and edit your data nodes.
    For more details, see the [data node visual elements](data-node-vizelmts.md) page.


!!! examples "Examples"

    === "Data integration with data access"

        Here is an example of how to integrate some data and use a global data node:

        ```python linenums="1"
        {%
        include-markdown "./code-example/index/complete-data-integration-example.py"
        comments=false
        %}
        ```

        The previous code snippet shows how to configure a data node, instantiate it,
        retrieve it, write some data, and read it back.<br>
        Here is the
        <a href="./code-example/index/complete-data-integration-example.py" download>complete python code</a>
        corresponding to the example.

    === "Data integration with user interface"

        Here is another example of how to integrate some data and visualize it using the
        data node visual elements:

        ```python linenums="1"
        {%
        include-markdown "./code-example/index/complete-data-integration-example-with-user-interface.py"
        comments=false
        %}
        ```

        In the previous code snippet three data node configurations are created. Some
        default data is passed to each of them. Then, the data nodes are instantiated.
        Finally, a GUI service is started with two visual elements to visualize and edit
        the data nodes though a user-friendly interface.<br>
        Here is the
        <a href="./code-example/index/complete-data-integration-example-with-user-interface.py" download>complete python code</a>
        corresponding to the example.
