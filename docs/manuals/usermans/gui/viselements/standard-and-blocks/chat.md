---
title: <tt>chat</tt>
hide:
  - navigation
---

<!-- Category: controls -->
A control that provides the user interface for chatting.

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
<td nowrap><code id="p-messages"><u><bold>messages</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>list[str]</code><br/><i>dynamic</i></td>
<td nowrap><i>Required</i></td>
<td><p>The list of messages. Each element is a list composed of an id, a message and an user identifier.</p></td>
</tr>
<tr>
<td nowrap><code id="p-users">users</code></td>
<td><code>list[str|Icon]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The list of users. See the <a href="../../binding/#list-of-values">section on List of Values</a> for details.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_action">on_action</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when the user enters a new message.<br/>All parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>var_name (str): the name of the messages variable.</li>
<li>payload (dict): the details on this callback's invocation.<br/>This dictionary has the following keys:
<ul>
<li>action: the name of the action that triggered this callback.</li>
<li>args (list): A list composed of a reason (click or Enter), variable name, message, sender id.</li></ul></li></ul>.</p></td>
</tr>
<tr>
<td nowrap><code id="p-with_input">with_input</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>If True, the input field is visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-sender_id">sender_id</code></td>
<td><code>str</code></td>
<td nowrap>"taipy"</td>
<td><p>The user id associated with the message sent from the input</p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str|int|float</code></td>
<td nowrap></td>
<td><p>The maximum height, in CSS units, of this element.</p></td>
</tr>
<tr>
<td nowrap><code id="p-page_size">page_size</code></td>
<td><code>int</code></td>
<td nowrap>50</td>
<td><p>The number of rows retrieved on the frontend.</p></td>
</tr>
<tr>
<td nowrap><code id="p-active">active</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>Indicates if this component is active.<br/>An inactive component allows no user interaction.</p></td>
</tr>
<tr>
<td nowrap><code id="p-id">id</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The identifier that will be assigned to the rendered HTML component.</p></td>
</tr>
<tr>
<td nowrap><code id="p-properties">properties</code></td>
<td><code>dict[str, any]</code></td>
<td nowrap></td>
<td><p>Bound to a dictionary that contains additional properties for this element.</p></td>
</tr>
<tr>
<td nowrap><code id="p-class_name">class_name</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The list of CSS class names that will be associated with the generated HTML Element.<br/>These class names will be added to the default <code>taipy-&lt;element_type&gt;</code>.</p></td>
</tr>
<tr>
<td nowrap><code id="p-hover_text">hover_text</code></td>
<td><code>str</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The information that is displayed when the user hovers over this element.</p></td>
</tr>
  </tbody>
</table>

<p><sup id="dv">(&#9733;)</sup><a href="#p-messages" title="Jump to the default property documentation."><code>messages</code></a> is the default property for this visual element.</p>

# Details

TODO

# Styling

All the date controls are generated with the "taipy-chat" CSS class. You can use this class
name to select the date selectors on your page and apply style.

# Usage

TODO
