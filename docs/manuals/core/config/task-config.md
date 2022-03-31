A task configuration is necessary to instantiate a [Task](../concepts/task.md). To create a
`TaskConfig^` you can use
the `taipy.configure_task()^` method with the following parameters:

- _**id**_: The id of the task configuration to be created. This id is **mandatory** and must be a unique and valid
  Python variable name.
- _**function**_: The function to execute.
- _**inputs**_: The input data nodes referring the parameter(s) data of the _function_ to be executed.
- _**outputs**_: The output data nodes referring the result(s) data of the _function_ to be executed.

Here is a simple example:

```python linenums="1"
from taipy import Config

def double(nb):
    return nb * 2

input_data_node_config = Config.configure_data_node("input", default_value=21)
output_data_node_config = Config.configure_data_node("output")

task_config = Config.configure_task("double_task", double, input_data_node_config, output_data_node_config)
```

In the previous example, we created a `TaskConfig^`.

In lines 3 and 4, we define a function that we want to use in a [Task](../concepts/task.md) instantiated from the task
config. It takes a single parameter and return a single value.

In lines 6 and 7, two data node configurations are created. They will be used as the function argument and the function
result.

Finally, on line 9, we create the task configuration with the id 'double_task' that represents the function
'double' that expects an 'input' data node as an input parameter and returns an 'output' data node.

Because a Task can have several inputs and outputs, `taipy.configure_task()^` can receive lists of `DataNodeConfig^`
objects.

```python linenums="1"
from taipy import Config

def multiply_and_add(nb1, nb2):
    return nb1 * nb2, nb1 + nb2

nb_1_cfg = Config.configure_data_node("nb_1", default_value=21)
nb_2_cfg = Config.configure_data_node("nb_2", default_value=2)

multiplication_cfg = Config.configure_data_node("multiplication")
addition_cfg = Config.configure_data_node("addition")

task_config = Config.configure_task("foo", multiply_and_add, [nb_1_cfg, nb_2_cfg], [multiplication_cfg, addition_cfg])
```

In lines 3 and 4, we define a function with two parameters and two return values.

In lines 6 and 7, two data node configurations are created. They will be used as the function arguments.

In line 9 and 10, two data node are configured. They will be used as the function results.

Finally, in line 12, we create the task configuration with the id 'foo' representing the function
'multiply_and_add'. It expects two 'input' data nodes and two 'output' data nodes.

[:material-arrow-right: The next section introduces the pipeline configuration](pipeline-config.md).
