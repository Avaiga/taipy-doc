---
hide:
  - navigation
---

# Release Notes

This is the list of changes to Taipy releases as they were published.

!!! note "Migration"

    Please refer to the [Migration page](./migration.md) for potential migration paths for your applications
    implemented on legacy Taipy versions.

## Community edition: 2.3 (Work in progress)

Not published yet.

[`taipy` 2.3](https://pypi.org/project/taipy/2.3.0/) contains the latest
[`taipy-config` 2.3](https://pypi.org/project/taipy-config/2.3.0/),
[`taipy-gui` 2.3](https://pypi.org/project/taipy-gui/2.3.0/),
[`taipy-core` 2.3](https://pypi.org/project/taipy-core/2.3.0/) and
[`taipy-rest` 2.3](https://pypi.org/project/taipy-rest/2.3.0/) packages.

### New Features

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
2.3.0

- New Taipy command-line interface. Please refer to the
  [Taipy command-line interface](./manuals/taipy_cli.md)
  documentation page for more information.
- User can now create a new Taipy application from a template by running `$ taipy create` from the
  Taipy command-line interface with an optional `--template` option.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.3.0

- All scenarios grouped by their cycles can now be retrieved by calling `taipy.get_cycles_scenarios()^`.
- All entities (cycles, scenarios, pipelines, tasks, data nodes, and jobs) expose two new methods: `get_label` and
  `get_simple_label`, that can be used to display the entity.
- `taipy.get_entities_by_config_id()^` can be used to retrieve all entities that are based on
  the provided configuration identifier.
- Commands for managing Taipy application versions can now be accessed via the `$ taipy manage-versions` command. Run `$ taipy manage-versions --help` for more details.
- A version can now be renamed by running `$ taipy manage-versions --rename <old_version> <new_version>` from a command-line interface.
- The configuration of a version can now be compared with another one by running `$ taipy manage-versions --compare-config <version_1> <version_2>` from a command-line interface.

### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.3.0

- A generic data node can now be created with only the `read_fct` for reading only or the `write_fct` for writing only data node.<br/>
- The `read_fct_params` and `write_fct_params` of a generic data node are renamed to `read_fct_args` and `write_fct_args`, and both must be populated with a List value to avoid the problem of passing Tuple of one string.<br/>

## Community edition: 2.2

Published on 2023-04.

[`taipy` 2.2](https://pypi.org/project/taipy/2.2.0/) contains the latest
[`taipy-config` 2.2](https://pypi.org/project/taipy-config/2.2.0/),
[`taipy-gui` 2.2](https://pypi.org/project/taipy-gui/2.2.1/),
[`taipy-core` 2.2](https://pypi.org/project/taipy-core/2.2.2/) and
[`taipy-rest` 2.2](https://pypi.org/project/taipy-rest/2.2.1/) packages.

### New Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- A default set of stylesheets are installed with Taipy GUI so that, by
  default, applications benefit from a homogeneous and good-looking
  style. This is called the [Stylekit](manuals/gui/styling/stylekit.md).<br/>
  The Stylekit can be easily customized to fit your application design's
  requirements.
- The [`table`](manuals/gui/viselements/table.md) and [`chart`](manuals/gui/viselements/chart.md)
  controls have a new property called *rebuild* that can be used if you need to entirely change the
  data they rely on, including their structure.

### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- The default property name for the [`part` block](manuals/gui/viselements/part.md)
  was changed from *render* to *class_name* to allow for directly using the
  style classes from the [Stylekit](manuals/gui/styling/stylekit.md).<br/>
  Please check the section on
  [Styled Sections](manuals/gui/styling/stylekit.md#styled-sections) for
  more information.
- The [`expandable` block](manuals/gui/viselements/expandable.md) has a new property
  called *on_change* enabling to set a specific callback when the block is expanded
  or collapsed.
- Better error messages when parsing Markdown content.
- Better support for auto-completion in IDE for the `Gui.run()^` configuration parameters, based
  on a generated Python Interface Definition file.
- The *status* entry point now provides information about the loaded element libraries and
  the elements they define.
- The `navigate()^` function and the *page* property of the [`part` block](manuals/gui/viselements/part.md)
  can now use, as their target, any URL. In the context of a `part` block, the page will be rendered
  in an *iframe*.<br/>
  See [issue #621](https://github.com/Avaiga/taipy-gui/issues/621).

### Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.2.0

- Bound variable scope issues fixed when used by elements defined at the root page
  level.<br/>
  See [issue #583](https://github.com/Avaiga/taipy-gui/issues/583).
- Filters management fixed in the [`table` controls](manuals/gui/viselements/table.md).<br/>
  See [issue #667](https://github.com/Avaiga/taipy-gui/issues/667).
- Communication with the server may break.<br/>
  See [issue #695](https://github.com/Avaiga/taipy-gui/issues/695).


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.2.3

- Error raised when running Core service in development mode after a function rename in the Config.<br/>
  See [issue #560](https://github.com/Avaiga/taipy-core/issues/560).

2.2.2

- PostgreSQL and MySQL engines do not support "driver" argument.<br/>
  See [issue #544](https://github.com/Avaiga/taipy-core/issues/544).<br/>
  To avoid conflict between engines, the default value of the _db_driver_ parameter in a SQL or a SQL table data
  node configuration has been removed.

## Studio: 1.0

Published on 2023-02.

The first release of the
[`Taipy Studio`](https://marketplace.visualstudio.com/items?itemName=Taipy.taipy-studio)
extension to [Visual Studio Code](https://code.visualstudio.com/).

Taipy Studio brings programmers tools that significantly improve productivity when
building Taipy applications.

It mainly provides:

- A graphical editor for building configuration files, so one does not have
    to code configurations in Python any longer;
- IntelliSense applied to the Markdown syntax extension that Taipy GUI
    uses to define the visual elements in the interface pages.

You can refer to the [Taipy Studio User Manual](manuals/studio/index.md) section for more
information.

## Community edition: 2.1

Published on 2023-01.

[`taipy` 2.1](https://pypi.org/project/taipy/2.1.0/) contains the latest
[`taipy-config` 2.1](https://pypi.org/project/taipy-config/2.1.0/),
[`taipy-gui` 2.1](https://pypi.org/project/taipy-gui/2.1.0/),
[`taipy-core` 2.1](https://pypi.org/project/taipy-core/2.1.0/) and
[`taipy-rest` 2.1](https://pypi.org/project/taipy-rest/2.1.0/) packages.

Please refer to the [Migration page](./migration.md#from-2.0-to-2.1) for
details on how to migrate from version older than 2.1.

### New Features

<h6 style="font-size: 1.2em"><strong><code>taipy</code></strong></h6>
2.1

- Taipy and all its dependencies now support Python 3.11.<br/>
  See [Python documentation](https://docs.python.org/3/whatsnew/3.11.html) for details.

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.1.0

- A security feature has been added: the file `.taipyignore`, located next to
  the Python main file, can list the paths that you want to prevent access to.<br/>
  See [issue #501](https://github.com/Avaiga/taipy-gui/issues/501) or
  [this section](manuals/gui/configuration.md#protect-your-application-files) for
  details.
- Charts can use a [Decimator]() instance that cleverly filters data
  points out to greatly improve performance.<br/>
  See the [Decimator documentation]() for more details.
- Charts now support polar, funnel, candlesticks and many other types of charts.<br/>
  See the [chart control](manuals/gui/viselements/chart.md) section for details.
- Charts now support the dark theme automatically.
- Tooltips can be set on individual table cells.<br/>
  See the [example](manuals/gui/viselements/table.md#cell-tooltip) for more information.
- [Long running callbacks](manuals/gui/callbacks.md#long-running-callbacks) have
  been improved to allow for easily returning a value.<br/>
  See the documentation of the `invoke_long_callback()^` function or the
  [issue #547](https://github.com/Avaiga/taipy-gui/issues/547) for more details.
- Developers can specify the location of the Taipy webapp, for debugging purposes.<br/>
  The `--webapp-path` command line option allows to specify that location.<br/>
  See [issue #564](https://github.com/Avaiga/taipy-gui/issues/564).


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.0

- New version management system for Taipy applications. Users can now run an application in development
  mode, save a version of the application as an experiment version, re-run older experiment versions,
  and push a version to production.<br/>
  See the [Version management system](./manuals/core/versioning/index.md) documentation page for more details.
- New data node named [MongoCollectionDataNode](./manuals/core/config/data-node-config.md#mongo-collection).
  It represents the data from a MongoDB collection.
- New data node named [ParquetDataNode](./manuals/core/config/data-node-config.md#parquet). It represents
  tabular data stored in the Apache Parquet format.
- Added support for [Modin](https://modin.readthedocs.io/en/stable/) as a new exposed type.
- Running the Core service is required to execute jobs. See `Core().run()^` method.
- The parent entities of a data node, a task, or a pipeline can be accessed via
  `DataNode.get_parents()^`, `Task.get_parents()^`, or `Pipeline.get_parents()^`, or by passing the
  data node entity, task entity or pipeline entity to the function `taipy.get_parents()^`.
- New data node property _expiration_date_ computed adding the _validity_period_ duration to the
  _last_edit_date_ of the data node.
- New data node property _is_up_to_date_ equals to `True` if the data node has not expired (refer to
  _expiration_date_ attribute). `False` otherwise.
- The **sql** _repository_type_ is now available on community edition to store Core entities in an
  SQL database. See [SQL storage section](./manuals/core/config/global-config.md#sql-storage-for-taipy-entities).


### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.1.0

- The Pie charts now use the *values* property to set values instead of *x*.<br/>
  See [Pie charts](manuals/gui/viselements/charts/pie.md) for details.
- Unselected data points or traces in charts now preserve their original opacity.<br/>
  See [issue #496](https://github.com/Avaiga/taipy-gui/issues/496).
- `class_name` is now a dynamic property.<br/>
  See [issue #480](https://github.com/Avaiga/taipy-gui/issues/480).
- The *allow_unsafe_werkzeug* option of [Werkzeug](https://werkzeug.palletsprojects.com/)
  (that [Flask](https://flask.palletsprojects.com/) depends on for the WSGI part) is forced
  to True when the Gui instance is run in Debug mode, because of a change in policy in
  recent updates.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.1

- Add overload type descriptions for the `taipy.get()` method that supports multiple different combinations
  of argument types.

2.1.0

- Deprecation of the data node _cacheable_ property. It is replaced by _skippable_ property on tasks.
  The mechanism remains unchanged but instead of setting _cacheable_ property to `True` for all the
  outputs of a task that can be skipped, just set the task _skippable_ property to `True`.
- The _last_edit_date_ attribute of a data node is now updated when the corresponding data is modified
  by either a Taipy task execution or an external factor. This behavior is limited to file-based
  data nodes: CSV, Excel, JSON, and pickle data nodes only.

### Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.1.2

- The version required for [openpyxl](https://openpyxl.readthedocs.io/en/stable/) has been downgraded
  from "openpyxl>=3.0.7,<4.0" to "openpyxl>=3.0.7,<3.1" to match the version used by
  [Modin](https://modin.readthedocs.io/en/stable/).

## Community edition: 2.0

Published on 2022-10.

[`taipy` 2.0](https://pypi.org/project/taipy/2.0.0/) contains the latest
[`taipy-config` 2.0](https://pypi.org/project/taipy-config/2.0.1/),
[`taipy-gui` 2.0](https://pypi.org/project/taipy-gui/2.0.2/),
[`taipy-core` 2.0](https://pypi.org/project/taipy-core/2.0.3/) and
[`taipy-rest` 2.0](https://pypi.org/project/taipy-rest/2.0.0/) packages.

### New Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.0

- Extension API: custom visual elements can be integrated into Taipy GUI applications.<br/>
  Third party HTML components can be integrated into Taipy GUI pages to address specific use cases.<br/>
  See [Extension API](manuals/gui/extension/) for details.
- New callbacks (`on_init`, `on_navigate`, `on_exception` and `on_status`) can be used to initialize a new
  session, detect navigation events, trigger code when exceptions are raised in user code,
  and invoke code when a *status* page is requested.<br/>
  See [Callbacks](manuals/gui/callbacks.md) for details.
- New functions allow applications to invoke long-running callbacks without blocking.<br/>
  See [Long Running Callbacks](manuals/gui/callbacks.md#long-running-callbacks) for
  details.
- The Taipy GUI application configuration uses the generic Taipy configuration mechanism exposed in the
  new `taipy-config` package.
- An application can request the status of the server application using the "status" predefined page.<br/>
- The new 'base' property of the chart control makes it possible to create Gantt chart-like displays.<br/>
  See [Gantt Charts](../manuals/gui/viselements/charts/gantt) for details.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

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
  as a service, Taipy initializes the scheduler and the job dispatcher based on the provided configuration. The
  Taipy Core service can be run along with Taipy GUI or Taipy Rest services.

<h6 style="font-size: 1.2em"><strong><code>taipy-config</code></strong></h6>
2.0.0

- The new `taipy-config` package was exposed to be used by any other Taipy package for configuration and logging.


### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.0

- Stopping then re-running the `Gui^` instance is no longer required in Notebook contexts.
- A discrete graphical indicator is displayed at the bottom of pages when the server is
  processing.

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

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

### Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
2.0.2

- `image` control may not render properly.<br/>
  See [issue #436](https://github.com/Avaiga/taipy-gui/issues/436).
- Clarify and improve the `editable` (and `editable[]`) property in the `table` control.<br/>
  See [issue #464](https://github.com/Avaiga/taipy-gui/issues/464).
- [gui] section in configuration files breaks the application.<br/>
  See [issue #469](https://github.com/Avaiga/taipy-gui/issues/469).

2.0.1

- Bar charts' "barmode" set to "stack" is broken.<br/>
  See [issue #445](https://github.com/Avaiga/taipy-gui/issues/445).

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.4

- Do not update `last_edit_date` when a job fails or is abandoned.
  See [issue #366](https://github.com/Avaiga/taipy-core/issues/366).

### Deprecations

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
2.0.0

- The field `*nb_of_workers*` within the Config has been deprecated in favor of `*max_nb_of_workers*`.

## Enterprise edition: 2.0

Published on 2022-10.

### New Features

- SQLLite or MongoDB databases can now be used as alternatives to the filesystem to store Taipy entities.

### Improvements and changes

- Simplification of the authentication API.

## Community edition: 1.1

Published on 2022-06.

[`taipy` 1.1](https://pypi.org/project/taipy/1.1.0/) contains the latest
[`taipy-gui` 1.1](https://pypi.org/project/taipy-gui/1.1.0/),
[`taipy-core` 1.1](https://pypi.org/project/taipy-core/1.1.0/) and
[`taipy-rest` 1.1](https://pypi.org/project/taipy-rest/1.1.0/) packages.


### Improvements and changes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.1.3

- The client-server communication settings are extended to accommodate various Flask deployment scenarios.<br/>
  See the documentation for the *async_mode* parameter to `Gui.run()^` for more information.
- Implicit re-run of the `Gui^` instance in Notebook environments.<br/>
  See [issue #320](https://github.com/Avaiga/taipy-gui/issues/320).
- Test server/client versions for safe interoperability.<br/>
  See [issue #323](https://github.com/Avaiga/taipy-gui/issues/323).
- Allow the edition of specific table columns.<br/>
  See [issue #366](https://github.com/Avaiga/taipy-gui/issues/366).

1.1.0

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


<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.1.0

- Execution modes: "_development_" mode (default) runs tasks in a synchronous way one task at
  a time, while "_standalone_" mode runs tasks in an asynchronous and parallel way using
  sub-processes.
- _Retry policy_ to read entities: the global configuration attribute _retry_read_entity_ indicates
  the number of times Taipy will retry in case of error.
- Performance improvements when reading and writing entities.

### Significant bug fixes

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.1.3

- Error fixed when modifying a State dictionary entry in a callback.<br/>
  See [issue #356](https://github.com/Avaiga/taipy-gui/issues/356).
- Boolean values not editable in tables.<br/>
  See [issue #365](https://github.com/Avaiga/taipy-gui/issues/365).
- Crash fixed when using a dictionary in the labels property of the slider control.<br/>
  See [issue #379](https://github.com/Avaiga/taipy-gui/issues/379).

1.1.0

- Concurrency issues were fixed.
- The [_attr_list_](https://python-markdown.github.io/extensions/attr_list) extension can
  be used to style individual Markdown elements without the need for a CSS file.<br/>
  See [issue #185](https://github.com/Avaiga/taipy-gui/issues/185).
- Taipy supports HTTPS via reverse proxies.<br/>
  See [issue #263](https://github.com/Avaiga/taipy-gui/issues/263).

### Deprecations

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.1.0

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

### Features

<h6 style="font-size: 1.2em"><strong><code>taipy-gui</code></strong></h6>
1.0.0

- Multiple pages support
- Binding to global variables
- Python expression support in visual element properties
- Initial visual element set including tables and charts.
- Page content support for Markdown and HTML
- Jupyter Notebook support

<h6 style="font-size: 1.2em"><strong><code>taipy-core</code></strong></h6>
1.0.0

- Full configuration system
- Data node management (read/write/filter/cache)
- Predefined data nodes (CSV, SQL, EXCEL, PICKLE)
- Scenario and cycle management
- Smart scheduling and execution (Scenario, Pipeline, and Task submission)

<h6 style="font-size: 1.2em"><strong><code>taipy-rest</code></strong></h6>
1.0.0

- REST APIs on top of `taipy-core`
