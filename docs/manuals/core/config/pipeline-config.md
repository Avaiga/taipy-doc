A pipeline configuration is necessary to instantiate a [Pipeline](../concepts/pipeline.md). To create a
[`PipelineConfig`](../../../reference/#taipy.core.config.pipeline_config.PipelineConfig) you can use
the `taipy.configure_pipeline()` method with the following parameters:

- `id`: The id of this new pipeline configuration. This id should be unique.
- `tasks`: The list of tasks configurations.
- `properties`: The dictionary of additional properties.

Basic example using the task configuration `task_config` created in the previous example:

```python linenums="1"
import taipy as tp

pipeline_config = tp.configure_pipeline("multiply_pipeline", [task_config])
```

On this example, we create a pipeline config which is made of a single task configuration created
in the previous example.

[:material-arrow-right: Next section introduces the scenario configuration](scenario-config.md).
