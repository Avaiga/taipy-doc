---
title: <tt>data_node</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays and edits of a data node.

The data node viewer control displays a data node entity's information and lets users edit it.

# Properties


<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Default</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
<td nowrap><code id="p-data_node"><u><bold>data_node</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>DataNode|list[DataNode]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The data node to display and edit.<br/>If the value is a list, it must have a single element otherwise nothing is shown.</p></td>
</tr>
<tr>
<td nowrap><code id="p-active">active</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>Indicates if this component is active.<br/>An inactive component allows no user interaction.</p></td>
</tr>
<tr>
<td nowrap><code id="p-expandable">expandable</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, the data node viewer can be expanded.<br/>If False, the data node viewer is not expandable and it is shown depending on expanded value.</p></td>
</tr>
<tr>
<td nowrap><code id="p-expanded">expanded</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, when a valid data node is selected, the data node viewer is expanded and its content is displayed.<br/>If False, the data node viewer is collapsed and only its name is visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_config">show_config</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the data node configuration label is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_owner">show_owner</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the data node owner label is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_edit_date">show_edit_date</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the data node edition date is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_expiration_date">show_expiration_date</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the data node expiration date is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_properties">show_properties</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the data node properties are not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_history">show_history</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the data node history is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_data">show_data</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the data node value is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-chart_config">chart_config</code></td>
<td><code>dict</code></td>
<td nowrap></td>
<td><p>Chart configs by data node configuration id.</p></td>
</tr>
<tr>
<td nowrap><code id="p-scenario">scenario</code></td>
<td><code>Scenario</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>A variable bound to this property is set to the selected <code>Scenario^</code> when the user picks it from the list of owner scenarios accessible from the 'Owner' field in the 'Properties' tab.<br/>This property is set to None if there is no selected owner scenario.</p></td>
</tr>
<tr>
<td nowrap><code id="p-id">id</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The identifier that will be assigned to the rendered HTML component.</p></td>
</tr>
<tr>
<td nowrap><code id="p-class_name">class_name</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The list of CSS class names associated with the generated HTML Element.<br/>These class names will be added to the default <code>taipy_gui_core-&lt;element_type&gt;</code>.</p></td>
</tr>
  </tbody>
</table>

