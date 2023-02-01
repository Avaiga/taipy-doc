# Building configurations

Applications that rely on [Taipy Core](../core/index.md) need to define
a [Configuration](../core/config/index.md) where the data flow is
described.<br/>
This configuration can be coded in Python and tuned using environment variables
(as described in the
[advanced configuration](../core/config/advanced-config.md#Python-code-configuration)
section).

Taipy Studio provides ways to design graphically the configuration for your applications.
Within the Visual Studio Code environment, you can create configuration elements (for
Data Nodes, Tasks, Pipelines, and Scenarios), specify the properties for those elements,
and use a visual representation of those configuration elements as a graph.

<p align="center">
  <img src="../images/config_overview.png" width=75%>
</p>

Taipy Studio stores those configuration in TOML files. These files can be used at
runtime by Taipy applications as described in the
[note on Studio](../core/config/advanced-config.md#studio).

## Introduction

Taipy Studio has a dedicated panel called "Taipy Configs" where mostly everything
happens. To open this panel, use the "View > Open View..." menu option and search
for the view called "Taipy Configs".

The view appears like this:

<p align="center">
  <img src="../images/config_panel.png" width=30%>
</p>

This panel is split into several sections that let the user access all the
configuration elements:

- Config Files: holds a list of configuration files (`*.toml`) that exist in the
    project.<br/>
    The user can select a configuration file in this list to populate the other
    sections of the Taipy Configs view.
- Data Notes: holds the list of
    [Data Node configurations](../core/config/data-node-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Data Node configuration in this list, to access all its
    properties in the Details section (see below).
- Tasks: holds the list of
    [Task configurations](../core/config/task-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Task configuration in this list to access all its
    properties in the Details section (see below).
- Pipelines: holds the list of 
    [Pipeline configurations](../core/config/pipeline-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Pipeline configuration in this list to access all its
    properties in the Details section (see below).
- Scenarios: holds the list of 
    [Scenario configurations](../core/config/scenario-config.md) defined
    in the selected configuration file.<br/>
    The user can select a Scenario configuration in this list to access all its
    properties in the Details section (see below).
- Details: When a configuration element is selected, the Details section displays
    all the properties of this configuration element and allows the user to
    modify these properties.

Using these different sections, you can add, rename or remove configuration
elements, as well as change their properties in the "Details" section.

All your actions impact the selected configuration file;
you can use Visual Studio Code's undo/redo feature if needed.

## Managing configuration files

The "Config Files" section holds the list of configuration files (`*.toml`) in your
project. You will select the one you want to edit from that list.<br/>
This list shows the base names of all the configuration files. If two configuration files
have the same name (but are located in two different directories), the path to the directory
where these files belong will be displayed next to the base file name to avoid
confusion.

Because the "Config Files" list is synchronized with the files included in your project,
adding a configuration file is simply a matter of creating it from the Visual Studio
Code Explorer panel:

<p align="center">
  <img src="../images/config_init.gif" width=80%>
</p>

Similarly, if you remove or rename a configuration file from the Explorer panel of Visual
Studio Code, the change is immediately reflected in the Config Files section of the
Taipy Configs panel.

Note that if you right-click a configuration file, Taipy Studio displays a menu that
let you choose one of two options:

- "Reveal file in explorer view": Visual Studio Code will select and focus on the file
    item in the project's files in the Explorer pane.
- "Show view": creates a view on the configuration file that represents the entire content
    of the configuration file as a [global graph](#the-graph-view), so you can see
    all the configuration elements and how they relate to each other.

## Configuring Data Nodes

The "Data Nodes" section list all the Data Node configuration defined in the selected
configuration file.

### Creating a new Data Node configuration

Press the '+' sign in the Data Node section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Data Node configuration
element.<br/>
Note that you cannot set the identifier of a new Data Node element to one
that is already used by another Data Node element.

### Renaming a Data Node configuration

Right-click a Data Node identifier in the Data Node section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Data Node element to one
that is already used by another Data Node element.

The new name of a Data Node element is propagated to the Task configurations
that reference it.

### Deleting a Data Node configuration

Right-click a Data Node identifier in the Data Node section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Properties

The "Details" section will let you:

- Change the Data Node configuration identifier.
- Specify the storage type property.
- Specify the scope property.
- Add Data Node-specific properties and their values, that Taipy Core can use.

## Configuring Tasks

The "Tasks" section list all the Task configuration elements defined in the selected
configuration file.

### Creating a new Task configuration

Press the '+' sign in the Task section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Task configuration
element.<br/>
Note that you cannot set the identifier of a new Task element to one
that is already used by another Task element.

### Renaming a Task configuration

Right-click a Task identifier in the Tasks section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Task element to one
that is already used by another Task element.

The new name of a Task element is propagated to the Pipeline configurations
that reference it.

### Deleting a Task configuration

Right-click a Task identifier in the Tasks section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Properties

The "Details" section will let you:

- Change the Task configuration identifier.
- Change the input and output Data Nodes used by this Task configuration.<br/>
    You will be able to pick the Data Node configurations from the list of
    configured Data Nodes in the selected configuration file.
- Specify the function used by this Task configuration.<br/>
    You will select the module to locate the function in, then the function
    itself.
- Specify whether this Task configuration is skippable or not.

## Configuring Pipelines

The "Pipelines" section list all the Pipeline configuration elements defined in the selected
configuration file.

### Creating a new Pipeline configuration

Press the '+' sign in the Pipelines section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Pipeline configuration
element.<br/>
Note that you cannot set the identifier of a new Pipeline element to one
that is already used by another Pipeline element.

### Renaming a Pipeline configuration

Right-click a Pipeline identifier in the Pipelines section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Pipeline element to one
that is already used by another Pipeline element.

The new name of a Pipeline element is propagated to the Scenario configurations
that reference it.

### Deleting a Pipeline configuration

Right-click a Pipeline identifier in the Pipelines section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Properties

The "Details" section will let you:

- Change the Pipeline configuration identifier.
- Change the Tasks used by this Pipeline configuration.<br/>
    You will be able to pick the Task configurations from the list of configured
    Tasks in the selected configuration file.

## Configuring Scenarios

The "Scenarios" section list all the Scenario configuration elements defined in the selected
configuration file.

### Creating a new Scenario configuration

Press the '+' sign in the Scenarios section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Scenario configuration
element.<br/>
Note that you cannot set the identifier of a new Scenario element to one
that is already used by another Scenario element.

### Renaming a Scenario configuration

Right-click a Scenario identifier in the Scenarios section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Scenario element to one
that is already used by another Scenario element.

### Deleting a Scenario configuration

Right-click a Scenario identifier in the Scenarios section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Properties

The "Details" section will let you:

- Change the Scenario configuration identifier.
- Change the Pipelines used by this Scenario configuration.<br/>
    You will be able to pick the Pipeline configurations from the list of
    configured Pipelines in the selected configuration file.
- Specify the frequency used by this Scenario configuration.
- Specify comparator functions used by this Scenario configuration.

## The graph view

## Text edition of the configuration file

A configuration file is a standard text file, with a '`.toml`' extension. Visual Studio
Code lets you edit it manually, as any other text file.<br/>
However, Taipy Studio provides some support for identifying problems in configuration
files and accelerating typing thanks to auto-completion features.

### Auto-completion

If you are entering text in a configuration section ([DATA_NODE.*id*], [TASK.*id*], etc.),
you can press the `Ctrl-<SPACE>` key combination, then Taipy Studio will suggest relevant
fragments that would prevent you from typing them entirely.

Those suggestions include property names and values, as demonstrated in the following animation,
showing how we could create a new Data Node configuration in the body of a configuration file:


<p align="center">
  <img src="../images/config_autocomplete.gif" width=80%>
</p>

You will also get support for auto-completion in other contexts, such as a reference
to another configuration element.

### Spotting problems

Taipy Studio helps point out potential problems in your configuration files that are
indicated in the body of the file content, in the Problems pane, and in the "Details"
section of the "Taipy Configs" pane.

<p align="center">
  <img src="../images/config_diagnostics.png" width=75%>
</p>

Here are the problems that Taipy Studio identifies:

- "No reference to element 'XXX'." (Warning)<br/>
    The configuration element (Data Node, Task, or Pipeline) is not referenced
    by any other element.
- "Element 'XXX' does not exist." (Error)<br/>
    A configuration element identifier that does not exist is referenced by this
    configuration element (Data Node, Task, Pipeline, or Scenario).
- "Cannot find Python function: 'XXX'." (Error)<br/>
    A function name that does not exist is used in this Task configuration element.<br/>
    A Quick Fix can create that function for you.

