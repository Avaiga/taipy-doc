---
title: Release Notes for version 4.2
---

These are the updates and changes introduced in Taipy version 4.2.

!!! note "Migration"

    Please refer to the [Upgrading page](../../userman/operations/upgrading/index.md) for potential
    migration paths for your applications implemented on legacy Taipy versions.

This version is in progress and has not been released yet.

# <strong><code>taipy</code></strong>

# <strong><code>taipy-gui</code></strong>

## 4.2.0

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`number`](../../refmans/gui/viselements/generic/number.md) control
  has a new property called *integer* that, if set to True, enforces numerical
  values to be integers.<br/>
  See [issue #2698](https://github.com/Avaiga/taipy/issues/2698).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The *unselected_value*
  property of the [`toggle`](../../refmans/gui/viselements/generic/toggle.md)
  control has been removed.<br/>
  When no item is selected, the
  [*value*](../../refmans/gui/viselements/generic/toggle.md#p-value) property is now set to None.

# <strong><code>taipy-core</code></strong>

## 4.2.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A scenario can now be
  duplicated with the `Scenario.duplicate()^` method.<br/>
  See [issue #397](https://github.com/Avaiga/taipy/issues/397).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The `ScenarioConfig^`
  class now exposes a new method `ScenarioConfig.draw()^` to export the scenario
  configuration graph as a PNG file.<br/>
  See [issue #1592](https://github.com/Avaiga/taipy/issues/1592).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The `CSVDataNode^`
  now supports the *separator* parameter to specify the separator used in the CSV file.<br/>
  See [issue #2603](https://github.com/Avaiga/taipy/issues/2603).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} `S3ObjectDataNode^`
  now supports all the parameters of the AWS APIs.<br/>
  See [issue #1858](https://github.com/Avaiga/taipy/issues/1858).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} `SQLDataNode^` now
  supports creating read-only or write-only data nodes by providing only the relevant
  parameter: either *read_query* for read-only or *write_query_builder* for write-only.
  At least one of the two parameters must be provided.<br/>
  See [issue #2616](https://github.com/Avaiga/taipy/issues/2616).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement" } The *root_folder* has been
  removed from the `CoreSection^` class.
  Please refer to the
  [Core configuration page](../../userman/advanced_features/configuration/core-config.md) for
  details.<br/>
  See [issue #2801](https://github.com/Avaiga/taipy/issues/2801).

<h4>Significant bug fixes</h4>

- :octicons-bug-24:{ .bug-icon title="Bug fix" } The `DataNode^` class now correctly
  handles the `editor_id` parameter when writing data.<br/>
  See [issue #2017](https://github.com/Avaiga/taipy/issues/2017).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } When the DAG of a `Scenario^` or a
  `Sequence^` is not valid, an error message is now logged before raising the
  `InvalidSequence^` exception.<br/>
  See [issue #2322](https://github.com/Avaiga/taipy/issues/2322).
- :octicons-bug-24:{ .bug-icon title="Bug fix" } Taipy now only checks the compatibility
  of the installed `taipy-core` version with the versions set in the existing entities
  when the application runs either in experiment or in production mode.<br/>
  See [issue #2420](https://github.com/Avaiga/taipy/issues/2420).

# <strong><code>taipy-templates</code></strong>

## 4.2.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new application template
  named "classification" is available. For more information on creating a new Taipy
  application with the new "classification" template, refer to
  [Classification application template](../../tp_templates/applications/classification_app.md).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New page templates are available
  for creating new pages on top of existing applications. For more information on creating
  new pages with the new page templates, refer to
  [Page templates](../../tp_templates/index.md#page-templates).

# <strong><code>taipy-enterprise</code></strong>

## 4.2.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } New data node named
  [AzureBlobDataNode](../../userman/advanced_features/3rd-party-integration/azure.md#azure-blob-data-node).
  It represents data from a blob in Azure Blob Storage.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } File-based DataNode (including
  `CSVDataNode^`, `ExcelDataNode^`, `JSONDataNode^`, `PickleDataNode^`, and `ParquetDataNode^`)
  now support URL that points to a file in Azure Blob Storage as the path. See
  [Azure File-based Data Node](../../userman/advanced_features/3rd-party-integration/azure.md#azure-file-based-data-node)
  for more details.

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The `SystemCredentials^`
  class can now be used to authorize for administrative actions when there is no authenticated
  user. See the page on authorizing code with
  [SystemCredentials](../../userman/advanced_features/auth/authorization.md#authorize-with-systemcredentials)
  for more details.

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The `Orchestrator^` service can
  now be run with a specific `Credentials^` instead of the default `SystemCredentials^`. See the
  page on how to run the Orchestrator service with
  [specific Credentials](../../userman/advanced_features/auth/authorization.md#run-the-orchestrator-service-with-specific-credentials)
  for more details.
