---
title: <tt>data_node_selector</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays a list of the Data Node entities that can be selected.

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
<td nowrap><code id="p-value"><u><bold>value</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>DataNode|list[DataNode]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>Bound to the selected <code>DataNode^</code>(s), or None if there is none.</p></td>
</tr>
<tr>
<td nowrap><code id="p-display_cycles">display_cycles</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the cycles are not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_primary_flag">show_primary_flag</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the primary scenarios are not identified with specific visual hint.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_change">on_change</code></td>
<td><code>callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when a data node is selected.<br/>The parameters of that function are all optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>var_name (str): the variable name.</li>
<li>value (<code>DataNode^</code>): the selected data node.</li>
</ul></p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str</code></td>
<td nowrap>"50vh"</td>
<td><p>The maximum height, in CSS units, of the control.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_pins">show_pins</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, a pin is shown on each item of the selector and allows to restrict the number of displayed items.</p></td>
</tr>
<tr>
<td nowrap><code id="p-scenario">scenario</code></td>
<td><code>Scenario|list[Scenario]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>TODO: If the <code>Scenario^</code> is set, the selector will only show datanodes owned by this scenario.</p></td>
</tr>
<tr>
<td nowrap><code id="p-multiple">multiple</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>TODO: If True, the user can select multiple datanodes.</p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-value" title="Jump to the default property documentation."><code>value</code></a> is the default property for this visual element.</p>

# Details

The control displays a tree selector where all data node entities are listed.<br/>
If [*display_cycles*](#p-display_cycles) is set to False, the cycles are not represented.

In an application that would have created a few data nodes, some of them being scoped at the
scenario level, here is what the data node selector would look like:
<figure class="tp-center">
  <img src="../data_node_selector-init-d.png" class="visible-dark"  width="70%"/>
  <img src="../data_node_selector-init-l.png" class="visible-light" width="70%"/>
  <figcaption>The list of selectable data nodes</figcaption>
</figure>

Data nodes are organized in their owning scenario and cycle, when relevant.

When the user selects a data node, the [*on_change*](#p-on_change) callback is invoked so that
the application can use the selected value. The value is set to the [*value*](#p-value) property.

<h2>Pins</h2/>

When there are many data nodes in your application, the user can filter out a set of data nodes
by *pinning* them and then set the *Pinned only* switch (that is active only if some data nodes are
pinned): only pinned data nodes will then appear in the list.

Assuming we are in the following situation:
<figure class="tp-center">
  <img src="../data_node_selector-pin1-d.png" class="visible-dark"  />
  <img src="../data_node_selector-pin1-l.png" class="visible-light" />
  <figcaption>Crowded data node selector</figcaption>
</figure>

If the user wants to focus only on the 'initial_dataset' and the data nodes from the scenario
called 'Peter's', she can click on the pin icon next to these two items. Here is what the display
would look like:
<figure class="tp-center">
  <img src="../data_node_selector-pin2-d.png" class="visible-dark"  />
  <img src="../data_node_selector-pin2-l.png" class="visible-light" />
  <figcaption>Data node selector with pinned items</figcaption>
</figure>

Here is what the control looks like after the 'Pinned only' switch was set and the scenario item
was expanded:
<figure class="tp-center">
  <img src="../data_node_selector-pin3-d.png" class="visible-dark"  />
  <img src="../data_node_selector-pin3-l.png" class="visible-light" />
  <figcaption>Filtering pinned data nodes</figcaption>
</figure>

You can see that only the pinned data nodes are visible.

Note that the cycle item is not pinned because the other scenarios it contains are not,  either.

- If all data nodes for a scenario or a cycle are pinned, the scenario or cycle item is itself
  pinned.
- A scenario or cycle item appears *not pinned* if any of its data nodes is not pinned.
- *Pinning* a scenario item pins all its data nodes.</br>
  *Unpinning* a scenario item unpins all its data nodes.
- *Pinning* a cycle item pins all the data nodes of all its scenarios.</br>
  *Unpinning* a cycle item unpins all the data nodes of all its scenarios.

To reveal all existing data nodes, the *Pinned only* switch must be turned off.
