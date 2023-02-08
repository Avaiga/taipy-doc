A `Task^` is a runnable Python function provided by the developer. It represents one of the
steps that the developer wants to implement in his/her pipeline.

For example, a _task_ could be a pre-processing function to clean the initial dataset. It could also be a more complex
function that computes a training model using machine learning algorithms.

Since a _task_ represents a function, it can take a set of parameters as input and return a set of results as output.
Each input parameter and each output result is modeled as a data node.


The attributes of a task (the input data nodes, the output data nodes, the Python function) are populated based on
the task configuration `TaskConfig^` that must be provided when instantiating a new task. (Please refer to the
[`configuration details`](../config/task-config) documentation for more details on configuration).

!!! example "In our example"
    We create three tasks:

    ![tasks and data nodes](../pic/tasks_and_data_nodes.svg){ align=left }

    The first is the _**training**_ task that takes the _**sales history**_ as the input data node and returns the
    _**trained model**_ as the output data node.

    The second is the _**predict**_ task that takes the _**trained model**_ and the _**current month**_ as input and
    returns the _**sales predictions**_.

    And the third task is the _**production planning**_ task that takes the _**capacity**_ and the _**sales
    predictions**_ as input data nodes and returns the _**production orders**_ as output.


!!! Important
    The data nodes _sales history_, _current month_, and _capacity_ are considered as **input**
    data nodes since no task computes them.<br/>
    The _trained model_ and _sales predictions_' data nodes are considered as **intermediate** data nodes while
    the _production orders_ data node is considered as an **output** data node since no task reads it.


[:material-arrow-right: The next section introduces the Pipeline concept.](pipeline.md)
