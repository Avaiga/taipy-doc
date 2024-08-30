This section provides details on how to submit a `Scenario^`, a `Sequence^`, or
a `Task^` for execution.

# Main principle

Submitting a `Scenario^`, a `Sequence^`, or a `Task^`, is the same as submitting
a set of tasks for execution. Each task execution is represented by a `Job^`
entity that is created when the task is submitted. The `Job^` entity holds the
status of the task execution and other related information.

To submit an entity, you need to call the `taipy.submit()^` function. This function
creates the `Job^` entities and returns a `Submission^` object as an entity holding
the jobs, the submission status, and other related information.

# Submit a scenario

In a Taipy application, running the Orchestrator service is required to execute jobs.
To see how you can run different Taipy services, please refer to the
[running Taipy services](../../run-deploy/run/running_services.md) page.

!!! note "Preventing configuration update when the Orchestrator service is running"

    After running the Orchestrator service, all configuration are blocked from update.

In this section, it is assumed that
<a href="../code-example/scenario-submission/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented. For more details on how to
configure a scenario for Task execution, see the
[scenario configuration](scenario-config.md) page.

To execute a scenario, you need to call the `taipy.submit()^` function. It returns a
`Submission^` object containing the information about the submission of the scenario
such as the created `Job^`s representing a `Task^` in the submitted scenario:

```python linenums="1"
{%
include-markdown "./code-example/scenario-submission/submit-scenario.py"
comments=false
%}
```

In line 7, we create a new scenario from a scenario configuration and submit it for
execution (line 8). The `taipy.submit()^` method triggers the submission of all the
scenario's tasks.

The Orchestrator service can also be started after `taipy.submit()^` method. Note that
jobs can only be executed after the Taipy Orchestrator service is started:

```python linenums="1"
{%
include-markdown "./code-example/scenario-submission/submit-scenario-before-run.py"
comments=false
%}
```

??? note "Another syntax."
    To submit a scenario, you can also use the method `Scenario.submit()^`:

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-submission/submit-scenario-other-syntax.py"
    comments=false
    %}
    ```

By default, Taipy will asynchronously execute the jobs. If you want to wait until the
submitted jobs are finished, you can use the parameter _wait_ and _timeout_:

```python linenums="1"
{%
include-markdown "./code-example/scenario-submission/submit-scenario-and-wait.py"
comments=false
%}
```
The parameter _wait_ is set to True. _timeout_ represents a time span in seconds. It can be an
integer or a float. By default, _wait_ is False and _timeout_ is None. If _wait_ is True and
_timeout_ is not specified or None, there is no limit to the wait time. If _wait_ is True and
_timeout_ is specified, taipy waits until all the submitted jobs are finished, or the timeout
expires (which ever occurred first).

# Submit a sequence

It is also possible to submit a `Sequence^` using the same `taipy.submit()^` function. It
returns a `Submission^` object containing the information about the submission of the sequence
such as the created `Job^`s representing the `Task^`s in the submitted sequence:

```python linenums="1"
{%
include-markdown "./code-example/scenario-submission/submit-sequence.py"
comments=false
%}
```

In line 8, we retrieve the sequence named `sales_sequence` from the created scenario. In line 10,
we submit this sequence for execution. The `taipy.submit()^` method triggers the submission of all
the sequence's tasks. When submitting a sequence, you can also use the two parameters _wait_ and
_timeout_.

??? note "Another syntax."
    To submit a sequence, you can also use the method `Sequence.submit()^`:

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-submission/submit-sequence-other-syntax.py"
    comments=false
    %}
    ```

# Submit a task

You can also submit a single task with the same `taipy.submit()^` function. It returns a
`Submission^` object containing the information about the submission of the task such as
the created `Job^` representing the submitted `Task^`:

```python linenums="1"
{%
include-markdown "./code-example/scenario-submission/submit-task.py"
comments=false
%}
```

In line 8, we retrieve the task named `predicting` from the created scenario. In line 10, we submit this
task for execution. When submitting a task, you can also use the two parameters _wait_ and _timeout_.


??? note "Another syntax."
    To submit a task, you can also use the method `Task.submit()^`:

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-submission/submit-task-other-syntax.py"
    comments=false
    %}
    ```

# Subscribe to job execution

You can subscribe to a `Sequence^` or a `Scenario^` execution to be notified when a job
status changes.

If you want a function named `my_function()` to be called on each status change of each
task execution of all scenarios, use `taipy.subscribe_scenario(my_function)`. You can use
`taipy.subscribe_sequence(my_function)` to work at the sequence level.

If you want your function `my_function()` to be called for each task of a scenario called
`my_scenario`, you should call `taipy.subscribe_scenario(my_function, my_scenario)`. It is
similar in the context of sequences: to be notified on a given sequence stored in `my_sequence`,
you must call `taipy.subscribe_sequence(my_function, my_sequence)`.

You can also define a function that receives multiple parameters to be used as a subscriber.
It is similar to the example above, you can just add your parameters as a list, for example
`taipy.subscribe_scenario(my_function, ["my_param", 42], my_scenario)`.

You can also unsubscribe to scenarios by using `taipy.unsubscribe_scenario(function)`
or `tp.unsubscribe_sequence(function)` for sequences. Same as for subscription, the un-subscription
can be global, or you can specify the scenario or sequence by passing it as a parameter.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/scenario-submission/subscribe-example.py"
    comments=false
    %}
    ```

    This example will produce the following output:

    ```console
    Submit: scenario_1
      my_global_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
      my_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
      my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_1'.
      my_subscriber: scenario 'my_scenario_1' ; task 'my_task_2'.
      my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_2'.
    Submit: scenario_2
      my_global_subscriber: scenario 'my_scenario_2'; task 'my_task_1'.
    Unsubscribe to my_global_subscriber for scenario_1
    Submit: scenario_1
      my_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
      my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_1'.
      my_subscriber: scenario 'my_scenario_1'; task 'my_task_2'.
      my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_2'.
    ```
