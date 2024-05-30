This page describes the `Submission^` management. It explains how to create submission,
access their attributes, and manipulate them.

TODO: What is a Submission?

# Submission creation

Every time an entity (`Scenario^`, `Sequence^` or `Task^`) is submitted for execution, a
new unique `Submission^` entity is instantiated.

TODO
- Main principle
- Cross-ref to the [Scenario submission](../../task-orchestration/scenario-execution.md) page.

# Submission attributes

Here is the list of the `Submission^`'s attributes:

- *entity_id*: The identifier of the entity that was submitted.
- _id_: The identifier of the `Submission^` entity.
- _jobs_: A list of jobs.
- _properties_: A dictionary of additional properties.
- _creation_date_: The date of this submission's creation.
- _submission_status_: The current status of this submission.
- _version_: The string indicates the application version of the submission to instantiate.
  If not provided, the latest version is used.

# Submission Status

- `SUBMITTED`: The submission has been submitted for execution but not processed yet by the orchestrator.
- `UNDEFINED`: The submission's jobs have been submitted for execution but got some undefined status changes.
- `PENDING`: The orchestrator has enqueued the submission. It is waiting for an available worker to start executing a first job.
   for its execution.
- `BLOCKED`: The submission is blocked by at least one blocked job waiting for its input data nodes to be ready.
- `RUNNING`: The submission has its jobs currently being executed.
- `CANCELED`: The submission has been submitted but its execution has been canceled.
- `FAILED`: The submission has a job that failed during its execution.
- `COMPLETED`: The submission has successfully been executed.

# Get/Delete Submission

A `Submission^` object is created when a `Scenario^`, a `Sequence^` or a `Task^` is submitted.

- You can get the latest submission of a `Scenario^`, a `Sequence^` or a `Task^` with `taipy.get_latest_submission()^`.
- You can retrieve a `Submission^` from its id by using the `taipy.get()^` function.

A Submission can be deleted using the `taipy.delete()^` function.

Deleting a Submission can raise a `SubmissionNotDeletedException^` if the `Status^` of the Submission is not `CANCELED`,
`COMPLETED`, `FAILED` or `UNDEFINED`.

!!! example

    ```python linenums="1"
    from taipy import Config
    import taipy as tp

    def double(nb):
        return nb * 2

    print(f'(1) Number of submission: {len(tp.get_submissions())}.')

    # Create a scenario then submit it.
    input_data_node_config = Config.configure_data_node("my_input", default_data=21)
    output_data_node_config = Config.configure_data_node("my_output")
    task_config = Config.configure_task("double_task", double)
    scenario_config = Config.configure_scenario("my_scenario", [task_config])

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
