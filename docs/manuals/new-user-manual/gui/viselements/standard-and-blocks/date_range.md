---
title: <tt>date_range</tt>
hide:
  - navigation
---

<!-- Category: controls -->
A control that can display and specify a range of dates or times.

The user is expected to select the starting and ending dates defining the date range, typically
stored as the first and second element of an array of `datetime.date` or `datetime.datetime`
objects.<br/>
Note that the control does *not* check whether the first day precedes the second one: should the
application enforce that, it must be programmed accordingly.

!!! warning "Warning on Windows"

    When you are using dates earlier than January 1st, 1970 (the UNIX epoch) in a date range
    control on a Windows system, you may receive a warning in the console where the script was run,
    indicating a raised exception in `datetime.astimezone()`.<br/>
    This is a known problem in the Python implementation, referenced in the
    [Python issue tracker](https://bugs.python.org/issue36759), that Taipy has no workaround for.

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
<td nowrap><code id="p-dates"><u><bold>dates</bold></u></code><sup><a href="#dv">(&#9733;)</a></sup></td>
<td><code>list(datetime</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>The dates that this control represents and can modify.<br/>It is typically bound to a list of two <code>datetime</code> object.</p></td>
</tr>
<tr>
<td nowrap><code id="p-with_time">with_time</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>Whether or not to show the time part of the date.</p></td>
</tr>
<tr>
<td nowrap><code id="p-format">format</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The format to apply to the value. See below.</p></td>
</tr>
<tr>
<td nowrap><code id="p-editable">editable</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>Shows the date as a formatted string if not editable.</p></td>
</tr>
<tr>
<td nowrap><code id="p-label_start">label_start</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The label associated with the first input.</p></td>
</tr>
<tr>
<td nowrap><code id="p-label_end">label_end</code></td>
<td><code>str</code></td>
<td nowrap></td>
<td><p>The label associated with the second input.</p></td>
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
<td nowrap><code id="p-propagate">propagate</code></td>
<td><code>bool</code></td>
<td nowrap><i>App config</i></td>
<td><p>Allows the control's main value to be automatically propagated.<br/>The default value is defined at the application configuration level.<br/>If True, any change to the control's value is immediately reflected in the bound application variable.</p></td>
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

<p><sup id="dv">(&#9733;)</sup><a href="#p-dates" title="Jump to the default property documentation."><code>dates</code></a> is the default property for this visual element.</p>

# Details

The [*format*](#p-format) property lets you indicate how to display the date objects set to the
[*dates*](#p-dates) property. Note that the format is used only when [*editable*](#p-editable) is
set to False (the date range control is read-only).<br/>
The [`date`](date.md) control has the same property. Please look at this control's documentation
for more information on this property.

# Styling

All the date range controls are generated with the "taipy-date_range" CSS class. You can use this
class name to select the date range selectors on your page and apply style.

# Usage

## Selecting a date range

The [*dates*](#p-dates) property (which is the default property for this control) must be set to an
array of two `datetime.date` objects, representing the selected start and end dates of the range.

Assuming the variable *dates* was defined by the following code:

```python
import datetime

start_date = datetime.date(1756, 1, 27)
end_date   = datetime.date(1791, 12, 5)
dates = [start_date, end_date]
```

The definition of the date range selector is as simple as: 

!!! example "Definition"

    === "Markdown"

        ```
        <|{dates}|date_range|>
        ```

    === "HTML"

        ```html
        <taipy:date_range>{dates}</taipy:date_range>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.date_range("{dates}")
        ```

The date range selector looks like this:
<figure>
    <img src="../date_range-simple-d.png" class="visible-dark" />
    <img src="../date_range-simple-l.png" class="visible-light"/>
    <figcaption>Date range selector</figcaption>
</figure>

An `on_change` callback can be set to retrieve the user's selection:

```python
def on_change(s: State, name: str, value: any):
    if name == "dates":
        # value[0] is set to the first selected date
        # value[1] is set to the first selected date
```

## Selecting a range with times

You can set the [*with_time*](#p-with_time) property to True to display the range time: the
dates should then be instances of `datetime.datetime`.

Here is some code that defines the date range with specific time values:

```python
import datetime

start_date = datetime.date(2023, 3, 26, 7, 37)
end_date   = datetime.date(2023, 3, 26, 19, 2)
dates = [start_date, end_date]
```

The control definition just has the [*with_time*](#p-with_time) property set to True:

!!! example "Definition"

    === "Markdown"

        ```
        <|{dates}|date_range|with_time|>
        ```

    === "HTML"

        ```html
        <taipy:date_range with_time>{dates}</taipy:date_range>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.date_range("{dates}", with_time=True)
        ```

Here is how the date range selector looks like:
<figure>
    <img src="../date_range-with_time-d.png" class="visible-dark" />
    <img src="../date_range-with_time-l.png" class="visible-light"/>
    <figcaption>Date range selector with time</figcaption>
</figure>

## Custom labels

The [*label_start*](#p-label_start) and [*label_end*](#p-label_end) properties can be used to
label the date fields to provide context to the user.

Here is how a hotel reservation application may declare a date range selector with appropriate
labels for booking a given period:

!!! example "Definition"

    === "Markdown"

        ```
        <|{dates}|date_range|label_start=Check-in|label_end=Check-out|>
        ```

    === "HTML"

        ```html
        <taipy:date_range label_start="Check-in" label_end="Check-out">{dates}</taipy:date_range>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.date_range("{dates}", label_start="Check-in", label_end="Check-out")
        ```

Here is how the date range selector looks like:
<figure>
    <img src="../date_range-labels-d.png" class="visible-dark" />
    <img src="../date_range-labels-l.png" class="visible-light"/>
    <figcaption>Labels on the date fields</figcaption>
</figure>
