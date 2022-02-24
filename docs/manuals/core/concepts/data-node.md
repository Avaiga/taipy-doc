A _data node_ is one of the most important concepts in Taipy core. It does not contain the data itself, but it holds all
the necessary information to read and write the actual data. It can be seen as a dataset descriptor or as a data
reference.

A _data node_ can reference any data. It could be a text, a numeric value, a list of parameters, a custom
python object, the content of a JSON or a CSV file, the content of one or multiple database table(s), or any other data.
It is made to model any type of data: Input, intermediate, or output data, internal or external data, local or remote
data, historical data, set of parameters, trained model, etc.

The _data node_ information depends on the data itself, its exposed format, and its storage type. For instance, if the
data is stored in an SQL database, the corresponding _data node_ should contain the username, password, host, and port,
but also the queries to read and write the data as well as the python class used for the deserialization. On another use
case, if the data is stored in a CSV file, the corresponding _data node_ should contain for instance, the path to the
file and the python class used for the deserialization.

!!! example "Let's take an example."

    Let's assume we want to build an application to predict some sales demand every month in
    order to adjust a production planning constrained by some capacity.

    For that purpose, we may have six data nodes to model the various data. One for the sales history, one for the
    trained model, one for the current month, one for the sales predictions, one for the capacity of production,
    and one for the production orders.

The various attributes that depend on the storage type (like sql query, file path, credentials, ...) are populated based
on the data node configuration
([`DataNodeConfig`](../../../reference/#taipy.core.config.data_node_config.DataNodeConfig))
that must be provided when instantiating a new data node. (Please refer to the
[`configuration details`](../user_core_configuration.md#data-node-configuration) documentation for more
details on configuration).


[:material-arrow-right: Next section introduces the Task concept](task.md).
