---
title: <tt>menu</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Shows a left-side menu.

This control is represented by a unique left-anchor and foldable vertical menu.

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
<td nowrap><code id="p-lov"><u><bold>lov</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>str|list[str|Icon|any]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The list of menu option values.</p></td>
</tr>
<tr>
<td nowrap><code id="p-adapter">adapter</code></td>
<td><code>Function</code></td>
<td nowrap>`"lambda x: str(x)"`</td>
<td><p>The function that transforms an element of <i>lov</i> into a <i>tuple(id:str, label:str|Icon)</i>.</p></td>
</tr>
<tr>
<td nowrap><code id="p-type">type</code></td>
<td><code>str</code></td>
<td nowrap><i>Type of the first lov element</i></td>
<td><p>Must be specified if <i>lov</i> contains a non specific type of data (ex: dict).<br/><i>value</i> must be of that type, <i>lov</i> must be an iterable on this type, and the adapter function will receive an object of this type.</p></td>
</tr>
<tr>
<td nowrap><code id="p-label">label</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The title of the menu.</p></td>
</tr>
<tr>
<td nowrap><code id="p-inactive_ids">inactive_ids</code></td>
<td><code>str|list[str]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>Semicolon (';')-separated list or a list of menu items identifiers that are disabled.</p></td>
</tr>
<tr>
<td nowrap><code id="p-width">width</code></td>
<td><code>str</code></td>
<td nowrap>"15vw"</td>
<td><p>The width, in CSS units, of the menu when unfolded.<br/>Note that when running on a mobile device, the property <i>width[active]</i> is used instead.</p></td>
</tr>
<tr>
<td nowrap><code id="p-width[mobile]">width[mobile]</code></td>
<td><code>str</code></td>
<td nowrap>"85vw"</td>
<td><p>The width, in CSS units, of the menu when unfolded, on a mobile device.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_action">on_action</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of the function that is triggered when a menu option is selected.<br/><br/>All the parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>id (str): the identifier of the button.</li>
<li>payload (dict): the details on this callback's invocation.<br/>
This dictionary has the following keys:
<ul>
<li>action: the name of the action that triggered this callback.</li>
<li>args: List where the first element contains the id of the selected option.</li>
</ul>
</li>
</ul></p></td>
</tr>
<tr>
<td nowrap><code id="p-active">active</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>Indicates if this component is active.<br/>An inactive component allows no user interaction.</p></td>
</tr>
  </tbody>
</table>

<p><sup id="dv">(&#9733;)</sup><a href="#p-lov" title="Jump to the default property documentation."><code>lov</code></a> is the default property for this visual element.</p>

# Styling

All the menu controls are generated with the "taipy-menu" CSS class. You can use this class
name to select the menu controls on your page and apply style.

# Usage

## Defining a simple static menu

!!! example "Definition"

    === "Markdown"

        ```
        <|menu|lov=menu 1;menu 2|>
        ```

    === "HTML"

        ```html
        <taipy:menu lov="menu 1;menu 2"/>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.menu(lov="menu 1;menu 2")
        ```

## Calling a user-defined function

To have the selection of a menu item call a user-defined function, you must set the
[*on_action*](#p-on_action) property to a user-defined function:

You page can define a menu control like:

!!! example "Definition"

    === "Markdown"

        ```
        <|menu|lov=menu 1;menu 2|on_action=my_menu_action|>
        ```

    === "HTML"

        ```html
        <taipy:menu lov="menu 1;menu 2" on_action="my_menu_action"/>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.menu(lov="menu 1;menu 2", on_action=my_menu_action)
        ```

Your Python script must define the *my_menu_action()* function:

```python
def my_menu_action(state, ...):
  ...
```

## Disabling menu options

The [*inactive_ids*](#p-inactive_ids) property can be set to dynamically disable any specific menu
options.

!!! example "Definition"

    === "Markdown"

        ```
        <|menu|lov=menu 1;menu 2;menu 3|inactive_ids=menu 2;menu 3|>
        ```

    === "HTML"

        ```html
        <taipy:menu lov="menu 1;menu 2;menu 3" inactive_ids="menu 2;menu 3"/>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.menu(lov="menu 1;menu 2;menu 3", inactive_ids="menu 2;menu 3")
        ```

## Adjusting presentation

The [*label*](#p-label) property defines the text associated with the main Icon.<br/>
The properties [*width*](#p-width) and [*width[mobile]*](#p-width[mobile]) specify the
requested width of the menu when expanded.

!!! example "Definition"

    === "Markdown"

        ```
        <|menu|lov=menu 1;menu 2;menu 3|label=Menu title|width=15vw|width[mobile]=80vw|>
        ```

    === "HTML"

        ```html
        <taipy:menu lov="menu 1;menu 2;menu 3" label="Menu title" width="15vw" width[mobile]="80vw"/>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.menu(lov="menu 1;menu 2;menu 3", label="Menu title", width="15vw", width__mobile="80vw")
        ```

## Menu icons

As for every control that deals with lov, each menu option can display an image (see Icon^) and/or
some text.

!!! example "Definition"

    === "Markdown"

        ```
        <|menu|lov={[("id1", Icon("/images/icon.png", "Menu option 1")), ("id2", "Menu option 2")]}|>
        ```

    === "HTML"

        ```html
        <taipy:menu lov="{[('id1', Icon('/images/icon.png', 'Menu option 1')), ('id2', 'Menu option 2')]}"/>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.menu(lov="{[('id1', Icon('/images/icon.png', 'Menu option 1')), ('id2', 'Menu option 2')]}")
        ```
