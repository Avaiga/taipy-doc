This section covers the *data node* management feature.
It explains how to configure, create and use data nodes in a Taipy application.

A `DataNode^` in Taipy is an abstraction that represents some data. It provides a uniform
interface for reading and writing data, regardless of the underlying storage mechanism.
This abstraction allows you to focus on your application's logic without worrying about the
intricacies of data management.

To create a *data node*, you first need to define a data node configuration.

# Data node configuration

`DataNodeConfig^` represents a data node configuration. It is used to instantiate
one (or multiple) *data node(s)* with the desired properties, such as its type,
storage mechanism, or any additional parameters required for reading and writing
related data. The most direct way to create a `DataNodeConfig^` is to use the
function `Config.configure_data_node()^`.

For more details, see the
[data integration configuration](../../data-integration/data-node-config.md)
page.

# Graphical User Interface

Taipy offers visual elements dedicated to data node management. These elements
are designed to help end-users select, visualize, and edit data nodes in an
intuitive way.

For more details and examples, see the
[data integration visual elements](../../data-integration/data-node-vizelmts.md) page.

# Data node usage

A `DataNode^` represents a pointer to a data, holds metadata, and all the necessary
information to read and write data. It is created from a `DataNodeConfig^`.

For more details and examples, see the
[data integration usage](../../data-integration/data-node-usage.md) page that list
all the methods available to interact with a data node.

