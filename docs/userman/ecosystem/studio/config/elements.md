Configuration elements defined in a configuration file are grouped
by type; each element type has a specific section in the
**Taipy Configs** panel.

## Data Nodes configuration

The **Data Nodes** section list all the Data Node configuration defined in the selected
configuration file.

### Creating a new Data Node configuration

Press the '+' sign that appears when you hover the title of the **Data Nodes** section of
the **Taipy Configs** panel.<br/>
Taipy Studio will prompt you for an identifier for this new Data Node configuration
element.<br/>
Note that you cannot set the identifier of a new Data Node element to one
already used by another.

Default values are provided for the essential properties of the new Data Node configuration
element: *storage_type* is set to "pickle", and *scope* is set to "SCENARIO:SCOPE".<br/>
The properties for the new element are displayed in the DETAILS section of the
**Taipy Configs** panel.

### Renaming a Data Node configuration

Right-click a Data Node identifier in the **Data Nodes** section and select the "Rename"
option.<br/>
Note that you cannot set the new identifier of a Data Node element to one that is already used by
another Data Node element.

The new name of a Data Node element is propagated to the Task configurations that reference it.

### Deleting a Data Node configuration

Right-click a Data Node identifier in the Data Node section and select the
"Delete from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Locate in the Graph View

If a [Graph View](graphview.md) is active and showing a Scenario configuration,
you add a specific Data Node configuration element to that view by selecting
the "Add/Show in active View" menu option that pops when you right-click the
relevant element identifier.

If that Data Node configuration element is already present in the Graph View,
the view is panned so you can spot it easily.

### Properties

The **Details** section will let you:

- Change the Data Node configuration identifier.
- Specify the storage type property.
- Specify the scope property.
- Add Data Node-specific properties and values that Taipy can use.

## Tasks configuration

The **Tasks** section lists all the Task configuration elements defined in the selected
configuration file.

### Creating a new Task configuration

Press the '+' sign that appears when you hover the title of the **Tasks** section of the
**Taipy Configs** panel.<br/>
Taipy Studio will prompt you for an identifier for this new Task configuration
element.<br/>
Note that you cannot set the identifier of a new Task element to one
already used by another.

Default values are provided for the essential properties of the new Task configuration
element: *inputs* and *outputs* are set to an empty list, and *skippable* is set to
"False:bool".<br/>
The properties for the new element are displayed in the DETAILS section of the
"Taipy Configs" panel.

### Renaming a Task configuration

Right-click a Task identifier in the **Tasks** section and select the "Rename" option.<br/>
Note that you cannot set the new identifier of a Task element to one that is already used by
another Task element.

The new name of a Task element is propagated to the Scenario configurations that reference it.

### Deleting a Task configuration

Right-click a Task element identifier in the **Tasks** section and select the
"Delete from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Locate in the Graph View

If a [Graph View](graphview.md) is active and showing a Scenario configuration,
you add a specific Task configuration element to that view by selecting
the "Add/Show in active View" menu option that pops when you right-click the
relevant element identifier.<br/>
Note that adding the Task configuration element to the Graph View also
adds the dependent Data Node configuration elements it depends on.

If that Task configuration element is already present in the Graph View,
then the view is panned so you can spot the Task element easily.

### Properties

The **Details** section will let you:

- Change the Task configuration identifier.
- Change the input and output Data Nodes used by this Task configuration.<br/>
    You can pick the Data Node configurations from the list of
    configured Data Nodes in the selected configuration file.
- Specify the function used by this Task configuration.<br/>
    You will select the module to locate the function, then the name of the function
    itself.<br/>
    If you right-click the function name in the **Details** section,
    you can select the "Show Source" menu option. This opens an editor showing
    the source code at the location where the function is defined.
- Specify whether this Task configuration is *skippable* or not.

## Scenarios configuration

The **Scenarios** section lists all the Scenario configuration elements defined in the selected
configuration file.

If a Scenario configuration element contains one or more sequences, its node can be expanded to
reveal the Sequence elements the Scenario configuration defines.

### Creating a new Scenario configuration

Press the '+' sign that appears when you hover the title of the **Scenarios** section of
the **Taipy Configs** panel.<br/>
Taipy Studio will prompt you for an identifier for this new Scenario configuration
element.<br/>
Note that you cannot set the identifier of a new Scenario element to one
already used by another.

Default values are provided for the essential properties of the new Scenario configuration
element: *sequences* is set to an empty list.<br/>
The properties for the new element are displayed in the DETAILS section of the
"Taipy Configs" panel.

### Renaming a Scenario configuration

Right-click a Scenario identifier in the **Scenarios** section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Scenario element to one
already used by another.

### Deleting a Scenario configuration

Right-click a Scenario identifier in the **Scenarios** section and select the
"Delete from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Showing in a Graph View

Right-click a Scenario identifier in the **Scenarios** section and select the
"Show View" option.<br/>
Taipy Studio will create a [Graph View](graphview.md) representing the selected Scenario
configuration element.

The Graph View will represent all the configuration elements referenced by this Scenario
configuration (all the dependent Task and Data Node configuration elements).

### Adding a sequence

Press the '+' sign that appears next to a **Scenario** configuration name in the **Scenarios**
section of the **Taipy Configs** panel.<br/>
Taipy Studio will prompt you for an identifier for a new sequence in this Scenario configuration
element.<br/>
Note that you cannot set the identifier of a sequence to one already used in this Scenario
configuration element.

### Renaming a sequence

Right-click a Sequence identifier in the list of child nodes of a Scenario element in the
**Scenarios** section and select the "Rename" option.<br/>
Note that you cannot set the new identifier of a sequence to one that is already used by the
selected Scenario configuration element.

### Deleting a sequence

Right-click a Sequence identifier in the list of child nodes of a Scenario element in the
**Scenarios** section and select the "Delete from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Properties

If a Scenario configuration element is selected in the **Scenarios** section, the **Details**
section displays the details of that Scenario element and lets you:

- Change the identifier of the Scenario configuration element.
- Change the Tasks used by this Scenario configuration.<br/>
    Selecting the value of the *tasks* field will prompt you to select the Tasks configuration
    elements you want to reference from the Scenario configuration element.

If a sequence of a Scenario configuration element is selected in the **Scenarios** section, the
**Details** section displays the details of that sequence and lets you:

- Change the sequence identifier.
- Change the Tasks used by this sequence.


