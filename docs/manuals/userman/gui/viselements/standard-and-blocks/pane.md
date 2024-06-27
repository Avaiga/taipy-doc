---
title: <tt>pane</tt>
hide:
  - navigation
---

<!-- Category: blocks -->
A side pane.

Pane allows showing some content on top of the current page.
The pane is closed when the user clicks outside the area of the pane (triggering a *on_close*
action).

Pane is a block control.

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
<td nowrap><code id="p-open"><u><bold>open</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>False</td>
<td><p>If True, this pane is visible on the page.<br/>If False, the pane is hidden.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_close">on_close</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when this pane is closed (if the user clicks outside of it or presses the Esc key).<br/>All parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>id (optional[str]): the identifier of the button.</li>
</ul><br/>If this property is not set, no function is called when this pane is closed.</p></td>
</tr>
<tr>
<td nowrap><code id="p-anchor">anchor</code></td>
<td><code>str</code></td>
<td nowrap>"left"</td>
<td><p>Anchor side of the pane.<br/>Valid values are "left", "right", "top", or "bottom".</p></td>
</tr>
<tr>
<td nowrap><code id="p-width">width</code></td>
<td><code>str</code></td>
<td nowrap>"30vw"</td>
<td><p>Width, in CSS units, of this pane.<br/>This is used only if <i>anchor</i> is "left" or "right".</p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str</code></td>
<td nowrap>"30vh"</td>
<td><p>Height, in CSS units, of this pane.<br/>This is used only if <i>anchor</i> is "top" or "bottom".</p></td>
</tr>
<tr>
<td nowrap><code id="p-persistent">persistent</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the pane covers the page where it appeared and disappears if the user clicks in the page.<br/>If True, the pane appears next to the page. Note that the parent section of the pane must have the <i>flex</i> display mode set. See below for an example using the <code>persistent</code> property.</p></td>
</tr>
<tr>
<td nowrap><code id="p-partial">partial</code></td>
<td><code>Partial</code></td>
<td nowrap></td>
<td><p>A Partial object that holds the content of the block.<br/>This should not be defined if <i>page</i> is set.</p></td>
</tr>
<tr>
<td nowrap><code id="p-page">page</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The page name to show as the content of the block.<br/>This should not be defined if <i>partial</i> is set.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_change">on_change</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when the value is updated.<br/>The parameters of that function are all optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>var_name (str): the variable name.</li>
<li>value (any): the new value.</li>
</ul></p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-open" title="Jump to the default property documentation."><code>open</code></a> is the default property for this visual element.</p>

# Styling

All the pane blocks are generated with the "taipy-pane" CSS class. You can use this class
name to select the pane blocks on your page and apply style.

# Usage

## Showing or hiding a pane

The default property, [*open*](#p-open), indicates whether the pane is visible or not:
!!! example "Definition"

    === "Markdown"

        ```
        <|{show}|pane|>
        ```

    === "HTML"

        ```html
        <taipy:pane>{show}</taipy:pane>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.pane("{show}")
        ```

## Choosing where the pane appears

The [*anchor*](#p-anchor) property defines on which side of the display the pane is shown.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show}|pane|anchor=left|>
        ```

    === "HTML"

        ```html
        <taipy:pane anchor="left">{show}</taipy:pane>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.pane("{show}", anchor="left")
        ```

## Showing the pane beside the page content

The pane is shown beside the page content instead of over it if the [*persistent*](#p-persistent)
property evaluates to True.

The parent element must have the *flex* display mode in CSS. To achieve this using
the Markdown syntax, you can leverage the
[*d-flex* class](../styling/stylekit.md#c-d-flex) provided in the
[Stylekit](../styling/stylekit.md).

Here is a full example of how to do this:
```python
from taipy.gui import Gui

show_pane=True

page="""
<|d-flex|
<|{show_pane}|pane|persistent|width=100px|
Pane content
|>
This button can be pressed to open the persistent pane:
<|Open|button|on_action={lambda s: s.assign("show_pane", True)}|>
|>
"""

Gui(page=page).run()
```

The pane is initially opened. If you close it, the bound variable *show_pane* is updated
(set to False).<br/>
Pressing the button sets the variable *show_pane* to True using a lambda callback, which opens the
pane again.

## Pane as block element

The content of the pane can be specified directly inside the pane block.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show}|pane|
        ...
        <|{some_content}|>
        ...
        |>
        ```
  
    === "HTML"

        ```html
        <taipy:pane open={show}>
            ...
            <taipy:text>{some_content}</taipy:text>
            ...
        </taipy:pane>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        with tgb.pane("{show}")
            tgb.text("{some_content}")
        ```

## Pane with page

The content of the pane can be specified as an existing page name using the [*page*](#p-page)
property.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show}|pane|page=page_name|>
        ```

    === "HTML"

        ```html
        <taipy:pane page="page_name">{show}</taipy:pane>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.pane("{show}", page="page_name")
        ```

## Pane with partial

The content of the pane can be specified as a `Partial^` instance using the
[*partial*](#p-partial) property.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show}|pane|partial={partial}|>
        ```

    === "HTML"

        ```html
        <taipy:pane partial="{partial}">{show}</taipy:pane>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.pane("{show}", partial="{partial}")
        ```