<p><sup id="dv">(&#9733;)</sup><a href="#p-data_node" title="Jump to the default property documentation."><code>data_node</code></a> is the default property for this visual element.</p>

# Details

The data node viewer displays the attributes of the data node set to the [*data_node*](#p-data_node)
property:
<figure class="tp-center">
  <img src="../data_node-init-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-init-l.png" class="visible-light" width="70%"/>
  <figcaption>The Data Node viewer</figcaption>
</figure>

The topmost section shows the data node's label and storage type.<br/>
The arrow button lets the user collapse or expand the whole control.

The lower section is made of three tabs whose content is described below.

## The 'Data' tab

The section is visible only if the [*show_data*](#p-show_data) property is set to True (which is
its default value).

In this section, the user can visualize the data referenced by the selected data node and change
the data interactively.

Depending on the data type the data node uses, there are two display and edit modes.

### Scalar data

When the data node refers to a scalar value, it is displayed as a simple text:
<figure class="tp-center">
  <img src="../data_node-data-scalar-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-scalar-l.png" class="visible-light" width="70%"/>
  <figcaption>Scalar value</figcaption>
</figure>

To edit the data node, the user can click the line where the value is displayed:
<figure class="tp-center">
  <img src="../data_node-data-scalar-edit-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-scalar-edit-l.png" class="visible-light" width="70%"/>
  <figcaption>Editing a scalar value</figcaption>
</figure>
Note that a 'Comment' field allows the user to explain why this value is changed. This information
is part of the history of the data node.

When the new value is entered, the user presses the 'Apply' (✓) or the 'Cancel' (⨉) button to
apply or cancel the change, respectively.

### Tabular data

Tabular data can be represented in tables or charts.<br/>
The way the data is represented depends on the setting of the representation switch located in the
top-left corner of the 'Properties' section:
<figure class="tp-center">
  <img src="../data_node-data-tabular-switch-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-tabular-switch-l.png" class="visible-light" width="70%"/>
  <figcaption>Data representation switch</figcaption>
</figure>

In the image above, the switch is set to the 'Table' mode.<br/>
The other option is the 'Chart' mode.

Tabular data can be edited only in the 'Table' mode, as described in
[this section](#editing-tabular-data).

#### Table mode

Here is an example of tabular data represented in a table:
<figure class="tp-center">
  <img src="../data_node-data-tabular-table-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-tabular-table-l.png" class="visible-light" width="70%"/>
  <figcaption>Tabular data in a table</figcaption>
</figure>

The 'Columns' drop-down button allows the user to select which dataset columns to represent in the
table.<br/>
The 'Reset view' button resets that setting so all columns are visible.

##### Editing tabular data

The tabular mode has an 'Edit data' switch in the top-right corner of the 'Data' section.
If this switch is turned on, the user can edit the table cells by clicking the relevant pencil
button next to cell values:
<figure class="tp-center">
  <img src="../data_node-data-tabular-edit-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-tabular-edit-l.png" class="visible-light" width="70%"/>
  <figcaption>Editing tabular data</figcaption>
</figure>

The user will typically edit several cells before quitting the edit mode.<br/>
When values are correctly updated manually, the user can set a comment (that will appear in the
data node history) and quit the edit mode.

#### Chart mode

The chart mode displays the data node's referenced data in a chart that can be customized:
<figure class="tp-center">
  <img src="../data_node-data-tabular-chart-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-tabular-chart-l.png" class="visible-light" width="70%"/>
  <figcaption>Tabular data in a chart</figcaption>
</figure>

Several traces can be added (using the '+ Add trace' button), and their respective settings can be
indicated (in the 'Category', 'x', and 'y' drop-down menus).<br/>
The user can also indicate that traces should be represented as accumulating values, setting
the 'Cumulative' switch *on*.<br/>
Here is an example of a data node that references data with several columns, represented as a
cumulative area chart:
<figure class="tp-center">
  <img src="../data_node-data-tabular-chart-2-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-data-tabular-chart-2-l.png" class="visible-light" width="70%"/>
  <figcaption>Tabular data in a chart</figcaption>
</figure>

## The 'Properties' tab

From this tab, you can access the attributes of the data node:
<figure class="tp-center">
  <img src="../data_node-properties-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-properties-l.png" class="visible-light" width="70%"/>
  <figcaption>The Properties section</figcaption>
</figure>

The label of the data node can be changed using the 'Label' field: click in the value area, change
the content, then press the 'Apply' button (with the ✓ icon.)<br/>
To cancel the change, press the 'Cancel' button (with the ⨉ icon).

If the data node has has an owner (a scenario or a cycle) and if the [*show_owner*](#p-show_owner)
property is set to True (which is its default value), the label of the owning entity appears in the
'Owner' information line:
<figure class="tp-center">
  <img src="../data_node-properties-owner-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node-properties-owner-l.png" class="visible-light" width="70%"/>
  <figcaption>The data node is owned by a scenario</figcaption>
</figure>
When the selected data node is owned by a scenario, a button is visible next to the scenario's
label. This button can be pressed to display the list of the owning scenarios so the user can
select one from there. As a result, any variable bound to the [*scenario*](#p-scenario) is set to
the selected scenario entity: the application can use that to update other parts of the page from
an `on_change` callback.

The section at the bottom lists the custom properties for the selected data node. This is visible
only if the [*show_properties*](#p-show_properties) property is set to True (which is its default
value).<br/>
The user can create new properties by clicking the 'New Property Key' line, providing a property
name and value, and then pressing the 'Apply' button (with the ✓ icon.).<br/>
The user can cancel the creation of a new property by pressing the 'Cancel' button (with the ⨉
icon).<br/>
The user can delete a property by selecting it and pressing the *trash* button.

## The 'History' tab

The section is visible only if the [*show_history*](#p-show_history) is set to True (which is its
default value).

In this section, the user has access to the chronological list of changes applied to the selected
data node.

Each history entry holds the date and time when the change was done and potentially some
information on the data changes.
