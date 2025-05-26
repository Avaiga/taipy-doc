---
title: Release Notes for version 2.2
---

These are the updates and changes introduced in Taipy version 2.2.

!!! note "Unsupported version"

    Version 2.2 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

Published on 2023-04.

[`taipy` 2.2](https://pypi.org/project/taipy/2.2.0/) contains the latest
[`taipy-config` 2.2](https://pypi.org/project/taipy-config/2.2.0/),
[`taipy-gui` 2.2](https://pypi.org/project/taipy-gui/2.2.1/),
[`taipy-core` 2.2](https://pypi.org/project/taipy-core/2.2.2/) and
[`taipy-rest` 2.2](https://pypi.org/project/taipy-rest/2.2.1/) packages.

# <strong><code>taipy-gui</code></strong>

## 2.2.0

<h4>New features</h4>

- :octicons-feed-plus-16:{ .plus-icon title="New feature" } A default set of stylesheets are installed with Taipy GUI
  so that, by default, applications benefit from a homogeneous and good-looking
  style. This is called the [Stylekit](../../userman/gui/styling/stylekit.md).<br/>
  The Stylekit can be easily customized to fit your application design's
  requirements.
- :octicons-feed-plus-16:{ .plus-icon title="New feature" } The [`table`](../../refmans/gui/viselements/generic/table.md)
  and [`chart`](../../refmans/gui/viselements/generic/chart.md) controls have a new property called
  *rebuild* that can be used if you need to entirely change the
  data they rely on, including their structure.

<h4>Improvements and changes</h4>

- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The default property name for the
  [`part` block](../../refmans/gui/viselements/generic/part.md)
  was changed from *render* to *class_name* to allow for directly using the
  style classes from the [Stylekit](../../userman/gui/styling/stylekit.md).<br/>
  Please check the section on
  [Styled Sections](../../userman/gui/styling/stylekit.md#styled-sections) for
  more information.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The
  [`expandable` block](../../refmans/gui/viselements/generic/expandable.md) has a new property
  called *on_change* enabling to set a specific callback when the block is expanded
  or collapsed.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Better error messages when parsing Markdown content.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} Better support for auto-completion in IDE for the
  `Gui.run()^` configuration parameters, based on a generated Python Interface Definition file.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The *status* entry point now provides information
  about the loaded element libraries and the elements they define.
- :octicons-feed-rocket-16:{ .rocket-icon title="Improvement"} The `navigate()^` function and the *page* property
  of the [`part` block](../../refmans/gui/viselements/generic/part.md) can now use, as their
  target, any URL. In the context of a `part` block, the page will be rendered in an *iframe*.<br/>
  See [issue #621](https://github.com/Avaiga/taipy-gui/issues/621).

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } Bound variable scope issues fixed when used by
  elements defined at the root page level.<br/>
  See [issue #583](https://github.com/Avaiga/taipy-gui/issues/583).
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } Filters management fixed in the
  [`table` controls](../../refmans/gui/viselements/generic/table.md).<br/>
  See [issue #667](https://github.com/Avaiga/taipy-gui/issues/667).
- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } Communication with the server may break.<br/>
  See [issue #695](https://github.com/Avaiga/taipy-gui/issues/695).

# <strong><code>taipy-core</code></strong>

## 2.2.3

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } Error raised when running Orchestrator service in
  development mode after a function rename in the Config.<br/>
  See [issue #560](https://github.com/Avaiga/taipy-core/issues/560).

## 2.2.2

<h4>Deprecations</h4>

- :octicons-alert-fill-24:{ .alert-icon title="Deprecation" } PostgreSQL and MySQL engines do not support
  "driver" argument.<br/>
  See [issue #544](https://github.com/Avaiga/taipy-core/issues/544).<br/>
  To avoid conflict between engines, the default value of the _db_driver_ parameter in a
  SQL or a SQL table data node configuration has been removed.
