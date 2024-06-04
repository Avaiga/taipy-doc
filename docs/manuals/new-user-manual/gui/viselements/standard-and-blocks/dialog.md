---
title: <tt>dialog</tt>
hide:
  - navigation
---

<!-- Category: controls -->
A modal dialog.

Dialog allows showing some content over the current page.
The dialog is closed when the user presses the Cancel or Validate buttons, or clicks outside the area of the dialog (triggering a Cancel action).

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
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If True, the dialog is visible. If False, it is hidden.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_action">on_action</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>Name of a function triggered when a button is pressed.<br/>The parameters of that function are all optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>id (str): the identifier of the dialog.</li>
<li>payload (dict): the details on this callback's invocation.<br/>This dictionary has the following keys:
<ul>
<li>action: the name of the action that triggered this callback.</li>
<li>args: a list where the first element contains the index of the selected label.</li>
</ul>
</li>
</ul></p></td>
</tr>
<tr>
<td nowrap><code id="p-close_label">close_label</code></td>
<td><code>str</code></td>
<td nowrap>"Close"</td>
<td><p>The tooltip of the top-right close icon button. In the <i>on_action</i> function, args will hold -1.</p></td>
</tr>
<tr>
<td nowrap><code id="p-labels">labels</code></td>
<td><code> str|list[str]</code></td>
<td nowrap></td>
<td><p>A list of labels to show in a row of buttons at the bottom of the dialog. The index of the button in the list is reported as args in the <i>on_action</i> function (-1 for the close icon).</p></td>
</tr>
<tr>
<td nowrap><code id="p-width">width</code></td>
<td><code>str|int|float</code></td>
<td nowrap></td>
<td><p>The width, in CSS units, of this dialog.<br/>(CSS property)</p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str|int|float</code></td>
<td nowrap></td>
<td><p>The height, in CSS units, of this dialog.<br/>(CSS property)</p></td>
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

All the dialogs are generated with the "taipy-dialog" CSS class. You can use this class
name to select the dialogs on your page and apply style.

# Usage

## Showing or hiding a dialog

The default property, [*open*](#p-open), indicates whether the dialog is visible or not:
!!! example "Definition"

    === "Markdown"

        ```
        <|{show_dialog}|dialog|on_action={lambda s: s.assign("show_dialog", False)}|>
        ```

    === "HTML"

        ```html
        <taipy:dialog on_action="{lambda s: s.assign('show_dialog', False)}">{show_dialog}</taipy:dialog>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.dialog("{show_dialog}", on_action="{lambda s: s.assign('show_dialog', False)}")
        ```

With another action that would have previously shown the dialog with:

```python
def button_action(state, id):
    state.show_dialog = True
```

## Specifying labels and actions

Several properties let you specify the buttons to show,
and the action (callback functions) triggered when buttons are pressed:

!!! example "Definition"

    === "Markdown"

        ```
        <|{show_dialog}|dialog|title=Dialog Title|page_id=page1|on_action=dialog_action|labels=Validate;Cancel|>
        ```

    === "HTML"

        ```html
        <taipy:dialog title="Dialog Title" page_id="page1" on_action="dialog_action" labels="Validate;Cancel">{show_dialog}</taipy:dialog>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.dialog("{show_dialog}", title="Dialog Title", page_id="page1", on_action=dialog_action, labels="Validate;Cancel")
        ```

The implementation of the dialog callback could be:

```python
def dialog_action(state, id, payload):
    with state as st:
        ...
        # depending on payload["args"][0]: -1 for close icon, 0 for Validate, 1 for Cancel
        ...
        st.show_dialog = False
```

## Dialog as block element

The content of the dialog can be specified directly inside the dialog block.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show_dialog}|dialog|
            ...
            <|{some_content}|>
            ...
        |>
        ```
  
    === "HTML"

        ```html
        <taipy:dialog open={show_dialog}>
            ...
            <taipy:text>{some_content}</taipy:text>
            ...
        </taipy:dialog>
        ```

    === "Python"
        ```python
        import taipy.gui.builder as tgb
        ...
        with tgb.dialog("{show_dialog}"):
            ...
            tgb.text("{some_content}")
            ...

## Dialog with page

The content of the dialog can be specified as an existing page name using the [*page*](#p-page)
property.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show_dialog}|dialog|page=page_name|>
        ```

    === "HTML"

        ```html
        <taipy:dialog page="page_name">{show_dialog}</taipy:dialog>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.dialog("{show_dialog}", page="page_name")
        ```

## Dialog with partial

The content of the dialog can be specified as a `Partial^` instance using the
[*partial*](#p-partial) property.

!!! example "Definition"

    === "Markdown"

        ```
        <|{show_dialog}|dialog|partial={partial}|>
        ```

    === "HTML"

        ```html
        <taipy:dialog partial="{partial}">{show_dialog}</taipy:dialog>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.dialog("{show_dialog}", partial="{partial}")
        ```
