---
title: Release Notes for version 2.3
---

This is the list of changes of taipy version 2.3.

!!! note "Unsupported version"

    Version 2.3 of Taipy is no longer supported. We strongly recommend
    that you upgrade to the latest version of Taipy.

Published on 2023-06.

[`taipy` 2.3](https://pypi.org/project/taipy/2.3.1/) contains the latest
[`taipy-config` 2.3](https://pypi.org/project/taipy-config/2.3.2/),
[`taipy-gui` 2.3](https://pypi.org/project/taipy-gui/2.3.1/),
[`taipy-core` 2.3](https://pypi.org/project/taipy-core/2.3.0/) and
[`taipy-rest` 2.3](https://pypi.org/project/taipy-rest/2.3.0/) packages.

# <strong><code>taipy</code></strong>

## 2.3.1

- :octicons-feed-rocket-16:{ .rocket-icon } The
  [expanded](../../refmans/gui/viselements/corelements/scenario.md#p-expanded) and
  [show_tags](../../refmans/gui/viselements/corelements/scenario.md#p-show_tags) properties
  of the [scenario](../../refmans/gui/viselements/corelements/scenario.md) control now
  have a default value of False.

## 2.3.0

- :octicons-feed-plus-16:{ .plus-icon } Scenario and Data Management Controls<br/>
  Taipy comes, in the [`taipy`](https://pypi.org/project/taipy/) package, with a set of
  ready-to-use GUI controls that connect to entities created by Taipy. Your application
  can then visualize the Taipy entities related to Scenario and Data Management and
  interact with them.<br/>
  Please check the list of Scenario and Data Management
  [Scenario and Data Management controls](../../refmans/gui/viselements/index.md#scenario-and-data-management-controls).
- :octicons-feed-plus-16:{ .plus-icon } New Taipy command-line interface (CLI). Please
  refer to the [Taipy command-line interface](../../userman/ecosystem/cli/index.md)
  documentation page for more information.
- :octicons-feed-plus-16:{ .plus-icon } Users can now create a new Taipy application
  from a template by running `$ taipy create` from the CLI. Besides the default template,
  "multi-page-gui" template can be chosen with the optional `--template` option.

#  <strong><code>taipy-gui</code></strong>

## 2.3.1

- :octicons-feed-rocket-16:{ .rocket-icon } Multi-line
  [input](../../refmans/gui/viselements/generic/input.md) controls accept the Shift+Enter
  combination to create a new line.<br/>
  See [issue #824](https://github.com/Avaiga/taipy-gui/issues/824).
- :octicons-feed-rocket-16:{ .rocket-icon }
  [Table](../../refmans/gui/viselements/generic/table.md) filters adapt to a change of the
  visible columns.<br/>
  See [issue #822](https://github.com/Avaiga/taipy-gui/issues/822).


## 2.3.0

- :octicons-feed-plus-16:{ .plus-icon } The [`table`](../../refmans/gui/viselements/generic/table.md) and
- :octicons-feed-plus-16:{ .plus-icon } [`chart`](../../refmans/gui/viselements/generic/chart.md)
  controls have a new property called *rebuild* that allows for modifying the control configuration
  at runtime, using properties that are *not* dynamic.<br/>
  See the details in the specific documentation sections for
  [tables](../../refmans/gui/viselements/generic/table.md#the-rebuild-property) and
  [charts](../../refmans/gui/viselements/generic/chart.md#the-rebuild-property).
- :octicons-feed-plus-16:{ .plus-icon } The [`part` block](../../refmans/gui/viselements/generic/part.md)
  now accepts any URL as a value for the
  [*page* property](../../refmans/gui/viselements/generic/part.md#p-page). You can then integrate any external
  web page as demonstrated in [this example](../../refmans/gui/viselements/generic/part.md#part-showing-a-page).
  <br/>
  To better control the layout of external pages, a new
  [*height* property](../../refmans/gui/viselements/generic/part.md#p-height) has been added to the
  [`part`](../../refmans/gui/viselements/generic/part.md) element.
- :octicons-feed-plus-16:{ .plus-icon } The `navigate()^` function has an additional parameter called
  *force* that, when set to True, re-renders the page (set to the *to* parameter). This allows to
  force the evaluation of bound variables in complex dependencies situations.
- :octicons-feed-rocket-16:{ .rocket-icon } Page scopes (how Taipy GUI finds bound variables in
  different modules) have been improved so any given page can locate a variable in any module that
  defines a local page.<br/>
  See the [section on page scopes](../../userman/gui/binding.md#scope-for-variable-binding) for
  more information and examples.
- :octicons-feed-rocket-16:{ .rocket-icon } A new mechanism to start the web server when
  [using Notebooks](../../userman/run-deploy/notebooks.md) was put in place to prevent
  potential bottlenecks when allocating a port number. This behavior is controlled by the
  [*notebook_proxy*](../../userman/advanced_features/configuration/gui-config.md#p-notebook_proxy)
  configuration parameter.
- :octicons-bug-24:{ .bug-icon } The removal of all the
  [`table`](../../refmans/gui/viselements/generic/table.md) filters has no immediate effect. <br/>
  See [issue #667](https://github.com/Avaiga/taipy-gui/issues/667).
- :octicons-bug-24:{ .bug-icon } Styling of the
  [`pane` block](../../refmans/gui/viselements/generic/pane.md) was not applied properly.<br/>
  See [issue #766](https://github.com/Avaiga/taipy-gui/issues/766).
- :octicons-bug-24:{ .bug-icon } Some notifications (see `notify()^`) could be missed when
  there were too many in a small period of time.<br/>
  See [issue #777](https://github.com/Avaiga/taipy-gui/issues/777).

#  <strong><code>taipy-core</code></strong>

## 2.3.1

- :octicons-alert-fill-24:{ .alert-icon } The `Config.configure_default_data_node()`
  method has been deprecated. The `Config.set_default_data_node_configuration()^` method
  should be used instead.
- :octicons-alert-fill-24:{ .alert-icon } The `Config.configure_task_node()` method
  has been deprecated. The `Config.set_task_node_configuration()^` method should be used instead.
- :octicons-alert-fill-24:{ .alert-icon } The `Config.configure_pipeline_node()` method has been
  deprecated. The `Config.set_pipeline_node_configuration()^` method should be used instead.
- :octicons-alert-fill-24:{ .alert-icon } The `Config.configure_scenario_node()` method has
  been deprecated. The `Config.set_scenario_node_configuration()^` method should be used instead.
- :octicons-feed-plus-16:{ .plus-icon } New exposed functions:

       * `is_submittable()^` checks if a scenario or a pipeline can be submitted;

       * `is_promotable()^` checks if a scenario can be promoted to primary;

       * `is_deletable()^` checks if an entity can be deleted.

## 2.3.0

- :octicons-feed-plus-16:{ .plus-icon } All scenarios grouped by their cycle can now be retrieved
  by calling `taipy.get_cycles_scenarios()^`.
- :octicons-feed-plus-16:{ .plus-icon } All entities (cycles, scenarios, pipelines, tasks, data
  nodes, and jobs) expose two new methods: `get_label()` and `get_simple_label()`, that can be
  used to display the entity.
- :octicons-feed-plus-16:{ .plus-icon } `taipy.get_entities_by_config_id()^` can be used to
  retrieve all entities that are based on the provided configuration identifier.
- :octicons-feed-plus-16:{ .plus-icon } Commands for managing Taipy application versions can now
  be accessed via the `$ taipy manage-versions` command. Run `$ taipy manage-versions --help` for
  more details.
- :octicons-feed-plus-16:{ .plus-icon } A version can now be renamed by running
  `$ taipy manage-versions --rename <old_version> <new_version>` from the CLI.
- :octicons-feed-plus-16:{ .plus-icon } The configuration of a version can now be compared with
  another one by running
  `$ taipy manage-versions --compare-config <version_1> <version_2>` from the CLI.
- :octicons-feed-rocket-16:{ .rocket-icon } A generic data node can now be created defining only
  the *read_fct* parameter for a read-only data node, or only the *write_fct* parameter for a
  write-only data node.
- :octicons-feed-rocket-16:{ .rocket-icon } The parameters *read_fct_params* and *write_fct_params*
  of the generic data nodes were renamed to *read_fct_args* and *write_fct_args*, and both must be
  populated with a List value to avoid the problem of passing Tuple of one string.
- :octicons-feed-rocket-16:{ .rocket-icon } The *validity_period* attribute of a data node is now
  exposed at the configuration level to set the up-to-date duration of a data node.
- :octicons-feed-rocket-16:{ .rocket-icon } Add support for SQLAlchemy 2.0
- :octicons-alert-fill-24:{ .alert-icon } `PipelineConfig` has been deprecated and will be combined
  with `ScenarioConfig^` in future updates.
- :octicons-alert-fill-24:{ .alert-icon } `taipy.create_pipeline()` has been deprecated.
