Configuration elements defined in a configuration file are grouped
by type; each element type has a specific section in the
"Taipy Configs" panel.

## Data Nodes configuration

The "Data Nodes" section list all the Data Node configuration defined in the selected
configuration file.

### Creating a new Data Node configuration

Press the '+' sign in the Data Node section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Data Node configuration
element.<br/>
Note that you cannot set the identifier of a new Data Node element to one
already used by another.

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

### Locate in the Graph View

If a [Graph View](graphview.md) is active,
you add a specific Data Node configuration element to that view by selecting
the "Add/Show in active View" menu option that pops when you right-click the
relevant element identifier.

If that Data Node configuration element is already present in the Graph View,
then the view is panned so you can spot it easily.

### Properties

The "Details" section will let you:

- Change the Data Node configuration identifier.
- Specify the storage type property.
- Specify the scope property.
- Add Data Node-specific properties and values that Taipy Core can use.

## Tasks configuration

The "Tasks" section list all the Task configuration elements defined in the selected
configuration file.

### Creating a new Task configuration

Press the '+' sign in the Task section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Task configuration
element.<br/>
Note that you cannot set the identifier of a new Task element to one
already used by another.

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

### Locate in the Graph View

If a [Graph View](graphview.md) is active,
you add a specific Task configuration element to that view by selecting
the "Add/Show in active View" menu option that pops when you right-click the
relevant element identifier.<br/>
Note that adding the Task configuration element to the Graph View also
adds the dependent Data Node configuration elements that it depends on.

If that Task configuration element is already present in the Graph View,
then the view is panned so you can spot it easily.

### Properties

The "Details" section will let you:

- Change the Task configuration identifier.
- Change the input and output Data Nodes used by this Task configuration.<br/>
    You can pick the Data Node configurations from the list of
    configured Data Nodes in the selected configuration file.
- Specify the function used by this Task configuration.<br/>
    You will select the module to locate the function, then the function
    itself.<br/>
    Note that if you right-click the function name in the Details section,
    you can select the "Show Source" menu option. This opens an editor showing
    the source code at the location where the function is defined.
- Specify whether this Task configuration is *skippable* or not.

## Pipelines configuration

The "Pipelines" section list all the Pipeline configuration elements defined in the selected
configuration file.

### Creating a new Pipeline configuration

Press the '+' sign in the Pipelines section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Pipeline configuration
element.<br/>
Note that you cannot set the identifier of a new Pipeline element to one
already used by another.

### Renaming a Pipeline configuration

Right-click a Pipeline identifier in the Pipelines section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Pipeline element to one
already used by another.

The new name of a Pipeline element is propagated to the Scenario configurations
that reference it.

### Deleting a Pipeline configuration

Right-click a Pipeline identifier in the Pipelines section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Showing in a Graph View

Right-click a Pipeline identifier in the Pipelines section and select the
"Show View" option.<br/>
Taipy Studio will create a [Graph View](graphview.md) that represents
the Pipeline configuration element you selected.

### Locate in the Graph View

If a [Graph View](graphview.md) is active,
you add a specific Pipeline configuration element to that view by selecting
the "Add/Show in active View" menu option that pops when you right-click the
relevant element identifier.<br/>
Note that adding the Pipeline configuration element to the Graph View does
not create any link between elements. All you get is a visual representation
of the Pipeline configuration.

If that Pipeline configuration element is already present in the Graph View,
then the view is panned so you can spot it easily.

### Properties

The "Details" section will let you:

- Change the Pipeline configuration identifier.
- Change the Tasks used by this Pipeline configuration.<br/>
    You can pick the Task configurations from the list of configured
    Tasks in the selected configuration file.

## Scenarios configuration

The "Scenarios" section list all the Scenario configuration elements defined in the selected
configuration file.

### Creating a new Scenario configuration

Press the '+' sign in the Scenarios section of the "Taipy Configs" panel.<br/>
Taipy Studio will prompt you for an identifier for this new Scenario configuration
element.<br/>
Note that you cannot set the identifier of a new Scenario element to one
already used by another.

### Renaming a Scenario configuration

Right-click a Scenario identifier in the Scenarios section and select the
"Rename node" option.<br/>
Note that you cannot set the new identifier of a Scenario element to one
already used by another.

### Deleting a Scenario configuration

Right-click a Scenario identifier in the Scenarios section and select the
"Delete node from configuration" option.<br/>
Taipy Studio will prompt you to confirm you really want to remove that
element from the configuration file.

### Showing in a Graph View

Right-click a Scenario identifier in the Scenarios section and select the
"Show View" option.<br/>
Taipy Studio will create a [Graph View](graphview.md) that represents
the Scenario configuration element you selected.

The Graph View will represent all the Pipeline configuration elements
referenced by this Scenario configuration and all the dependent
Task and Data Node configuration elements.

### Properties

The "Details" section will let you:

- Change the Scenario configuration identifier.
- Change the Pipelines used by this Scenario configuration.<br/>
    You can pick the Pipeline configurations from the list of
    configured Pipelines in the selected configuration file.
- Specify the frequency used by this Scenario configuration.
- Specify comparator functions used by this Scenario configuration.
