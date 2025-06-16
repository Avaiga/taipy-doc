---
title: Release Notes for version 3.0
---

This is the list of changes of taipy version 3.0.

!!! note "Unsupported version"

    Version 3.0 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

!!! warning "Error when downgrading from Taipy 3.1 to Taipy 3.0"

    If you are experiencing an error downgrading to Taipy 3.0, please
    reinstall Taipy with options `--no-cache-dir -I` like so:
    `pip install --no-cache-dir -I taipy==3.0.0`

    See [issue #1180](https://github.com/Avaiga/taipy/issues/1180) for more details.

Published on 2023-10.

[`taipy` 3.0](https://pypi.org/project/taipy/3.0.0/) contains the latest
[`taipy-config` 3.0](https://pypi.org/project/taipy-config/3.0.1/),
[`taipy-gui` 3.0](https://pypi.org/project/taipy-gui/3.0.0/),
[`taipy-core` 3.0](https://pypi.org/project/taipy-core/3.0.0/),
[`taipy-templates` 3.0](https://pypi.org/project/taipy-templates/3.0.0/), and
[`taipy-rest` 3.0](https://pypi.org/project/taipy-rest/3.0.0/) packages.

# <strong><code>taipy</code></strong>

## 3.0.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Taipy application can now be run with the
  Taipy command-line interface (CLI) using the `taipy run` command. For more information,
  refer to [Run application in Taipy CLI](../../userman/ecosystem/cli/run.md).

# <strong><code>taipy-gui</code></strong>

## 3.0.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new package holds the
  [*Page Builder API*](../../userman/gui/pages/builder.md): a set of classes that
  let you define the pages for your application entirely with Python.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } You can now update variables on all clients
  using the *shared variables* concept. See the `Gui.add_shared_variable()^` and
  `State.dispatch()^` methods for details.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } You can now invoke a callback for all clients
  using the `broadcast_callback()^` function.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The
  [`slider`](../../refmans/gui/viselements/generic/slider.md) control can now handle several
  knobs, allowing for range selection.<br/>
  Please check the [example](../../refmans/gui/viselements/generic/slider.md#multi-selection)
  for more information.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The
  [`file_download`](../../refmans/gui/viselements/generic/file_download.md) control now lets
  developers generate the file content dynamically, at download time.<br/>
  Please check the [example](../../refmans/gui/viselements/generic/file_download.md#dynamic-content)
  for more information.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new CSS class called *toggle-navbar* was added to the
  [Stylekit](../../userman/gui/styling/stylekit.md) to give a
  [`toggle`](../../refmans/gui/viselements/generic/toggle.md) control the aspect of a
  [`navbar`](../../refmans/gui/viselements/generic/navbar.md).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The [`chart`](../../refmans/gui/viselements/generic/chart.md)
  control now supports the [*treemap*](../../refmans/gui/viselements/generic/charts/treemap.md) and
  [*waterfall*](../../refmans/gui/viselements/generic/charts/waterfall.md) chart types.

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The `navigate()^` function has an additional
  parameter *params* that is used to add query parameters to the requested URL. The query
  parameters can be retrieved in the `on_navigate` callback.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The *on_action* parameter of the `download()^`
  function can be a function and not just a function name.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Setting the *debug* parameter of `Gui.run()^`
  to True provides stack traces to be shown in the console when exceptions occur in user code.

<h4>Significant bug fixes</h4>

- :octicons-bug-24:{ .bug-icon title="Bug fix" } The callback function set to the *on_action* parameter
  of the function `download()^` may be called too early. It is now ensured to be invoked
  *after* the download operation is performed.<br/>
  See [issue #916](https://github.com/Avaiga/taipy-gui/issues/916).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Setting the
  [*properties*](../../userman/gui/viselements/introduction.md#generic-properties) property
  of a visual element as the returned value from a function may not succeed.</br>
  See [issue #897](https://github.com/Avaiga/taipy-gui/issues/897).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Variables imported by an `import *` directive are not
  handled properly in the state of a callback defined in the importing module.</br>
  See [issue #908](https://github.com/Avaiga/taipy-gui/issues/908).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } The [`date`](../../refmans/gui/viselements/generic/date.md)
  control does not use the *format* property if *with_time* is not set.<br/>
  See [issue #909](https://github.com/Avaiga/taipy-gui/issues/909).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } The [`date`](../../refmans/gui/viselements/generic/date.md)
  control uses the `datetime.date` type and does not apply time zones if time is not involved.<br/>
  See [issue #895](https://github.com/Avaiga/taipy-gui/issues/895) and
  [issue #923](https://github.com/Avaiga/taipy-gui/issues/923).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Updating a
  [`chart`](../../refmans/gui/viselements/generic/chart.md) control data may cause data
  congestion or display flickering.<br/>
  See [issue #864](https://github.com/Avaiga/taipy-gui/issues/864) and
  [issue #932](https://github.com/Avaiga/taipy-gui/issues/932).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Selection in a
  [`chart`](../../refmans/gui/viselements/generic/chart.md) with type *pie* type is not
  properly handled.<br/>
  See [issue #919](https://github.com/Avaiga/taipy-gui/issues/919).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Hover text doesn't show properly in a
  [`selector`](../../refmans/gui/viselements/generic/selector.md) that
  is crowded.<br/>
  See [issue #927](https://github.com/Avaiga/taipy-gui/issues/927).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Options with a long text in a
  [`selector`](../../refmans/gui/viselements/generic/selector.md) cannot cbe
  deselected.<br/>
  See [issue #917](https://github.com/Avaiga/taipy-gui/issues/917).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } The [`table`](../../refmans/gui/viselements/generic/toggle.md)
  control does not support undefined date values from Pandas data frames.<br/>
  See [issue #886](https://github.com/Avaiga/taipy-gui/issues/886).

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The *action* parameter of the `on_action` callback
  was removed for every control.<br/>
  The signature of all *on_action()* callback functions are now unified to the following:
    - *state* (`State^`): the state of the client invoking that callback;
    - *id* (str): the identifier of the visual element that triggers that callback;
    - *payload* (dict): a dictionary that provides additional information to the callback.<br/>
      This dictionary now has the additional *action* key that is set to the action name.

    This change not only impact the *on_action* callback of all controls that support it,
    but in an exactly similar manner the following callback signatures:

    - *on_range_change* in the [`chart`](../../refmans/gui/viselements/generic/chart.md) control;
    - *on_edit*, *on_add*, and *on_delete* in the [`table`](../../refmans/gui/viselements/generic/table.md)
      control;
    - *on_close* in the [`pane`](../../refmans/gui/viselements/generic/pane.md) block.

# <strong><code>taipy-core</code></strong>

## 3.0.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A production version of a Taipy application can now
  be provided with **migration functions** to automatically migrate entities and keep them
  compatible with previous versions.<br/>
  For more information, refer to
  [Production mode](../../userman/advanced_features/versioning/production_mode.md).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A `GLOBAL` scope data node can be created from a
  data node configuration calling the new `taipy.create_global_data_node()^` method.<br/>
  For more information, refer to
  [Create a data node](../../userman/scenario_features/data-integration/data-node-usage.md#create-a-data-node).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A data node configuration can be built from an
  existing data node configuration. For more information, refer to the documentation page on
  [data node configuration](../../userman/scenario_features/data-integration/data-node-config.md#configure-a-data-node-from-another-configuration).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new class `Submittable^` models entities that
  can be submitted for execution. It is an Abstract class instantiated by `Scenario^` and
  `Sequence^`. It can be handy to use the new following `Submittable^` methods:
   - `Submittable.get_inputs()^` retrieves input data nodes of a `Submittable` entity;
   - `Submittable.get_outputs()^` retrieves output data nodes of a `Submittable` entity;
   - `Submittable.get_intermediate()^` retrieves intermediate data nodes of a `Submittable`
     entity;
   - `Submittable.is_ready_to_run()^` checks if an entity is ready to be run;
   - `Submittable.data_nodes_being_edited()^` retrieves data nodes that are being edited
     of a `Submittable^` entity.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New functions exposed by the `taipy` module:
   - `taipy.is_deletable()^` checks if an entity can be deleted;
   - `taipy.exists()^` checks if an entity exists.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The encoding type of CSVDataNode and JSONDataNode
  can now be configured using the *encoding* parameter. For more information, please refer to
  [Configure a CSVDataNode](../../userman/scenario_features/data-integration/data-node-config.md#csv)
  and [Configure a JSONDataNode](../../userman/scenario_features/data-integration/data-node-config.md#json)
  sections.

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Function `DataNode.track_edit` has been made public.

<h4>Significant bug fixes</h4>

- :octicons-bug-24:{ .bug-icon title="Bug fix" } When running the Orchestrator service in development mode,
  changing the name of the function used by a task then running the application again would
  raise an error.<br/>
  See [issue #743](https://github.com/Avaiga/taipy-core/issues/743).

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } A `ScenarioConfig^` graph is now created directly
  from `TaskConfig^` and `DataNodeConfig^`. Consequently, `PipelineConfig` has been removed.
  For more information, refer to
  [Configure a scenario](../../userman/scenario_features/sdm/scenario/scenario-config.md).
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The `Pipeline` object has been removed and replaced
  by `Sequence^`. A sequence is held by a `Scenario^` and represents a subset of its tasks than
  can be submitted together independently of the other tasks of the scenario. For more information,
  refer to `Scenario.add_sequence()^` and `Scenario.remove_sequence()^`.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } `Scope.PIPELINE` has been removed from possible `Scope^`
  values.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The *root_folder*, *storage_folder*, *read_entity_retry*,
  *repository_type*, and *repository_properties* attributes of the `GlobalAppConfig^` have been
  moved to the `CoreSection^`.<br/>
  Please refer to the
  [Core configuration page](../../userman/advanced_features/configuration/core-config.md) for
  details.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The *clean_entities* attribute has been removed from
  the `CoreSection^`. Correspondingly, the `--clean-entities` option has been removed from the
  version management CLI.<br/>
  To clean entities of a version, please run your application in development mode, or delete your
  version with the `--delete` CLI option. For more information, refer to
  [Taipy command-line interface](../../userman/ecosystem/cli/index.md)
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The deprecated *nb_of_workers* attribute of the
  `JobConfig` has been removed.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The deprecated *parent_id* attribute of a DataNode,
  Task, Pipeline, or Scenario entity, has been removed.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The deprecated *last_edition_date* and
  *edition_in_progress* attributes of a DataNode entity have been removed.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The deprecated `DataNode.lock_edition()` and
  `DataNode.unlock_edition()` methods have been removed.
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } The deprecated `taipy.create_pipeline()` method
  has been removed.

# <strong><code>taipy-template</code></strong>

## 3.0.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new template named "scenario-management" is available.
  For more information on creating a new Taipy application with the new "scenario-management"
  template, refer to the documentation page on
  [templates](../../userman/ecosystem/cli/create.md#from-a-specific-application-template).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The default template also supports creating a
  multi-pages application with Orchestrator and Rest
  services. These options are available when creating a new application from the template.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The "multi-page-gui" template has been removed.
  Please use the default instead to create a Taipy multi-pages application.

# <strong><code>taipy-enterprise</code></strong>

## 3.0.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Python functions including scenario management
  methods can be scheduled to run at a specific time using the new `taipy.Scheduler^`
  API. For more information, refer to
  [Schedule a method](../../userman/advanced_features/scheduling/index.md).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The job recovery mechanism is now only
  available when the Orchestrator service is run.
