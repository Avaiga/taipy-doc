---
title: <tt>scenario_dag</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays the DAG of a scenario.

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
<td nowrap><code id="p-scenario"><u><bold>scenario</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>Scenario|list[Scenario]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The <code>Scenario^</code> whose diagram is displayed.<br/>If the value is a list, it must have a single element otherwise nothing is shown.</p></td>
</tr>
<tr>
<td nowrap><code id="p-render">render</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>If False, this scenario's DAG is not displayed.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_toolbar">show_toolbar</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the DAG toolbar is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str</code></td>
<td nowrap>"50vh"</td>
<td><p>The maximum height, in CSS units, of the control.</p></td>
</tr>
<tr>
<td nowrap><code id="p-width">width</code></td>
<td><code>str</code></td>
<td nowrap>"100%"</td>
<td><p>The maximum width, in CSS units, of the control.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_action">on_action</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of the function that is triggered when a a node is selected.<br/><br/>All the parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>entity (DataNode | Task): the entity (DataNode or Task) that was selected.</li>
</ul></p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-scenario" title="Jump to the default property documentation."><code>scenario</code></a> is the default property for this visual element.</p>

# Details

When the [*scenario*](#p-scenario) property is set to an instance of `Scenario^`, the control
displays a graphical representation of its DAG.

Here is what the control looks like when connected to a scenario instance:
<figure class="tp-center">
  <img src="../scenario_dag-init-d.png" class="visible-dark"  width="90%"/>
  <img src="../scenario_dag-init-l.png" class="visible-light" width="90%"/>
  <figcaption>The DAG of a scenario</figcaption>
</figure>

The visual representation of the Data Nodes and Tasks is the same as the one used in the
[Taipy Studio extension](../../../../studio/config/graphview.md).

The toolbar, which can be removed by setting the [*show_toolbar*](#p-show_toolbar) property to
False, contains a button that adapts the rendering area zoom factor to the graph representation.

