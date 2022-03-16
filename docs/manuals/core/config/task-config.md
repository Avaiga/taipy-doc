A task configuration is necessary to instantiate a [Task](../concepts/task.md). To create a
`TaskConfig^` you can use
the `taipy.configure_task()^` method with the following parameters:

- _id_: The id of the task configuration to be created. This id is **mandatory** and must be a unique valid Python
    variable name.
- _function_: The function to execute.
- _inputs_: The inputs of the function.
- _outputs_: The function result(s).

Here is a simple example:

```python linenums="1"
import taipy as tp

def double(nb):
    return nb * 2

input_data_node_config = tp.configure_data_node("input", default_value=21)
output_data_node_config = tp.configure_data_node("output")

task_config = tp.configure_task("double_task", double, input_data_node_config, output_data_node_config)
```

On the previous example, we created a `TaskConfig^`.

In lines 3 and 4, we define a function that we want to use in a [Task](../concepts/task.md) instantiated from the task
config.
In lines 6 and 7, two data node configurations are created. They will be used as the function argument and the function
result. Finally, on line 9, we create the task configuration with the id 'double_task' that represents the function
'double' that expects a 'input' data node as an input parameter and that returns an 'output' data node.

Because a Task can have several inputs and outputs, `tp.configure_task()^` can receive lists of `DataNodeConfig^`
objects.

```python
import taipy as tp

def multiply(nb, by):
    return nb * by

nb_to_multiple = tp.configure_data_node("nb_to_multiple", default_value=21)
multiply_by = tp.configure_data_node("multiply_by", default_value=2)

output_config = tp.configure_data_node("output")

task_config = tp.configure_task("foo", multiply, [nb_to_multiple, multiply_by], output_config)
```

[:material-arrow-right: Next section introduces the pipeline configuration](pipeline-config.md).
