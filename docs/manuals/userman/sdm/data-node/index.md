This section covers the `DataNode^` management feature.
It explains how to configure, create and use data nodes in a Taipy application.

# Data node configuration

`DataNodeConfig^` represents a data node configuration. It is used to instantiate
one (or multiple) *data node(s)* with the desired properties, such as its type,
storage mechanism, or any additional parameters required for reading and writing
related data.

The most direct way to create a `DataNodeConfig^` is to use the function
`Config.configure_data_node()^`.<br>
For more details, see the
[data integration configuration](../../data-integration/data-node-config.md)
page.

# Data node usage

A `DataNode^` represents a pointer to a data, holds metadata, and all the necessary
information to read and write data. It is created from a `DataNodeConfig^`.

For more details and examples, see the
[data integration usage](../../data-integration/data-node-usage.md) page.


# Graphical User Interface

Taipy offers visual elements dedicated to data node management. These elements
are designed to help end-users select, visualize, and edit data nodes in an
intuitive way.

For more details and examples, see the
[data integration visual elements](../../data-integration/data-node-vizelmts.md) page.
