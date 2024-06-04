---
title: <tt>indicator</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays a label on a red to green scale at a specific position.

The *min* value **can** be greater than the *max* value.<br/>
The value will be maintained between min and max.

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
<td nowrap><code id="p-display"><u><bold>display</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>any</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The label to be displayed.<br/>This can be formatted if it is a numerical value.</p></td>
</tr>
<tr>
<td nowrap><code id="p-value">value</code></td>
<td><code>int,float</code><br/><i>dynamic</i></td>
<td nowrap><i>min</i></td>
<td><p>The location of the label on the [<i>min</i>, <i>max</i>] range.</p></td>
</tr>
<tr>
<td nowrap><code id="p-min">min</code></td>
<td><code>int|float</code></td>
<td nowrap>0</td>
<td><p>The minimum value of the range.</p></td>
</tr>
<tr>
<td nowrap><code id="p-max">max</code></td>
<td><code>int|float</code></td>
<td nowrap>100</td>
<td><p>The maximum value of the range.</p></td>
</tr>
<tr>
<td nowrap><code id="p-format">format</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The format to use when displaying the value.<br/>This uses the <code>printf</code> syntax.</p></td>
</tr>
<tr>
<td nowrap><code id="p-orientation">orientation</code></td>
<td><code>str</code></td>
<td nowrap>"horizontal"</td>
<td><p>The orientation of this slider.</p></td>
</tr>
<tr>
<td nowrap><code id="p-width">width</code></td>
<td><code>str</code></td>
<td nowrap>None</td>
<td><p>The width, in CSS units, of the indicator (used when orientation is horizontal).</p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str</code></td>
<td nowrap>None</td>
<td><p>The height, in CSS units, of the indicator (used when orientation is vertical).</p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-display" title="Jump to the default property documentation."><code>display</code></a> is the default property for this visual element.</p>

# Styling

All the indicator controls are generated with the "taipy-indicator" CSS class. You can use this
class name to select the indicator controls on your page and apply style.

# Usage

## Minimal usage

Shows a message at a specified position between min and max.

!!! example "Definition"

    === "Markdown"

        ```
        <|Value|indicator|value={val}|min=0|max=100|>
        ```

    === "HTML"

        ```html
        <taipy:indicator value="{val}" min="0" max="100">Value</taipy:indicator>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.indicator("Value", value="{val}", min="0", max="100")
        ```

## Formatting the message

The [*format*](#p-format) property can be set to the format of the value to be displayed.

A _format_ can be applied to the message. 

!!! example "Definition"

    === "Markdown"

        ```
        <|50|indicator|format=%.2f|value=10|>
        ```

    === "HTML"

        ```html
        <taipy:indicator format="%.2f" value="10">50</taipy:indicator>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.indicator("50", format="%.2f", value="10")
        ```

## Vertical indicators

The [*orientation*](#p-orientation) property can be specified to "vertical" (or "v") to create a
vertical indicator.

!!! example "Definition"

    === "Markdown"

        ```
        <|Value|indicator|orientation=v|value=10|>
        ```

    === "HTML"

        ```html
        <taipy:indicator orientation="v" value="10">Value</taipy:indicator>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.indicator("Value", orientation="v", value="10")
        ```

## Dimensions

The properties [*width*](#p-width) and [*height*](#p-height) can be specified, depending on
the value of [*orientation*](#p-orientation).

!!! example "Definition"

    === "Markdown"

        ```
        <|Value 1|indicator|value={val1}|width=50vw|>

        <|Value 2|indicator|value={val2}|orientation=vertical|height=50vh|>
        ```
  
    === "HTML"

        ```html
        <taipy:indicator value="{val1}" width="50vw">Value 1</taipy:indicator>

        <taipy:indicator value="{val2}" orientation="vertical" height="50vh">Value 2</taipy:indicator>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.indicator("{Value 1}", value="{val1}", width="50vw")
        tgb.indicator("{Value 2}", value="{val2}", orientation="vertical", width="50vw")
        ```
