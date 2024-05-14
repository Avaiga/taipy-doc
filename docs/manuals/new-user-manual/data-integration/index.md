
Taipy provides the key concept of *Data node* to facilitate data integration and data management.

A *Data node* can be seen as a reference to a dataset. It can be used to read and write the actual data.
It does not hold the data itself, but refers to any type of data: a built-in Python object
(e.g. an integer, a string, a dictionary or list of parameters, etc.) or a more complex object
(e.g. a file, a machine learning model, a list of custom objects, the result of a database query, etc.).
For more information, see the [Data node](data-node-concept.md) concept page.

Main advantages using data nodes in a Taipy project are:

1. **Easy to configure**:
    Thanks to the various predefined data nodes, many types of data can be easily integrated.
    For more details, see the [Data node configuration](data-node-config.md).

2. **Easy to use**:
    Taipy already implemented the necessary util methods to create, get, read, write, filter,
    or append data nodes.
    For more details, see the [Data node usage](data-node-usage.md).

3. **Taipy visual elements**:
    Benefit from smart visual elements to empower end users just in one line of code.
    Manage, display, and edit data nodes in a user-friendly graphical interface.
    For more details, see the [Data node selector](viselemts/data_node_selector.md) or
    the [Data node viewer](viselemts/data_node.md).

4. **Data history and validity period**:
    Keep track of the data editing history, and monitor the data validity.
    For more information, see the [Data node history](data-node-history.md).

5. **Manage multiple variations of a dataset**:
    Examples,
    For more information, see the [Data node scope](scope.md).

