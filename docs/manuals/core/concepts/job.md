Tasks, Pipelines and Scenarios entities can be submitted for execution. The submission of a scenario triggers the
submission of all the pipelines it refers to. Similarly, submission of a pipeline triggers the submission of all the
tasks it refers to.

Each time a task is submitted for execution, a new _Job_ is created. A `Job^` represents a single execution of a task.
It holds all the information related to the task execution, including the **creation date**, the execution `Status^`,
the **log messages** of the user function, and the **stacktrace** of any exception that may be raised.


[:material-arrow-right: The Next section provide information on the Execution flow.](execution-flow.md)
