---
title: Release Notes for version 2.0
---

This is the list of changes of taipy version 2.0.

!!! note "Unsupported version"

    Version 2.0 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

Published on 2022-10.

[`taipy` 2.0](https://pypi.org/project/taipy/2.0.0/) contains the latest
[`taipy-config` 2.0](https://pypi.org/project/taipy-config/2.0.1/),
[`taipy-gui` 2.0](https://pypi.org/project/taipy-gui/2.0.2/),
[`taipy-core` 2.0](https://pypi.org/project/taipy-core/2.0.3/) and
[`taipy-rest` 2.0](https://pypi.org/project/taipy-rest/2.0.0/) packages.

# <strong><code>taipy-gui</code></strong>

## 2.0.2

- :octicons-bug-24:{ .bug-icon } `image` control may not render properly.<br/>
  See [issue #436](https://github.com/Avaiga/taipy-gui/issues/436).
- :octicons-bug-24:{ .bug-icon } Clarify and improve the `editable` (and `editable[]`) property
  in the `table` control.<br/>
  See [issue #464](https://github.com/Avaiga/taipy-gui/issues/464).
- :octicons-bug-24:{ .bug-icon } [gui] section in configuration files breaks the application.<br/>
  See [issue #469](https://github.com/Avaiga/taipy-gui/issues/469).

## 2.0.1

- :octicons-bug-24:{ .bug-icon } Bar charts' "barmode" set to "stack" is broken.<br/>
  See [issue #445](https://github.com/Avaiga/taipy-gui/issues/445).

## 2.0.0

- :octicons-feed-plus-16:{ .plus-icon } Extension API: custom visual elements can be integrated
  into Taipy GUI applications.<br/>
  Third party HTML components can be integrated into Taipy GUI pages to address specific use
  cases.<br/>
  See [Extension API](../../userman/gui/extension/index.md) for details.
- :octicons-feed-plus-16:{ .plus-icon } New callbacks (`on_init`, `on_navigate`, `on_exception`
  and `on_status`) can be used to initialize a new session, detect navigation events, trigger code
  when exceptions are raised in user code, and invoke code when a *status* page is requested.<br/>
  See [Callbacks](../../userman/gui/callbacks.md) for details.
- :octicons-feed-plus-16:{ .plus-icon } New functions allow applications to invoke long-running
  callbacks without blocking.<br/>
  See [Long Running Callbacks](../../userman/gui/callbacks.md#long-running-callbacks) for
  details.
- :octicons-feed-plus-16:{ .plus-icon } The Taipy GUI application configuration uses the generic
  Taipy configuration mechanism exposed in the new `taipy-config` package.
- :octicons-feed-plus-16:{ .plus-icon } An application can request the status of the server
  application using the "status" predefined page.<br/>
- :octicons-feed-plus-16:{ .plus-icon } The new 'base' property of the chart control makes it
  possible to create Gantt chart-like displays.<br/>
  See [Gantt Charts](../../refmans/gui/viselements/generic/charts/gantt.md) for details.
- :octicons-feed-rocket-16:{ .rocket-icon } Stopping then re-running the `Gui^` instance is no
  longer required in Notebook contexts.
- :octicons-feed-rocket-16:{ .rocket-icon } A discrete graphical indicator is displayed at the
  bottom of pages when the server is processing.

# <strong><code>taipy-core</code></strong>

## 2.0.4

- :octicons-bug-24:{ .bug-icon } Do not update `last_edit_date` when a job fails or is abandoned.
  See [issue #366](https://github.com/Avaiga/taipy-core/issues/366).

## 2.0.0

- :octicons-feed-plus-16:{ .plus-icon } New data node named SQLTableDataNode. It represents a
  table in a SQL database.
- :octicons-feed-plus-16:{ .plus-icon } New data node named JSONDataNode. It represents the data
  from a JSON file.
- :octicons-feed-plus-16:{ .plus-icon } SQLDataNode behavior is changed due to the release of
  `SQLTableDataNode`. Now it represents the data using custom read and write queries.
- :octicons-feed-plus-16:{ .plus-icon } In standalone mode, a job whose status is `SUBMITTED`,
  `PENDING`, or `BLOCKED` can be canceled. When canceling the job, its subsequent jobs will be
  abandoned, and their statuses will be set to `ABANDONED`. When the cancel method is called on
  a job whose status is either `RUNNING`, `COMPLETED`, or `SKIPPED`, its subsequent jobs will
  be abandoned while its status remains unchanged. A job whose status is `FAILED`, `CANCELED` or
  `ABANDONED` cannot be canceled.
- :octicons-feed-plus-16:{ .plus-icon } Taipy Orchestrator can now be run as a service by using
  `Orchestrator().run()` or `tp.run(Orchestrator())`. By running Orchestrator as a service, Taipy
  initializes the scheduler and the job dispatcher based on the provided configuration. The
  Taipy Orchestrator service can be run along with Taipy GUI or Taipy Rest services.
- :octicons-feed-rocket-16:{ .rocket-icon } The data node of a scenario or a pipeline can now be
  accessed directly at the scenario or pipeline
  levels.
- :octicons-feed-rocket-16:{ .rocket-icon } When submitting a scenario, a pipeline, or a task, the
  job(s) created will be returned.
- :octicons-feed-rocket-16:{ .rocket-icon } When submitting a scenario, pipeline, or task in
  standalone mode, the user can use the parameters _wait_ and _timeout_ to wait until the
  submitted jobs are finished or up to _timeout_ seconds.
- :octicons-feed-rocket-16:{ .rocket-icon } When in standalone mode, the job dispatcher runs in a
  sub-thread that periodically checks for new jobs submitted by Taipy to execute.
- :octicons-feed-rocket-16:{ .rocket-icon } When a running job fails, its subsequent jobs will be
  automatically abandoned.
- :octicons-feed-rocket-16:{ .rocket-icon } A primary scenario can be deleted along with its cycle
  if it is the only scenario in the cycle.
- :octicons-feed-rocket-16:{ .rocket-icon } The messages of the various Exceptions that can be
  raised have been improved to help the users debug their applications.
- :octicons-alert-fill-24:{ .alert-icon } The field *nb_of_workers* within the Config has been
  deprecated in favor of *max_nb_of_workers*.

# <strong><code>taipy-config</code></strong>

## 2.0.0

- :octicons-feed-plus-16:{ .plus-icon } The new `taipy-config` package was exposed to be used by any
  other Taipy package for configuration and logging.
