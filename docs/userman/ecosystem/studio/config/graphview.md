Taipy Studio can create a specific kind of view representing configuration
elements in a directed acyclic graph (DAG) that you can visualize and modify.<br/>
We call these views "Graph Views".

There are two types of elements displayed in these views:

- Nodes:<br/>
    These are rectangular boxes that represent specific configuration elements. All
    elements have an "In" and an "Out" port that connect elements one to another.
- Links:<br/>
    These are lines that represent the relation between two elements. All links
    go from the "Out" port of an element to the "In" port of another:<br/>
    - A link from a Data Node element to a Task element indicates that
      the Data Node element is one of the input Data Nodes of the Task element.
    - A link from a Task element to a Data Node element indicates that
      the Data Node element is one of the output Data Nodes of the Task element.
    - A link from a Scenario element to a Task element indicates that
      the Task element is one of the tasks of the Scenario element.

## Opening a Graph View

A Graph View can be created in three situations:

- To display the entire content of a configuration file.<br/>
    Right-click a configuration file item in the **Config Files** section of
    the **Taipy Configs** pane, and select "Show View".
- To display a Scenario configuration element.<br/>
    Right-click a Scenario configuration element in the **Scenarios** section of
    the **Taipy Configs** pane, and select "Show View".

## The Graph View actions

At the top of a Graph View, you can see the identifier of the focused configuration element.

Below that top row, there is a row of icons that can be clicked to trigger actions.

This row is split into two sections:

- Left section: General tools
    - ![Re-layout](../images/config-icon-relayout.png)<br/>
       Rearrange the elements so they look better in the view.
    - ![Refresh](../images/config-icon-refresh.png)<br/>
       Reload the configuration file in case a desynchronization occurs.
    - ![Unsaved](../images/config-icon-modified.png)<br/>
       Displayed as a circle if the configuration file was saved and as a filled disk
       if the file needs saving.<br/>
       This icon is not present when the Graph View represents a whole configuration
       file since this information is already in the tab title.
    - ![Save as PNG](../images/config-icon-saveimage.png)<br/>
       Save the Graph View in a PNG image file.
    - ![Zoom to fit](../images/config-icon-zoomfit.png):<br/>
       Adjust the panning and zoom factor of the Graph View so the entire graph can be
       represented.
- Right section: Configuration element creation tools.
    - ![Add Scenario](../images/config-icon-add-scenario.png)<br/>
       Adds a new Scenario configuration element in the configuration file as well as in the Graph
       View.<br/>
       This icon appears **only** when the Graph View represents a full configuration file.
    - ![Add Task](../images/config-icon-add-task.png)<br/>
       Adds a new Task configuration element in the configuration file as well as in the Graph
       View.
    - ![Add Data Node](../images/config-icon-add-datanode.png)<br/>
       Adds a new Data Node configuration element in the configuration file as well as in the Graph
       View.

## Editing in a Graph View

To demonstrate the capabilities of the Graph View, we will create the configuration
described in the
[Python code configuration](../../../advanced_features/configuration/advanced-config.md#python-code-configuration)
example, using the interactive features that Taipy Studio provides.<br/>
Note that for the sake of conciseness, we will create a Scenario configuration that
holds only one sequence. When you understand the process, you will see that creating other
sequences is straightforward.

We are starting from a project where only the Python code was developed:

<p align="center">
  <img src="../../images/config_explorer.png" width="50%"/>
</p>

- `main.py` loads the configuration file and submits a scenario
- `functions.py` defines the functions used by the Task configuration elements.

Note that there is no Python code for defining the `Config^` object in these source files.

We also start with an empty `config.toml` file, where the configuration elements will
be defined.

You can see the 'T' sign next to the `main.py` file in the **Explorer** pane. This indicates
that this Python file is considered the *main* Python module for the application. This
is used when assigning a function to be executed in a Task configuration element.<br/>
To set another source file as the *main* Python module file, simply right-click on the file
in the **Explorer** pane and select "Taipy: Set as main module".

### Creating the first configuration elements

We will start by opening a Graph View representing the entire configuration file.
Then, we will create the Data Node and Task configuration elements using the
[Graph View action buttons](#the-graph-view-actions).

<p align="center">
  <img src="../../images/config_graphview_1.gif" width="80%"/>
</p>

After the Task configuration and all three Data Node configurations are created,
we connect the Out ports to the appropriate In ports by dragging links.

Note how the Details section reflects the selected configuration element.

### Creating the Scenario configuration

Similarly, we create the Scenario configuration element and connect its Out port to the In port of
the "planning" task to indicate that this Task configuration element is part of the
"my_scenario" scenario:

<p align="center">
  <img src="../../images/config_graphview_2.gif" width="80%"/>
</p>

### Setting the configuration elements parameters

You can select a configuration element from the Graph View and use the Details
section of the **Taipy Configs** pane.<br/>
From there, you can set the properties of the selected element.

Here is how we can set the function used in the Task configuration we have created above. Taipy
Studio can locate the functions module and name, so it is easy to spot the one you want to
use.<br/>
In our example, we want our Task configuration to use the function called `plan` from the
`functions` module (the `functions.py` source file):

<p align="center">
  <img src="../../images/config_graphview_3.gif" width="80%"/>
</p>

After this final step, the configuration file can be saved from the Graph View
itself (pressing the `Ctrl-S` key combination). The generated configuration file can be
used by a Taipy application: in the source file `main.py`, you can load this
configuration file and submit an entity created from the scenario configuration you just
have designed:

```py
import taipy.core as tp
from taipy import Config


if __name__ == "__main__":
    Config.load("config.toml")
    tp.Orchestrator().run()

    # Retrieve the scenario configuration from the Config
    scenario_cfg = Config.scenarios["my_scenario"]
    # Create a scenario entity
    scenario = tp.create_scenario(scenario_cfg)
    # Submit the scenario
    tp.submit(scenario)
```

### Changing the links

- To add a control point on a link, click the link where you want to create
    the control point, then drag the point where you want it. Release the
    mouse button when you are done.
- To remove a control point, select it (its color changes when you click on it),
  then press the `<DEL>` key.
- To remove a link, select it while pressing the `<SHIFT>` key, then press the `<DEL>`
  key.<br/>
  Note that the source element of the link is removed from the Graph View but not
  from the configuration file.
