---
title: <tt>status</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays a status or a list of statuses.

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
<td><code>tuple|dict|list[dict]|list[tuple]</code></td>
<td nowrap></td>
<td><p>The different status items to represent. See below.</p></td>
</tr>
<tr>
<td nowrap><code id="p-without_close">without_close</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If True, the user cannot remove the status items from the list.</p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-value" title="Jump to the default property documentation."><code>value</code></a> is the default property for this visual element.</p>

# Details

Every status line has a message to be displayed and a status priority.

The status priority is defined by a string among "info" (or "i"), "success" (or "s"), "warning" (or "w"), and
"error" (or "e"). An unknown string value sets the priority to "info".<br/>
These priorities are sorted from lower to higher as indicated here.

The property [*value*](#p-value) can be set to a value with the following type:

- A tuple: the status shows a single line; the first element of the tuple defines the *status* value, and the second
  element holds the *message*.
- A dictionary: the status shows a single line; the key "status" of the dictionary holds the *status* value, and the
  key "message" holds the *message*.
- A list of tuples: a list of status entries, each defined as described above.
- A list of dictionaries: a list of status entries, each defined as described above.

When a list of statuses is provided, the status control can be expanded to show all individual
status entries. Users can then remove individual statuses if [*without_close*](#p-without_close)
is set to False (which is the default value).

# Styling

All the status controls are generated with the "taipy-status" CSS class. You can use this class
name to select the status controls on your page and apply style.

# Usage

## Show a simple status

To show a simple `status` control, you would define a Python variable:

```python
status = ("error", "An error has occurred.")
```

This variable can be used as the value of the property [*value*](#p-value) of
the `status` control:

!!! example "Definition"

    === "Markdown"

        ```
        <|{value}|status|>
        ```

    === "HTML"

        ```html
        <taipy:status>{value}</taipy:status>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.status("{value}")
        ```

The control is displayed as follows:
<figure>
    <img src="../status-basic-d.png" class="visible-dark" />
    <img src="../status-basic-l.png" class="visible-light"/>
    <figcaption>A simple status</figcaption>
</figure>

Note that the variable *status* could have been defined as a dictionary to achieve the
same result:

```python
status = {
    "status": "error",
    "message": "An error has occurred."
}
```

## Show a list of statuses

The `status` control can show several status items. They are initially collapsed, where the
control shows the number of statuses with a status priority corresponding to the highest priority
in the status list.

You can create a list of status items as a Python variable:

```python
status = [
    ("warning", "Task is launched."),
    ("warning", "Taks is waiting."),
    ("error", "Task timeout."),
    ("info", "Process was cancelled.")
]
```

The declaration of the control remains the same:

!!! example "Definition"

    === "Markdown"

        ```
        <|{value}|status|>
        ```

    === "HTML"

        ```html
        <taipy:status>{value}</taipy:status>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.status("{value}")
        ```

The control is initially displayed as this:
<figure>
    <img src="../status-multiple1-d.png" class="visible-dark" />
    <img src="../status-multiple1-l.png" class="visible-light"/>
    <figcaption>A collapsed status list</figcaption>
</figure>

If the user clicks on the arrow button, the status list is expanded:
<figure>
    <img src="../status-multiple2-d.png" class="visible-dark" />
    <img src="../status-multiple2-l.png" class="visible-light"/>
    <figcaption>An expanded status list</figcaption>
</figure>

The user can remove a status entry by clicking on the cross button. Here, the user
has removed the third status entry:
<figure>
    <img src="../status-multiple3-d.png" class="visible-dark" />
    <img src="../status-multiple3-l.png" class="visible-light"/>
    <figcaption>After the removal of a status</figcaption>
</figure>

## Prevent status dismissal

If you don't want the user to be allowed to dismiss the displayed statuses, you can set the
[*without_close*](#p-without_close) property to True:

!!! example "Definition"

    === "Markdown"

        ```
        <|{value}|status|without_close|>
        ```

    === "HTML"

        ```html
        <taipy:status without_close>{value}</taipy:status>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.status("{value}", without_close=True)
        ```

With the same array as above, here is what the expanded control looks like:
<figure>
    <img src="../status-multiple4-d.png" class="visible-dark" />
    <img src="../status-multiple4-l.png" class="visible-light"/>
    <figcaption>Preventing removals</figcaption>
</figure>
