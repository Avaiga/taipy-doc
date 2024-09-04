Taipy provides some visual elements dedicated to the Data Node Management. These elements are the
data node selector and the data node viewer.

# Data node selector
The `data_node_selector` control displays all data node entities that can be selected.

The default usage is really simple. It does not require any specific configuration to display
the selectable data nodes. The following image shows the default behavior of the
data node selector control.

<figure class="tp-center">
<img src="../img/data-node-vizelmts/data-node-selector-default-behavior.png" class="visible-dark"/>
<img src="../img/data-node-vizelmts/data-node-selector-default-behavior.png" class="visible-light"/>
<figcaption>The list of selectable data nodes</figcaption>
</figure>

Thanks to its rich configurability, you can customize the display of the data node selector,
for example, by adding a search bar, adding a filter or a sort capability, grouping the
data nodes by scenarios and cycles, etc. For more details, see the
[data node selector](../../../refmans/gui/viselements/corelements/data_node_selector.md) page.

# Data node viewer
The `data_node` control displays a data node's information and lets end-users edit it.

The default usage is really simple. It does not require any specific configuration to display
the selectable data nodes.

<figure class="tp-center">
<img src="../img/data-node-vizelmts/data-node-viewer-default-behavior.png" class="visible-dark" width="70%"/>
<img src="../img/data-node-vizelmts/data-node-viewer-default-behavior.png" class="visible-light" width="70%"/>
<figcaption>The data node viewer</figcaption>
</figure>

Three main sections are displayed as three tabs: the data itself, the data node's
properties, and the data node's historical edits.

In the previous picture, the data is a date so the data node viewer displays it with its string
representation. The data node viewer can display the data in a more appropriate way depending on
the data type and the data itself. It can also display the data in a tabular form or a graphical
form if the data is a table. Note that the end-user can easily change the way the data is
displayed. The following two images show the data node viewer displaying a table and a graph.

<figure class="tp-center">
<img src="../img/data-node-vizelmts/data-node-viewer-table-default-behavior.png" class="visible-dark" width="70%"/>
<img src="../img/data-node-vizelmts/data-node-viewer-table-default-behavior.png" class="visible-light" width="70%"/>
<figcaption>Table view of some tabular data</figcaption>
</figure>

<figure class="tp-center">
<img src="../img/data-node-vizelmts/data-node-viewer-chart-default-behavior.png" class="visible-dark" width="70%"/>
<img src="../img/data-node-vizelmts/data-node-viewer-chart-default-behavior.png" class="visible-light" width="70%"/>
<figcaption>Graphical view of some tabular data</figcaption>
</figure>

For more details, see the [data node viewer](../../../refmans/gui/viselements/corelements/data_node.md) page.

# Data management interface

Once the data is modeled as data nodes, it becomes easy to expose it to the end-users.
The combination of the `data_node_selector` and the `data_node_viewer` controls provides a
user-friendly interface for data selection, visualization, and validation, covering the whole
data management workflow.

!!! example "Combining both visual elements"

    === "Data management interface"
        The following image shows an example of how to combine the `data_node_selector` and the
        `data_node` controls for data management. On the top, the `data_node_selector`
        displays all the data nodes that can be selected. Below, the `data_node` displays
        the selected data node.

        <figure class="tp-center">
        <img src="../img/data-node-vizelmts/data-node-vizelements-default-behavior.png" class="visible-dark" width="70%"/>
        <img src="../img/data-node-vizelmts/data-node-vizelements-default-behavior.png" class="visible-light" width="70%"/>
        <figcaption>Data management interface</figcaption>
        </figure>

    === "Corresponding code"
        The following code shows a complete example of how to combine the two visual elements.
        It consists of creating some data to be integrated to a Taipy application using data node
        configurations. Then three data nodes are instantiated.
        Finally, a Gui service is created with a data node selector and a data node viewer.

        ```python linenums="1"
        {%
        include-markdown "./code-example/data-node-vizelmts/data-node-vizelements-default-behavior.py"
        comments=false
        %}
        ```
