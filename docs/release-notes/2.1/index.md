---
title: Release Notes for version 2.1
---

These are the updates and changes introduced in Taipy version 2.1.

!!! note "Unsupported version"

    Version 2.1 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

Published on 2023-01.

[`taipy` 2.1](https://pypi.org/project/taipy/2.1.0/) contains the latest
[`taipy-config` 2.1](https://pypi.org/project/taipy-config/2.1.0/),
[`taipy-gui` 2.1](https://pypi.org/project/taipy-gui/2.1.0/),
[`taipy-core` 2.1](https://pypi.org/project/taipy-core/2.1.0/) and
[`taipy-rest` 2.1](https://pypi.org/project/taipy-rest/2.1.0/) packages.

Please refer to the [Migration page](../migration.md#from-20-to-21) for
details on how to migrate from version older than 2.1.

# <strong><code>taipy</code></strong>

## 2.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Taipy and all its dependencies
  now support Python 3.11.<br/>
  See [Python documentation](https://docs.python.org/3/whatsnew/3.11.html) for details.

# <strong><code>taipy-gui</code></strong>

## 2.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A security feature has been added: the file
  `.taipyignore`, located next to the Python main file, can list the paths that you want
  to prevent access to.<br/>
  See [issue #501](https://github.com/Avaiga/taipy-gui/issues/501) or
  [this section](../../userman/advanced_features/configuration/gui-config.md#protect-your-application-files)
  for details.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Charts can use the new `Decimator^` class to
  cleverly filter data points out to significantly improve performance.<br/>
  See the paragraph on [large datasets](../../refmans/gui/viselements/generic/chart.md#large-datasets)
  for specific information.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Charts now support polar, funnel, candlesticks and
  many other types of charts.<br/>
  See the [chart control](../../refmans/gui/viselements/generic/chart.md) section for details.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Charts now support the dark theme automatically.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Tooltips can be set on individual table cells.<br/>
  See the [example](../../refmans/gui/viselements/generic/table.md#cell-tooltips) for more
  information.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" }
  [Long running callbacks](../../userman/gui/callbacks.md#long-running-callbacks)
  have been improved to allow for easily returning a value.<br/>
  See the documentation of the `invoke_long_callback()^` function or the
  [issue #547](https://github.com/Avaiga/taipy-gui/issues/547) for more details.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Developers can specify the location of the Taipy
  webapp, for debugging purposes.<br/>
  The `--webapp-path` command line option allows to specify that location.<br/>
  See [issue #564](https://github.com/Avaiga/taipy-gui/issues/564).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The Pie charts now use the *values* property
  to set values instead of *x*.<br/>
  See [Pie charts](../../refmans/gui/viselements/generic/charts/pie.md) for details.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Unselected data points or traces in charts now preserve
  their original opacity.<br/>
  See [issue #496](https://github.com/Avaiga/taipy-gui/issues/496).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} `class_name` is now a dynamic property.<br/>
  See [issue #480](https://github.com/Avaiga/taipy-gui/issues/480).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The *allow_unsafe_werkzeug* option of
  [Werkzeug](https://werkzeug.palletsprojects.com/)
  (that [Flask](https://flask.palletsprojects.com/) depends on for the WSGI part) is forced
  to True when the Gui instance is run in Debug mode, because of a change in policy in
  recent updates.

# <strong><code>taipy-core</code></strong>

## 2.1.2

<h4>Significant bug fixes</h4>

- :octicons-bug-24:{ .bug-icon title="Bug fix" } The version required for
  [openpyxl](https://openpyxl.readthedocs.io/en/stable/) has been downgraded from
  "openpyxl>=3.0.7,<4.0" to "openpyxl>=3.0.7,<3.1" to match the version used by
  [Modin](https://modin.readthedocs.io/en/stable/).

## 2.1.1

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Add overload type descriptions for the
  `taipy.get()` method that supports multiple different combinations of argument types.

## 2.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New version management system for Taipy
  applications. Users can now run an application in development mode, save a version of
  the application as an experiment version, re-run older experiment versions, and push a
  version to production.<br/>
  See the [Version management system](../../userman/advanced_features/versioning/index.md)
  documentation page for more details.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New data node named
  [MongoCollectionDataNode](../../userman/scenario_features/data-integration/data-node-config.md#mongo-collection).
  It represents the data from a MongoDB collection.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New data node named
  [ParquetDataNode](../../userman/scenario_features/data-integration/data-node-config.md#parquet).
  It represents tabular data stored in the Apache Parquet format.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Added support for
  [Modin](https://modin.readthedocs.io/en/stable/) as a new exposed type.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Running the Orchestrator service is required to execute
  jobs. See `Orchestrator().run()^` method.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The parent entities of a data node, a task, or a
  pipeline can be accessed via `DataNode.get_parents()^`, `Task.get_parents()^`, or
  `Pipeline.get_parents()^`, or by passing the
  data node entity, task entity or pipeline entity to the function `taipy.get_parents()^`.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New data node property *expiration_date* computed adding
  the *validity_period* duration to the *last_edit_date* of the data node.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New data node property *is_up_to_date* equals to `True` if
  the data node has not expired (refer to *expiration_date* attribute). `False` otherwise.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The **sql** *repository_type* is now available on community
  edition to store Taipy entities in an
  SQL database.

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The *last_edit_date* attribute of a data node is now
  updated when the corresponding data is modified by either a Taipy task execution or an external
  factor. This behavior is limited to file-based data nodes: CSV, Excel, JSON, and pickle data
  nodes only.

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } Deprecation of the data node *cacheable* property. It is
  replaced by *skippable* property on tasks.
  The mechanism remains unchanged but instead of setting *cacheable* property to `True` for all the
  outputs of a task that can be skipped, just set the task *skippable* property to `True`.
