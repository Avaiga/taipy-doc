---
title: Release Notes for version 1.1
---

This is the list of changes of taipy version 1.1.

!!! note "Unsupported version"

    Version 1.1 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

Published on 2022-06.

[`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/) contains the latest
[`taipy-gui` 1.1](https://pypi.org/project/taipy-gui/1.1.0/),
[`taipy-core` 1.1](https://pypi.org/project/taipy-core/1.1.0/) and
[`taipy-rest` 1.1](https://pypi.org/project/taipy-rest/1.1.0/) packages.


# <strong><code>taipy-gui</code></strong>

## 1.1.3

- :octicons-feed-rocket-16:{ .rocket-icon } The client-server communication settings are extended
  to accommodate various Flask deployment scenarios.<br/>
  See the documentation for the *async_mode* parameter to `Gui.run()^` for more information.
- :octicons-feed-rocket-16:{ .rocket-icon } Implicit re-run of the `Gui^` instance in Notebook
  environments.<br/>
  See [issue #320](https://github.com/Avaiga/taipy-gui/issues/320).
- :octicons-feed-rocket-16:{ .rocket-icon } Test server/client versions for safe
  interoperability.<br/>
  See [issue #323](https://github.com/Avaiga/taipy-gui/issues/323).
- :octicons-feed-rocket-16:{ .rocket-icon } Allow the edition of specific table columns.<br/>
  See [issue #366](https://github.com/Avaiga/taipy-gui/issues/366).
- :octicons-bug-24:{ .bug-icon } Error fixed when modifying a State dictionary entry
  in a callback.<br/>
  See [issue #356](https://github.com/Avaiga/taipy-gui/issues/356).
- :octicons-bug-24:{ .bug-icon } Boolean values not editable in tables.<br/>
  See [issue #365](https://github.com/Avaiga/taipy-gui/issues/365).
- :octicons-bug-24:{ .bug-icon } Crash fixed when using a dictionary in the labels property
  of the slider control.<br/>
  See [issue #379](https://github.com/Avaiga/taipy-gui/issues/379).

## 1.1.0

- :octicons-feed-rocket-16:{ .rocket-icon } The `State^` instance can be initialized in a
  user-defined function. See the _on_init_ attribute of the `Gui^` class for more details.
- :octicons-feed-rocket-16:{ .rocket-icon } Page definitions and the bound variables can be
  isolated in a module to clarify the application code organization.<br/>
  See this <a href="javascript:void(0)">section</a> for details.
- :octicons-feed-rocket-16:{ .rocket-icon } The <a href="javascript:void(0)">chart</a> control
  can display geo-referenced data on top of maps.<br/>
  See this <a href="javascript:void(0)">example</a>
  for details.
- :octicons-feed-rocket-16:{ .rocket-icon }- The <a href="javascript:void(0)">input</a> and
  <a href="javascript:void(0)">slider</a> controls have a new _change_delay_ property that lets
  you tune how fast you want to propagate changes.<br/>
  This allows for a better user experience.
- :octicons-feed-rocket-16:{ .rocket-icon } The <a href="javascript:void(0)">input</a> control
  has a new _password_ property that, if True, obscures the user input.
- :octicons-feed-rocket-16:{ .rocket-icon } The <a href="javascript:void(0)">input</a>,
  <a href="javascript:void(0)">number</a> and
  <a href="javascript:void(0)">selector</a> controls have a
  new _label_ property that lets you display a label inside the control.
- :octicons-feed-rocket-16:{ .rocket-icon } The <a href="javascript:void(0)">layout</a> block has new
  syntax that makes it easier to define a repetition of a column definition.
- :octicons-feed-rocket-16:{ .rocket-icon } Support for multiple assignments to variables in *on_change()*.
- :octicons-bug-24:{ .bug-icon } Concurrency issues were fixed.
- :octicons-bug-24:{ .bug-icon } The [_attr_list_](https://python-markdown.github.io/extensions/attr_list)
  extension can be used to style individual Markdown elements without the need
  for a CSS file.<br/>
  See [issue #185](https://github.com/Avaiga/taipy-gui/issues/185).
- :octicons-bug-24:{ .bug-icon } Taipy supports HTTPS via reverse proxies.<br/>
  See [issue #263](https://github.com/Avaiga/taipy-gui/issues/263).

# <strong><code>taipy-core</code></strong>

## 1.1.0

- :octicons-feed-rocket-16:{ .rocket-icon } Execution modes: "_development_" mode (default) runs tasks
  in a synchronous way one task at
  a time, while "_standalone_" mode runs tasks in an asynchronous and parallel way using
  sub-processes.
- :octicons-feed-rocket-16:{ .rocket-icon } _Retry policy_ to read entities: the global configuration
  attribute _retry_read_entity_ indicates the number of times Taipy will retry in case of error.
- :octicons-feed-rocket-16:{ .rocket-icon } Performance improvements when reading and writing entities.
- :octicons-alert-fill-24:{ .alert-icon } The _path_ attribute of `DataNodeConfig`,
  for CSV, Excel and Pickle types is now deprecated.<br/>
  _default_path_ must be used instead: it is the default path to use when
  instantiating a data node from the config. Note that the attribute in the
  `DataNode` entity is still called _path_.
- :octicons-alert-fill-24:{ .alert-icon } The _last_edition_date_ attribute of data nodes
  is now deprecated.<br/>
  _last_edit_date_ must be used instead.
- :octicons-alert-fill-24:{ .alert-icon } The _edition_in_progress_ attribute of data nodes
  is now deprecated.<br/>
  _edit_in_progress_ must be used instead.

# <strong><code>taipy-enterprise</code></strong>

## 1.1.0

- :octicons-feed-plus-16:{ .plus-icon } User authentication.
- :octicons-feed-plus-16:{ .plus-icon } Authorization checks for all entities.
- :octicons-feed-plus-16:{ .plus-icon } Job recovery mechanism on application restart.
- :octicons-feed-plus-16:{ .plus-icon } Page generation based on the user's identity.
