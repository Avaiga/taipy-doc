---
hide:
  - navigation
---

# Release Notes

This is the list of changes to Taipy releases as they were published.

## Community edition: 1.2 (In progress)

#### Improvements

**`taipy-core`**<br/>1.2.0

   - The data node of a scenario or a pipeline can now be accessed at the scenario or pipeline levels.
   - When submitting a scenario, a pipeline or a task, a list of jobs or a Job will be returned.
   - In standalone mode, a job whose status is `SUBMITTED`, `PENDING`, or `BLOCKED`, can be canceled. When canceling the job, its subsequent jobs will be abandoned. On the other hand, a job whose status is `RUNNING`, `COMPLETED`, `SKIPPED`, `FAILED`, `CANCELED`, or `ABANDONED`, cannot be canceled. When the cancel method is called on a job with its status being either `RUNNING`, `COMPLETED`, or `SKIPPED`, its subsequent jobs will be abandoned while its status remains unchanged.
   - When submitting a scenario, pipeline, or task in standalone mode, the user can use the parameters _wait_ and _timeout_ to wait until the submitted jobs are finished or up to _timeout_ seconds.
   - A primary scenario can be deleted along with its cycle if it is the only scenario in the cycle.

## Community edition: 1.1

Published on 2022-06.

[`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/) contains the latest
[`taipy-gui` 1.1](https://pypi.org/project/taipy-gui/1.1.0/),
[`taipy-core` 1.1](https://pypi.org/project/taipy-core/1.1.0/) and
[`taipy-rest` 1.1](https://pypi.org/project/taipy-rest/1.1.0/) packages.


#### Improvements

**`taipy-gui`**<br/>1.1.0

   - The `State^` instance can be initialized in a user-defined function. See the _on_init_
     attribute of the `Gui^` class for more details.
   - Page definitions and the bound variables can be isolated in a module to clarify the
     application code organization.<br/>
     See this [section](manuals/gui/binding.md#scope-of-variable-binding) for details.
   - The [`chart`](manuals/gui/viselements/chart.md) control can display georeferenced data on top
     of maps.<br/>
     See this [example](manuals/gui/viselements/charts/others.md#plotting-on-a-map) for details.
   - The [`input`](manuals/gui/viselements/input.md) and [`slider`](manuals/gui/viselements/slider.md)
     controls have a new _change_delay_ property that lets you tune how fast you want to propagate
     changes.<br/>
     This allows for a better user experience.
   - The [`input`](manuals/gui/viselements/input.md) control has a new _password_ property that, if True,
     obscures the user input.
   - The [`input`](manuals/gui/viselements/input.md), [`number`](manuals/gui/viselements/number.md) and
     [`selector`](manuals/gui/viselements/selector.md) controls have a new _label_ property that lets you
    display a label inside the control.
   - The [`layout`](manuals/gui/viselements/layout.md) block has new syntax that makes it easier to define
     a repetition of column definition.
   - Support for multiple assignment to variables in _on_change()_.


**`taipy-core`**<br/>1.1.0

   - Execution modes: "_development_" mode (default) runs tasks in a synchronous way one task at
     a time, while "_standalone_" mode runs tasks in an asynchronous and parallel way using
     sub-processes.
   - _Retry policy_ to read entities: the global configuration attribute _retry_read_entity_ indicates
     the number of times Taipy will retry in case of error.
   - Performance improvements when reading and writing entities.

#### Significant bug fixes

**`taipy-gui`**<br/>1.1.0

   - Concurrency issues were fixed.
   - Taipy supports HTTPS via reverse proxies.<br/>
     See [issue](https://github.com/Avaiga/taipy-gui/issues/263).
   - The [_attr_list_](https://python-markdown.github.io/extensions/attr_list) extension can
     be used to style individual Markdown elements without the need for a CSS file.<br/>
     See [issue](https://github.com/Avaiga/taipy-gui/issues/185).

#### Deprecations

**`taipy-core`**<br/>1.1.0

   - The _path_ attribute of `DataNodeConfig`, for CSV, Excel and Pickle types is now deprecated.<br/>
     _default_path_ must be used instead: it is the default path to use when instantiating a data node from
    the config. Note that the attribute in the `DataNode` entity is still called _path_.
   - The _last_edition_date_ attribute of data nodes is now deprecated.<br/>
     _last_edit_date_ must be used instead.
   - The _edition_in_progress_ attribute of data nodes is now deprecated.<br/>
     _edit_in_progress_ must be used instead.

## Enterprise edition: 1.1

Published on 2022-06.

This release contains all of [`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/)
as well as additional features.

### Features

   - User authentication.
   - Authorization checks for all entities.
   - Job recovery mechanism on application restart.
   - Page generation based on the user's identity.

## Community edition: 1.0

Published on 2022-04.

[`taipy` 1.0](https://pypi.org/project/taipy/1.0.0/) contains the latest
[`taipy-gui` 1.0](https://pypi.org/project/taipy-gui/1.0.2/),
[`taipy-core` 1.0](https://pypi.org/project/taipy-core/1.0.3/) and
[`taipy-rest` 1.0](https://pypi.org/project/taipy-rest/1.0.1/) packages.

#### Features

**`taipy-gui`**<br/>1.0.0

   - Multiple pages support
   - Binding to global variables
   - Python expression support in visual element properties
   - Initial visual element set including tables and charts.
   - Page content support for Markdown and HTML
   - Jupyter Notebook support

**`taipy-core`**<br/>1.0.0

   - Full configuration system
   - Data node management (read/write/filter/cache)
   - Predefined data nodes (CSV, SQL, EXCEL, PICKLE)
   - Scenario and cycle management
   - Smart scheduling and execution (Scenario, Pipeline, and Task submission)

**`taipy-rest`**<br/>1.0.0

   - REST APIs on top of `taipy-core`
