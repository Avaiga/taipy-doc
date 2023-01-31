A pipeline configuration is necessary to instantiate a [Pipeline](../concepts/pipeline.md). To create a
`PipelineConfig^`, you can use the `Config.configure_pipeline()^` method with the following parameters:

- _**id**_: The id of this new pipeline configuration. This id is **mandatory** and must be a unique and valid Python
  variable name.
- _**tasks**_: The list of task configurations.
- _**properties**_: A dictionary of additional properties.

```python linenums="1"
{%
include-markdown "./code_example/pipeline_cfg/pipeline-config_simple.py"
comments=false
%}
```

In the previous code example, in line 16, we create a pipeline configuration with the id "my_pipeline" and made of a
single task configuration `task_config`.

```python linenums="1"
{%
include-markdown "./code_example/pipeline_cfg/pipeline-config_multiple.py"
comments=false
%}
```

In this second code example, in line 21, we create a pipeline configuration with the id "another_pipeline" and made
of the two task configurations created in lines 12 and 16 `first_task_cfg` and `second_task_cfg`.

!!! note

    Note that the order of the task_config in the list does not matter. The following lines are equivalent.
    ```python
    pipeline_cfg = Config.configure_pipeline("pipeline",
                                             [first_task_cfg, second_task_cfg])
    ```
    ```python
    pipeline_cfg = Config.configure_pipeline("pipeline",
                                             [second_task_cfg, first_task_cfg])
    ```

[:material-arrow-right: The next section introduces the scenario configuration](scenario-config.md).
