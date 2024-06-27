This page describes the `Job^` management. It explains how to create jobs,
access their attributes, and manipulate them.

TODO: What is a Job?

# Job creation

Every time a task is orchestrated (through a `Scenario^`, a `Sequence^` or a `Task^` submission), a new
`Job^` entity is instantiated.

TODO
- Main principle
- Cross-ref to the [Task orchestration](../../task-orchestration/scenario-submission.md) page.

# Graphical User Interface

TODO
- Motivation of using graphical components, functionalities, screenshots
- Cross-ref to the [Job Selector](job-selector.md) page.

# Job attributes

Here is the list of the `Job^`'s attributes:

- _task_: The `Task^` of the job.
- _force_: The force attribute is `True` if the execution of the job has been forced.
- _creation_date_: The date of the creation of the job with the status `SUBMITTED`.
- _status_: The status of the job.
- _stacktrace_: The stacktrace of the exceptions handled during the execution of the jobs.

# Job Status

- `SUBMITTED`: The job is created but not enqueued for execution.
- `BLOCKED`: The job is blocked because inputs are not ready.
- `PENDING`: The job is waiting for execution.
- `RUNNING`: The job is being executed.
- `CANCELED`: The job was canceled by the user.
- `FAILED`: The job failed due to timeout or execution error.
- `COMPLETED`: The job execution is done and outputs were written.
- `SKIPPED`: The job was and will not be executed.
- `ABANDONED`: The job was abandoned and will not be executed.

# Get/Delete Job

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
    from taipy import Config

    def double(nb):
        return nb * 2

    print(f'(1) Number of jobs: {len(tp.get_jobs())}.')

    # Create a scenario then submit it.
    input_data_node_config = Config.configure_data_node("my_input", default_data=21)
    output_data_node_config = Config.configure_data_node("my_output")
    task_config = Config.configure_task("double_task", double)
    scenario_config = Config.configure_scenario("my_scenario", [task_config])

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

# Cancel Job

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
    input_data_node_cfg = Config.configure_data_node("my_input", default_data=21)
    output_data_node_cfg = Config.configure_data_node("my_output")
    double_task_config = Config.configure_task("double_task", double, input_data_node_cfg, output_data_node_cfg)
    print_task_config = Config.configure_task("print_task", print, output_data_node_cfg)
    scenario_config = Config.configure_scenario("my_scenario", [double_task_config, print_task_config])

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
    input_data_node_cfg = Config.configure_data_node("my_input", default_data=21)
    output_data_node_cfg = Config.configure_data_node("my_output")
    double_task_config = Config.configure_task("double_task", double, input_data_node_cfg, output_data_node_cfg)
    print_task_config = Config.configure_task("print_task", print, output_data_node_cfg)
    scenario_config = Config.configure_scenario("my_scenario", [double_task_config, print_task_config])

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

TODO: Refer to Task orchestration
