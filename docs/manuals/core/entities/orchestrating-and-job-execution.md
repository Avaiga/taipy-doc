# Submit a scenario, sequence, or task

In a Taipy application, running the Core service is required to execute jobs. To see how you
can run different Taipy services, please refer to the
[Running Taipy services](../../run-deploy/run/running_services.md) page.

!!! note "Preventing configuration update when the Taipy Core service is running"

    After running the Core service, all configuration are blocked from update.

In this section, it is assumed that <a href="./code_example/my_config.py" download>`my_config.py`</a>
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

# Submission

Each time a `Scenario^`, a `Sequence^` or a `Task^` is submitted, a new `Submission^` entity is created.

## Submission attributes

Here is the list of the `Submission^`'s attributes:

- *entity_id*: The identifier of the entity that was submitted.
- _id_: The identifier of the `Submission^` entity.
- _jobs_: A list of jobs.
- _properties_: A dictionary of additional properties.
- _creation_date_: The date of this submission's creation.
- _submission_status_: The current status of this submission.
- _version_: The string indicates the application version of the submission to instantiate.
  If not provided, the latest version is used.

## Submission Status

- `SUBMITTED`: The submission has been submitted for execution but not processed yet by the orchestrator.
- `UNDEFINED`: The submission's jobs have been submitted for execution but got some undefined status changes.
- `PENDING`: The submission has been enqueued by the orchestrator. It is waiting for an executor to be available
   for its execution.
- `BLOCKED`: The submission has been blocked because it has been finished with a job being blocked.
- `RUNNING`: The submission has its jobs currently being executed.
- `CANCELED`: The submission has been submitted but its execution has been canceled.
- `FAILED`: The submission has a job that failed during its execution.
- `COMPLETED`: The submission has successfully been executed.

## Get/Delete Submission

A `Submission^` object is created when a `Scenario^`, a `Sequence^` or a `Task^` is submitted.

- You can get the latest submission of a `Scenario^`, a `Sequence^` or a `Task^` with `taipy.get_latest_job()^`.
- You can retrieve a `Submission^` from its id by using the `taipy.get()^` method.

A Submission can be deleted using the `taipy.delete()^` method.

Deleting a Submission can raise an `SubmissionNotDeletedException^` if the `Status^` of the Submission is not `CANCELED`,
`COMPLETED`, `FAILED` or `UNDEFINED`.

!!! example

    ```python linenums="1"
    import taipy as tp

    def double(nb):
        return nb * 2

    print(f'(1) Number of submission: {len(tp.get_submissions())}.')

    # Create a scenario then submit it.
    input_data_node_config = tp.configure_data_node("input", default_data=21)
    output_data_node_config = tp.configure_data_node("output")
    task_config = tp.configure_task("double_task", double)
    scenario_config = tp.configure_scenario("my_scenario", [task_config])

    tp.Core().run()

    scenario = tp.create_scenario(scenario_config)
    tp.submit(scenario)

    # Retrieve all submission.
    print(f'(2) Number of submissions: {len(tp.get_submissions())}.')

    # Get the latest created submission of the scenario.
    tp.get_latest_submission(scenario)

    # Then delete it.
    tp.delete(submission)
    print(f'(3) Number of submissions: {len(tp.get_submissions())}.')
    ```

This example will produce the following output:

```
(1) Number of submissions: 0.
(2) Number of submissions: 1.
(3) Number of submissions: 0.
```

# Job

Each time a task is orchestrated (through a `Scenario^`, a `Sequence^` or a `Task^` submission), a new
`Job^` entity is instantiated.

## Job attributes

Here is the list of the `Job^`'s attributes:

- _task_: The `Task^` of the job.
- _force_: The force attribute is `True` if the execution of the job has been forced.
- _creation_date_: The date of the creation of the job with the status `SUBMITTED`.
- _status_: The status of the job.
- _stacktrace_: The stacktrace of the exceptions handled during the execution of the jobs.

## Job Status

- `SUBMITTED`: The job is created but not enqueued for execution.
- `BLOCKED`: The job is blocked because inputs are not ready.
- `PENDING`: The job is waiting for execution.
- `RUNNING`: The job is being executed.
- `CANCELED`: The job was canceled by the user.
- `FAILED`: The job failed due to timeout or execution error.
- `COMPLETED`: The job execution is done and outputs were written.
- `SKIPPED`: The job was and will not be executed.
- `ABANDONED`: The job was abandoned and will not be executed.

## Get/Delete Job

Jobs are created when a task is submitted.

- You can get all of them with `taipy.get_jobs()^`.
- You can get the latest job of a Task with `taipy.get_latest_job()^`.
- You can retrieve a job from its id by using the `taipy.get()^` method.

A Job can be deleted using the `taipy.delete_job()^` method. You can also delete all jobs with `taipy.delete_jobs()^`.

Deleting a Job can raise an `JobNotDeletedException^` if the `Status^` of the Job is not `SKIPPED`, `COMPLETED` or
`FAILED`. You can overcome this behaviour by forcing the deletion with the _force_ parameter set to True:
`taipy.delete_job(job, force=True)`.

