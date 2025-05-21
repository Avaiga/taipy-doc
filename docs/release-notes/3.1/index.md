---
title: Release Notes for version 3.1
---

This is the list of changes of taipy version 3.1.


Published on 2024-03.

[`taipy` 3.1](https://pypi.org/project/taipy/3.1.1/) contains the latest
[`taipy-config` 3.1](https://pypi.org/project/taipy-config/3.1.1/),
[`taipy-gui` 3.1](https://pypi.org/project/taipy-gui/3.1.4/),
[`taipy-core` 3.1](https://pypi.org/project/taipy-core/3.1.1/),
[`taipy-templates` 3.1](https://pypi.org/project/taipy-templates/3.1.1/), and
[`taipy-rest` 3.1](https://pypi.org/project/taipy-rest/3.1.1/) packages.

# <strong><code>taipy</code></strong>

## 3.1.1
- :octicons-bug-24:{ .bug-icon } Data is not shown or not automatically refreshed in
  [Data Node viewer](../../refmans/gui/viselements/corelements/data_node.md).<br/>
  See [issue #908](https://github.com/Avaiga/taipy/issues/908) and
  [issue #950](https://github.com/Avaiga/taipy/issues/950).
- :octicons-bug-24:{ .bug-icon } Data Nodes holding dates may not show in
  [Data Node viewers](../../refmans/gui/viselements/corelements/data_node.md).<br/>
  See [issue #1043](https://github.com/Avaiga/taipy/issues/1043).

## 3.1.0

- :octicons-feed-plus-16:{ .plus-icon } Taipy and all its dependencies
  now support Python 3.12.<br/>
  See [Python documentation](https://docs.python.org/3/whatsnew/3.12.html) for details.
- :octicons-rocket-16:{ .rocket-icon } Task nodes in the
  [`scenario_dag`](../../refmans/gui/viselements/corelements/scenario_dag.md)
  control dynamically reflect the status of related jobs for the user that submitted the
  scenario or sequences.
- :octicons-rocket-16:{ .rocket-icon } The
  [`scenario`](../../refmans/gui/viselements/corelements/scenario.md) control lets you add,
  modify, and edit sequences.
- :octicons-rocket-16:{ .rocket-icon } The
  [`data_node`](../../refmans/gui/viselements/corelements/data_node.md) control can now
  represent collections.

# <strong><code>taipy-gui</code></strong>

## 3.1.0

- :octicons-feed-plus-16:{ .plus-icon } The
  [`chart`](../../refmans/gui/viselements/generic/chart.md) control has a new property called
  *figure* that expects an instance of `plotly.graph_objects.Figure`. This class is provided
  by the [Plotly Open Source Graphing Library for Python](https://plotly.com/python/) so you
  can create all sorts of graphs in Python.<br/>
  See the [`figure` property](../../refmans/gui/viselements/generic/chart.md#p-figure) of the
  `chart` control and the
  [section on the *figure* property](../../refmans/gui/viselements/generic/chart.md#the-figure-property)
  for more information.
- :octicons-feed-plus-16:{ .plus-icon } The [`part`](../../refmans/gui/viselements/generic/part.md)
  block has a new property called *content* that lets developers integrate any third-party library
  that can generate HTML.<br/> See the documentation for the
  [`part`](../../refmans/gui/viselements/generic/part.md) block and the examples using
  *content providers* for more information.
- :octicons-feed-plus-16:{ .plus-icon } A new control called
  [`date_range`](../../refmans/gui/viselements/generic/date_range.md) is available if
  you need to represent and edit date ranges in your application pages.
- :octicons-feed-plus-16:{ .plus-icon } A new control called
  [`login`](../../refmans/gui/viselements/generic/login.md) is available if you need users
  to authenticate in your application.
- :octicons-rocket-16:{ .rocket-icon } The
  [`table`](../../refmans/gui/viselements/generic/table.md) control supports enumerated
  values. That allows for a better user experience when users edit cell values.<br/>
  See the section on
  [enumerated values in tables](../../refmans/gui/viselements/generic/table.md#enumerated-values)
  for the details.
- :octicons-rocket-16:{ .rocket-icon } The [`toggle`](../../refmans/gui/viselements/generic/toggle.md)
  control appears as a switch button if its
  [*value*](../../refmans/gui/viselements/generic/toggle.md#p-value) property holds a Boolean value.
- :octicons-bug-24:{ .bug-icon } Selectors with dropdown menus cannot be deactivated.<br/>
  See [issue #894](https://github.com/Avaiga/taipy/issues/894).
- :octicons-bug-24:{ .bug-icon } Problems scoping non-global variables used in Partials.<br/>
  See [issue #561](https://github.com/Avaiga/taipy/issues/561).
- :octicons-bug-24:{ .bug-icon } Important error messages are mangled.<br/>
  See [issue #560](https://github.com/Avaiga/taipy/issues/560).

# <strong><code>taipy-core</code></strong>

## 3.1.1

- :octicons-bug-24:{ .bug-icon } The signatures for `Config.configure_sql_data_node()`,
  `Config.configure_s3_object_data_node()`, and `configure_core()` methods are out-of-date.<br/>
  See [issue #1014](https://github.com/Avaiga/taipy/issues/1014).

## 3.1.0
- :octicons-feed-plus-16:{ .plus-icon } The `DataNode.filter()^` method and the
  indexing/filtering style now also support filtering a Numpy array, a list of objects, and a
  list of dictionaries.<br/>
  For more information, please refer to
  [Filter a data node](../../userman/scenario_features/data-integration/data-node-usage.md#filter).
- :octicons-feed-plus-16:{ .plus-icon } You can now append new data to a data node using the
  `DataNode.append()^` method. The method is available for `CSVDataNode`, `ExcelDataNode`,
  `JSONDataNode`, `ParquetDataNode`, `SQLDataNode`, `SQLTableDataNode`, and
  `MongoCollectionDataNode`.<br/>
  For more information, please refer to
  [Append a data node](../../userman/scenario_features/data-integration/data-node-usage.md#append).
- :octicons-feed-plus-16:{ .plus-icon } A new class called `Submission^` holds meta-data (such as
  its status or submission date) related to a submitted entity: `Scenario^`, `Sequence^`, and/or
  `Task^`.<br/>
  The function `taipy.get_latest_submission()^` returns the last submission of a given entity.<br/>
  For more information, please refer to
  [Submission](../../userman/scenario_features/sdm/submission/index.md).
- :octicons-feed-plus-16:{ .plus-icon } `taipy.submit()^`, `Scenario.submit()^`,
  `Sequence.submit()^`, and `Task.submit()^` now return a `Submission^` entity.
- :octicons-feed-plus-16:{ .plus-icon } A new predefined data node named `S3ObjectDataNode^`
  has been implemented.<br/>
  For more information, please refer to
  [S3ObjectDataNode](../../userman/scenario_features/data-integration/data-node-config.md#amazon-web-service-s3-object).
- :octicons-alert-fill-24:{ .alert-icon } The `modin` exposed type as been deprecated. When used,
  a fallback on Pandas is applied.<br/>
  See [issue #631](https://github.com/Avaiga/taipy/issues/631) for details.
- :octicons-rocket-16:{ .rocket-icon } Running twice the Orchestrator service raises an exception
  to prevent running multiple instances at the same time.
- :octicons-rocket-16:{ .rocket-icon } Running the Orchestrator service or creating an entity by
  `taipy.create_scenario()` or `taipy.create_global_data_node()` blocks the configuration from
  being modified.

# <strong><code>taipy-enterprise</code></strong>

## 3.1.0

- :octicons-feed-plus-16:{ .plus-icon } A new job execution mode named *cluster mode*
  is available. It enables to run the jobs on a cluster of dedicated machines in a remote,
  distributed and scalable environment.
