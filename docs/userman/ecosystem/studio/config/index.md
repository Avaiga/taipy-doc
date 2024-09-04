Applications that rely on Taipy Scenarios need to define a
[Configuration](../../../scenario_features/sdm/scenario/scenario-config.md) where the data flow is
described.<br/>
This configuration can be coded in Python and tuned using environment variables
(as described in the
[advanced configuration](../../../advanced_features/configuration/advanced-config.md#python-code-configuration)
section).

Taipy Studio provides ways to design graphically Taipy application configurations.
Within the Visual Studio Code environment, you can create configuration elements (for
Data Nodes, Tasks, and Scenarios), specify the properties for those elements,
and use a visual representation of those configuration elements as a graph.

<p align="center">
  <img src="../images/config_overview.png" width="75%"/>
</p>

Taipy Studio stores those configurations in TOML files. These files can be used at
runtime by Taipy applications as described in the
[note on Studio](../../../advanced_features/configuration/advanced-config.md#studio).

Taipy Studio has a dedicated panel called **Taipy Configs**, where almost everything
happens. To open this panel, use the "View > Open View..." menu option and search
for the view called "Taipy Configs".

The view appears like this:

<p align="center">
  <img src="../images/config_panel.png" width="40%"/>
</p>

This panel is split into several sections that let the user access all the
configuration elements:

- **Config Files**: holds a list of configuration files (`*.toml`) that exist in the
    project.<br/>
    The user can select a configuration file in this list to populate the other
    sections of the Taipy Configs view.
- **Data Nodes**: holds the list of
    [Data Node configurations](../../../scenario_features/data-integration/data-node-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Data Node configuration in this list to access all its
    properties in the Details section (see below).
- **Tasks**: holds the list of
    [Task configurations](../../../scenario_features/task-orchestration/scenario-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Task configuration in this list to access all its
    properties in the Details section (see below).
- **Scenarios**: holds the list of
    [Scenario configurations](../../../scenario_features/sdm/scenario/scenario-config.md) defined
    in the selected configuration file.<br/>
    Each Scenario configuration element may contain sequences that appear as child nodes of the
    scenario element.<br/>
    The user can select a Scenario configuration in this list to access all its
    properties in the Details section (see below).
- **Details**: When a configuration element is selected, the Details section displays
    all the properties of this configuration element and allows the user to
    modify these properties.

Using these different sections, you can add, rename, or remove configuration
elements, as well as change their properties in the "Details" section.

All your actions impact the selected configuration file;
you can use Visual Studio Code's undo/redo feature if needed.
