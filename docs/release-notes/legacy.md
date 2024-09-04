---
title: Release Notes for Legacy Taipy versions
---

This is the list of changes to legacy major Taipy releases as they were published.

The Release Notes for the latest major version of Taipy can be found in
[this page](index.md).

!!! note "Unsupported released versions"

    Only the current and previous major versions of Taipy are supported.

    Therefore, since Taipy 4.0 was shipped, we no longer provide support for Taipy 1.x and 2.x. We
    accordingly removed the documentation for the legacy Taipy versions from public access.

# Community edition: 3.1

Published on 2024-03.

[`taipy` 3.1](https://pypi.org/project/taipy/3.1.1/) contains the latest
[`taipy-config` 3.1](https://pypi.org/project/taipy-config/3.1.1/),
[`taipy-gui` 3.1](https://pypi.org/project/taipy-gui/3.1.1/),
[`taipy-core` 3.1](https://pypi.org/project/taipy-core/3.1.1/),
[`taipy-templates` 3.1](https://pypi.org/project/taipy-templates/3.1.1/), and
[`taipy-rest` 3.1](https://pypi.org/project/taipy-rest/3.1.1/) packages.


## New Features

<h4><strong><code>taipy</code></strong> 3.1.0</h4>

- Taipy and all its dependencies now support Python 3.12.<br/>
  See [Python documentation](https://docs.python.org/3/whatsnew/3.12.html) for details.

<h4><strong><code>taipy-gui</code></strong> 3.1.0</h4>

- The [`chart`](../refmans/gui/viselements/generic/chart.md) control has a new property called *figure* that
  expects an instance of `plotly.graph_objects.Figure`. This class is provided by the
[Plotly Open Source Graphing Library for Python](https://plotly.com/python/) so you can create
  all sorts of graphs in Python.<br/>
  See the [`figure` property](../refmans/gui/viselements/generic/chart.md#p-figure) of the `chart` control and
  the [section on the *figure* property](../refmans/gui/viselements/generic/chart.md#the-figure-property) for
  more information.
- The [`part`](../refmans/gui/viselements/generic/part.md) block has a new property called *content* that
  lets developers integrate any third-party library that can generate HTML.<br/>
  See the documentation for the [`part`](../refmans/gui/viselements/generic/part.md) block and the examples
  using *content providers* for more information.
- A new control called [`date_range`](../refmans/gui/viselements/generic/date_range.md) is available if
  you need to represent and edit date ranges in your application pages.
- A new control called [`login`](../refmans/gui/viselements/generic/login.md) is available if you need users
  to authenticate in your application.

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- The `DataNode.filter()^` method and the indexing/filtering style now also support filtering a
  Numpy array, a list of objects, and a list of dictionaries.<br/>
  For more information, please refer to
  [Filter a data node](../userman/scenario_features/data-integration/data-node-usage.md#filter).
- You can now append new data to a data node using the `DataNode.append()^` method. The method is
  available for `CSVDataNode`, `ExcelDataNode`, `JSONDataNode`, `ParquetDataNode`, `SQLDataNode`,
  `SQLTableDataNode`, and `MongoCollectionDataNode`.<br/>
  For more information, please refer to
  [Append a data node](../userman/scenario_features/data-integration/data-node-usage.md#append).
- A new class called `Submission^` holds meta-data (such as its status or
  submission date) related to a submitted entity: `Scenario^`, `Sequence^`, and/or `Task^`.<br/>
  The function `taipy.get_latest_submission()^` returns the last submission of a given entity.<br/>
  For more information, please refer to
  [Submission](../userman/scenario_features/sdm/submission/index.md).
- `taipy.submit()^`, `Scenario.submit()^`, `Sequence.submit()^`, and `Task.submit()^` now return a
  `Submission^` entity.
- A new predefined data node named `S3ObjectDataNode^` has been implemented.<br/>
  For more information, please refer to
  [S3ObjectDataNode](../userman/scenario_features/data-integration/data-node-config.md#amazon-web-service-s3-object).

## Improvements and changes

<h4><strong><code>taipy</code></strong> 3.1.0</h4>

- Task nodes in the [`scenario_dag`](../refmans/gui/viselements/corelements/scenario_dag.md) control dynamically
  reflect the status of related jobs for the user that submitted scenarios or sequences.
- The [`scenario`](../refmans/gui/viselements/corelements/scenario.md) control lets you add, modify, and edit
  sequences.
- The [`data_node`](../refmans/gui/viselements/corelements/data_node.md) control can now represent collections.

<h4><strong><code>taipy-gui</code></strong> 3.1.0</h4>

- The [`table`](../refmans/gui/viselements/generic/table.md) control supports enumerated values. That allows
  for a better user experience when users edit cell values.<br/>
  See the
  [section on enumerated values in tables](../refmans/gui/viselements/generic/table.md#enumerated-values) for
  the details.
- The [`toggle`](../refmans/gui/viselements/generic/toggle.md) control appears as a switch button if its
  [*value*](../refmans/gui/viselements/generic/toggle.md#p-value) property holds a Boolean value.

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- The `modin` exposed type as been deprecated. When used, a fallback on Pandas is applied.<br/>
  See [issue #631](https://github.com/Avaiga/taipy/issues/631) for details.
- Running twice the Orchestrator service raises an exception to prevent running multiple instances
  at the same time.
- Running the Orchestrator service or creating an entity by `taipy.create_scenario()` or
  `taipy.create_global_data_node()` blocks the Configuration from being modified.

## Significant bug fixes

<h4><strong><code>taipy</code></strong></h4>

<h5>3.1.1</h5>

- Data is not shown or not automatically refreshed in
  [Data Node viewer](../refmans/gui/viselements/corelements/data_node.md).<br/>
  See [issue #908](https://github.com/Avaiga/taipy/issues/908) and
  [issue #950](https://github.com/Avaiga/taipy/issues/950).
- Data Nodes holding dates may not show in
  [Data Node viewers](../refmans/gui/viselements/corelements/data_node.md).<br/>
  See [issue #1043](https://github.com/Avaiga/taipy/issues/1043).

<h4><strong><code>taipy-gui</code></strong></h4>

<h5>3.1.0</h5>

- Selectors with dropdown menus cannot be deactivated.<br/>
  See [issue #894](https://github.com/Avaiga/taipy/issues/894).
- Problems scoping non-global variables used in Partials.<br/>
  See [issue #561](https://github.com/Avaiga/taipy/issues/561).
- Important error messages are mangled.<br/>
  See [issue #560](https://github.com/Avaiga/taipy/issues/560).

<h4><strong><code>taipy-core</code></strong></h4>

<h5>3.1.1</h5>

- The signatures for `Config.configure_sql_data_node()`, `Config.configure_s3_object_data_node()`, and
  `configure_core()` methods are out-of-date.<br/>
  See [issue #1014](https://github.com/Avaiga/taipy/issues/1014).

# Enterprise edition: 3.1

Published on 2024-03.

This release contains all of [`taipy` 3.1](https://pypi.org/project/taipy/3.1.0) as well as
additional features.

## New Features

- A new job execution mode named *cluster mode* is available. It enables to run the jobs
  on a cluster of dedicated machines in a remote, distributed and scalable environment.

# Community edition: 3.0

Published on 2023-10.

!!! warning Error([#1180](https://github.com/Avaiga/taipy/issues/1180)) when downgrading from Taipy 3.1 to Taipy 3.0

    If you are experiencing an error downgrading to Taipy 3.0, please
    reinstall Taipy with options `--no-cache-dir -I` like so:
      `pip install --no-cache-dir -I taipy==3.0.0`

## New Features

<h4><strong><code>taipy</code></strong> 3.0.0</h4>

- Taipy application can now be run with the Taipy command-line interface (CLI) using the
  `taipy run` command. For more information, refer to
  [Run application in Taipy CLI](../userman/ecosystem/cli/run.md).

<h4><strong><code>taipy-gui</code></strong> 3.0.0</h4>

- A new package holds the [*Page Builder API*](../userman/gui/pages/builder.md): a set of classes that
  let you define the pages for your application entirely with Python.
- You can now update variables on all clients using the *shared variables* concept. See
  the `Gui.add_shared_variable()^` and `State.dispatch()^` methods for details.
- You can now invoke a callback for all clients using the `broadcast_callback()^` function.
- The [`slider`](../refmans/gui/viselements/generic/slider.md) control can now handle several knobs,
  allowing for range selection.<br/>
  Please check the [example](../refmans/gui/viselements/generic/slider.md#multi-selection) for more
  information.
- The [`file_download`](../refmans/gui/viselements/generic/file_download.md) control now lets developers
  generate the file content dynamically, at download time.<br/>
  Please check the [example](../refmans/gui/viselements/generic/file_download.md#dynamic-content) for more information.
- A new CSS class called *toggle-navbar* was added to the
  [Stylekit](../userman/gui/styling/stylekit.md) to give a
  [`toggle`](../refmans/gui/viselements/generic/toggle.md) control the aspect of a
  [`navbar`](../refmans/gui/viselements/generic/navbar.md).
- The [`chart`](../refmans/gui/viselements/generic/chart.md) control now supports the
  [*treemap*](../refmans/gui/viselements/generic/charts/treemap.md) and
  [*waterfall*](../refmans/gui/viselements/generic/charts/waterfall.md) chart types.

<h4><strong><code>taipy-core</code></strong> 3.0.0</h4>

- A production version of a Taipy application can now be provided with **migration functions** to
  automatically migrate entities and keep them compatible with previous versions.<br/>
  For more information, refer to [Production mode](../userman/advanced_features/versioning/production_mode.md).
- A `GLOBAL` scope data node can be created from a data node configuration calling
  the new `taipy.create_global_data_node()^` method.<br/>
  For more information, refer to
  [Create a data node](../userman/scenario_features/data-integration/data-node-usage.md#create-a-data-node).
- A data node configuration can be built from an existing data node configuration.
  For more information, refer to the documentation page on
  [data node configuration](../userman/scenario_features/data-integration/data-node-config.md#configure-a-data-node-from-another-configuration).
- A new class `Submittable^` models entities that can be submitted for execution.
  It is an Abstract class instantiated by `Scenario^` and `Sequence^`.
  It can be handy to use the new following `Submittable^` methods:
    * `Submittable.get_inputs()^` retrieves input data nodes of a `Submittable` entity;
    * `Submittable.get_outputs()^` retrieves output data nodes of a `Submittable` entity;
    * `Submittable.get_intermediate()^` retrieves intermediate data nodes of a `Submittable`
        entity;
    * `Submittable.is_ready_to_run()^` checks if an entity is ready to be run;
    * `Submittable.data_nodes_being_edited()^` retrieves data nodes that are being edited
        of a `Submittable^` entity.
- New functions exposed by the `taipy` module:
    * `taipy.is_deletable()^` checks if an entity can be deleted;
    * `taipy.exists()^` checks if an entity exists.
- The encoding type of CSVDataNode and JSONDataNode can now be configured using the
  *encoding* parameter. For more information, please refer to
  [Configure a CSVDataNode](../userman/scenario_features/data-integration/data-node-config.md#csv)
  and [Configure a JSONDataNode](../userman/scenario_features/data-integration/data-node-config.md#json)
  sections.

<h4><strong><code>taipy-template</code></strong> 3.0.0</h4>

- A new template named "scenario-management" is available. For more information on creating
  a new Taipy application with the new "scenario-management" template, refer to the
  documentation page on [templates](../userman/ecosystem/cli/create.md#from-a-specific-application-template).

## Improvements and changes

<h4><strong><code>taipy-gui</code></strong> 3.0.0</h4>

- :warning: The *action* parameter of the `on_action` callback was removed for every control.<br/>
    The signature of all *on_action()* callback functions are now unified to the following:
    - *state* (`State^`): the state of the client invoking that callback;
    - *id* (str): the identifier of the visual element that triggers that callback;
    - *payload* (dict): a dictionary that provides additional information to the callback.<br/>
      This dictionary now has the additional *action* key that is set to the action name.
      This change not only impact the *on_action* callback of all controls that support it,
      but in an exactly similar manner the following callback signatures:
        - *on_range_change* in the [`chart`](../refmans/gui/viselements/generic/chart.md) control;
        - *on_edit*, *on_add*, and *on_delete* in the [`table`](../refmans/gui/viselements/generic/table.md)
          control;
        - *on_close* in the [`pane`](../refmans/gui/viselements/generic/pane.md) block.
- The `navigate()^` function has an additional parameter *params* that is used to add query
  parameters to the requested URL. The query parameters can be retrieved in the `on_navigate`
  callback.
- The *on_action* parameter of the `download()^` function can be a function and not just a function
  name.
- Setting the *debug* parameter of `Gui.run()^` to True provides stack traces to be shown in the
  console when exceptions occur in user code.

<h4><strong><code>taipy-core</code></strong> 3.0.0</h4>

- :warning: A `ScenarioConfig^` graph is now created directly from `TaskConfig^` and
  `DataNodeConfig^`. Consequently, `PipelineConfig` has been removed. For more
  information, refer to [Configure a scenario](../userman/scenario_features/sdm/scenario/scenario-config.md).
- :warning: The `Pipeline` object has been removed and replaced by `Sequence^`. A sequence is
  held by a `Scenario^` and represents a subset of its tasks than can be submitted
  together independently of the other tasks of the scenario. For more information,
  refer to `Scenario.add_sequence()^` and `Scenario.remove_sequence()^`.
- `Scope.PIPELINE` has been removed from possible `Scope^` values.
- The `root_folder`, `storage_folder`, `read_entity_retry`, `repository_type`, and
  `repository_properties` attributes of the `GlobalAppConfig^` have been moved to the
  `CoreSection^`.<br/>
  Please refer to the [Core configuration page](../userman/advanced_features/configuration/core-config.md)
  for details.
- The `clean_entities` attribute has been removed from the `CoreSection^`. Correspondingly, the
  `--clean-entities` option has been removed from the version management CLI.<br/>
  To clean entities of a version, please run your application in development mode, or delete your
  version with the `--delete` CLI option. For more information, refer to
  [Taipy command-line interface](../userman/ecosystem/cli/index.md)
- The deprecated `nb_of_workers` attribute of the JobConfig has been removed.
- The deprecated `parent_id` attribute of a DataNode, Task, Pipeline, or Scenario entity, has
  been removed.
- The deprecated `last_edition_date` and `edition_in_progress` attributes of a DataNode entity
  have been removed.
- The deprecated `DataNode.lock_edition()` and `DataNode.unlock_edition()` methods have been
  removed.
- The deprecated `taipy.create_pipeline()` method has been removed.
- Function `DataNode.track_edit` has been made public.

<h4><strong><code>taipy-template</code></strong> 3.0.0</h4>

- The default template also supports creating a multi-pages application with Orchestrator and Rest
  services. These options are available when creating a new application from the template.
- The "multi-page-gui" template has been removed. Please use the default instead to create
  a Taipy multi-pages application.

## Significant bug fixes

<h4><strong><code>taipy-gui</code></strong> 3.0.0</h4>

- The callback function set to the *on_action* parameter of the function `download()^` may
  be called too early. It is now ensured to be invoked *after* the download operation is
  performed.<br/>
  See [issue #916](https://github.com/Avaiga/taipy-gui/issues/916).
- Setting the [*properties*](../userman/gui/viselements/introduction.md#generic-properties) property of
  a visual element as the returned value from a function may not succeed.</br>
  See [issue #897](https://github.com/Avaiga/taipy-gui/issues/897).
- Variables imported by an `import *` directive are not handled properly in the state of
  a callback defined in the importing module.</br>
  See [issue #908](https://github.com/Avaiga/taipy-gui/issues/908).
- The [`date`](../refmans/gui/viselements/generic/date.md) control does not use the *format* property if
  *with_time* is not set.<br/>
  See [issue #909](https://github.com/Avaiga/taipy-gui/issues/909).
- The [`date`](../refmans/gui/viselements/generic/date.md) control uses the `datetime.date` type and does
  not apply time zones if time is not involved.<br/>
  See [issue #895](https://github.com/Avaiga/taipy-gui/issues/895) and
  [issue #923](https://github.com/Avaiga/taipy-gui/issues/923).
- Updating a [`chart`](../refmans/gui/viselements/generic/chart.md) control data may cause data congestion
  or display flickering.<br/>
  See [issue #864](https://github.com/Avaiga/taipy-gui/issues/864) and
  [issue #932](https://github.com/Avaiga/taipy-gui/issues/932).
- Selection in a [`chart`](../refmans/gui/viselements/generic/chart.md) with type *pie* type is not
  properly handled.<br/>
  See [issue #919](https://github.com/Avaiga/taipy-gui/issues/919).
- Hover text doesn't show properly in a [`selector`](../refmans/gui/viselements/generic/selector.md) that
  is crowded.<br/>
  See [issue #927](https://github.com/Avaiga/taipy-gui/issues/927).
- Options with a long text in a [`selector`](../refmans/gui/viselements/generic/selector.md) cannot cbe
  deselected.<br/>
  See [issue #917](https://github.com/Avaiga/taipy-gui/issues/917).
- The [`table`](../refmans/gui/viselements/generic/toggle.md) control does not support undefined date values
    from Pandas data frames.<br/>
    See [issue #886](https://github.com/Avaiga/taipy-gui/issues/886).

<h4><strong><code>taipy-core</code></strong> 3.0.0</h4>

- When running the Orchestrator service in development mode, changing the name of the function used by a
  task then running the application again would raise an error.<br/>
  See [issue #743](https://github.com/Avaiga/taipy-core/issues/743).

# Enterprise edition: 3.0

Published on 2023-10.

This release contains all of [`taipy` 3.0](https://pypi.org/project/taipy/3.0.0) as well as
additional features.

## New Features

- Python functions including scenario management methods can be scheduled to run at a specific
  time using the new `taipy.Scheduler^` API. For more information, refer to
  [Schedule a method](../userman/advanced_features/scheduling/index.md).

## Improvements and changes

- The job recovery mechanism is now only available when the Orchestrator service is run.

# Community edition: 2.3

Published on 2023-06.

[`taipy` 2.3](https://pypi.org/project/taipy/2.3.0/) contains the latest
[`taipy-config` 2.3](https://pypi.org/project/taipy-config/2.3.0/),
[`taipy-gui` 2.3](https://pypi.org/project/taipy-gui/2.3.0/),
[`taipy-core` 2.3](https://pypi.org/project/taipy-core/2.3.0/) and
[`taipy-rest` 2.3](https://pypi.org/project/taipy-rest/2.3.0/) packages.

## New Features

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
2.3.0

- Scenario and Data Management Controls<br/>
  Taipy comes, in the [`taipy`](https://pypi.org/project/taipy/) package, with a set of
  ready-to-use GUI controls that connect to entities created by Taipy. Your application
  can then visualize the Taipy entities related to Scenario and Data Management and
  interact with them.<br/>
  Please check the
  [list of Scenario and Data Management controls](../refmans/gui/viselements/index.md#scenario-and-data-management-controls).
- New Taipy command-line interface (CLI). Please refer to the
  [Taipy command-line interface](../userman/ecosystem/cli/index.md) documentation page for more information.
- Users can now create a new Taipy application from a template by running `$ taipy create` from the
  CLI. Besides the default template, "multi-page-gui" template can be chosen with the optional
  `--template` option.

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.3.0

- The [`table`](../refmans/gui/viselements/generic/table.md) and
- [`chart`](../refmans/gui/viselements/generic/chart.md)
  controls have a new property called *rebuild* that allows for modifying the control configuration
  at runtime, using properties that are *not* dynamic.<br/>
  See the details in the specific documentation sections for
  [tables](../refmans/gui/viselements/generic/table.md#the-rebuild-property) and
  [charts](../refmans/gui/viselements/generic/chart.md#the-rebuild-property).
- The [`part` block](../refmans/gui/viselements/generic/part.md) now accepts any URL as a value for the
  [*page* property](../refmans/gui/viselements/generic/part.md#p-page). You can then integrate any external
  web page as demonstrated in [this example](../refmans/gui/viselements/generic/part.md#part-showing-a-page).
  <br/>
  To better control the layout of external pages, a new
  [*height* property](../refmans/gui/viselements/generic/part.md#p-height) has been added to the
  [`part`](../refmans/gui/viselements/generic/part.md) element.
- The `navigate()^` function has an additional parameter called *force* that, when set to True,
  re-renders the page (set to the *to* parameter). This allows to force the evaluation of bound
  variables in complex dependencies situations.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.3.1

- New exposed functions:

       * `is_submittable()^` checks if a scenario or a pipeline can be submitted;

       * `is_promotable()^` checks if a scenario can be promoted to primary;

       * `is_deletable()^` checks if an entity can be deleted.

2.3.0

- All scenarios grouped by their cycle can now be retrieved by calling
  `taipy.get_cycles_scenarios()^`.
- All entities (cycles, scenarios, pipelines, tasks, data nodes, and jobs) expose two new methods:
  `get_label()` and `get_simple_label()`, that can be used to display the entity.
- `taipy.get_entities_by_config_id()^` can be used to retrieve all entities that are based on the
  provided configuration identifier.
- Commands for managing Taipy application versions can now be accessed via the
  `$ taipy manage-versions` command. Run `$ taipy manage-versions --help` for more details.
- A version can now be renamed by running
  `$ taipy manage-versions --rename <old_version> <new_version>` from the CLI.
- The configuration of a version can now be compared with another one by running
  `$ taipy manage-versions --compare-config <version_1> <version_2>` from the CLI.

## Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
2.3.2

- The [expanded](../refmans/gui/viselements/corelements/scenario.md#p-expanded) and
  [show_tags](../refmans/gui/viselements/corelements/scenario.md#p-show_tags) properties of the
  [scenario](../refmans/gui/viselements/corelements/scenario.md) control now have a default value of
  False.

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.3.2

- Multi-line [input](../refmans/gui/viselements/generic/input.md) controls accept the Shift+Enter combination
  to create a new line.<br/>
  See [issue #824](https://github.com/Avaiga/taipy-gui/issues/824).
- [Table](../refmans/gui/viselements/generic/table.md) filters adapt to a change of the visible columns.<br/>
  See [issue #822](https://github.com/Avaiga/taipy-gui/issues/822).

2.3.0

- Page scopes (how Taipy GUI finds bound variables in different modules) have been
  improved so any given page can locate a variable in any module that defines a local page.<br/>
  See the [section on page scopes](../userman/gui/binding.md#scope-for-variable-binding) for more
  information and examples.
- A new mechanism to start the web server when [using Notebooks](../userman/run-deploy/notebooks.md) was put
  in place to prevent potential bottlenecks when allocating a port number. This behavior is
  controlled by the [*notebook_proxy*](../userman/advanced_features/configuration/gui-config.md#p-notebook_proxy) configuration
  parameter.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.3.0

- A generic data node can now be created defining only the *read_fct* parameter for a read-only data
  node, or only the *write_fct* parameter for a write-only data node.
- The parameters *read_fct_params* and *write_fct_params* of the generic data nodes were renamed to
  *read_fct_args* and *write_fct_args*, and both must be populated with a List value to avoid the
  problem of passing Tuple of one string.
- The *validity_period* attribute of a data node is now exposed at the configuration level to set
  the up-to-date duration of a data node.
- Add support for SQLAlchemy 2.0

## Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.3.0

- The removal of all the [`table`](../refmans/gui/viselements/generic/table.md) filters has no immediate effect.
  <br/>
  See [issue #667](https://github.com/Avaiga/taipy-gui/issues/667).
- Styling of the [`pane` block](../refmans/gui/viselements/generic/pane.md) was not applied properly.<br/>
  See [issue #766](https://github.com/Avaiga/taipy-gui/issues/766).
- Some notifications (see `notify()^`) could be missed when there were too many in a small period
  of time.<br/>
  See [issue #777](https://github.com/Avaiga/taipy-gui/issues/777).

## Deprecations

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.3.2

- The `Config.configure_default_data_node()` method has been deprecated.
  The `Config.set_default_data_node_configuration()^` method should be used instead.
- The `Config.configure_task_node()` method has been deprecated.
  The `Config.set_task_node_configuration()^` method should be used instead.
- The `Config.configure_pipeline_node()` method has been deprecated.
  The `Config.set_pipeline_node_configuration()^` method should be used instead.
- The `Config.configure_scenario_node()` method has been deprecated.
  The `Config.set_scenario_node_configuration()^` method should be used instead.

2.3.0

- `PipelineConfig` has been deprecated and will be combined with `ScenarioConfig^` in future updates.
- `taipy.create_pipeline()` has been deprecated.

# Community edition: 2.2

Published on 2023-04.

[`taipy` 2.2](https://pypi.org/project/taipy/2.2.0/) contains the latest
[`taipy-config` 2.2](https://pypi.org/project/taipy-config/2.2.0/),
[`taipy-gui` 2.2](https://pypi.org/project/taipy-gui/2.2.1/),
[`taipy-core` 2.2](https://pypi.org/project/taipy-core/2.2.2/) and
[`taipy-rest` 2.2](https://pypi.org/project/taipy-rest/2.2.1/) packages.

## New Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- A default set of stylesheets are installed with Taipy GUI so that, by
  default, applications benefit from a homogeneous and good-looking
  style. This is called the [Stylekit](../userman/gui/styling/stylekit.md).<br/>
  The Stylekit can be easily customized to fit your application design's
  requirements.
- The [`table`](../refmans/gui/viselements/generic/table.md) and [`chart`](../refmans/gui/viselements/generic/chart.md)
  controls have a new property called *rebuild* that can be used if you need to entirely change the
  data they rely on, including their structure.

## Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- The default property name for the [`part` block](../refmans/gui/viselements/generic/part.md)
  was changed from *render* to *class_name* to allow for directly using the
  style classes from the [Stylekit](../userman/gui/styling/stylekit.md).<br/>
  Please check the section on
  [Styled Sections](../userman/gui/styling/stylekit.md#styled-sections) for
  more information.
- The [`expandable` block](../refmans/gui/viselements/generic/expandable.md) has a new property
  called *on_change* enabling to set a specific callback when the block is expanded
  or collapsed.
- Better error messages when parsing Markdown content.
- Better support for auto-completion in IDE for the `Gui.run()^` configuration parameters, based
  on a generated Python Interface Definition file.
- The *status* entry point now provides information about the loaded element libraries and
  the elements they define.
- The `navigate()^` function and the *page* property of the [`part` block](../refmans/gui/viselements/generic/part.md)
  can now use, as their target, any URL. In the context of a `part` block, the page will be rendered
  in an *iframe*.<br/>
  See [issue #621](https://github.com/Avaiga/taipy-gui/issues/621).

## Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- Bound variable scope issues fixed when used by elements defined at the root page
  level.<br/>
  See [issue #583](https://github.com/Avaiga/taipy-gui/issues/583).
- Filters management fixed in the [`table` controls](../refmans/gui/viselements/generic/table.md).<br/>
  See [issue #667](https://github.com/Avaiga/taipy-gui/issues/667).
- Communication with the server may break.<br/>
  See [issue #695](https://github.com/Avaiga/taipy-gui/issues/695).


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.2.3

- Error raised when running Orchestrator service in development mode after a function rename in the Config.<br/>
  See [issue #560](https://github.com/Avaiga/taipy-core/issues/560).

2.2.2

- PostgreSQL and MySQL engines do not support "driver" argument.<br/>
  See [issue #544](https://github.com/Avaiga/taipy-core/issues/544).<br/>
  To avoid conflict between engines, the default value of the _db_driver_ parameter in a SQL or a SQL table data
  node configuration has been removed.

# Studio: 1.0

Published on 2023-02.

The first release of the
[`Taipy Studio`](https://marketplace.visualstudio.com/items?itemName=Taipy.taipy-studio)
extension to [Visual Studio Code](https://code.visualstudio.com/).

Taipy Studio brings programmers tools that significantly improve productivity when
building Taipy applications.

It mainly provides:

- A graphical editor for building configuration files, so one does not have
    to code configurations in Python any longer;
- IntelliSense applied to the Markdown syntax extension that Taipy GUI
    uses to define the visual elements in the interface pages.

You can refer to the [Taipy Studio User Manual](../userman/ecosystem/studio/index.md) section for more
information.

# Community edition: 2.1

Published on 2023-01.

[`taipy` 2.1](https://pypi.org/project/taipy/2.1.0/) contains the latest
[`taipy-config` 2.1](https://pypi.org/project/taipy-config/2.1.0/),
[`taipy-gui` 2.1](https://pypi.org/project/taipy-gui/2.1.0/),
[`taipy-core` 2.1](https://pypi.org/project/taipy-core/2.1.0/) and
[`taipy-rest` 2.1](https://pypi.org/project/taipy-rest/2.1.0/) packages.

Please refer to the [Migration page](migration.md#from-20-to-21) for
details on how to migrate from version older than 2.1.

## New Features

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
2.1

- Taipy and all its dependencies now support Python 3.11.<br/>
  See [Python documentation](https://docs.python.org/3/whatsnew/3.11.html) for details.

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.1.0

- A security feature has been added: the file `.taipyignore`, located next to
  the Python main file, can list the paths that you want to prevent access to.<br/>
  See [issue #501](https://github.com/Avaiga/taipy-gui/issues/501) or
  [this section](../userman/advanced_features/configuration/gui-config.md#protect-your-application-files) for
  details.
- Charts can use the new `Decimator^` class to cleverly filter data points out to significantly
  improve performance.<br/>
  See the paragraph on [large datasets](../refmans/gui/viselements/generic/chart.md#large-datasets) for
  specific information.
- Charts now support polar, funnel, candlesticks and many other types of charts.<br/>
  See the [chart control](../refmans/gui/viselements/generic/chart.md) section for details.
- Charts now support the dark theme automatically.
- Tooltips can be set on individual table cells.<br/>
  See the [example](../refmans/gui/viselements/generic/table.md#cell-tooltips) for more information.
- [Long running callbacks](../userman/gui/callbacks.md#long-running-callbacks) have
  been improved to allow for easily returning a value.<br/>
  See the documentation of the `invoke_long_callback()^` function or the
  [issue #547](https://github.com/Avaiga/taipy-gui/issues/547) for more details.
- Developers can specify the location of the Taipy webapp, for debugging purposes.<br/>
  The `--webapp-path` command line option allows to specify that location.<br/>
  See [issue #564](https://github.com/Avaiga/taipy-gui/issues/564).


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.0

- New version management system for Taipy applications. Users can now run an application in development
  mode, save a version of the application as an experiment version, re-run older experiment versions,
  and push a version to production.<br/>
  See the [Version management system](../userman/advanced_features/versioning/index.md) documentation page for more details.
- New data node named [MongoCollectionDataNode](../userman/scenario_features/data-integration/data-node-config.md#mongo-collection).
  It represents the data from a MongoDB collection.
- New data node named [ParquetDataNode](../userman/scenario_features/data-integration/data-node-config.md#parquet). It represents
  tabular data stored in the Apache Parquet format.
- Added support for [Modin](https://modin.readthedocs.io/en/stable/) as a new exposed type.
- Running the Orchestrator service is required to execute jobs. See `Orchestrator().run()^` method.
- The parent entities of a data node, a task, or a pipeline can be accessed via
  `DataNode.get_parents()^`, `Task.get_parents()^`, or `Pipeline.get_parents()^`, or by passing the
  data node entity, task entity or pipeline entity to the function `taipy.get_parents()^`.
- New data node property _expiration_date_ computed adding the _validity_period_ duration to the
  _last_edit_date_ of the data node.
- New data node property _is_up_to_date_ equals to `True` if the data node has not expired (refer to
  _expiration_date_ attribute). `False` otherwise.
- The **sql** _repository_type_ is now available on community edition to store Taipy entities in an
  SQL database.

## Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.1.0

- The Pie charts now use the *values* property to set values instead of *x*.<br/>
  See [Pie charts](../refmans/gui/viselements/generic/charts/pie.md) for details.
- Unselected data points or traces in charts now preserve their original opacity.<br/>
  See [issue #496](https://github.com/Avaiga/taipy-gui/issues/496).
- `class_name` is now a dynamic property.<br/>
  See [issue #480](https://github.com/Avaiga/taipy-gui/issues/480).
- The *allow_unsafe_werkzeug* option of [Werkzeug](https://werkzeug.palletsprojects.com/)
  (that [Flask](https://flask.palletsprojects.com/) depends on for the WSGI part) is forced
  to True when the Gui instance is run in Debug mode, because of a change in policy in
  recent updates.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.1

- Add overload type descriptions for the `taipy.get()` method that supports multiple different combinations
  of argument types.

2.1.0

- Deprecation of the data node _cacheable_ property. It is replaced by _skippable_ property on tasks.
  The mechanism remains unchanged but instead of setting _cacheable_ property to `True` for all the
  outputs of a task that can be skipped, just set the task _skippable_ property to `True`.
- The _last_edit_date_ attribute of a data node is now updated when the corresponding data is modified
  by either a Taipy task execution or an external factor. This behavior is limited to file-based
  data nodes: CSV, Excel, JSON, and pickle data nodes only.

## Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.2

- The version required for [openpyxl](https://openpyxl.readthedocs.io/en/stable/) has been downgraded
  from "openpyxl>=3.0.7,<4.0" to "openpyxl>=3.0.7,<3.1" to match the version used by
  [Modin](https://modin.readthedocs.io/en/stable/).

# Community edition: 2.0

Published on 2022-10.

[`taipy` 2.0](https://pypi.org/project/taipy/2.0.0/) contains the latest
[`taipy-config` 2.0](https://pypi.org/project/taipy-config/2.0.1/),
[`taipy-gui` 2.0](https://pypi.org/project/taipy-gui/2.0.2/),
[`taipy-core` 2.0](https://pypi.org/project/taipy-core/2.0.3/) and
[`taipy-rest` 2.0](https://pypi.org/project/taipy-rest/2.0.0/) packages.

## New Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.0

- Extension API: custom visual elements can be integrated into Taipy GUI applications.<br/>
  Third party HTML components can be integrated into Taipy GUI pages to address specific use cases.<br/>
  See [Extension API](../userman/gui/extension/index.md) for details.
- New callbacks (`on_init`, `on_navigate`, `on_exception` and `on_status`) can be used to
  initialize a new session, detect navigation events, trigger code when exceptions are raised in
  user code, and invoke code when a *status* page is requested.<br/>
  See [Callbacks](../userman/gui/callbacks.md) for details.
- New functions allow applications to invoke long-running callbacks without blocking.<br/>
  See [Long Running Callbacks](../userman/gui/callbacks.md#long-running-callbacks) for
  details.
- The Taipy GUI application configuration uses the generic Taipy configuration mechanism exposed in the
  new `taipy-config` package.
- An application can request the status of the server application using the "status" predefined page.<br/>
- The new 'base' property of the chart control makes it possible to create Gantt chart-like displays.<br/>
  See [Gantt Charts](../refmans/gui/viselements/generic/charts/gantt.md) for details.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

- New data node named SQLTableDataNode. It represents a table in a SQL database.
- New data node named JSONDataNode. It represents the data from a JSON file.
- SQLDataNode behavior is changed due to the release of SQLTableDataNode. Now it represents the data
  using custom read and write queries.
- In standalone mode, a job whose status is `SUBMITTED`, `PENDING`, or `BLOCKED` can be canceled. When canceling
  the job, its subsequent jobs will be abandoned, and their statuses will be set to `ABANDONED`. When the cancel
  method is called on a job whose status is either `RUNNING`, `COMPLETED`, or `SKIPPED`, its subsequent jobs will
  be abandoned while its status remains unchanged. A job whose status is `FAILED`, `CANCELED` or `ABANDONED`
  cannot be canceled.
- Taipy Orchestrator can now be run as a service by using `Orchestrator().run()` or `tp.run(Orchestrator())`. By
  running Orchestrator as a service, Taipy initializes the scheduler and the job dispatcher based on the provided configuration. The
  Taipy Orchestrator service can be run along with Taipy GUI or Taipy Rest services.

<h6 style="font-size: 1.2em"><strong><code>taipy-config</code></strong></h6>
2.0.0

- The new `taipy-config` package was exposed to be used by any other Taipy package for configuration and logging.


## Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.0

- Stopping then re-running the `Gui^` instance is no longer required in Notebook contexts.
- A discrete graphical indicator is displayed at the bottom of pages when the server is
  processing.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

- The data node of a scenario or a pipeline can now be accessed directly at the scenario or pipeline
  levels.
- When submitting a scenario, a pipeline, or a task, the job(s) created will be returned.
- When submitting a scenario, pipeline, or task in standalone mode, the user can use the parameters
  _wait_ and _timeout_ to wait until the submitted jobs are finished or up to _timeout_ seconds.
- When in standalone mode, the job dispatcher runs in a sub-thread that periodically checks for new
  jobs submitted by Taipy to execute.
- When a running job fails, its subsequent jobs will be automatically abandoned.
- A primary scenario can be deleted along with its cycle if it is the only scenario in the cycle.
- The messages of the various Exceptions that can be raised have been improved to help the users
  debug their applications.

## Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.2

- `image` control may not render properly.<br/>
  See [issue #436](https://github.com/Avaiga/taipy-gui/issues/436).
- Clarify and improve the `editable` (and `editable[]`) property in the `table` control.<br/>
  See [issue #464](https://github.com/Avaiga/taipy-gui/issues/464).
- [gui] section in configuration files breaks the application.<br/>
  See [issue #469](https://github.com/Avaiga/taipy-gui/issues/469).

2.0.1

- Bar charts' "barmode" set to "stack" is broken.<br/>
  See [issue #445](https://github.com/Avaiga/taipy-gui/issues/445).

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.4

- Do not update `last_edit_date` when a job fails or is abandoned.
  See [issue #366](https://github.com/Avaiga/taipy-core/issues/366).

## Deprecations

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

- The field `*nb_of_workers*` within the Config has been deprecated in favor of `*max_nb_of_workers*`.

# Enterprise edition: 2.0

Published on 2022-10.

## New Features

- SQLLite or MongoDB databases can now be used as alternatives to the filesystem to store Taipy
  entities.

## Improvements and changes

- Simplification of the authentication API.

# Community edition: 1.1

Published on 2022-06.

[`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/) contains the latest
[`taipy-gui` 1.1](https://pypi.org/project/taipy-gui/1.1.0/),
[`taipy-core` 1.1](https://pypi.org/project/taipy-core/1.1.0/) and
[`taipy-rest` 1.1](https://pypi.org/project/taipy-rest/1.1.0/) packages.


## Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.1.3

- The client-server communication settings are extended to accommodate various Flask deployment scenarios.<br/>
  See the documentation for the *async_mode* parameter to `Gui.run()^` for more information.
- Implicit re-run of the `Gui^` instance in Notebook environments.<br/>
  See [issue #320](https://github.com/Avaiga/taipy-gui/issues/320).
- Test server/client versions for safe interoperability.<br/>
  See [issue #323](https://github.com/Avaiga/taipy-gui/issues/323).
- Allow the edition of specific table columns.<br/>
  See [issue #366](https://github.com/Avaiga/taipy-gui/issues/366).

1.1.0

- The `State^` instance can be initialized in a user-defined function. See the _on_init_
  attribute of the `Gui^` class for more details.
- Page definitions and the bound variables can be isolated in a module to clarify the
  application code organization.<br/>
  See this <a href="javascript:void(0)">section</a> for details.
- The <a href="javascript:void(0)">chart</a> control
  can display geo-referenced data on top of maps.<br/>
  See this <a href="javascript:void(0)">example</a>
  for details.
- The <a href="javascript:void(0)">input</a> and
- <a href="javascript:void(0)">slider</a>
  controls have a new _change_delay_ property that lets you tune how fast you want to propagate
  changes.<br/>
  This allows for a better user experience.
- The <a href="javascript:void(0)">input</a> control has a new
  _password_ property that, if True, obscures the user input.
- The <a href="javascript:void(0)">input</a>,
- <a href="javascript:void(0)">number</a> and
  <a href="javascript:void(0)">selector</a> controls have a
  new _label_ property that lets you display a label inside the control.
- The <a href="javascript:void(0)">layout</a> block has new
  syntax that makes it easier to define a repetition of a column definition.
- Support for multiple assignments to variables in *on_change()*.


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.1.0

- Execution modes: "_development_" mode (default) runs tasks in a synchronous way one task at
  a time, while "_standalone_" mode runs tasks in an asynchronous and parallel way using
  sub-processes.
- _Retry policy_ to read entities: the global configuration attribute _retry_read_entity_ indicates
  the number of times Taipy will retry in case of error.
- Performance improvements when reading and writing entities.

## Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.1.3

- Error fixed when modifying a State dictionary entry in a callback.<br/>
  See [issue #356](https://github.com/Avaiga/taipy-gui/issues/356).
- Boolean values not editable in tables.<br/>
  See [issue #365](https://github.com/Avaiga/taipy-gui/issues/365).
- Crash fixed when using a dictionary in the labels property of the slider control.<br/>
  See [issue #379](https://github.com/Avaiga/taipy-gui/issues/379).

1.1.0

- Concurrency issues were fixed.
- The [_attr_list_](https://python-markdown.github.io/extensions/attr_list) extension can
  be used to style individual Markdown elements without the need for a CSS file.<br/>
  See [issue #185](https://github.com/Avaiga/taipy-gui/issues/185).
- Taipy supports HTTPS via reverse proxies.<br/>
  See [issue #263](https://github.com/Avaiga/taipy-gui/issues/263).

## Deprecations

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.1.0

- The _path_ attribute of `DataNodeConfig`, for CSV, Excel and Pickle types is now deprecated.<br/>
  _default_path_ must be used instead: it is the default path to use when instantiating a data node from
  the config. Note that the attribute in the `DataNode` entity is still called _path_.
- The _last_edition_date_ attribute of data nodes is now deprecated.<br/>
  _last_edit_date_ must be used instead.
- The _edition_in_progress_ attribute of data nodes is now deprecated.<br/>
  _edit_in_progress_ must be used instead.

# Enterprise edition: 1.1

!!! warning

Published on 2022-06.

This release contains all of [`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/)
as well as additional features.

## Features

- User authentication.
- Authorization checks for all entities.
- Job recovery mechanism on application restart.
- Page generation based on the user's identity.

# Community edition: 1.0

Published on 2022-04.

[`taipy` 1.0](https://pypi.org/project/taipy/1.0.0/) contains the latest
[`taipy-gui` 1.0](https://pypi.org/project/taipy-gui/1.0.2/),
[`taipy-core` 1.0](https://pypi.org/project/taipy-core/1.0.3/) and
[`taipy-rest` 1.0](https://pypi.org/project/taipy-rest/1.0.1/) packages.

## Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.0.0

- Multiple pages support
- Binding to global variables
- Python expression support in visual element properties
- Initial visual element set including tables and charts.
- Page content support for Markdown and HTML
- Jupyter Notebook support

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.0.0

- Full configuration system
- Data node management (read/write/filter/cache)
- Predefined data nodes (CSV, SQL, EXCEL, PICKLE)
- Scenario and cycle management
- Smart scheduling and execution (Scenario, Pipeline, and Task submission)

<h6 style="font-size: 1.2em"><strong><code>taipy-rest</code></strong></h6>
1.0.0

- REST APIs on top of `taipy-core`
