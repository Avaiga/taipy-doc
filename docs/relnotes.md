---
hide:
  - navigation
---

# Release Notes

This is the list of changes to Taipy releases as they were published.

!!! note "Migration"

    Please refer to the [Migration page](./migration.md) for potential migration paths for your applications
    implemented on legacy Taipy versions.

!!! note "Legacy Releases"

    This page shows the changes that were made in the most recent major release of Taipy.<br/>
    If you are using a legacy version, please refer to the [Legacy Release Notes](relnotes-legacy.md)
    page.

## Community edition: 3.0 (Work in progress)

Not published yet.

### New Features

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
3.0.0

- Taipy application can now be run with the Taipy command-line interface (CLI) using the `taipy run`
  command. For more information, refer to [Run application in Taipy CLI](./manuals/cli/run.md).

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
3.0.0

- TODO
- The [`file_download` control](manuals/gui/viselements/file_download.md) now lets developers
  generate the file content dynamically, at download time.<br/>
  Please check the [example](manuals/gui/viselements/file_download.md/#dynamic-content) for more
  information.
- Sliders with multiple knobs
- dispatch()
- Builder API


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
3.0.0

- A production version of a Taipy application can now be provided with **migration functions** to
  automatically migrate entities and keep them compatible with previous versions.<br/>
  For more information, refer to [Production mode](./manuals/core/versioning/production_mode.md).
- A `GLOBAL` scope data node can be created from a data node configuration calling
  the new `taipy.create_global_data_node()^` method.<br/>
  For more information, refer to
  [Create a data node](./manuals/core/entities/data-node-mgt.md#create-a-data-node).
- A data node configuration can be built from an existing data node configuration.
  For more information, refer to
  [Configure a data node from another configuration](./manuals/core/config/data-node-config.md#configure-a-data-node-from-another-configuration).
- A new class `Submittable^` models entities that can be submitted for execution.
  It is an Abstract class instantiated by `Scenario^` and `Sequence^`;
  It can be handy to use the new following `Submittable^` methods:

      * `Submittable.get_inputs()^` retrieves input data nodes of a `Submittable` entity;
      * `Submittable.get_outputs()^` retrieves output data nodes of a `Submittable` entity;
      * `Submittable.get_intermediate()^` retrieves intermediate data nodes of a `Submittable` entity;
      * `Submittable.is_ready_to_run()^` checks if an entity is ready to be run;
      * `Submittable.data_nodes_being_edited()^` retrieves data nodes that are being edited
        of a `Submittable^` entity;
- New functions exposed by the `taipy` module: `taipy.is_deletable()^` checks if an entity can be deleted.
  `taipy.exists()^` checks if an entity exists.
- The encoding type of CSVDataNode and JSONDataNode can now be configured using the
  *encoding* parameter. For more information, please refer to
  [Configure a CSVDataNode](./manuals/core/config/data-node-config.md#csv)
  and [Configure a JSONDataNode](./manuals/core/config/data-node-config.md#json)
  sections.


<h6 style="font-size: 1.2em"><strong><code>taipy-template</code></strong></h6>
3.0.0

- A new template named "scenario-management" is available. For more information on creating
  a new Taipy application with the new "scenario-management" template, refer to
  [Create a Taipy application from a specific template](./manuals/cli/create.md#from-a-specific-template).

### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
3.0.0

- A `ScenarioConfig^` graph is now created directly from `TaskConfig^` and
  `DataNodeConfig^`. Consequently, `PipelineConfig` has been removed. For more
  information, refer to [Configure a scenario](./manuals/core/config/scenario-config.md).
- The `Pipeline^` object has been removed and replaced by `Sequence^`. A sequence is
  held by a `Scenario^` and represents a subset of its tasks than can be submitted
  together independently of the other tasks of the scenario. For more information,
  refer to `Scenario.add_sequence()^` and `Scenario.remove_sequence()^`.
- `Scope.PIPELINE` has been removed from `Scope^` values.
- The `root_folder`, `storage_folder`, `read_entity_retry`, `repository_type`, and `repository_properties`
  attributes of the `GlobalAppConfig^` have been moved to the `CoreSection^`.<br/>
  Please refer to the [Core configuration page](manuals/core/config/core-config.md) for details.
- The `clean_entities` attribute has been removed from the `CoreSection^`. Correspondingly, the
  `--clean-entities` option has been removed from the version management CLI.<br/>
  To clean entities of a version, please run your application in development mode, or delete your
  version with the `--delete` CLI option. For more information, refer to
  [Taipy command-line interface](./manuals/cli/index.md)
- The deprecated `nb_of_workers` attribute of the JobConfig has been removed.
- The deprecated `parent_id` attribute of a DataNode, Task, Pipeline, or Scenario entity, has been removed.
- The deprecated `last_edition_date` and `edition_in_progress` attributes of a DataNode entity have been removed.
- The deprecated `DataNode.lock_edition()` and `DataNode.unlock_edition()` methods have been removed.
- The deprecated `taipy.create_pipeline()` method has been removed.
- Function `DataNode.track_edit` has been made public.

<h6 style="font-size: 1.2em"><strong><code>taipy-template</code></strong></h6>
3.0.0

- The default template also supports creating a multi-pages application with Core and Rest services.
  These options are available when creating a new application from the template.
- The "multi-page-gui" template has been removed. Please use the default instead to create
  a Taipy multi-pages application.

### Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
3.0.0

- The callback function set to the *on_action* parameter of the function `download()^` may
  be called too early. It is now ensured to be invoked *after* the download operation is
  performed.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
3.0.0

- When running the Core service in development mode, changing the name of the function used by a task then running
  the application again would raise an error.<br/>
  See [issue #743](https://github.com/Avaiga/taipy-core/issues/743).

## Enterprise edition: 3.0 (Work in progress)

Not published yet.

This release contains all of [`taipy` 3.0](Link to Taipy pypi)
as well as additional features.

### New Features

- Python functions including scenario management methods can be scheduled to run at a specific time using the new `taipy.Scheduler^` API.
  For more information, refer to [Schedule a method](./manuals/core/scheduling/index.md).

### Improvements and changes

- The job recovery mechanism is now only available when the Core service is run.
