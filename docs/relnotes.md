---
hide:
  - navigation
---

# Release Notes

This is the list of changes to Taipy releases as they were published.

## Community edition: 2.1 (In progress)

#### New Features

**`taipy-core`** *<br/>2.1

   - New data node named `MongoCollectionDataNode`. It represents the data from a MongoDB collection.
   - The parent entities of a data node, a task, or a pipeline can be accessed via `DataNode.get_parents()^`,
   `Task.get_parents()^`, or `Pipeline.get_parents()^`, or by passing the data node entity, task entity or pipeline
   entity to the function `taipy.get_parents()^`.
   - Data node caching mechanism now also considered the date and time of the last modification of a file caused
   by either Taipy execution or an external factor. This behavior is currently limited to only CSV files, Excel
   files, JSON files and pickle files.

## Community edition: 2.0

Published on 2022-10.

[`taipy` 2.0](https://pypi.org/project/taipy/2.0.0/) contains the latest
[`taipy-config` 2.0](https://pypi.org/project/taipy-config/2.0.0/),
[`taipy-gui` 2.0](https://pypi.org/project/taipy-gui/2.0.0/),
[`taipy-core` 2.0](https://pypi.org/project/taipy-core/2.0.0/) and
[`taipy-rest` 2.0](https://pypi.org/project/taipy-rest/2.0.0/) packages.

#### New Features

**`taipy-gui`**<br/>2.0.0

- Extension API: custom visual elements can be integrated into Taipy GUI applications.<br/>
  Third party HTML components can be integrated into Taipy GUI pages to address specific use cases.<br/>
  See [Extension API](../manuals/gui/extension) for details.
- New callbacks (`on_init`, `on_navigate`, `on_exception` and `on_status`) can be used to initialize a new
  session, detect navigation events, trigger code when exceptions are raised in user code,
  and invoke code when a *status* page is requested.<br/>
  See [Callbacks](../manuals/gui/callbacks) for details.
- New functions allow applications to invoke long-running callbacks without blocking.<br/>
  See [Long Running Callbacks](../manuals/gui/callbacks/#long-running-callbacks) for
  details.
- The Taipy GUI application configuration uses the generic Taipy configuration mechanism exposed in the
  new `taipy-config` package.
- An application can request the status of the server application using the "status" predefined page.<br/>
- The new 'base' property of the chart control makes it possible to create Gantt chart-like displays.<br/>
  See [Gantt Charts](../manuals/gui/viselements/charts/gantt) for details.

**`taipy-core`**<br/>2.0.0

- New data node named SQLTableDataNode. It represents a table in a SQL database.
- New data node named JSONDataNode. It represents the data from a JSON file.
- SQLDataNode behavior is changed due to the release of SQLTableDataNode. Now it represents the data
  using custom read and write queries.
- In standalone mode, a job whose status is `SUBMITTED`, `PENDING`, or `BLOCKED` can be canceled. When canceling
  the job, its subsequent jobs will be abandoned, and their statuses will be set to `ABANDONED`. When the cancel
  method is called on a job whose status is either `RUNNING`, `COMPLETED`, or `SKIPPED`, its subsequent jobs will
  be abandoned while its status remains unchanged. A job whose status is `FAILED`, `CANCELED` or `ABANDONED`
  cannot be canceled.
- Taipy Core can now be run as a service by using `Core().run()` or `tp.run(Core())`. By running Core
  as a service, Taipy initializes the scheduler and the job dispatcher based on the provided configuration. The Taipy Core service can be run along with Taipy GUI or Taipy Rest services.

**`taipy-config`**<br/>2.0.0

- The new `taipy-config` package was exposed to be used by any other Taipy package for configuration and logging.


#### Improvements

**`taipy-gui`**<br/>2.0.0
- Stopping then re-running the `Gui^` instance is no longer required in Notebook contexts.
- A discrete graphical indicator is displayed on top of pages when the server is processing.

**`taipy-core`**<br/>2.0.0

- The data node of a scenario or a pipeline can now be accessed directly at the scenario or pipeline
  levels.
- When submitting a scenario, a pipeline, or a task, the job(s) created will be returned.
- When submitting a scenario, pipeline, or task in standalone mode, the user can use the parameters
  _wait_ and _timeout_ to wait until the submitted jobs are finished or up to _timeout_ seconds.
- When in standalone mode, the job dispatcher runs in a sub-thread that periodically checks for new jobs submitted by Taipy to execute.
- When a running job fails, its subsequent jobs will be automatically abandoned.
- A primary scenario can be deleted along with its cycle if it is the only scenario in the cycle.
- The messages of the various Exceptions that can be raised have been improved to help the users
  debug their applications.

#### Significant bug fixes

**`taipy-gui`**<br/><br/>2.0.1

- Bar charts' "barmode" set to "stack" is broken.<br/>
  See [issue #445](https://github.com/Avaiga/taipy-gui/issues/445).


#### Deprecations

**`taipy-core`**<br/>2.0.0

- The field `*nb_of_workers*` within the Config has been deprecated in favor of `*max_nb_of_workers*`.

## Enterprise edition: 2.0

Published on 2022-10.

#### New Features

- SQLLite or MongoDB databases can now be used as alternatives to the filesystem to store Taipy entities.

#### Improvements

- Simplification of the authentication API.

## Community edition: 1.1

Published on 2022-06.

[`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/) contains the latest
[`taipy-gui` 1.1](https://pypi.org/project/taipy-gui/1.1.0/),
[`taipy-core` 1.1](https://pypi.org/project/taipy-core/1.1.0/) and
[`taipy-rest` 1.1](https://pypi.org/project/taipy-rest/1.1.0/) packages.


#### Improvements

**`taipy-gui`**<br/>1.1.3

- The client-server communication settings are extended to accommodate various Flask deployment scenarios.<br/>
  See the documentation for the *async_mode* parameter to `Gui.run()^` for more information.
- Implicit re-run of the `Gui^` instance in Notebook environments.<br/>
  See [issue #320](https://github.com/Avaiga/taipy-gui/issues/320).
- Test server/client versions for safe interoperability.<br/>
  See [issue #323](https://github.com/Avaiga/taipy-gui/issues/323).
- Allow the edition of specific table columns.<br/>
  See [issue #366](https://github.com/Avaiga/taipy-gui/issues/366).

<br/>1.1.0

- The `State^` instance can be initialized in a user-defined function. See the _on_init_
  attribute of the `Gui^` class for more details.
- Page definitions and the bound variables can be isolated in a module to clarify the
  application code organization.<br/>
  See this [section](manuals/gui/binding.md#scope-for-variable-binding) for details.
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

**`taipy-gui`**<br/><br/>1.1.3

- Error fixed when modifying a State dictionary entry in a callback.<br/>
  See [issue #356](https://github.com/Avaiga/taipy-gui/issues/356).
- Boolean values not editable in tables.<br/>
  See [issue #365](https://github.com/Avaiga/taipy-gui/issues/365).
- Crash fixed when using a dictionary in the labels property of the slider control.<br/>
  See [issue #379](https://github.com/Avaiga/taipy-gui/issues/379).

<br/>1.1.0

- Concurrency issues were fixed.
- The [_attr_list_](https://python-markdown.github.io/extensions/attr_list) extension can
  be used to style individual Markdown elements without the need for a CSS file.<br/>
  See [issue #185](https://github.com/Avaiga/taipy-gui/issues/185).
- Taipy supports HTTPS via reverse proxies.<br/>
  See [issue #263](https://github.com/Avaiga/taipy-gui/issues/263).

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
