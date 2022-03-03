# Submit a scenario or pipeline

=> TODO tp.submit

# Jobs

## Properties

-   `task`: The [Task](../concepts/task.md) of the [Job](../concepts/job.md).
-   `force`: If True, the execution of the task is forced.
-   `creation_date`: The date of the creation of the Job with the status `SUBMITTED`.
-   `status`: The status of the [Job](../concepts/job.md).
-   `exceptions`: The exceptions handled during the execution of the [Jobs](../concepts/job.md).

## Job Status

-   `SUBMITTED`: The job is created but not enqueue for execution.
-   `BLOCKED`: The job is blocked by inputs not ready.
-   `PENDING`: The job is waiting for execution.
-   `RUNNING`: The job is being executing.
-   `CANCELLED`: The job was cancelled by user.
-   `FAILED`: The job failed due to timeout or execution error.
-   `COMPLETED`: The job execution is done and outputs were writen.
-   `SKIPPED`: The job was and will not be executed.

## Create/Get/Delete Job

[Jobs](../concepts/job.md) are created when a task is submitted.

You can get all of them with [`taipy.get_jobs`](../../../reference/#taipy.core.get_jobs). You can also get the latest
[Job](../concepts/job.md) of a [Task](../concepts/task.md) with
[`taipy.get_latest_job(task)`](../../reference/#taipy.core.get_latest_job).
You can also get a job from its id by using the [`taipy.get`](../../../reference/#taipy.core.get).

You can delete a [Job](../concepts/job.md) by using [`taipy.delete_job(job)`](../../../reference/#taipy.core.delete_job), or
you can also delete all jobs with [`taipy.delete_jobs`](../../../reference/#taipy.core.delete_jobs).

Delete a [Job](../concepts/job.md) can raise an `JobNotDeletedException` if the status of the
[Job](../concepts/job.md) is not `SKIPPED`, `COMPLETED` or `FAILED`. You can overcome this behaviour by forcing the
deletion by doing `tp.delete_job(job, force=True)`.

!!! Example

    ```python linenums="1"
    import taipy as tp

    def double(nb):
        return nb * 2

    print(f'(1) Number of job: {len(tp.get_jobs())}.')

    # Create a task then submit it.
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

# Subscribe a scenario or pipeline

After each [Task](../concepts/task.md) execution, you can be notified by subscribing to a
[Pipeline](../concepts/pipeline.md) or [Scenario](../concepts/scenario.md).

You will be notified for each scenario or pipeline by default, except if you specify one as a target.

If you want a function named `my_function` to be called on each task execution of all scenarios, use
`tp.subscribe_scenario(my_function)`.
You can use `tp.subscribe_pipeline(my_function)` to work at the pipeline level.

If you want your function `my_function` to be called for each task of a scenario called `my_scenario`, you should call
`tp.subscribe_scenario(my_function, my_scenario)`. It is similar in the context of pipelines: to be notified on a given
pipeline stored in `my_pipeline`, you must call `tp.subscribe_pipeline(my_function, my_pipeline)`.

You can also unsubscribe to scenarios by using `tp.unsubscribe_scenario(function)`
or `tp.unsubscribe_pipeline(function)` for pipelines. Same as for subscription, the unsubscription can be global,
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
