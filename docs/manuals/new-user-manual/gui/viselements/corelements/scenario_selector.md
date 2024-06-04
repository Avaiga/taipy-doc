---
title: <tt>scenario_selector</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Select scenarios from the list of all scenario entities.

The scenario selector shows all the scenario entities handled by Taipy Core and lets the user
select a scenario from a list, create new scenarios or edit existing scenarios.

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
<td><code>Scenario</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>Bound to the selected <code>Scenario^</code>, or None if there is none.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_add_button">show_add_button</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the button to create a new scenario is not displayed.</p></td>
</tr>
<tr>
<td nowrap><code id="p-display_cycles">display_cycles</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the cycles are not shown.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_primary_flag">show_primary_flag</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the primary scenarios are not identified with specific visual hint.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_change">on_change</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when the value is updated.<br/>The parameters of that function are all optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>var_name (str): the variable name.</li>
<li>value (<code>Scenario^</code>): the selected scenario.</li>
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
<td nowrap>False</td>
<td><p>If True, a pin is shown on each item of the selector and allows to restrict the number of displayed items.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_creation">on_creation</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of the function that is triggered when a scenario is about to be created.<br/><br/>All the parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>id (str): the identifier of the scenario selector.</li>
<li>payload (dict): the details on this callback's invocation.<br/>
This dictionary has the following keys:
<ul>
<li>config: the name of the selected scenario configuration.</li>
<li>date: the creation date for the new scenario.</li>
<li>label: the user-specified label.</li>
<li>properties: a dictionary containing all the user-defined custom properties.</li>
</ul>
</li>
<li>The callback function can return a scenario, a string containing an error message (a scenario will not be created), or None (then a new scenario is created with the user parameters).</li>
</ul></p></td>
</tr>
<tr>
<td nowrap><code id="p-show_dialog">show_dialog</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, a dialog is shown when the user click on the 'Add scenario' button.</p></td>
</tr>
<tr>
<td nowrap><code id="p-scenarios">scenarios</code></td>
<td><code>list[Scenario|Cycle]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>TODO: The list of Scenario/Cycle to show. Shows all Cycle/Scenario if value is None.</p></td>
</tr>
<tr>
<td nowrap><code id="p-multiple">multiple</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>TODO: If True, the user can select multiple scenarios.</p></td>
</tr>
<tr>
<td nowrap><code id="p-filter">filter</code></td>
<td><code>bool|str|list[str]</code></td>
<td nowrap>"Config id;Label;Creation date;Cycle label;Cycle start;Cycle end;Primary;Tags"</td>
<td><p>TODO: a list of scenario attributes to filter on. If False, do not allow filter.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_search">show_search</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>TODO: If True, allows the user to search locally on label.</p></td>
</tr>
<tr>
<td nowrap><code id="p-sort">sort</code></td>
<td><code>bool|str|list[str]</code></td>
<td nowrap>"Config id;Label;Creation date"</td>
<td><p>TODO: a list of scenario attributes to sort on. If False, do not allow sort.</p></td>
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

