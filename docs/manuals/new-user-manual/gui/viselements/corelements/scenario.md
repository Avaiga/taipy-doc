---
title: <tt>scenario</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Displays and modify the definition of a scenario.

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
<td><p>The scenario to display and edit.<br/>If the value is a list, it must have a single element otherwise nothing is shown.</p></td>
</tr>
<tr>
<td nowrap><code id="p-active">active</code></td>
<td><code>bool</code><br/><i>dynamic</i></td>
<td nowrap>True</td>
<td><p>Indicates if this component is active.<br/>An inactive component allows no user interaction.</p></td>
</tr>
<tr>
<td nowrap><code id="p-expandable">expandable</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, the scenario viewer can be expanded.<br/>If False, the scenario viewer is not expandable and it is shown depending on expanded value.</p></td>
</tr>
<tr>
<td nowrap><code id="p-expanded">expanded</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If True, when a valid scenario is selected, the scenario viewer is expanded and its content is displayed.<br/>If False, the scenario viewer is collapsed and only its name and <i>submit</i> button are visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_submit">show_submit</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the scenario submit button is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_delete">show_delete</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the button to delete a scenario is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_config">show_config</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the scenario configuration label is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_creation_date">show_creation_date</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the scenario creation date is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_cycle">show_cycle</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If False, the scenario cycle label is not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_tags">show_tags</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the scenario tags are not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_properties">show_properties</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the scenario properties are not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_sequences">show_sequences</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the scenario sequences are not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_submit_sequences">show_submit_sequences</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the buttons to submit scenario sequences are not visible.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_submission_change">on_submission_change</code></td>
<td><code>Callback</code></td>
<td nowrap></td>
<td><p>The name of the function that is triggered when a submission status is changed.<br/><br/>All the parameters of that function are optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>submission (Submission): the submission entity containing submission information.</li>
<li>details (dict): the details on this callback's invocation.<br/>
This dictionary has the following keys:
<ul>
<li>submission_status (str): the new status of the submission (possible values: SUBMITTED, COMPLETED, CANCELED, FAILED, BLOCKED, WAITING, RUNNING).</li>
<li>job: the Job (if any) that is at the origin of the submission status change.</li>
<li>submittable_entity: submittable (Submittable): the entity (usually a Scenario) that was submitted.</li>
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

The *scenario control* displays the information stored in a given scenario, lets the user change
its parameters at runtime, and provides ways to submit it or one of its sequences.

When the [*scenario*](#p-scenario) property is set to a `Scenario^` instance, the control displays
the information for that scenario.

Here is what the control would look like when representing a scenario entity:
<figure class="tp-center">
  <img src="../scenario-init-d.png" class="visible-dark"  width="75%"/>
  <img src="../scenario-init-l.png" class="visible-light" width="75%"/>
  <figcaption>Viewing the parameters of a scenario</figcaption>
</figure>

Next to the scenario's label at the top of the control and if the scenario is *primary* in its
cycle, there is an icon showing a flag.<br/>
On the right side of the label, a 'play' button can trigger the scenario submission.

The user can click the scenario label to change it:
<figure class="tp-center">
  <img src="../scenario-edit-label-d.png" class="visible-dark"  width="60%"/>
  <img src="../scenario-edit-label-l.png" class="visible-light" width="60%"/>
  <figcaption>Editing the scenario label</figcaption>
</figure>

The user must click the 'check' button to apply the change or the 'cross' button to cancel the
operation.

The user can see the scenario's tags in the 'Tags' section.<br/>
To add a tag, enter text in the tags area and press 'Enter'. You can create as many tags as you
want. When you have created all the tags and want to add those tags to the scenario, press the
'Apply' button to the right of the tags area.<br/>
You can cancel your actions by pressing the 'Cancel' button.

The 'Sequences' section presents the potential sequences of the scenario.<br/>
To add a sequence, press the 'Add +' button. A new sequence is then created, for which you must
provide a name (note each sequence must have a unique name).<br/>
To edit a sequence, click anywhere on its row. You can then rename it and select its tasks.<br/>
To delete a sequence, click the trash icon of its row.

If the scenario has sequences, the user can submit each sequence independently by pressing the
'Submit' button to the right of the sequence's label.

Users can also add or modify custom properties. Click on an existing property name or value to
modify it, and the "New Property Key" label or "Value" next to it to create a new custom
property.<br/>
Here is what the section looks like when the user requests the creation of a new property:
<figure class="tp-center">
  <img src="../scenario-edit-props-d.png" class="visible-dark"  />
  <img src="../scenario-edit-props-l.png" class="visible-light" />
  <figcaption>Editing custom properties</figcaption>
</figure>

To delete a custom property, the user must select it, then press The 'trash' button that appears on
the right side.

# Usage

## Show or hide sections

A few properties (namely [*show_submit*](#p-show_submit), [*show_delete*](#p-show_delete),
[*show_config*](#p-show_config), [*show_cycle*](#p-show_cycle), [*show_tags*](#p-show_tags), 
[*show_properties*](#p-show_properties), [*show_sequences*](#p-show_sequences), and
[*show_submit_sequences*](#p-show_submit_sequences)) let you customize what sections of the
`scenario` control are visible.

Here is the definition of such a control where the *tags*, *properties* and *sequences* sections
are hidden:
!!! example "Definition"

    === "Markdown"

        ```
        <|{scenario}|scenario|don't show_tags|don't show_properties|don't show_sequences|>
        ```

    === "HTML"

        ```html
        <taipy:scenario show_tags="false" show_properties="false" show_sequences="false">{scenario}</taipy:scenario>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.scenario("{scenario}", show_tags=False, show_properties=False, show_sequences=False)
        ```

The control appears as follows, in a more compact manner:
<figure>
    <img src="../scenario-flags-d.png" class="visible-dark" />
    <img src="../scenario-flags-l.png" class="visible-light"/>
    <figcaption>Hiding some sections</figcaption>
</figure>
