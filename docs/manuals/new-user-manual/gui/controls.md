Controls are user interface objects representing data. Users can interact with these controls.

# Standard controls

Standard controls can be used in all situations when a user interface is needed.
These controls are elements representing generic data.<br/>
Here, you can find common graphical controls such as push buttons and sliders, as well as more
advanced graphical controls such as selectors, tables, and charts.

!!! note "Available in Taipy GUI, Taipy Community, and Enterprise editions"

    The controls listed in this section are provided in the
    [`taipy-gui`](https://pypi.org/project/taipy-gui/) Python package. These controls are
    also present when [`taipy`](https://pypi.org/project/taipy/) is installed.

Here is the list of all available controls in Taipy:

<div class="tp-ve-cards">
<a class="tp-ve-card" href="../text/">
<div>text</div>
<img class="tp-ve-l" src="../text-l.png"/><img class="tp-ve-lh" src="../text-lh.png"/>
<img class="tp-ve-d" src="../text-d.png"/><img class="tp-ve-dh" src="../text-dh.png"/>
<p>Displays a value as a static text.</p>
</a>
<a class="tp-ve-card" href="../button/">
<div>button</div>
<img class="tp-ve-l" src="../button-l.png"/><img class="tp-ve-lh" src="../button-lh.png"/>
<img class="tp-ve-d" src="../button-d.png"/><img class="tp-ve-dh" src="../button-dh.png"/>
<p>A control that can trigger a function when pressed.</p>
</a>
<a class="tp-ve-card" href="../input/">
<div>input</div>
<img class="tp-ve-l" src="../input-l.png"/><img class="tp-ve-lh" src="../input-lh.png"/>
<img class="tp-ve-d" src="../input-d.png"/><img class="tp-ve-dh" src="../input-dh.png"/>
<p>A control that displays some text that can potentially be edited.</p>
</a>
<a class="tp-ve-card" href="../number/">
<div>number</div>
<img class="tp-ve-l" src="../number-l.png"/><img class="tp-ve-lh" src="../number-lh.png"/>
<img class="tp-ve-d" src="../number-d.png"/><img class="tp-ve-dh" src="../number-dh.png"/>
<p>A kind of [`input`](input.md) that handles numbers.</p>
</a>
<a class="tp-ve-card" href="../slider/">
<div>slider</div>
<img class="tp-ve-l" src="../slider-l.png"/><img class="tp-ve-lh" src="../slider-lh.png"/>
<img class="tp-ve-d" src="../slider-d.png"/><img class="tp-ve-dh" src="../slider-dh.png"/>
<p>Displays and allows the user to set a value within a range.</p>
</a>
<a class="tp-ve-card" href="../toggle/">
<div>toggle</div>
<img class="tp-ve-l" src="../toggle-l.png"/><img class="tp-ve-lh" src="../toggle-lh.png"/>
<img class="tp-ve-d" src="../toggle-d.png"/><img class="tp-ve-dh" src="../toggle-dh.png"/>
<p>A series of toggle buttons that the user can select.</p>
</a>
<a class="tp-ve-card" href="../date/">
<div>date</div>
<img class="tp-ve-l" src="../date-l.png"/><img class="tp-ve-lh" src="../date-lh.png"/>
<img class="tp-ve-d" src="../date-d.png"/><img class="tp-ve-dh" src="../date-dh.png"/>
<p>A control that can display and specify a formatted date, with or without time.</p>
</a>
<a class="tp-ve-card" href="../date_range/">
<div>date_range</div>
<img class="tp-ve-l" src="../date_range-l.png"/><img class="tp-ve-lh" src="../date_range-lh.png"/>
<img class="tp-ve-d" src="../date_range-d.png"/><img class="tp-ve-dh" src="../date_range-dh.png"/>
<p>A control that can display and specify a range of dates or times.</p>
</a>
<a class="tp-ve-card" href="../chart/">
<div>chart</div>
<img class="tp-ve-l" src="../chart-l.png"/><img class="tp-ve-lh" src="../chart-lh.png"/>
<img class="tp-ve-d" src="../chart-d.png"/><img class="tp-ve-dh" src="../chart-dh.png"/>
<p>Displays data sets in a chart or a group of charts.</p>
</a>
<a class="tp-ve-card" href="../file_download/">
<div>file_download</div>
<img class="tp-ve-l" src="../file_download-l.png"/><img class="tp-ve-lh" src="../file_download-lh.png"/>
<img class="tp-ve-d" src="../file_download-d.png"/><img class="tp-ve-dh" src="../file_download-dh.png"/>
<p>Allows downloading of a file content.</p>
</a>
<a class="tp-ve-card" href="../file_selector/">
<div>file_selector</div>
<img class="tp-ve-l" src="../file_selector-l.png"/><img class="tp-ve-lh" src="../file_selector-lh.png"/>
<img class="tp-ve-d" src="../file_selector-d.png"/><img class="tp-ve-dh" src="../file_selector-dh.png"/>
<p>Allows uploading a file content.</p>
</a>
<a class="tp-ve-card" href="../image/">
<div>image</div>
<img class="tp-ve-l" src="../image-l.png"/><img class="tp-ve-lh" src="../image-lh.png"/>
<img class="tp-ve-d" src="../image-d.png"/><img class="tp-ve-dh" src="../image-dh.png"/>
<p>A control that can display an image.</p>
</a>
<a class="tp-ve-card" href="../indicator/">
<div>indicator</div>
<img class="tp-ve-l" src="../indicator-l.png"/><img class="tp-ve-lh" src="../indicator-lh.png"/>
<img class="tp-ve-d" src="../indicator-d.png"/><img class="tp-ve-dh" src="../indicator-dh.png"/>
<p>Displays a label on a red to green scale at a specific position.</p>
</a>
<a class="tp-ve-card" href="../login/">
<div>login</div>
<img class="tp-ve-l" src="../login-l.png"/><img class="tp-ve-lh" src="../login-lh.png"/>
<img class="tp-ve-d" src="../login-d.png"/><img class="tp-ve-dh" src="../login-dh.png"/>
<p>A control that lets users enter their username and password.</p>
</a>
<a class="tp-ve-card" href="../menu/">
<div>menu</div>
<img class="tp-ve-l" src="../menu-l.png"/><img class="tp-ve-lh" src="../menu-lh.png"/>
<img class="tp-ve-d" src="../menu-d.png"/><img class="tp-ve-dh" src="../menu-dh.png"/>
<p>Shows a left-side menu.</p>
</a>
<a class="tp-ve-card" href="../navbar/">
<div>navbar</div>
<img class="tp-ve-l" src="../navbar-l.png"/><img class="tp-ve-lh" src="../navbar-lh.png"/>
<img class="tp-ve-d" src="../navbar-d.png"/><img class="tp-ve-dh" src="../navbar-dh.png"/>
<p>A navigation bar control.</p>
</a>
<a class="tp-ve-card" href="../selector/">
<div>selector</div>
<img class="tp-ve-l" src="../selector-l.png"/><img class="tp-ve-lh" src="../selector-lh.png"/>
<img class="tp-ve-d" src="../selector-d.png"/><img class="tp-ve-dh" src="../selector-dh.png"/>
<p>A control that allows for selecting items from a list of choices.</p>
</a>
<a class="tp-ve-card" href="../status/">
<div>status</div>
<img class="tp-ve-l" src="../status-l.png"/><img class="tp-ve-lh" src="../status-lh.png"/>
<img class="tp-ve-d" src="../status-d.png"/><img class="tp-ve-dh" src="../status-dh.png"/>
<p>Displays a status or a list of statuses.</p>
</a>
<a class="tp-ve-card" href="../table/">
<div>table</div>
<img class="tp-ve-l" src="../table-l.png"/><img class="tp-ve-lh" src="../table-lh.png"/>
<img class="tp-ve-d" src="../table-d.png"/><img class="tp-ve-dh" src="../table-dh.png"/>
<p>Displays a data set as tabular data.</p>
</a>
<a class="tp-ve-card" href="../dialog/">
<div>dialog</div>
<img class="tp-ve-l" src="../dialog-l.png"/><img class="tp-ve-lh" src="../dialog-lh.png"/>
<img class="tp-ve-d" src="../dialog-d.png"/><img class="tp-ve-dh" src="../dialog-dh.png"/>
<p>A modal dialog.</p>
</a>
<a class="tp-ve-card" href="../tree/">
<div>tree</div>
<img class="tp-ve-l" src="../tree-l.png"/><img class="tp-ve-lh" src="../tree-lh.png"/>
<img class="tp-ve-d" src="../tree-d.png"/><img class="tp-ve-dh" src="../tree-dh.png"/>
<p>A control that allows for selecting items from a hierarchical view of items.</p>
</a>
</div>


# Scenario management controls

Some controls are dedicated to Scenario Management. These controls let users select
Entities and interact with them.

!!! warning "Available in Taipy Community and Enterprise editions"

    The controls listed in this section are available only if the
    [`taipy`](https://pypi.org/project/taipy/) Python package is installed. These controls are
    **not** present if only [`taipy-gui`](https://pypi.org/project/taipy-gui/) is installed.

Here is the list of all the scenario management-related controls that are available in Taipy:

<div class="tp-ve-cards">
<a class="tp-ve-card" href="../../corelements/scenario_selector/">
<div style="font-size: .8em;">scenario_selector</div>
<img class="tp-ve-l" src="../../corelements/scenario_selector-l.png"/><img class="tp-ve-lh" src="../../corelements/scenario_selector-lh.png"/>
<img class="tp-ve-d" src="../../corelements/scenario_selector-d.png"/><img class="tp-ve-dh" src="../../corelements/scenario_selector-dh.png"/>
<p>Select scenarios from the list of all scenario entities.</p>
</a>
<a class="tp-ve-card" href="../../corelements/scenario/">
<div>scenario</div>
<img class="tp-ve-l" src="../../corelements/scenario-l.png"/><img class="tp-ve-lh" src="../../corelements/scenario-lh.png"/>
<img class="tp-ve-d" src="../../corelements/scenario-d.png"/><img class="tp-ve-dh" src="../../corelements/scenario-dh.png"/>
<p>Displays and modify the definition of a scenario.</p>
</a>
<a class="tp-ve-card" href="../../corelements/scenario_dag/">
<div>scenario_dag</div>
<img class="tp-ve-l" src="../../corelements/scenario_dag-l.png"/><img class="tp-ve-lh" src="../../corelements/scenario_dag-lh.png"/>
<img class="tp-ve-d" src="../../corelements/scenario_dag-d.png"/><img class="tp-ve-dh" src="../../corelements/scenario_dag-dh.png"/>
<p>Displays the DAG of a scenario.</p>
</a>
<a class="tp-ve-card" href="../../corelements/data_node_selector/">
<div style="font-size: .8em;">data_node_selector</div>
<img class="tp-ve-l" src="../../corelements/data_node_selector-l.png"/><img class="tp-ve-lh" src="../../corelements/data_node_selector-lh.png"/>
<img class="tp-ve-d" src="../../corelements/data_node_selector-d.png"/><img class="tp-ve-dh" src="../../corelements/data_node_selector-dh.png"/>
<p>Displays a list of the Data Node entities that can be selected.</p>
</a>
<a class="tp-ve-card" href="../../corelements/data_node/">
<div>data_node</div>
<img class="tp-ve-l" src="../../corelements/data_node-l.png"/><img class="tp-ve-lh" src="../../corelements/data_node-lh.png"/>
<img class="tp-ve-d" src="../../corelements/data_node-d.png"/><img class="tp-ve-dh" src="../../corelements/data_node-dh.png"/>
<p>Displays and edits of a data node.</p>
</a>
<a class="tp-ve-card" href="../../corelements/job_selector/">
<div>job_selector</div>
<img class="tp-ve-l" src="../../corelements/job_selector-l.png"/><img class="tp-ve-lh" src="../../corelements/job_selector-lh.png"/>
<img class="tp-ve-d" src="../../corelements/job_selector-d.png"/><img class="tp-ve-dh" src="../../corelements/job_selector-dh.png"/>
<p>Select jobs from the list of all job entities.</p>
</a>
</div>

