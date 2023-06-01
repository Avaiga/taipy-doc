A task configuration is necessary to instantiate a [Task](../concepts/task.md). To create a
`TaskConfig^`, you can use the `Config.configure_task()^` method with the following parameters:

- _**id**_: The id of the task configuration to be created. This id is **mandatory** and must be a unique and valid
  Python identifier.
- _**function**_: The function to execute.
- _**inputs**_: The input data nodes referring to the _function_'s parameter(s) data to be executed.
- _**outputs**_: The output data nodes referring to the result(s) data of the _function_ to be executed.
- _**skippable**_: Boolean attribute indicating if the task execution can be skipped if all output
  data nodes are up-to-date (see *validity_period* attribute in the
  [Data node management page](../entities/data-node-mgt.md) for more detail). The default value of
  _skippable_ is `False`.

Here is a simple example:

```python linenums="1"
{%
include-markdown "./code_example/task_cfg/task-config_simple.py"
comments=false
%}
```

In the example above, we created a `TaskConfig^` named `double_task_cfg`.

In lines 4-5, we define a function `double()`, to be used in a [Task](../concepts/task.md)
instantiated from the task config. It takes a single parameter and returns a single value.

In lines 8-9, two data node configurations are created. They will be used respectively as
argument and result of the function `double()`.

Finally, on line 12-16, we create the task configuration with the id _double_task_. It
represents the function _double()_ that expects an _input_ data node as a parameter and
returns an _output_ data node. On line 13, the Task configuration has been set `skippable`.
That means when submitting a Task entity instantiated from this TaskConfig, Taipy will skip
its execution if its input data nodes haven't changed since the previous execution.

Because a Task can have several inputs and outputs, `Config.configure_task()^` can receive
lists of `DataNodeConfig^` objects.

```python linenums="1"
{%
include-markdown "./code_example/task_cfg/task-config_multiple.py"
comments=false
%}
```

In lines 4-5, we define a function with two parameters and two return values.

In lines 8-9, two data nodes configurations are created. They will be used as the
function arguments.

In lines 11-12, two data nodes are configured. They will be used as the function results.

Finally, in lines 14-17, we create the task configuration with the id _foo_ representing
the function _multiply_and_add_. It expects two _input_ data nodes and two _output_ data nodes.

[:material-arrow-right: The next section introduces the pipeline configuration](pipeline-config.md).
