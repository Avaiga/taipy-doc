---
title: <tt>job_selector</tt>
hide:
  - navigation
---

<!-- Category: controls -->
Select jobs from the list of all job entities.

The job selector shows all the job entities handled by Taipy Core and lets the user
select a job or a set of jobs from the list.

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
<td><code>Job|list[Job]</code><br/><i>dynamic</i></td>
<td nowrap></td>
<td><p>Bound to the selected <code>Job^</code>(s), or None if there is none.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_id">show_id</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the <code>Job^</code> id is not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_submitted_label">show_submitted_label</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the <code>Scenario^</code> or <code>Sequence^</code> label is not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_submitted_id">show_submitted_id</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If True, the <code>Scenario^</code> or <code>Sequence^</code> id is shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_submission_id">show_submission_id</code></td>
<td><code>bool</code></td>
<td nowrap>False</td>
<td><p>If True, the submission id is shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_date">show_date</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the <code>Job^</code> date is not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_cancel">show_cancel</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the Cancel buttons are not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-show_delete">show_delete</code></td>
<td><code>bool</code></td>
<td nowrap>True</td>
<td><p>If False, the Delete buttons are not shown in the selector.</p></td>
</tr>
<tr>
<td nowrap><code id="p-on_change">on_change</code></td>
<td><code>callback</code></td>
<td nowrap></td>
<td><p>The name of a function that is triggered when the selection is updated.<br/>The parameters of that function are all optional:
<ul>
<li>state (<code>State^</code>): the state instance.</li>
<li>var_name (str): the variable name.</li>
<li>value (<code>Job^</code>): the selected job.</li>
</ul></p></td>
</tr>
<tr>
<td nowrap><code id="p-height">height</code></td>
<td><code>str</code></td>
<td nowrap>"50vh"</td>
<td><p>The maximum height, in CSS units, of the control.</p></td>
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

The `job_selector` control lists all jobs resulting from submissions of entities.

All jobs are represented as a row in a table with all the related details.

Here is an example of what the job selector control would look like with default settings after a
few jobs were executed:
<figure class="tp-center">
  <img src="../job_selector-init-d.png" class="visible-dark"  />
  <img src="../job_selector-init-l.png" class="visible-light" />
  <figcaption>The list of Jobs</figcaption>
</figure>

<h2>Selection</h2>

The user can select one or more jobs from the list. The variable bound to the [*value*](#p-value)
property is updated accordingly. A list of selected jobs is returned if several jobs were selected.

All jobs can be selected or deselected by switching the top-left check box to set or unset.

<h2>Actions</h2>

If the [*show_delete*](#p-show_delete) property is not set to False, a trash icon appears on the
right side of the row, for jobs that can be deleted (jobs that are not running). This allows for
removing the job from the list.<br/>
Similarly, if jobs that can be deleted are selected, and if the [*show_delete*](#p-show_delete)
property is set to True, a trash icon appears at the top-right corner of the control, to delete
all selected jobs from the list.

If the [*show_cancel*](#p-show_cancel) property is not set to False, running jobs have a 'stop'
icon in their row, allowing to cancel them.<br/>
A similar icon appears at the top-right corner of the control when selected jobs can be canceled.

<h2>Filters</h2>

In the top left corner of the job selector control, there is a *filter* button that can be used to
filter the displayed jobs depending on criteria that the user can specify:
<figure class="tp-center">
  <img src="../job_selector-filter-d.png" class="visible-dark"  />
  <img src="../job_selector-filter-l.png" class="visible-light" />
  <figcaption>The filter button</figcaption>
</figure>

When the user clicks that button, a filter dialog pops up where one can set different filters with
different criteria:
<figure class="tp-center">
  <img src="../job_selector-filter1-d.png" class="visible-dark"  width="80%"/>
  <img src="../job_selector-filter1-l.png" class="visible-light" width="80%"/>
  <figcaption>The filter dialog</figcaption>
</figure>

Initially, this dialog has no configured filter, therefore the *apply* button indicates that '0'
filters would be set.

To create a new filter, the user must select one of the control's columns, an operator (such as
*is* and *is not*), and an operand as a value.<br/>
In the following image, the user has indicated that only the jobs where the *Status* is set to
"ABANDONED" should be listed:
<figure class="tp-center">
  <img src="../job_selector-filter2-d.png" class="visible-dark"  width="80%"/>
  <img src="../job_selector-filter2-l.png" class="visible-light" width="80%"/>
  <figcaption>Specifying a filter</figcaption>
</figure>

After the 'Add filter' button (with the '+' sign) is pressed, the filter is created:
<figure class="tp-center">
  <img src="../job_selector-filter3-d.png" class="visible-dark"  width="80%"/>
  <img src="../job_selector-filter3-l.png" class="visible-light" width="80%"/>
  <figcaption>Adding a filter</figcaption>
</figure>

The filter can be removed by pressing the trash icon to the right of the filter row.

Note that the 'Apply' button now indicates that there is a filter that can be applied.

Pressing the 'Apply' button applies the filter to the job selector list, resulting in the following
image:
<figure class="tp-center">
  <img src="../job_selector-filter4-d.png" class="visible-dark"  />
  <img src="../job_selector-filter4-l.png" class="visible-light" />
  <figcaption>The filter is applied</figcaption>
</figure>

Note that next to the 'filter' button, the control now displays the number of currently applied
filters.

# Usage

## Show or hide columns

The control's properties [*show_id*](#p-show_id),
[*show_submitted_label*](#p-show_submitted_label), [*show_submitted_id*](#p-show_submitted_id),
[*show_submission_id*](#p-show_submission_id), [*show_date*](#p-show_date),
[*show_cancel*](#p-show_cancel), and [*show_delete*](#p-show_delete) let you indicate what columns
the job selector control displays.

We can define our control so the job identifiers and the submission dates are not shown, to have a
more compact display:
!!! example "Definition"

    === "Markdown"

        ```
        <|{job}|job_selector|don't show_id|don't show_date|>
        ```

    === "HTML"

        ```html
        <taipy:job_selector show_id="false" show_date="false">{job}</taipy:job_selector>
        ```

    === "Python"

        ```python
        import taipy.gui.builder as tgb
        ...
        tgb.job_selector("{job}", show_id=False, show_date=False)
        ```

Here is what the control would look like:
<figure class="tp-center">
  <img src="../job_selector-columns-d.png" class="visible-dark"  />
  <img src="../job_selector-columns-l.png" class="visible-light" />
  <figcaption>Choosing the displayed columns</figcaption>
</figure>
