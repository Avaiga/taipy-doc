This page describes how to manage *tasks* in Taipy. It explains how to configure,
create and use *tasks*.

A `Task^` is a submittable entity that represents a function to execute. It is
created from a `TaskConfig^` and can be submitted to the Taipy orchestration
for execution. It brings together the user code as function, the inputs and
the outputs as data nodes (instances of the `DataNode^` class).

# Task configuration

A task configuration is necessary to instantiate a `Task^`. To create a
`TaskConfig^`, you can use the `Config.configure_task()^` method with the following parameters:

- _**id**_: The id of the task configuration to be created. This id is **mandatory** and must
  be a unique and valid Python identifier.
- _**function**_: The function to execute.
- _**inputs**_: The input data nodes referring to the *function*'s parameter(s) data to be
  executed.
- _**outputs**_: The output data nodes referring to the result(s) data of the *function*
  to be executed.
- _**skippable**_: Boolean attribute indicating if the task execution can be skipped if
  all output data nodes are up-to-date (see the *validity_period* attribute in the
  [data node configuration](../../data-integration/data-node-config.md#config-attributes)
  page). The default value of *skippable* is False.

!!! example

    === "Single input and output"

        ```python linenums="1"
        {%
        include-markdown "./code-example/task-config-simple.py"
        comments=false
        %}
        ```

        In the example above, we created a `TaskConfig^` named `double_task_cfg`.

        In lines 4-5, we define a function `double()`, to be used in a `Task^`
        instantiated from the task config. It takes a single parameter and returns
        a single value.

        In lines 8-9, two data node configurations are created. They will be used
        respectively as argument and result of the function `double()`.

        Finally, on line 12-16, we create the task configuration with the id *double_task*.
        It represents the function `double()` that expects an *input* data node as a parameter
        and returns an *output* data node. On line 13, the Task configuration has been set as
        `skippable`. That means when submitting a Task entity instantiated from this TaskConfig,
        Taipy will skip its execution if its input data nodes haven't changed since the previous
        execution.

    === "Multiple inputs and outputs"

        Because a Task can have several inputs and outputs, `Config.configure_task()^` can
        receive lists of `DataNodeConfig^` objects.

        ```python linenums="1"
        {%
        include-markdown "./code-example/task-config-multiple.py"
        comments=false
        %}
        ```

        In lines 4-5, we define a function with two parameters and two return values.

        In lines 8-9, two data nodes configurations are created. They will be used as the
        function arguments.

        In lines 11-12, two data nodes are configured. They will be used as the function
        results.

        Finally, in lines 14-17, we create the task configuration with the id *foo*
        representing the function *multiply_and_add*. It expects two *input* data nodes
        and two *output* data nodes.

# Task creation

Tasks get created when scenarios are created using the `taipy.create_scenario()^` method.

For more details, see the [scenario creation](../scenario/index.md#scenario-creation) page.

# Task attributes

A `Task^` entity is identified by a unique identifier `id` Taipy generates.
A task also holds various properties accessible as an attribute of the task:

- _**config_id**_ is the id of the scenario configuration.
- _**input**_ is the list of input data nodes.
- _**output**_ is the list of output data nodes.
- _**function**_ is the Python function associated with the Task config.<br/>
  The *function* takes as many parameters as there are data nodes in the *input* attribute.
  Each parameter corresponds to the return value of an input data node `read()` method.<br/>
  The function returns as many parameters as there are data nodes in the *output* attribute. Each
  *function*'s returned value corresponds to the parameter of an output data node `write()` method.
- _**version**_: The string indicates the application version of the task to instantiate.
  If not provided, the current version is used. Refer to the
  [version management](../../../advanced_features/versioning/index.md) page for more details.
- _**skippable**_: Boolean attribute indicating if a task execution can be skipped when all output
  data nodes are up-to-date (see the *validity_period* attribute in the
  [data node management](../../data-integration/data-node-config.md#config-attributes)
  page). The default value of *skippable* is False.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to shows the task attributes.

    ```python linenums="1"
    {%
    include-markdown "./code-example/attribute-example.py"
    comments=false
    %}
    ```

# Get tasks

## Get tasks by id

The first method to access a task is from its id by using the `taipy.get()^` method.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to get a task by its id.

    ```python linenums="1"
    {%
    include-markdown "./code-example/get-task-by-id.py"
    comments=false
    %}
    ```

Here, the two variables `task` and `task_retrieved` are equal.

## Get tasks by config id

A task can be retrieved from a scenario or a sequence, by accessing the task config_id attribute.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to get a task by its configuration id.

    ```python linenums="1"
    {%
    include-markdown "./code-example/get-task-by-config-id.py"
    comments=false
    %}
    ```

Tasks can also be retrieved using `taipy.get_entities_by_config_id()^` providing the config_id.
This method returns the list of all existing tasks instantiated from the config_id provided as a parameter.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to get tasks by configuration id.

    ```python linenums="1"
    {%
    include-markdown "./code-example/get-entities-by-config-id.py"
    comments=false
    %}
    ```

## Get all tasks

All tasks that are part of a **scenario** or a **sequence** can be
directly accessed as attributes:

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to get all tasks from a scenario.

    ```python linenums="1"
    {%
    include-markdown "./code-example/get-all-tasks.py"
    comments=false
    %}
    ```

All the tasks can be retrieved using the method `taipy.get_tasks()^`.
which returns the list of all existing tasks.

!!! example

    ```python linenums="1"
    import taipy as tp

    # Retrieve all tasks
    tasks = tp.get_tasks()
    ```

# Get parent scenarios and sequences

To access the parent entities of a task (scenarios or sequences), you can
use either the method `Task.get_parents()^` or the function
`taipy.get_parents()^`. Both return the parents of the task.

!!! example

    The code below uses the `monthly_scenario_cfg` configuration imported from the
    <a href="../code-example/index/my_config.py" download>`my_config.py`</a>
    module to demonstrate how to get parent entities from a task.

    ```python linenums="1"
    {%
    include-markdown "./code-example/get-parents.py"
    comments=false
    %}
    ```

# Submit a task

A `Task^` is a submittable entity. You can submit a task with the `taipy.submit()^` function
or the `Task.submit()^` method. Submitting a task automatically creates a `Job^` modeling the
`Task^` execution and returns a `Submission^` object containing the information about the
submission of the task such as the created `Job^` and the submission status.

For more details and examples on how to submit a task, see the
[scenario submission](../../task-orchestration/scenario-submission.md#submit-a-task) page.
