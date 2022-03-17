A pipeline configuration is necessary to instantiate a [Pipeline](../concepts/pipeline.md). To create a
`PipelineConfig^` you can use
the `taipy.configure_pipeline()^` method with the following parameters:

- _id_: The id of this new pipeline configuration. This id is **mandatory** and must be a unique valid Python variable name.
- _tasks_: The list of tasks configurations.
- _properties_: A dictionary of additional properties.

Here is a simple example using the task configuration `task_config` created in the previous example:

```python linenums="1"
import taipy as tp

pipeline_config = tp.configure_pipeline("multiply_pipeline", [task_config])
```

On this example, we create a pipeline config which is made of a single task configuration created
in the previous example.

[:material-arrow-right: Next section introduces the scenario configuration](scenario-config.md).
