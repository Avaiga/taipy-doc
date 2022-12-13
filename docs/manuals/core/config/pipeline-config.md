A pipeline configuration is necessary to instantiate a [Pipeline](../concepts/pipeline.md). To create a
`PipelineConfig^` you can use the `Config.configure_pipeline()^` method with the following parameters:

- _**id**_: The id of this new pipeline configuration. This id is **mandatory** and must be a unique and valid Python
  variable name.
- _**tasks**_: The list of tasks configurations.
- _**properties**_: A dictionary of additional properties.

```python linenums="1"
from taipy import Config

def double(nb):
    return nb * 2

input_data_node_config = Config.configure_data_node("input",
                                                    default_data=21)
output_data_node_config = Config.configure_data_node("output")
task_config = Config.configure_task("double_task",
                                    double,
                                    input_data_node_config,
                                    output_data_node_config)

pipeline_cfg = Config.configure_pipeline("my_pipeline", [task_config])
```

In the previous code example, in line 10, we create a pipeline configuration with the id "my_pipeline" and made of a
single task configuration `task_config`.

```python linenums="1"
from taipy import Config

def double(nb):
    return nb * 2

input_data_node_config = Config.configure_data_node("input",
                                                    default_data=21)
intermediate_data_node_config = Config.configure_data_node("intermediate")
output_data_node_config = Config.configure_data_node("output")
first_task_config = Config.configure_task("first_double_task",
                                          double,
                                          input_data_node_config,
                                          intermediate_data_node_config)
second_task_config = Config.configure_task("second_double_task",
                                           double,
                                           intermediate_data_node_config,
                                           output_data_node_config)

other_pipeline_cfg = Config.configure_pipeline("another_pipeline",
                                               [first_task_config, second_task_config])
```

In this second code example, in line 12, we create a pipeline configuration with the id "another_pipeline" and made
of the two task configuration created in lines 9 and 10 `first_task_config` and `second_task_config`.

!!! note

    Note that the order of the task_config in the list does not matter. The two following lines are equivalent.
    ```python
    pipeline_cfg = Config.configure_pipeline("pipeline",
                                             [first_task_config, second_task_config])
    ```
    ```python
    pipeline_cfg = Config.configure_pipeline("pipeline",
                                             [second_task_config, first_task_config])
    ```

[:material-arrow-right: The next section introduces the scenario configuration](scenario-config.md).
