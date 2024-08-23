---
title : Release Notes
---

This is the list of changes to Taipy releases as they were published.

!!! note "Migration"

    Please refer to the [Migration page](./migration.md) for potential migration paths for your
    applications implemented on legacy Taipy versions.

!!! note "Legacy Releases"

    This page shows the changes made in the most recent major release of Taipy.<br/>
    If you are using a legacy version (pre-4.0), please refer to the
    [Legacy Release Notes](legacy.md) page.

    Note that we support the latest major version and the one before that. Because we have
    released Taipy 4.0, support and documentation for Taipy versions older than 3.0 are disrupted.

# Community edition: 4.0

(Work in progress - the following links are invalid for the time being)

[`taipy` 4.0](https://pypi.org/project/taipy/4.0.0/) contains the latest
[`taipy-config` 4.0](https://pypi.org/project/taipy-config/4.0.0/),
[`taipy-gui` 4.0](https://pypi.org/project/taipy-gui/4.0.0/),
[`taipy-core` 4.0](https://pypi.org/project/taipy-core/4.0.0/),
[`taipy-templates` 4.0](https://pypi.org/project/taipy-templates/4.0.0/), and
[`taipy-rest` 4.0](https://pypi.org/project/taipy-rest/4.0.0/) packages.

## New Features

<h4><strong><code>taipy</code></strong> 4.0.0</h4>

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

- A new control called [`metric`](../manuals/userman/gui/viselements/generic/metric.md) was added
  to represent significant numerical information such as an industrial KPI.
- A new control called [`chat`](../manuals/userman/gui/viselements/generic/chat.md) was added
  to simplify the creation of chatting applications.

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- The `taipy.get_scenarios()` and `taipy.get_primary_scenarios()^` methods now accept optional
  parameters to:

    - sort the output list of scenarios by name, id, creation date, or tag
    - filter the output list of scenarios that are created in a specific time range.<br/>
  For more information, please refer to
  [Get all scenarios](../manuals/userman/sdm/scenario/index.md#get-all-scenarios) and
  [Get primary scenarios](../manuals/userman/sdm/scenario/index.md#get-primary-scenarios).

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- Creating a new application using any template now also supports initializing the application as a
  Git repository.

## Improvements and changes

<h4><strong><code>taipy</code></strong> 4.0.0</h4>

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

- Setting up styling: if a file called `taipy.css` sits next to the Python script (`<app>.py`) that
  runs a Taipy GUI application, and if there is no file called `<app>.css` at the same location,
  then this CSS file is loaded and applied to all pages. This feature allows you to share styles
  across different Taipy GUI applications.<br/>
  See the [Styling section](../manuals/userman/gui/styling/index.md#style-sheets) for more
  information.<br/>
  See [issue #1597](https://github.com/Avaiga/taipy/issues/1597) for a description of this
  functionality.
- In the [`chart`](../manuals/userman/gui/viselements/generic/chart.md) control, the Modebar (that
  appears when the cart is hovered on) no longer has the Plotly logo button by default.
  You can bring it back by setting the chart's
  [*plot_config* property](../manuals/userman/gui/viselements/generic/chart.md#p-plot_config)
  to a dictionary with a property called "displaylogo" set to True.<br/>
  See [issue #1600](https://github.com/Avaiga/taipy/issues/1600).

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- In standalone job execution mode, the default value of *max_nb_of_workers* is now 2 instead of 1.
  For more information, please refer to
  [Job execution configuration](../manuals/userman/configuration/job-config.md).
- When using the Taipy command-line interface, if an unsupported argument is provided, the CLI
  will display a message indicating the invalid argument. If the invalid argument is possibly a
  typo, the CLI will suggest the closest valid argument.
- The `Scenario.export()` and `taipy.export_scenario()` have been transfered from the Community
  edition to the Enterprise edition as it is more suitable for enterprise applications.
- Removed support for SQL repository. Taipy community edition now only supports the `filesystem`
  repository type.
- Two scenarios belonging to the same cycle can now have the same tag.<br/>
  See [issue #1292](https://github.com/Avaiga/taipy/issues/1292)

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- The *--template* option of the `taipy create` command is now renamed to *--application* option
  to correctly reflect the application template to use when creating a new Taipy application.

## Significant bug fixes

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

<h4><strong><code>taipy-core</code></strong> 4.0.0</h4>

- `DataNode.is_up_to_date^` raises an error when the data node has never been written.<br/>
  See [issue #1198](https://github.com/Avaiga/taipy/issues/1198).

# Enterprise edition: 4.0

(Work in progress - the following link is invalid for the time being)

This release contains all of [`taipy` 4.0](https://pypi.org/project/taipy/4.0.0) as well as
additional features.

## New Features

- The `taipy.export_scenario()^` method now supports exporting file-based data nodes' data to the
  export folder if the path exists.
- The `taipy.export_scenario()^` method now exports a zip archive instead of a
  folder. For more information, please refer to
  [Export a scenario](../manuals/userman/sdm/scenario/index.md#export-a-scenario).
- The `taipy.export_scenario()^` method now raises the `ExportPathAlreadyExists^`
  exception if the export path already exists. You can explicitly set the *overwrite* parameter to
  True to overwrite the existing export path. For more information, please refer to
  [Export a scenario](../manuals/userman/sdm/scenario/index.md#export-a-scenario).
- The new `taipy.import_scenario()^` method can be used to import a scenario from an exported
  archive. For more information, please refer to
  [Import a scenario](../manuals/userman/sdm/scenario/index.md#import-a-scenario).
- The default application template now supports authentication and authorization features.