The scenario selector displays a tree selector where scenarios are grouped based on their cycle
(if the property [*display_cycles*](#p-display_cycles) has not been set to False).<br/>
If the [*show_primary_flag*](#p-show_primary_flag) property has not been forced to False, the
label of the primary scenario are overlaid with a small visual hint that lets users spot them
immediately.

If no created scenario has been created yet, the tree selector will appear empty. The default
behavior, controlled by the [*show_add_button*](#p-show_add_button) property, is to display a
button letting users create new scenarios:
<figure class="tp-center">
  <img src="../scenario_selector-empty-d.png" class="visible-dark"  width="80%"/>
  <img src="../scenario_selector-empty-l.png" class="visible-light" width="80%"/>
  <figcaption>Empty scenario selector</figcaption>
</figure>

When the user presses that button, a form appears so that the settings of the new scenario can be
set:
<figure class="tp-center">
  <img src="../scenario_selector-create-d.png" class="visible-dark"  width="60%"/>
  <img src="../scenario_selector-create-l.png" class="visible-light" width="60%"/>
  <figcaption>Dialog to create a new scenario</figcaption>
</figure>

In this form, the user must indicate which scenario configuration should be used and specify the
scenario creation date.<br/>
Custom properties can also be added to the new scenario by pressing the '+' button located on the
right side of the property key and value fields.

When several new scenarios are created, the scenario selector will list all the scenarios,
potentially grouped in their relevant cycle:
<figure class="tp-center">
  <img src="../scenario_selector-filled-d.png" class="visible-dark"  width="60%"/>
  <img src="../scenario_selector-filled-l.png" class="visible-light" width="60%"/>
  <figcaption>Showing all the created scenarios</figcaption>
</figure>

Notice how the primary scenario for a cycle is immediately flagged as "primary" (you may choose
not to show that icon by setting the [*show_primary_flag*](#p-show_primary_flag) property to
False).

## Editing a scenario

Users can press the pencil icon located next to the scenario labels. When that happens, a dialog
box similar to the scenario creation dialog is displayed to let users modify the scenario
settings.

Here is how this dialog box looks like:
<figure class="tp-center">
  <img src="../scenario_selector-edition-d.png" class="visible-dark"  width="60%"/>
  <img src="../scenario_selector-edition-l.png" class="visible-light" width="60%"/>
  <figcaption>Editing a scenario</figcaption>
</figure>

The user can change the scenario label and custom properties then press the 'Apply' button to
propagate the changes.<br/>
To add a new custom property, the user has to fill the 'Key' and 'Value' fields in the 'Custom
Properties' section, then press the '+' button.<br/>
A custom property can be removed by pressing the trash button next to it.<br/>

The 'Cancel' button closes the dialog without changing anything.<br/>
The 'Delete' button deletes the edited scenario.

Note that there is no way to change the scenario configuration or its creation date.

## Selecting a scenario

When the user selects a scenario in the tree selector, the [*value*](#p-value) property is
set to the selected entity and the [*on_change*](#p-on_change) callback is invoked. The
application can then use the selected value.

If no scenario is selected, [*value*](#p-value) is set no None.

# Usage

## Customizing the creation

You can set the [*on_creation*](#p-on_creation) property to a callback function that lets you
customize how a new scenario is created when pressing the 'Add Scenario' button.

This callback function expects three parameters:

- *state*: the `State^` of the user;
- *id*: the identifier of the control, if any;
- *payload*: a dictionary that contains the following keys:
    - *action*: the name of the callback function;
    - *config*: the `ScenarioConfig^` that was selected in the dialog;
    - *date*: a `datetime.datetime` object representing the date and time when the creation was
      requested;
    - *label*: the scenario label as specified in the dialog. This string is used as the scenario
      name;
    - *properties*: a dictionary that contains all the custom properties that the user has defined
      in the creation dialog.

The *payload* parameter contains all the information that is needed to create a new scenario. In
the callback function, you can use these parameters to customize the new scenario creation further.

- If all those parameters look just fine in terms of what needs to be achieved, the callback
  function can simply return None. That will get Taipy to carry on with the scenario creation with
  no customization whatsoever.<br/>
  That is the default behavior of a `scenario_selector` control that has no value in its
  [*on_creation*](#p-on_creation).
- If the parameters (typically the custom property keys or values) are invalid in the application's
  context, you may want to refuse the creation of the scenario. In this case, the callback function
  should return a string that provides visual feedback to the user (or an empty string if this
  is not needed).
- You can also create the scenario in the function callback and return it. This is the opportunity
  to change the scenario creation parameters to fit the application's needs.

Here is an example of a creation callback function that deals with these three situations.

Imagine that the application, if the user has added the "index" custom property to a scenario,
needs to check that the property value is valid and transform it before the scenario is actually
created.<br/>
In our example, we expect the user to set a positive integer value to the property "index". The
code will check that the value is valid and replace it with a string representation of this value
minus one, prefixed with the sharp ('#') sign.<br/>
Here is the code for the creation callback function:

```python linenums="1"
def check_index(state, id, payload):
  # Retrieve the custom properties
    properties = payload.get("properties", None)
    if not properties or not "index" in properties:
        # No custom 'index' property
        # Create a regular scenario
        return None
    # Read the 'index' property
    index = None
    try:
        index = int(properties["index"])
        # Invalid value: must be greater than 1
        if index < 1:
            return "'index' must be strictly positive"
        # Replace the property value
        properties["index"] = f"#{index-1}"
    except: # Invalid value: not an integer
        return "'index' property is not a valid integer"
    # Create a new scenario with the same configuration, label, and date
    scenario = tp.create_scenario(payload["config"], payload["date"], payload["label"])
    # Set the scenario properties
    scenario.properties.update(properties)
    return scenario
```

When the user requests the creation of a new scenario, the creation dialog pops up. When fields
are properly set (only the label is mandatory), the user will press the 'Create' button to confirm
the scenario creation.<br/>
At this time, the application will invoke the creation callback to customize the scenario
parameters.

Lines 4-7 deal with the case where the *index* custom property was *not* set. In this case, we want
to do nothing special and carry on with the regular creation of the control, returning None from
the callback function.

Line 9-18 verify that the *index* custom property is a valid integer greater than one. If this is
not the case, an error message is returned to the user for correction.

Finally, lines 20-22 take care of creating the scenario with the new settings.<br/>
This scenario is returned by the callback function to let Taipy know it was created properly.

The scenario selector control definition needs to have the [*on_creation*](#p-on_creation) property
set to the function:
!!! example "Definition"

    === "Markdown"

        ```
        <|{scenario}|scenario_selector|on_creation=check_index|>
        ```

    === "HTML"

        ```html
        <taipy:scenario_selector on_creation="check_index">{scenario}</taipy:scenario_selector>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.scenario_selector("{scenario}", on_creation=check_index)
        ```
