---
title: Release Notes for version 4.1
---

These are the updates and changes introduced in Taipy version 4.1.

!!! note "Upgrading to Taipy 4.1"

    Please refer to the [Upgrading page](../../userman/operations/upgrading/index.md) for potential
    migration paths for your applications implemented on legacy Taipy versions.

Published on 2026-02.

`taipy-enterprise` 4.1 depends on the latest
[`taipy` 4.1](https://pypi.org/project/taipy/4.1.1/) package which depends on the latest
[`taipy-common` 4.1](https://pypi.org/project/taipy-common/4.1.1/),
[`taipy-gui` 4.1](https://pypi.org/project/taipy-gui/4.1.1/),
[`taipy-core` 4.1](https://pypi.org/project/taipy-core/4.1.1/),
[`taipy-templates` 4.1](https://pypi.org/project/taipy-templates/4.1.1/), and
[`taipy-rest` 4.1](https://pypi.org/project/taipy-rest/4.1.1/) packages.

# <strong><code>taipy</code></strong>

## 4.1.1

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Pandas version
  dependency has been updated for the latest Python versions. The supported versions
  are:

    - for Python 3.9: From 1.3.5 to 2.2.3 included.
    - for Python versions >= 3.10: Pandas versions >= 2.2.0 and < 3.0.0.


## 4.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } Event management simplification:
  A new `EventProcessor^` class has been introduced to simplify the management of events
  in Taipy.<br/>
  See [issue #2306](https://github.com/Avaiga/taipy/issues/2306).

# <strong><code>taipy-gui</code></strong>

## 4.1.1

<h4>Significant bug fixes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Fix for hover text not working
  with the [`number`](../../refmans/gui/viselements/generic/number.md) element.<br/>
  See [issue #2791](https://github.com/Avaiga/taipy/issues/2791).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`chart`](../../refmans/gui/viselements/generic/chart.md) element performance
  was improved when using the
  [*figure*](../../refmans/gui/viselements/generic/chart.md#the-figure-property) property.<br/>
  See [issue #2716](https://github.com/Avaiga/taipy/issues/2716).

## 4.1.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A mock implementation of `State^`,
  called `MockState^`, is available for testing purposes. You can learn about how tu use this
  class on the
  [_Mocking State in unit tests_ page](../../userman/gui/utilities.md#mocking-state-in-unit-tests).<br/>
  See [issue #2098](https://github.com/Avaiga/taipy/issues/2098).
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The
  [`text`](../../refmans/gui/viselements/generic/text.md) element supports LaTeχ rendering, setting
  the [*mode*](../../refmans/gui/viselements/generic/text.md#p-mode) property to "latex".<br/>
  See [issue #1401](https://github.com/Avaiga/taipy/issues/1401).

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The syntax for creating
  [long running callbacks](../../userman/gui/callbacks.md#long-running-callbacks) can be simplified
  by using the `async ` keyword of Python 3.<br/>
  TODO: Point to the code sample that demonstrates the usage of that feature.<br/>
  See [issue #2288](https://github.com/Avaiga/taipy/issues/2288).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`input`](../../refmans/gui/viselements/generic/input.md) and
  [`number`](../../refmans/gui/viselements/generic/number.md) elements now trigger the `on_change`
  callback if the new
  [*action_on_blur*](../../refmans/gui/viselements/generic/input.md#p-action_on_blur) property is
  set to True.<br/>
  See [issue #2023](https://github.com/Avaiga/taipy/issues/2023).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`selector`](../../refmans/gui/viselements/generic/selector.md) element supports multiple
  selection when configured as a dropdown selector.<br/>
  See [issue #1834](https://github.com/Avaiga/taipy/issues/1834).
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`chat`](../../refmans/gui/viselements/generic/chat.md) element supports images in text areas.<br/>
  See [issue #1314](https://github.com/Avaiga/taipy/issues/1314).

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
