Taipy provides a checking mechanism to validate your configuration is correct.

You can trigger the check by calling:
```python linenums="1"
import taipy as tp

tp.check_configuration()
```

The `tp.check_configuration()` method returns a collector of issues. Each issue corresponds to an inconsistency on
the configuration attached to an issue level (`INFO`, `WARNING`, `ERROR`). `tp.check_configuration()` raises an
exception if at least one issue collected has the `ERROR` level.

Here is the list of the issues possibly returned by the checker:

- An `ERROR` issue is created if the `clean_entities_enabled` property is populated in the
[`GlobalAppConfig`](../../../reference/#taipy.core.config.global_app_config.GlobalAppConfig)
with a non-Boolean value.

- An `ERROR` issue is created if the `storage_type` and the `scope` properties of any
[`DataNodeConfig`](../../../reference/#taipy.core.config.data_node_config.DataNodeConfig)
have not been provided with a correct value.

- Depending on the `storage_type` value of a
[`DataNodeConfig`](../../../reference/#taipy.core.config.data_node_config.DataNodeConfig),
an `ERROR` issue is created if a specific required properties is missing.

- An `ERROR` issue is created if one of the `inputs` and `outputs` parameters of a
[`TaskConfig`](../../../reference/#taipy.core.config.task_config.TaskConfig)
does not correspond to a `DataNodeConfig`.

- A `WARNING` issue is created if a
[`TaskConfig`](../../../reference/#taipy.core.config.task_config.TaskConfig) have no input and no output.

- An `ERROR` issue is created if the `function` parameter of a
[`TaskConfig`](../../../reference/#taipy.core.config.task_config.TaskConfig)
is not a callable function.

- An `ERROR` issue is created if one of the `task` parameters of a
[`PipelineConfig`](../../../reference/#taipy.core.config.pipeline_config.PipelineConfig)
does not correspond to a `TaskConfig`.

- A `WARNING` issue is created if a
[`PipelineConfig`](../../../reference/#taipy.core.config.pipeline_config.PipelineConfig) have no task configuration
defined.

- An `ERROR` issue is created if one of the `pipeline` parameters of a
[`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig)
does not correspond to a `PipelineConfig`.

- A `WARNING` issue is created if a
[`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig) have no pipeline
configuration defined.

- An `ERROR` issue is created if the `frequency` parameter of a
[`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig)
has an incorrect [`Frequency`](../../../reference/#taipy.core.common.frequency.Frequency) value.

- An `INFO` issue is created if a
[`ScenarioConfig`](../../../reference/#taipy.core.config.scenario_config.ScenarioConfig) have no `comparator` defined.

- If the [`JobConfig`](../../../reference/#taipy.core.config.job_config.JobConfig) has been
  configured with multiple workers, an `ERROR` issue is created if an `in_memory` `DataNodeConfigs` is defined.


[:material-arrow-right: Next section presents advanced configuration](advanced-config.md).
