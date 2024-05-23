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

To create a *data node*, you first need to define a data node configuration using a
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
    For more details, see the [data node selector](viselemts/data_node_selector.md) or
    the [data node viewer](viselemts/data_node.md) pages.

4. **Data history and validity period**:
    Keep track of the data editing history, and monitor the data validity.
    For more information, see the [data node history](data-node-history.md) page.

5. **Support multiple alternative datasets as Scenarios**:
    Easily manage alternative data nodes as different versions or variations of your dataset within the same
    application. For more information, see the [Data nodes and scenarios](data-node-and-scenario.md) page.

6. **Seamless integration with Data Processing and Scenario management**:
    Data pipelines in Taipy are modeled as execution graphs within Scenarios connecting data nodes
    through tasks. For more information, see the [Data Pipelines](../data-processing/index.md) or
    [Scenario Management](../scenario-mgt/index.md) pages.
