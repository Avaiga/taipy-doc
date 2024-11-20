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

Published on 2024-10.

[`taipy` 4.0](https://pypi.org/project/taipy/4.0.1/) depends on the latest
[`taipy-common` 4.0](https://pypi.org/project/taipy-common/4.0.1/),
[`taipy-gui` 4.0](https://pypi.org/project/taipy-gui/4.0.1/),
[`taipy-core` 4.0](https://pypi.org/project/taipy-core/4.0.1/),
[`taipy-templates` 4.0](https://pypi.org/project/taipy-templates/4.0.1/), and
[`taipy-rest` 4.0](https://pypi.org/project/taipy-rest/4.0.1/) packages.

!!! warning "Upgrading to Taipy 4.0 from 3.x"

    Due to changes in Taipy’s package structure in version 4.0, the previous version of the
    `taipy-config` package may not be automatically removed during the upgrade process. This could
    lead to runtime issues as the system may attempt to reference outdated dependencies.

    To ensure a clean installation, please manually uninstall Taipy 3.x and then install a fresh
    Taipy 4.0.

## New Features

<h4><strong><code>taipy</code></strong> 4.0.0</h4>

The User Experience of the Scenario and Data management controls have been greatly improved by the
following new functionalities:

- [*Scenario Selector*](../refmans/gui/viselements/corelements/scenario_selector.md):
    - Multiple selection is now available.<br/>
      See the [*multiple*](../refmans/gui/viselements/corelements/scenario_selector.md#p-multiple)
      property for more details.
    - A filter capability has been added to the scenario selector: TODO add details
    - A sort capability has been added to the scenario selector: TODO add details
    - A search capability has been added to the scenario selector: TODO add details
- [*Data Node Selector*](../refmans/gui/viselements/corelements/data_node_selector.md):
    - Multiple selection is now available.<br/>
      See the [*multiple*](../refmans/gui/viselements/corelements/data_node_selector.md#p-multiple)
      property for more details.
    - Users can now filter data nodes in the list.<br/>
      See the
      [section on Filtering](../refmans/gui/viselements/corelements/data_node_selector.md#filtering)
      for more details.
    - Users can now sort data nodes in the list.<br/>
      See the
      [section on Sorting](../refmans/gui/viselements/corelements/data_node_selector.md#sorting) for
      more details.
    - Users can now search data nodes in the list<br/>
      See the
      [section on Searching](../refmans/gui/viselements/corelements/data_node_selector.md#searching)
      for more details.
- [*Data Node Viewer*](../refmans/gui/viselements/corelements/data_node.md):
    - Users can now upload and download data of file-based data nodes.
- [*Job Selector*](../refmans/gui/viselements/corelements/job_selector.md):
    - A new detail panel has been added to the job selector.

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
    - A new property, [*use_checkbox*](../refmans/gui/viselements/generic/table.md#p-use_checkbox),
      can be set to True to display checkboxes in cells containing Boolean values.<br/>
      This significantly reduces the rendering time for large tables with Boolean columns.
- You can define CSS rules for individual pages using the new *style* parameter of the `Page^`
  class or via the `Page.set_style()^` method.<br/>
  See the [section on Styling](../userman/gui/styling/index.md#style-sheets) for more
  information.
- *List-of-values* can now be built directly from enumeration classes.<br/>
  See [the section on enumerated LoVs](../userman/gui/binding.md#lovs-as-enumeration) for more
  information.

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- The `taipy.get_scenarios()` and `taipy.get_primary_scenarios()^` methods now accept optional
  parameters to:
      - sort the output list of scenarios by name, id, creation date, or tag
      - filter the output list of scenarios that are created in a specific time range.<br/>
  See [issue #393](https://github.com/Avaiga/taipy/issues/393).<br/>
  For more information, please refer to
  [Get all scenarios](../userman/scenario_features/sdm/scenario/index.md#get-all-scenarios) and
  [Get primary scenarios](../userman/scenario_features/sdm/scenario/index.md#get-primary-scenarios).

- The `Job^` and `Submission^` entities have new attributes based on the record of job
  status changes. For more information on job statuses, please refer to
  [Job Status](../userman/scenario_features/sdm/job/index.md#job-status). </br>
  See [issue #1704](https://github.com/Avaiga/taipy/issues/1704) and
  [issue #1544](https://github.com/Avaiga/taipy/issues/1544).
      - The `Job^` entity exposes the following timestamp attributes: *submitted_at*, *run_at*,
        *finished_at*.
      - The `Job^` entity exposes the following duration attributes: *execution_duration*,
        *pending_duration*, and *blocked_duration*.
      - The `Submission^` entity exposes the following timestamp attributes: *submitted_at*,
      *run_at*, *finished_at*.
      - The `Submission^` entity exposes the *execution_duration* attribute.

  - Expose an Abstract class `CoreEventConsumerBase^` to implement a custom event consumer.<br/>
    See [issue #405](https://github.com/Avaiga/taipy/issues/405).<br/>
    A consumer can be used to listen to Taipy events (mainly CRUD operations on Taipy
    entities) and react to them. For more information, please refer to the
    [Track activities and Trigger actions](../userman/scenario_features/events/index.md)
    documentation page.

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- Creating a new application using any template now also supports initializing the application
  as a Git repository.

## Improvements and changes

<h4><strong><code>taipy</code></strong> 4.0.1</h4>

- The impact of the
  [*show_properties*](../refmans/gui/viselements/corelements/data_node.md#p-show_properties)
  property of the [`data_node`](../refmans/gui/viselements/corelements/data_node.md) control was
  changed. This property now controls whether or not the "Properties" tab is visible.<br/>
  To show or hide the list of custom properties in the "Properties" tab, you must now use the
  [*show_custom_properties*](../refmans/gui/viselements/corelements/data_node.md#p-show_custom_properties)
  property.

<h4>4.0.0</h4>

- Taipy and all its dependencies now stop support Python 3.8.<br/>
  The minimum supported Python version is now 3.9.
- Taipy package structure has been reorganized. The dependency on `taipy-config` has been
  removed. Taipy now depends on a new `taipy-common` package that includes the configuration
  features among the common code shared by all `taipy`, `taipy-gui`, and `taipy-core` packages.

<h4><strong><code>taipy-gui</code></strong> 4.0.0</h4>

- Setting up styling:<br/>
  If a file named `taipy.css` is located in the same directory as the Python script (`<app>.py`)
  running a Taipy GUI application, and no `<app>.css` file exists in the same location, this CSS
  file will be loaded and applied to all pages. This enables sharing styles across different Taipy
  GUI applications.<br/>
  See [issue #1597](https://github.com/Avaiga/taipy/issues/1597) for more details and the
  [section on Styling](../userman/gui/styling/index.md#style-sheets).
- The *style* and *style[column_name]* properties of the
  [`table`](../refmans/gui/viselements/generic/table.md) control have been
  renamed to [*row_class_name*](../refmans/gui/viselements/generic/table.md#p-row_class_name) and
  [*cell_class_name[column_name]*](../refmans/gui/viselements/generic/table.md#p-cell_class_name[column_name]),
  respectively. A warning message is issued if you use these properties.
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
      API to simplify dynamic generation.<br/>
      See [issue #1379](https://github.com/Avaiga/taipy/issues/1379).
    - Controls defined with the Page Builder API have an additional property called *inline* which,
      when set to True, will not generate a line skip, to facilitate layout.<br/>
      See [issue #1725](https://github.com/Avaiga/taipy/issues/1725).
- The configuration of the `Gui^` object was improved for easier deployment:
    - The [*port*](../userman/advanced_features/configuration/gui-config.md#p-port) configuration
      parameter can now be set to "auto". When `Gui.run()^` is executed with this setting, it will
      attempt to find an available port by automatically trying different port numbers.
    - A new configuration parameter,
      [*port_auto_ranges*](../userman/advanced_features/configuration/gui-config.md#p-port_auto_ranges),
      allows specifying the range of port numbers that Taipy GUI will search when
      [*port*](../userman/advanced_features/configuration/gui-config.md#p-port) is set to "auto".

<h4><strong><code>taipy-core</code></strong> 4.0.0 </h4>

- In standalone job execution mode, the default value of *max_nb_of_workers* is now 2 instead of 1.
  For more information, please refer to
  [Job execution configuration](../userman/advanced_features/configuration/job-config.md).
- In standalone job execution mode, the workers are started in a separate process are now
  started in "spawn" *mp_context* instead of the default from the system.
- The `Core` service has been deprecated and renamed `Orchestrator`. The `Core` service is still
  available for backward compatibility but will be removed in a future release.<br/>
  See [issue #1567](https://github.com/Avaiga/taipy/issues/1567).
- When using the Taipy command-line interface, if an unsupported argument is provided, the CLI
  will display a message indicating the invalid argument. If the invalid argument is possibly a
  typo, the CLI will suggest the closest valid argument.
- The `Scenario.export()` and `taipy.export_scenario()` functions have been transferred from the
  Community edition to the Enterprise edition as it is more suitable for enterprise applications.
- The production mode and the migration configuration of the version management system has been
  transferred from the Community edition to the Enterprise edition as it is more suitable for
  enterprise applications.
- Support for the SQL repository was removed. Taipy Community edition now only supports the
  `filesystem` repository type.<br/>
  See [issue #1513](https://github.com/Avaiga/taipy/issues/1513).
- Support for different encodings in `S3ObjectDataNode^`.<br/>
  See [issue #680](https://github.com/Avaiga/taipy/issues/680).
- Reading an `ExcelDataNode^` is more consistent across the various expose types.<br/>
  See [issue #796](https://github.com/Avaiga/taipy/issues/796).
- Two scenarios belonging to the same cycle can now have the same tag.<br/>
  See [issue #1292](https://github.com/Avaiga/taipy/issues/1292).<br/>
- The custom properties of a `Scenario` are not exposed as attribute anymore.<br/>
  See [issue #1572](https://github.com/Avaiga/taipy/issues/1572).
- Methods and functions returning a Boolean value and related to entities now return
  a `ReasonCollection^` object, which is a set of `Reason^` instances. Each reason contains a message
  explaining why the returned value is `False`. The collection is empty if the value is `True`
  .<br/>
  Examples: `is_deletable()^`, `exists()^`, `is_readable()^` etc.
  See [issue #1568](https://github.com/Avaiga/taipy/issues/1568).
- The `Config.check()^` method now raises `ERROR` issues if any data node, task, or sequence of
  a `ScenarioConfig^` has the same configuration id as another one in the same `ScenarioConfig^`,
  or any additional property of any configuration has the same name as one of the attributes
  of the configuration class.<br/>
  See [issue #1696](https://github.com/Avaiga/taipy/issues/1696) and
  [issue #411](https://github.com/Avaiga/taipy/issues/411).<br/>
  For more information on checkers, please refer to
  [Configuration checker](../userman/advanced_features/configuration/config-checker.md).

<h4><strong><code>taipy-templates</code></strong> 4.0.0 </h4>

- The *--template* option of the `taipy create` command is now renamed to *--application* option
  to correctly reflect the application template to use when creating a new Taipy application.<br/>
  See [issue #1472](https://github.com/Avaiga/taipy/issues/1472).

## Significant bug fixes

<h4><strong><code>taipy</code></strong> 4.0.1</h4>

- Scenario selection becomes impossible in the `scenario_selector` control after creating a new
  Scenario.<br/>
  See [issue #2169](https://github.com/Avaiga/taipy/issues/2169).
- The Delete button of the "Edit scenario" dialog of the `scenario_selector` control is disabled 
  when it should not be.<br/>
  See [issue #1995](https://github.com/Avaiga/taipy/issues/1995).
- A warning is issued when a scenario is created from the `scenario_selector` control.<br/>
  See [issue #2009](https://github.com/Avaiga/taipy/issues/2009).
- Scenario management controls may not be fully recognized by linters or auto-completion features in
  some IDEs.<br/>
  See [issue #1620](https://github.com/Avaiga/taipy/issues/1620).

<h4><strong><code>taipy-gui</code></strong> 4.0.1</h4>

- The `-H` command line option is broken.<br/>
  You must use the long `--host` option instead to specify the server hostname.
- The *id* and *payload* parameters of the `on_action` callback functions are swapped.<br/>
  See [issue #2045](https://github.com/Avaiga/taipy/issues/2045).
- The chart control refresh may stop rendering automatically if too many data changes are
  requested. The page must be refreshed manually.<br/>
  See [issue #1992](https://github.com/Avaiga/taipy/issues/1992).
- Aggregation in a table control may raise an error if the table has columns holding dates.<br/>
  See [issue #1994](https://github.com/Avaiga/taipy/issues/1994).
- Table columns are too narrow if there are many.<br/>
  See [issue #2082](https://github.com/Avaiga/taipy/issues/2082).
- Styling is not applied to a [`table`](../refmans/gui/viselements/generic/table.md) control if its
  [*rebuild*](../refmans/gui/viselements/generic/table.md#p-rebuild) property is set to
  True.<br/>
  See [issue #2005](https://github.com/Avaiga/taipy/issues/2005).

<h4>4.0.0</h4>

- The value of multiline [`input`](../refmans/gui/viselements/generic/input.md) controls is
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
- Reload the cache on all *_build_manager()* methods when the *repository_type* is changed.<br/>
  See [issue #1692](https://github.com/Avaiga/taipy/pull/1692)

<h4><strong><code>taipy-templates</code></strong> 4.0.0</h4>
- The first cli option of the `taipy create` command is skipped if it's before the positional
  argument. <br/>
  See [issue #1687](https://github.com/Avaiga/taipy/issues/1687).

# Enterprise edition: 4.0

Published on 2024-10.

This release contains all of [`taipy` 4.0](https://pypi.org/project/taipy/4.0.1) as well as
additional features.

## New Features

- Authentication now supports
  [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)
  including SSO and GUI integration.<br/>
  TODO - Documentation is in progress.
- Support for [Polars DataFrame Library](https://docs.pola.rs/).<br/>
  Tabular data nodes (`CSVDataNode^`, `ParquetDataNode^`, `ExcelDataNode^`, `SQLTableDataNode^`,
  and `SQLDataNode^`) can now expose the data as Polars objects. They all support
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

- The `taipy.export_scenario()^` function now:
    - exports a zip archive instead of a folder.
    - supports exporting file-based data nodes' data to the exported archive if the path exists.
    - raises the `ExportPathAlreadyExists^`
        exception if the export path already exists. You can explicitly set the *overwrite* parameter to
        True to overwrite the existing export path.
    For more information, please refer to
    [Export a scenario](../userman/scenario_features/sdm/scenario/index.md#export-a-scenario).
