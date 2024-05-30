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


# Submit a scenario, sequence, or task

In a Taipy application, running the Core service is required to execute jobs.
To see how you can run different Taipy services, please refer to the
[Running Taipy services](../../run-deploy/run/running_services.md) page.

!!! note "Preventing configuration update when the Taipy Core service is running"

    After running the Core service, all configuration are blocked from update.

In this section, it is assumed that <a href="../code-example/my_config.py" download>`my_config.py`</a>
module contains a Taipy configuration already implemented.

To execute a scenario, you need to call the `taipy.submit()^` function. It returns a `Submission^` object containing
the information about the submission of the scenario such as the created `Job^`s representing a `Task^` in
the submitted scenario:

```python linenums="1"
import taipy as tp
import my_config

tp.Core().run()

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

submission = tp.submit(scenario)
```

In line 6, we create a new scenario from a scenario configuration and submit it for execution (line 8).
The `taipy.submit()^` method triggers the submission of all the scenario's tasks.

The Core service can also be started after `taipy.submit()^` method. Note that jobs can only be executed
after the Taipy Core service is started.

```python linenums="1"
import taipy as tp
import my_config

tp.Core().run()

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

tp.submit(scenario)
```

!!! note "Another syntax."
    To submit a scenario, you can also use the method `Scenario.submit()^`:

    ```python linenums="1"
    import taipy as tp
    import my_config

    tp.Core().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    scenario.submit()
    ```

By default, Taipy will asynchronously execute the jobs. If you want to wait until the submitted jobs
are finished, you can use the parameter _wait_ and _timeout_:

```python linenums="1"
import taipy as tp
import my_config

tp.Core().run()

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
task = scenario.predicting

tp.submit(task, wait=True, timeout=3)
```

_timeout_ represents a time span in seconds. It can be an integer or a float. By default, _wait_
is False and _timeout_ is None. If _wait_ is True and _timeout_ is not specified or None, there
is no limit to the wait time. If _wait_ is True and _timeout_ is specified,
taipy waits until all the submitted jobs are finished, or the timeout expires (which ever occurred
first).

It is also possible to submit a single sequence using the same `taipy.submit()^` function. It returns
a `Submission^` object containing the information about the submission of the sequence such as the created `Job^`s
representing a `Task^` in the submitted sequence:

```python linenums="1"
import taipy as tp
import my_config

tp.Core().run()

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
sequence = scenario.sales_sequence

submission = tp.submit(sequence)
```

In line 5, we retrieve the sequence named `sales_sequence` from the created scenario. In line 7, we submit this
sequence for execution. The `taipy.submit()^` method triggers the submission of all the sequence's tasks. When
submitting a sequence, you can also use the two parameters _wait_ and _timeout_.

!!! note "Another syntax."
    To submit a sequence, you can also use the method `Sequence.submit()^`:

    ```python linenums="1"
    import taipy as tp
    import my_config

    tp.Core().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    sequence = scenario.sales_sequence
    sequence.submit()
    ```

You can also submit a single task with the same `taipy.submit()^` function. It returns a `Submission^` object containing
the information about the submission of the task such as the created `Job^` representing the submitted `Task^`:

```python linenums="1"
import taipy as tp
import my_config

tp.Core().run()

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
task = scenario.predicting

submission = tp.submit(task)
```

In line 5, we retrieve the task named `predicting` from the created scenario. In line 7, we submit this
task for execution. When submitting a task, you can also use the two parameters _wait_ and _timeout_.

!!! note "Another syntax."
    To submit a task, you can also use the method `Task.submit()^`:

    ```python linenums="1"
    import taipy as tp
    import my_config

    tp.Core().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task = scenario.predicting
    task.submit()
    ```

# Subscribe to job execution

You can subscribe to a `Sequence^` or a `Scenario^` execution to be notified when a job status changes.

If you want a function named `my_function()` to be called on each status change of each task execution
of all scenarios, use `taipy.subscribe_scenario(my_function)`. You can use
`taipy.subscribe_sequence(my_function)` to work at the sequence level.

If you want your function `my_function()` to be called for each task of a scenario called `my_scenario`,
you should call `taipy.subscribe_scenario(my_function, my_scenario)`. It is similar in the context of
sequences: to be notified on a given sequence stored in `my_sequence`, you must call
`taipy.subscribe_sequence(my_function, my_sequence)`.

You can also define a function that receives multiple parameters to be used as a subscriber. It is
similar to the example above, you can just add your parameters as a list, for example
`taipy.subscribe_scenario(my_function, ["my_param", 42], my_scenario)`.

You can also unsubscribe to scenarios by using `taipy.unsubscribe_scenario(function)`
or `tp.unsubscribe_sequence(function)` for sequences. Same as for subscription, the un-subscription
can be global, or you can specify the scenario or sequence by passing it as a parameter.

!!! example

    ```python linenums="1"
    import taipy as tp

    def do_nothing():
        ...

    def my_global_subscriber(scenario, job):
        print(f"my_global_subscriber: scenario '{scenario.config_id}'; task '{job.task.config_id}'.")

    def my_subscriber(scenario, job):
        print(f"my_subscriber: scenario '{scenario.config_id}'; task '{job.task.config_id}'.")

    def my_subscriber_multi_param(scenario, job, params):
        print(f"my_subscriber_multi_param: params {params}; task '{job.task.config_id}'.")

    task_1 = Config.configure_task("my_task_1", do_nothing)
    task_2 = Config.configure_task("my_task_2", do_nothing)
    scenario_1 = Config.configure_scenario("my_scenario", [task, task])
    scenario_2 = Config.configure_scenario("my_scenario", [task, task])

    tp.Core().run()

    params = ["my_param_1", 42]

    tp.subscribe_scenario(my_global_subscriber)  # Global subscription
    tp.subscribe_scenario(my_subscriber, scenario_1)  # Subscribe only to one scenario
    tp.subscribe_scenario(my_subscriber_multi_param, params, scenario_1)  # Subscribe with params

    print('Submit: scenario_1')
    tp.submit(scenario_1)
    print('Submit: scenario_2')

    print('Unsubscribe to my_global_subscriber for scenario_1')
    tp.unsubscribe_scenario(my_global_subscriber, scenario_1)
    print('Submit: scenario_1')
    tp.submit(scenario_1)
    ```

    This example will produce the following output:

    ```
    Submit: scenario_1
    my_global_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
    my_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
    my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_1 .
    my_subscriber: scenario 'my_scenario_1' ; task 'my_task_2'.
    my_subscriber_multi_param: params ["my_param_1", 42]; task 'my_task_2'.
    Submit: scenario_2
    my_global_subscriber: scenario 'my_scenario_2'; task 'my_task_1'.
    Unsubscribe to my_global_subscriber for scenario_1
    Submit: scenario_1
    my_subscriber: scenario 'my_scenario_1'; task 'my_task_1'.
    my_subscriber: scenario 'my_scenario_1'; task 'my_task_2'.
    ```
