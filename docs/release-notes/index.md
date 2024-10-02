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

- A new control, [`metric`](../refmans/gui/viselements/generic/metric.md), has been added to
  represent significant numerical information, such as industrial KPIs.
- A new control, [`progress`](../refmans/gui/viselements/generic/progress.md), has been added to
  provide a compact representation of a process's progress.
- A new control, [`chat`](../refmans/gui/viselements/generic/chat.md), has been introduced to
  simplify the development of chat-based applications.
- The [`table`](../refmans/gui/viselements/generic/table.md) control has new features:
    - Built-in edit functionality are now available for all supported data types. You no longer need
      to define functions for the
      [*on_edit*](../refmans/gui/viselements/generic/table.md#p-on_edit),
      [*on_add*](../refmans/gui/viselements/generic/table.md#p-on_add), and
      [*on_delete*](../refmans/gui/viselements/generic/table.md#p-on_delete) properties. However,
      you can still customize these actions by providing your own functions.<br/>
      Please read
      [this section](../refmans/gui/viselements/generic/table.md#editing-the-table-content) for more
      details.
    - A new indexed property,
      [*format_fn[column_name]*](../refmans/gui/viselements/generic/table.md#p-format_fn[column_name])
      allows you to define a custom Python function to format cell values.<br/>
      Please look at the
      [example code](../refmans/gui/viselements/generic/table.md#custom-formatting) for details. 
- You can define CSS rules for individual pages using the new *style* parameter of the `Page^`
  class or via the `Page.set_style()^` method.<br/>
  See the [section on Styling](../userman/gui/styling/index.md#style-sheets) for more
  information.

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- The `taipy.get_scenarios()` and `taipy.get_primary_scenarios()^` methods now accept optional
  parameters to:

    - sort the output list of scenarios by name, id, creation date, or tag
    - filter the output list of scenarios that are created in a specific time range.<br/>
  For more information, please refer to
  [Get all scenarios](../userman/scenario_features/sdm/scenario/index.md#get-all-scenarios) and
  [Get primary scenarios](../userman/scenario_features/sdm/scenario/index.md#get-primary-scenarios).

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- Creating a new application using any template now also supports initializing the application as a
  Git repository.

## Improvements and changes

<h4><strong><code>taipy</code></strong> 4.0.0</h4>

- Taipy and all its dependencies now stop support Python 3.8.<br/>
  The minimum supported Python version is now 3.9.

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

- Setting up styling:<br/>
  If a file named `taipy.css` is located in the same directory as the Python script (`<app>.py`)
  running a Taipy GUI application, and no `<app>.css` file exists in the same location, this CSS
  file will be loaded and applied to all pages. This enables sharing styles across different Taipy
  GUI applications.<br/>
  See [issue #1597](https://github.com/Avaiga/taipy/issues/1597) for more details and the
  [section on Styling](../userman/gui/styling/index.md#style-sheets).
- Most visual elements now implement the *width* property, simplifying page layout.<br/>
  See [issue #1720](https://github.com/Avaiga/taipy/issues/1720).
- The [`input`](../refmans/gui/viselements/generic/input.md) control has a new
  [*type*](../refmans/gui/viselements/generic/input.md#p-type) property, allowing you to specify the
  expected input type (e.g., email address, URL).
- The [`pane`](../refmans/gui/viselements/generic/pane.md) block now includes a new property,
  [*show_button*](../refmans/gui/viselements/generic/pane.md#p-show_button). When set to True, a
  persistent *open* button appears on the page when the pane is closed, eliminating the need for an
  external control to open the pane.
- The Modebar in the [`chart`](../refmans/gui/viselements/generic/chart.md) control (visible when
  the chart is hovered over) no longer includes the Plotly logo button by default. To restore it,
  set the [*plot_config*](../refmans/gui/viselements/generic/chart.md#p-plot_config) property to a
  dictionary with `"displaylogo": True`.<br/>
  See [issue #1600](https://github.com/Avaiga/taipy/issues/1600).
- The *decimator* property of the [`chart`](../refmans/gui/viselements/generic/chart.md) control
  now applies to traces that are only "lines" or "markers".
- A new toggle button has been added to the [`login`](../refmans/gui/viselements/generic/login.md)
  control, enabling users to show or hide the entered password.
- Page Builder API:
    - Properties that expect a function can now be set to a lambda function in the Page Builder
      API.<br/>
      See [issue #1379](https://github.com/Avaiga/taipy/issues/1379).
    - Controls defined with the Page Builder API have an additional property called *inline* which,
      when set to True, will not generate a line skip, to facilitate layout.<br/>
      See [issue #1725](https://github.com/Avaiga/taipy/issues/1725).

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- In standalone job execution mode, the default value of *max_nb_of_workers* is now 2 instead of 1.
  For more information, please refer to
  [Job execution configuration](../userman/advanced_features/configuration/job-config.md).
- When using the Taipy command-line interface, if an unsupported argument is provided, the CLI
  will display a message indicating the invalid argument. If the invalid argument is possibly a
  typo, the CLI will suggest the closest valid argument.
- The `Scenario.export()` and `taipy.export_scenario()` functions have been transferred from the
  Community edition to the Enterprise edition as it is more suitable for enterprise applications.
- The production mode of the version management system has been transferred from the Community
  edition to the Enterprise edition as it is more suitable for enterprise applications.
- Support for for the SQL repository was removed. Taipy Community edition now only supports the
  `filesystem` repository type.
- Two scenarios belonging to the same cycle can now have the same tag.<br/>
  See [issue #1292](https://github.com/Avaiga/taipy/issues/1292).
- The `Config.check()^` method now raises `ERROR` issues if any data node, task, or sequence of
  a `ScenarioConfig^` has the same configuration id as another one in the same `ScenarioConfig^`,
  or any additional property of any configuration has the same name as one of the attributes
  of the configuration class.<br/>
  For more information, please refer to
  [Configuration checker](../userman/advanced_features/configuration/config-checker.md).

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- The *--template* option of the `taipy create` command is now renamed to *--application* option
  to correctly reflect the application template to use when creating a new Taipy application.

## Significant bug fixes

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

- The value of multiline [`input`](../refmans/gui/viselements/generic/pane.md) controls is
  cleared when the ENTER key is pressed.<br/>
  See [issue #1762](https://github.com/Avaiga/taipy/issues/1762).
- The [`chart`](../refmans/gui/viselements/generic/chart.md) control properly handles its
  *selected* property in the case it uses the *figure* property.<br/>
  See [issue #1786](https://github.com/Avaiga/taipy/issues/1786).
- Indexed properties can be used in the Page Builder API as described in the information box in
  [this](../userman/gui/pages/builder.md#setting-property-values) section.<br/>
  See [issue #1715](https://github.com/Avaiga/taipy/issues/1715).
- Binding to an element of a collection is now supported.<br/>
  See [issue #1785](https://github.com/Avaiga/taipy/issues/1785).

<h4><strong><code>taipy-core</code></strong> 4.0.0</h4>

- `DataNode.is_up_to_date()^` raises an error when the data node has never been written.<br/>
  See [issue #1198](https://github.com/Avaiga/taipy/issues/1198).

# Enterprise edition: 4.0

(Work in progress - the following link is invalid for the time being)

This release contains all of [`taipy` 4.0](https://pypi.org/project/taipy/4.0.0) as well as
additional features.

## New Features

- Support for [Polars DataFrame Library](https://docs.pola.rs/).<br/>
  Tabular data nodes (`CSVDataNode^`, `ParquetDataNode^`, `ExcelDataNode^`, `SQLTableDataNode^` and
  `SQLDataNode`) can now expose the data as Polars objects. They all support
  [`polars.LazyFrame`](https://docs.pola.rs/api/python/stable/reference/lazyframe/index.html),
  [`polars.DataFrame`](https://docs.pola.rs/api/python/stable/reference/dataframe/index.html) or
  [`polars.Series`](https://docs.pola.rs/api/python/stable/reference/series/index.html) as exposed
  type through the *exposed_type* configuration attribute.<br/>
  The [`table`](../refmans/gui/viselements/generic/table.md) and
  [`chart`](../refmans/gui/viselements/generic/chart.md)` controls both have native support for
  these tabular data types as well.
- The new `taipy.import_scenario()^` function can be used to import a scenario from an exported
  archive. For more information, please refer to
  [Import a scenario](../userman/scenario_features/sdm/scenario/index.md#import-a-scenario).
- The default application template now supports authentication and authorization features.

## Improvements and changes

- The `taipy.export_scenario()^` function now supports exporting file-based data nodes' data to the
  export folder if the path exists.
- The `taipy.export_scenario()^` function now exports a zip archive instead of a
  folder. For more information, please refer to
  [Export a scenario](../userman/scenario_features/sdm/scenario/index.md#export-a-scenario).
- The `taipy.export_scenario()^` function now raises the `ExportPathAlreadyExists^`
  exception if the export path already exists. You can explicitly set the *overwrite* parameter to
  True to overwrite the existing export path. For more information, please refer to
  [Export a scenario](../userman/scenario_features/sdm/scenario/index.md#export-a-scenario).
