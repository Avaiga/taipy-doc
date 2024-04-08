---
title : Release Notes
hide:
  - navigation
---

This is the list of changes to Taipy releases as they were published.

!!! note "Migration"

    Please refer to the [Migration page](./migration.md) for potential migration paths for your
    applications implemented on legacy Taipy versions.

!!! note "Legacy Releases"

    This page shows the changes that were made in the most recent major release of Taipy.<br/>
    If you are using a legacy version (pre-3.0), please refer to the
    [Legacy Release Notes](relnotes-legacy.md) page.

# Community edition: 3.2

(Work in progress - the following links are invalid for the time being)

[`taipy` 3.2](https://pypi.org/project/taipy/3.2.0/) contains the latest
[`taipy-config` 3.2](https://pypi.org/project/taipy-config/3.2.0/),
[`taipy-gui` 3.2](https://pypi.org/project/taipy-gui/3.2.0/),
[`taipy-core` 3.2](https://pypi.org/project/taipy-core/3.2.0/),
[`taipy-templates` 3.2](https://pypi.org/project/taipy-templates/3.2.0/), and
[`taipy-rest` 3.2](https://pypi.org/project/taipy-rest/3.2.0/) packages.

## New Features

<h4><strong><code>taipy</code></strong> 3.2.0</h4>

<h4><strong><code>taipy-gui</code></strong> 3.2.0</h4>

<h4><strong><code>taipy-core</code></strong> 3.2.0 </h4>

## Improvements and changes

<h4><strong><code>taipy</code></strong> 3.2.0</h4>

<h4><strong><code>taipy-gui</code></strong> 3.2.0</h4>

<h4><strong><code>taipy-core</code></strong> 3.2.0 </h4>

- In standalone job execution mode, the default value of *max_nb_of_workers* is now 2 instead of 1.
  For more information, please refer to [Job execution configuration](./manuals/core/config/job-config.md).
- When using the Taipy command-line interface, if an unsupported argument is provided, the CLI
  will display a message indicating the invalid argument. If the invalid argument is possibly a
  typo, the CLI will suggest the closest valid argument.

## Significant bug fixes

<h4><strong><code>taipy-gui</code></strong> 3.2.0</h4>

<h4><strong><code>taipy-core</code></strong> 3.2.1</h4>

# Enterprise edition: 3.2

(Work in progress - the following link is invalid for the time being)

This release contains all of [`taipy` 3.2](https://pypi.org/project/taipy/3.2.0) as well as
additional features.

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

- The [`chart`](manuals/gui/viselements/chart.md) control has a new property called *figure* that
  expects an instance of `plotly.graph_objects.Figure`. This class is provided by the
[Plotly Open Source Graphing Library for Python](https://plotly.com/python/) so you can create
  all sorts of graphs in Python.<br/>
  See the [`figure` property](manuals/gui/viselements/chart.md#p-figure) of the `chart` control and
  the [section on the *figure* property](manuals/gui/viselements/chart.md#the-figure-property) for
  more information.
- The [`part`](manuals/gui/viselements/part.md) block has a new property called *content* that
  lets developers integrate any third-party library that can generate HTML.<br/>
  See the documentation for the [`part`](manuals/gui/viselements/part.md) block and the examples
  using *content providers* for more information.
- A new control called [`date_range`](manuals/gui/viselements/date_range.md) is available if
  you need to represent and edit date ranges in your application pages.
- A new control called [`login`](manuals/gui/viselements/login.md) is available if you need users
  to authenticate in your application.

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- The `DataNode.filter()^` method and the indexing/filtering style now also support filtering a
  Numpy array, a list of objects, and a list of dictionaries.<br/>
  For more information, please refer to
  [Filter a data node](./manuals/core/entities/data-node-mgt.md#filter).
- You can now append new data to a data node using the `DataNode.append()^` method. The method is
  available for `CSVDataNode`, `ExcelDataNode`, `JSONDataNode`, `ParquetDataNode`, `SQLDataNode`,
  `SQLTableDataNode`, and `MongoCollectionDataNode`.<br/>
  For more information, please refer to
  [Append a data node](./manuals/core/entities/data-node-mgt.md#append).
- A new class called `Submission^` holds meta-data (such as its status or
  submission date) related to a submitted entity: `Scenario^`, `Sequence^`, and/or `Task^`.<br/>
  The function `taipy.get_latest_submission()^` returns the last submission of a given entity.<br/>
  For more information, please refer to
  [Submission](./manuals/core/entities/orchestrating-and-job-execution.md#submission).
- `taipy.submit()^`, `Scenario.submit()^`, `Sequence.submit()^`, and `Task.submit()^` now return a
  `Submission^` entity.
- A new predefined data node named `S3ObjectDataNode^` has been implemented.<br/>
  For more information, please refer to
  [S3ObjectDataNode](./manuals/core/config/data-node-config.md#amazon-web-service-s3-object).

## Improvements and changes

<h4><strong><code>taipy</code></strong> 3.1.0</h4>

- Task nodes in the [`scenario_dag`](manuals/gui/corelements/scenario_dag.md) control dynamically
  reflect the status of related jobs for the user that submitted scenarios or sequences.
- The [`scenario`](manuals/gui/corelements/scenario.md) control lets you add, modify, and edit
  sequences.
- The [`data_node`](manuals/gui/corelements/data_node.md) control can now represent collections.

<h4><strong><code>taipy-gui</code></strong> 3.1.0</h4>

- The [`table`](manuals/gui/viselements/table.md) control supports enumerated values. That allows
  for a better user experience when users edit cell values.<br/>
  See the
  [section on enumerated values in tables](manuals/gui/viselements/table.md/#enumerated-values) for
  the details.
- The [`toggle`](manuals/gui/viselements/toggle.md) control appears as a switch button if its
  [*value*](manuals/gui/viselements/toggle.md#p-value) property holds a Boolean value.

<h4><strong><code>taipy-core</code></strong> 3.1.0 </h4>

- The `modin` exposed type as been deprecated. When used, a fallback on Pandas is applied.<br/>
  See [issue #631](https://github.com/Avaiga/taipy/issues/631) for details.
- Running twice the Core service raises an exception to prevent running multiple instances
  at the same time.
- Running the Core service or creating an entity by `taipy.create_scenario()` or
  `taipy.create_global_data_node()` blocks the Configuration from being modified.

## Significant bug fixes

<h4><strong><code>taipy</code></strong></h4>

<h5>3.1.1</h5>

- Data is not shown or not automatically refreshed in
  [Data Node viewer](manuals/gui/corelements/data_node.md).<br/>
  See [issue #908](https://github.com/Avaiga/taipy/issues/908) and
  [issue #950](https://github.com/Avaiga/taipy/issues/950).
- Data Nodes holding dates may not show in
  [Data Node viewers](manuals/gui/corelements/data_node.md).<br/>
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

## New Features

<h4><strong><code>taipy</code></strong> 3.0.0</h4>

- Taipy application can now be run with the Taipy command-line interface (CLI) using the
  `taipy run` command. For more information, refer to
  [Run application in Taipy CLI](./manuals/cli/run.md).

<h4><strong><code>taipy-gui</code></strong> 3.0.0</h4>

- A new package holds the [*Page Builder API*](manuals/gui/pages/builder.md): a set of classes that
  let you define the pages for your application entirely with Python.
- You can now update variables on all clients using the *shared variables* concept. See
  the `Gui.add_shared_variable()^` and `State.dispatch()^` methods for details.
- You can now invoke a callback for all clients using the `broadcast_callback()^` function.
- The [`slider`](manuals/gui/viselements/slider.md) control can now handle several knobs,
  allowing for range selection.<br/>
  Please check the [example](manuals/gui/viselements/slider.md#multi-selection) for more
  information.
- The [`file_download`](manuals/gui/viselements/file_download.md) control now lets developers
  generate the file content dynamically, at download time.<br/>
  Please check the [example](manuals/gui/viselements/file_download.md#dynamic-content) for more information.
- A new CSS class called *toggle-navbar* was added to the
  [Stylekit](manuals/gui/styling/stylekit.md) to give a
  [`toggle`](manuals/gui/viselements/toggle.md) control the aspect of a
  [`navbar`](manuals/gui/viselements/navbar.md).
- The [`chart`](manuals/gui/viselements/chart.md) control now supports the
  [*treemap*](manuals/gui/viselements/charts/treemap.md) and
  [*waterfall*](manuals/gui/viselements/charts/waterfall.md) chart types.

<h4><strong><code>taipy-core</code></strong> 3.0.0</h4>

- A production version of a Taipy application can now be provided with **migration functions** to
  automatically migrate entities and keep them compatible with previous versions.<br/>
  For more information, refer to [Production mode](./manuals/core/versioning/production_mode.md).
- A `GLOBAL` scope data node can be created from a data node configuration calling
  the new `taipy.create_global_data_node()^` method.<br/>
  For more information, refer to
  [Create a data node](./manuals/core/entities/data-node-mgt.md#create-a-data-node).
- A data node configuration can be built from an existing data node configuration.
  For more information, refer to the documentation page on
  [data node configuration](./manuals/core/config/data-node-config.md#configure-a-data-node-from-another-configuration).
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
  [Configure a CSVDataNode](./manuals/core/config/data-node-config.md#csv)
  and [Configure a JSONDataNode](./manuals/core/config/data-node-config.md#json)
  sections.

<h4><strong><code>taipy-template</code></strong> 3.0.0</h4>

- A new template named "scenario-management" is available. For more information on creating
  a new Taipy application with the new "scenario-management" template, refer to the
  documentation page on [templates](./manuals/cli/create.md#from-a-specific-template).

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
        - *on_range_change* in the [`chart`](manuals/gui/viselements/chart.md) control;
        - *on_edit*, *on_add*, and *on_delete* in the [`table`](manuals/gui/viselements/table.md)
          control;
        - *on_close* in the [`pane`](manuals/gui/viselements/pane.md) block.
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
  information, refer to [Configure a scenario](./manuals/core/config/scenario-config.md).
- :warning: The `Pipeline` object has been removed and replaced by `Sequence^`. A sequence is
  held by a `Scenario^` and represents a subset of its tasks than can be submitted
  together independently of the other tasks of the scenario. For more information,
  refer to `Scenario.add_sequence()^` and `Scenario.remove_sequence()^`.
- `Scope.PIPELINE` has been removed from possible `Scope^` values.
- The `root_folder`, `storage_folder`, `read_entity_retry`, `repository_type`, and
  `repository_properties` attributes of the `GlobalAppConfig^` have been moved to the
  `CoreSection^`.<br/>
  Please refer to the [Core configuration page](manuals/core/config/core-config.md) for details.
- The `clean_entities` attribute has been removed from the `CoreSection^`. Correspondingly, the
  `--clean-entities` option has been removed from the version management CLI.<br/>
  To clean entities of a version, please run your application in development mode, or delete your
  version with the `--delete` CLI option. For more information, refer to
  [Taipy command-line interface](./manuals/cli/index.md)
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

- The default template also supports creating a multi-pages application with Core and Rest
  services. These options are available when creating a new application from the template.
- The "multi-page-gui" template has been removed. Please use the default instead to create
  a Taipy multi-pages application.

## Significant bug fixes

<h4><strong><code>taipy-gui</code></strong> 3.0.0</h4>

- The callback function set to the *on_action* parameter of the function `download()^` may
  be called too early. It is now ensured to be invoked *after* the download operation is
  performed.<br/>
  See [issue #916](https://github.com/Avaiga/taipy-gui/issues/916).
- Setting the [*properties*](manuals/gui/viselements/index.md#generic-properties) property of
  a visual element as the returned value from a function may not succeed.</br>
  See [issue #897](https://github.com/Avaiga/taipy-gui/issues/897).
- Variables imported by an `import *` directive are not handled properly in the state of
  a callback defined in the importing module.</br>
  See [issue #908](https://github.com/Avaiga/taipy-gui/issues/908).
- The [`date`](manuals/gui/viselements/date.md) control does not use the *format* property if
  *with_time* is not set.<br/>
  See [issue #909](https://github.com/Avaiga/taipy-gui/issues/909).
- The [`date`](manuals/gui/viselements/date.md) control uses the `datetime.date` type and does
  not apply time zones if time is not involved.<br/>
  See [issue #895](https://github.com/Avaiga/taipy-gui/issues/895) and
  [issue #923](https://github.com/Avaiga/taipy-gui/issues/923).
- Updating a [`chart`](manuals/gui/viselements/chart.md) control data may cause data congestion
  or display flickering.<br/>
  See [issue #864](https://github.com/Avaiga/taipy-gui/issues/864) and
  [issue #932](https://github.com/Avaiga/taipy-gui/issues/932).
- Selection in a [`chart`](manuals/gui/viselements/chart.md) with type *pie* type is not
  properly handled.<br/>
  See [issue #919](https://github.com/Avaiga/taipy-gui/issues/919).
- Hover text doesn't show properly in a [`selector`](manuals/gui/viselements/selector.md) that
  is crowded.<br/>
  See [issue #927](https://github.com/Avaiga/taipy-gui/issues/927).
- Options with a long text in a [`selector`](manuals/gui/viselements/selector.md) cannot cbe
  deselected.<br/>
  See [issue #917](https://github.com/Avaiga/taipy-gui/issues/917).
- The [`table`](manuals/gui/viselements/toggle.md) control does not support undefined date values
    from Pandas data frames.<br/>
    See [issue #886](https://github.com/Avaiga/taipy-gui/issues/886).

<h4><strong><code>taipy-core</code></strong> 3.0.0</h4>

- When running the Core service in development mode, changing the name of the function used by a
  task then running the application again would raise an error.<br/>
  See [issue #743](https://github.com/Avaiga/taipy-core/issues/743).

# Enterprise edition: 3.0

Published on 2023-10.

This release contains all of [`taipy` 3.0](https://pypi.org/project/taipy/3.0.0) as well as
additional features.

## New Features

- Python functions including scenario management methods can be scheduled to run at a specific
  time using the new `taipy.Scheduler^` API. For more information, refer to
  [Schedule a method](./manuals/core/scheduling/index.md).

## Improvements and changes

- The job recovery mechanism is now only available when the Core service is run.
