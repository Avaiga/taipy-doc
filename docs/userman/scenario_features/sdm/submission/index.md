This page describes how to manage *submissions* in a Taipy application.

A `Submission^` is created every time an entity (`Scenario^`, a `Sequence^` or a `Task^`)
is submitted for execution. It holds the list of jobs created during the submission process,
and the submission's status.

# Submission creation

The `Submission^` is created using the `submit()^` function, passing a submittable entity
(i.e., a `Task^`, a `Scenario^`, or a `Sequence^`) as an argument. The `Submission^` entity
is returned, holding the list of jobs created during the submission process.

!!! example

    The code below demonstrates how to create a submission by submitting a scenario. When
    the scenario is submitted, a `Submission^` is returned containing the list of jobs
    created. In our case, only one job is created.

    ```python linenums="1"
    {%  include-markdown "./code-example/submission-creation.py" comments=false %}
    ```

For more details and examples on how to submit scenarios, sequences or tasks, see the
[task orchestration](../../task-orchestration/scenario-submission.md) page.

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

## Submission Status

- `SUBMITTED`: The submission has been submitted for execution but not processed yet by the
    orchestrator.
- `UNDEFINED`: The submission's jobs have been submitted for execution but got some undefined
    status changes.
- `PENDING`: The orchestrator has enqueued the submission. It is waiting for an available
    worker to start executing a first job.
- `BLOCKED`: The submission is blocked by at least one blocked job waiting for its input data
    nodes to be ready.
- `RUNNING`: The submission has its jobs currently being executed.
- `CANCELED`: The submission has been submitted but its execution has been canceled.
- `FAILED`: The submission has a job that failed during its execution.
- `COMPLETED`: The submission has successfully been executed.

# Get/Delete Submission

Three methods are available to get existing submissions:

- You can get all of them similarly to other entities with `taipy.get_submissions()^`.
- You can get the latest submission of a `Scenario^`, a `Sequence^` or a `Task^` with
    `taipy.get_latest_submission()^`.
- You can retrieve a `Submission^` from its id by using the generic `taipy.get()^` function.

A Submission can be deleted using the `taipy.delete()^` function. Deleting a Submission can
raise a `SubmissionNotDeletedException^` if the `Status^` of the Submission is not `CANCELED`,
`COMPLETED`, `FAILED` or `UNDEFINED`.

!!! example

    The code below demonstrates how to create a submission by submitting a scenario, and
    how to retrieve and delete it.

    ```python linenums="1"
    {%  include-markdown "./code-example/get-delete.py" comments=false %}
    ```

    This example produces the following output:

    ```
    (1) Number of submissions: 0.
    (2) Number of submissions: 1.
    (3) Number of submissions: 0.
    ```
