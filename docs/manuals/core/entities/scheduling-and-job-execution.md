# Submit a scenario, pipeline or task.

To execute a scenario, you need to call the `taipy.submit()^` method:

```python linenums="1"
import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

tp.submit(scenario)
```

In line 4, we create a new scenario from a scenario configuration and submit it for execution (line 6). The `submit`
method triggers the submission of all the scenario's pipelines. Then each task of each pipeline will be submitted.

!!! Note "Other syntax."
    To submit a scenario, you can also use the method `Scenario.submit()^`:

    ```python linenums="1"
        import taipy as tp
        import my_config

        scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

        scenario.submit()
    ```

You can also submit just a single pipeline with the same `taipy.submit()^` method:

```python linenums="1"
import taipy as tp
import my_config

scenario = tp.create_scenario(monthly_scenario_cfg)
pipeline = scenario.sales_pipeline

tp.submit(pipeline)
```
In line 5, we retrieve the pipeline named `sales_pipeline` from the created scenario. In line 7, we submit only this
pipeline for execution. The `taipy.submit()^` method triggers the submission of all the pipeline's tasks.

!!! Note "Other syntax."
    To submit a pipeline, you can also use the method `Pipeline.submit()^`:

    ```python linenums="1"
        import taipy as tp
        import my_config

        scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
        pipeline = scenario.sales_pipeline
        pipeline.submit()
    ```

You can also submit just a single task with the same `taipy.submit()^` method:

```python linenums="1"
import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
task = scenario.predicting

tp.submit(task)
```
In line 5, we retrieve the task named `predicting` from the created scenario. In line 7, we submit only this
task for execution.

!!! Note "Other syntax."
    To submit a task, you can also use the method `Task.submit()^`:

    ```python linenums="1"
        import taipy as tp
        import my_config

        scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
        task = scenario.predicting
        task.submit()
    ```

# Job

Each time a task is submitted (through a `Scenario^` or a `Pipeline^` submission), a new
`Job^` entity is instantiated.

## Job attributes

Here is the list of the job's attributes:

- _task_: The `Task^` of the job.
- _force_: The force attribute is `True` if the execution of the job has been forced.
- _creation_date_: The date of the creation of the job with the status `SUBMITTED`.
- _status_: The status of the job.
- _stacktrace_: The stacktrace of the exceptions handled during the execution of the jobs.

## Job Status

-   `SUBMITTED`: The job is created but not enqueued for execution.
-   `BLOCKED`: The job is blocked by inputs not ready.
-   `PENDING`: The job is waiting for execution.
-   `RUNNING`: The job is being executed.
-   `CANCELLED`: The job was cancelled by the user.
-   `FAILED`: The job failed due to timeout or execution error.
-   `COMPLETED`: The job execution is done and outputs were written.
-   `SKIPPED`: The job was and will not be executed.

## Get/Delete Job

Jobs are created when a task is submitted.

- You can get all of them with `taipy.get_jobs()^`.
- You can get the latest job of a Task with `taipy.get_latest_job()^`.
- You can retrieve a job from its id by using the `taipy.get()^` method.

A Job can be deleted using the `taipy.delete_job()^` method. You can also delete all jobs with `taipy.delete_jobs()^`.

Deleting a Job can raise an `JobNotDeletedException^` if the `Status^` of the Job is not `SKIPPED`, `COMPLETED` or
`FAILED`. You can overcome this behaviour by forcing the deletion with the _force_ parameter set to True:
`taipy.delete_job(job, force=True)`.

!!! Example

    ```python linenums="1"
    import taipy as tp

    def double(nb):
        return nb * 2

    print(f'(1) Number of job: {len(tp.get_jobs())}.')

    # Create a scenario then submit it.
    input_data_node_config = tp.configure_data_node("input", default_value=21)
    output_data_node_config = tp.configure_data_node("output")
    task_config = tp.configure_task("double_task", double)
    scenario_config = tp.configure_scenario_from_tasks("my_scenario", [task_config])
    scenario = tp.create_scenario(scenario_config)
    tp.submit(scenario)

    # Retrieve all jobs.
    print(f'(2) Number of job: {len(tp.get_jobs())}.')

    # Get the latest created job of a Task.
    tp.get_latest_job(scenario.double_task)

    # Then delete it.
    tp.delete_job(scenario.double_task)
    print(f'(3) Number of job: {len(tp.get_jobs())}.')
    ```

This example will produce the following output:

```
(1) Number of job: 0.
(2) Number of job: 1.
(3) Number of job: 0.
```

# Subscribe to job execution

After each `Task^` execution, you can be notified by subscribing to a `Pipeline^` or a `Scenario^`.

You will be notified for each scenario or pipeline by default, except if you specify one as a target.

If you want a function named `my_function` to be called on each status change of each task execution of all scenarios,
use `taipy.subscribe_scenario(my_function)`. You can use `taipy.subscribe_pipeline(my_function)` to work at the
pipeline level.

If you want your function `my_function` to be called for each task of a scenario called `my_scenario`, you should call
`taipy.subscribe_scenario(my_function, my_scenario)`. It is similar in the context of pipelines: to be notified on a
given pipeline stored in `my_pipeline`, you must call `taipy.subscribe_pipeline(my_function, my_pipeline)`.

You can also unsubscribe to scenarios by using `taipy.unsubscribe_scenario(function)`
or `tp.unsubscribe_pipeline(function)` for pipelines. Same as for subscription, the un-subscription can be global,
or you can specify the scenario or pipeline by passing it as a parameter.

!!! Example
```python linenums="1"
import taipy as tp

def do_nothing():
    ...

def my_global_subscriber(scenario, job):
    print(f"Called from my_global_subscriber from scenario '{scenario.config_id}' and job for task '{job.task.config_id}'.")

def my_subscriber(scenario, job):
    print(f"Called from my_subscriber from scenario '{scenario.config_id}' and job for task '{job.task.config_id}'.")

task_1 = tp.configure_task("my_task_1", do_nothing)
task_2 = tp.configure_task("my_task_2", do_nothing)
scenario_1 = tp.configure_scenario_from_tasks("my_scenario", [task, task])
scenario_2 = tp.configure_scenario_from_tasks("my_scenario", [task, task])

tp.subscribe_scenario(my_global_subscriber)  # Global subscription
tp.subscribe_scenario(my_subscriber, scenario_1)  # Subscribe only on one scenario

print('Submit: scenario_1')
tp.submit(scenario_1)
print('Submit: scenario_2')

print('Unsubscribe to my_global_subscriber for scenario_1')
tp.unsubscribe_scenario(my_global_subscriber, scenario_1)
print('Submit: scenario_1)
tp.submit(scenario_1)
```

This example will produce the following output:

```
Submit: scenario_1
Called from my_global_subscriber from scenario 'my_scenario_1' and job for task 'my_task_1'.
Called from my_subscriber from scenario 'my_scenario_1' and job for task 'my_task_1'.
Called from my_subscriber from scenario 'my_scenario_1' and job for task 'my_task_2'.
Submit: scenario_2
Called from my_global_subscriber from scenario 'my_scenario_2' and job for task 'my_task_1'.
Unsubscribe to my_global_subscriber for scenario_1
Submit: scenario_1
Called from my_subscriber from scenario 'my_scenario_1' and job for task 'my_task_1'.
Called from my_subscriber from scenario 'my_scenario_1' and job for task 'my_task_2'.
```
