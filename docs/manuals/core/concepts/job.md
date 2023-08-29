Tasks, Sequences, and Scenarios entities can be submitted for execution. The submission of a scenario triggers the
submission of all the contained tasks. Similarly, the submission of a sequence also triggers the request of
all the ordered tasks.

Each time a task is submitted for execution, a new _Job_ is created. A `Job^` represents a single execution of a task.
It holds all the information related to the task execution, including the **creation date**, the execution `Status^`,
the **log messages** of the user function, and the **stacktrace** of any exception that may be raised.


[:material-arrow-right: The Next section provide information on the Execution flow.](execution-flow.md)