!!! example

    ```python linenums="1"
    import taipy as tp

    def double(nb):
        return nb * 2

    print(f'(1) Number of jobs: {len(tp.get_jobs())}.')

    # Create a scenario then submit it.
    input_data_node_config = tp.configure_data_node("input", default_data=21)
    output_data_node_config = tp.configure_data_node("output")
    task_config = tp.configure_task("double_task", double)
    scenario_config = tp.configure_scenario("my_scenario", [task_config])

    tp.Core().run()

    scenario = tp.create_scenario(scenario_config)
    tp.submit(scenario)

    # Retrieve all jobs.
    print(f'(2) Number of jobs: {len(tp.get_jobs())}.')

    # Get the latest created job of a Task.
    tp.get_latest_job(scenario.double_task)

    # Then delete it.
    tp.delete_job(scenario.double_task)
    print(f'(3) Number of jobs: {len(tp.get_jobs())}.')
    ```

This example will produce the following output:

```
(1) Number of jobs: 0.
(2) Number of jobs: 1.
(3) Number of jobs: 0.
```

## Cancel Job

Jobs are created when a task is submitted.

- You can cancel a job with the following statuses `SUBMITTED`, `PENDING`, or `BLOCKED` with `taipy.cancel_job(job)^`.
  When canceling a job, you will set the `Status^` of subsequent jobs of the canceled job to `ABANDONED`. However, a
  job whose status is `RUNNING`, `COMPLETED`, `SKIPPED`, `FAILED`, `CANCELED`, or `ABANDONED`, cannot be canceled.
  When the cancel method is called on a job with its status being either `RUNNING`, `COMPLETED`, or `SKIPPED`, its
  subsequent jobs will be abandoned while its status remains unchanged.

!!! example "Canceling a job"

    ```python
    import taipy as tp

    def double(nb):
        sleep(5)
        return nb * 2

    print(f'(1) Number of jobs: {len(tp.get_jobs())}.')

    # Create a scenario then submit it.
    input_data_node_cfg = tp.configure_data_node("input", default_data=21)
    output_data_node_cfg = tp.configure_data_node("output")
    double_task_config = tp.configure_task("double_task", double, input_data_node_cfg, output_data_node_cfg)
    print_task_config = tp.configure_task("print_task", print, output_data_node_cfg)
    scenario_config = tp.configure_scenario("my_scenario", [double_task_config, print_task_config])

    tp.Core().run()

    scenario = tp.create_scenario(scenario_config)
    tp.submit(scenario)

    # Count the jobs.
    print(f'(2) Number of jobs: {len(tp.get_jobs())}.')

    jobs = tp.get_latest_job(scenario.double_task)

    # Get status of the job.
    print(f'(3) Status of job double_task: {job[0].status}')
    print(f'(4) Status of job print_task: {jobs[1].status}')

    # Then cancel the second job.
    tp.cancel_job(job[1])

    sleep(10)

    print(f'(5) Status of job double_task: {job[0].status}')
    print(f'(6) Status of job print_task: {jobs[1].status}')
    ```

This example produces the following output:

```
(1) Number of jobs: 0.
(2) Number of jobs: 2.
(3) Status of job double_task: Status.RUNNING
(4) Status of job print_task: Status.BLOCKED
(5) Status of job double_task: Status.COMPLETED
(6) Status of job print_task: Status.CANCELED
```

!!! example "Canceling a running job"

    ```python
    import taipy as tp

    def double(nb):
        sleep(5)
        return nb * 2

    print(f'(1) Number of jobs: {len(tp.get_jobs())}.')

    # Create a scenario then submit it.
    input_data_node_cfg = tp.configure_data_node("input", default_data=21)
    output_data_node_cfg = tp.configure_data_node("output")
    double_task_config = tp.configure_task("double_task", double, input_data_node_cfg, output_data_node_cfg)
    print_task_config = tp.configure_task("print_task", print, output_data_node_cfg)
    scenario_config = tp.configure_scenario("my_scenario", [double_task_config, print_task_config])

    tp.Core().run()

    scenario = tp.create_scenario(scenario_config)
    tp.submit(scenario)

    # Count the jobs.
    print(f'(2) Number of jobs: {len(tp.get_jobs())}.')

    jobs = tp.get_latest_job(scenario.double_task)

    # Get status of the job.
    print(f'(3) Status of job double_task: {job[0].status}')
    print(f'(4) Status of job print_task: {jobs[1].status}')

    # Then cancel the first job.
    tp.cancel_job(job[0])

    sleep(10)

    print(f'(5) Status of job double_task: {job[0].status}')
    print(f'(6) Status of job print_task: {jobs[1].status}')
    ```

This example produces the following output:

```
(1) Number of jobs: 0.
(2) Number of jobs: 2.
(3) Status of job double_task: Status.RUNNING
(4) Status of job print_task: Status.BLOCKED
(5) Status of job double_task: Status.COMPLETED
(6) Status of job print_task: Status.ABANDONED
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

    task_1 = tp.configure_task("my_task_1", do_nothing)
    task_2 = tp.configure_task("my_task_2", do_nothing)
    scenario_1 = tp.configure_scenario("my_scenario", [task, task])
    scenario_2 = tp.configure_scenario("my_scenario", [task, task])

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
