---
title: Release Notes for version 4.1
---

These are the updates and changes introduced in Taipy version 4.1.

!!! note "Upgrading to Taipy 4.1"

    Please refer to the [Upgrading page](../../userman/operations/upgrading/index.md) for potential
    migration paths for your applications implemented on legacy Taipy versions.

Published on 2025-06.

`taipy-enterprise` 4.1 depends on the latest
[`taipy` 4.1](https://pypi.org/project/taipy/4.1.0/) package which depends on the latest
[`taipy-common` 4.1](https://pypi.org/project/taipy-common/4.1.0/),
[`taipy-gui` 4.1](https://pypi.org/project/taipy-gui/4.1.0/),
[`taipy-core` 4.1](https://pypi.org/project/taipy-core/4.1.0/),
[`taipy-templates` 4.1](https://pypi.org/project/taipy-templates/4.1.0/), and
[`taipy-rest` 4.1](https://pypi.org/project/taipy-rest/4.1.0/) packages.

# <strong><code>taipy</code></strong>

## 4.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Event management simplification:
  A new `EventProcessor^` class has been introduced to simplify the management of events
  in Taipy.<br/>
  See [issue #2306](https://github.com/Avaiga/taipy/issues/2306).

# <strong><code>taipy-gui</code></strong>

## 4.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A mock implementation of `State^`,
  called `MockState^`, is available for testing purposes. You can learn about how tu use this
  class on the
  [_Mocking State in unit tests_ page](../../userman/gui/utilities.md#mocking-state-in-unit-tests).<br/>
  See [issue #2098](https://github.com/Avaiga/taipy/issues/2098).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } TODO: https://github.com/Avaiga/taipy/issues/1401

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} TODO: https://github.com/Avaiga/taipy/issues/2288
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} TODO: https://github.com/Avaiga/taipy/issues/2023
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} TODO: https://github.com/Avaiga/taipy/issues/1834
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} TODO: https://github.com/Avaiga/taipy/issues/1314

# <strong><code>taipy-core</code></strong>

## 4.1.0

<h4>Significant bug fixes</h4>

- :octicons-bug-24:{ .bug-icon title="Bug fix" } Global data nodes depending
  on the order of task configs in the scenario config constructor are missing
  some task IDs in the parent_ids attribute. <br/>
  See [issue #2597](https://github.com/Avaiga/taipy/issues/2597).

<h4>Deprecations</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Class
  `CoreEventConsumerBase` has been deprecated in favor of the new API
  `EventProcessor^`.

# <strong><code>taipy-enterprise</code></strong>

## 4.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A new migration function
  has been added to help upgrading to a new production version. This function is designed
  to automatically migrate entities based on changes in the scenario configuration graph
  topology. This includes adding, moving or removing task configurations and/or data node
  configurations from a scenario configuration graph. <br/>
  See `Config.auto_migrate_scenario_graph()^` for more details.<br/>
  Note that renaming task or data node configurations is considered as a deletion and an addition.
  Resulting entities won't keep their IDs or previous attributes. <br/>
  Note that changes in the various configurations' attributes are not automatically migrated. Please refer to
  the `Config.add_migration_function()^` method and the
  [migration](../../userman/operations/versioning/production-mode.md#production-version-with-migration-functions)
  page for more details.
