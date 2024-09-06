This section describes a core feature of Taipy: **The Scenario and Data management**.
It is a set of concepts and functionalities that allow Python developers to model
data science problems and empower their end-users by putting data and algorithms
directly into their hands.

End-users can then solve their problem instances by creating and shaping *Scenarios*,
which are composed of *Data nodes* and *Tasks*. They can then run these scenarios to
solve their data science problems. It democratizes access to advanced data processing
and analysis tools, enabling non-technical users to leverage complex algorithms for
their business needs.

# Scenario

Taipy provides the key concept of *Scenario*. Among other functionalities, a *Scenario*
represents an instance of a data science problem with its datasets (modeled as *Data nodes*)
and the algorithms to solve the problem. The algorithms are modeled as an execution
graph (a Directed Acyclic Graph or DAG) that can be seen as a succession of functions
(or *Tasks*) that exchange data. With Taipy, one can model simple as well as very
complex algorithms.

!!! example "Let's take some examples."

    === "Simple single function example"

        The following picture represents a simple scenario made of a single *cleaning*
        function processing a single input, the *raw data*, and returning a single
        output, the *cleaned data*.

        ![Simple scenario](img/simple-algo.svg){ margin-left=25% width=52%}

    === "Linear example with two functions"

        The second example below is slightly more complex. The first function *cleaning*
        processes a single input, the *raw data*, and returns some intermediate data named
        *cleaned data*. The second function *filtering* reads the same intermediate data
        *cleaned data* and returns a single output *filtered data*.

        ![Linear scenario](img/linear-algo.svg)

    === "Branching example"

        The third example below introduces some complexity. As you can see in the picture
        below, the function *generating* does not have any input. On the contrary, the function
        *aggregating* takes multiple inputs and returns multiple outputs.

        ![Linear scenario](img/branching-algo.svg)

# Main concepts

A few concepts are essential to leverage scenario and data management.

- A `DataNode^` (the dark blue boxes) represents a reference to a dataset, a parameter or any data.
  A data node can be used/shared by multiple tasks as input or output. It can refer to any type of
  data: a built-in Python object (e.g. an integer, a string, a dictionary or list of parameters,
  ...) or a more complex object (e.g. a file, a machine learning model, a list of custom objects,
  the result of a database query, ...).<br/>
  A data node can be shared by multiple tasks as input or output.
- A `Task^` (the orange boxes) can be seen as a function receiving data node(s) as input and
  returning data node(s) as output.
- A `Job^` represents a unique execution of a Task.
- A `Scenario^` represents a set of tasks connected through data nodes forming a
  Directed Acyclic Graph, that should be executed as a whole (or as sub-graphs via sequences) and
  create a consistent algorithm. It can also contain a set of additional data nodes for related
  data that are not part of the executable graph.
- A `Sequence^` represents a set of tasks connected through data nodes, that should be
  executed as a whole and forming a consistent algorithm. A sequence belongs to a scenario and
  can be thought of as a subgraph of the scenario's complete graph.
- A `Cycle^` is a time period corresponding to an iteration of a recurrent
  business problem. For instance, a company's sales forecast needs to be generated
  *every week*.<br/>
  A cycle is defined thanks to the **_Frequency_** of scenarios. For instance, if scenarios have
  a weekly frequency, then each cycle represents a particular week, and every scenario will be
  attached to a particular cycle (i.e. a week).
- A `Scope^` represents the *visibility* of a data node in the graph of entities, and the
  level of its owner (Scenario, Cycle, Global).

# Overview

To benefit from scenario and data management in your Taipy application, three steps have to be
followed. Note that these steps are not necessarily sequential, and can be done simultaneously,
or iteratively base on some end-users' feedback.

1. **Scenario design:**
    Identify the data nodes and tasks of your scenarios, and how they need to be connected.
    This is an important step, as it will define the behavior of your application.<br>
    Usually, it consists in identifying the application data (input datasets, parameters,
    variables, intermediate datasets, models, output data, kpis, results, etc.) that will be
    modeled as data nodes, and the Python functions (preprocessing, feature engineering, algorithms,
    training, testing, fitting, post-processing, etc.) that will be modeled as tasks.

2. **Scenario configuration:**
    Configure your application. In particular, you need to configure your data nodes, tasks, and
    scenarios based on the first step: Scenario design.
    You can use the `Config.configure_data_node()^`, `Config.configure_task()^`, and
    `Config.configure_scenario()^` methods to configure your scenarios with the execution graphs.

    !!! important "Definition: Config vs Entities"

        Among the concepts described in this section, **data nodes**, **tasks**, and **scenarios**
        require some configuration information to be created. They have a *configuration* object
        attached to their *runtime* objects.

        To differentiate them, the configuration objects are named **_configs_** (`DataNodeConfig`,
        `TaskConfig`, and `ScenarioConfig`). In contrast, the runtime objects (`DataNode`, `Task`, and
        `Scenario`) are called **_entities_**.

        One thing to wrap your head around (it may not be very intuitive for everyone at first) is that
        the **configs** are really just configuration objects describing the characteristics and the
        behaviors of the concepts they relate to. **Configs** can be seen as generators and created
        at the development time (by developers). They are not meant to be exposed to end-users.

        Then, each **entity** is instantiated from a **config** at run time (most often by end-users).
        Note also that the same **config** can be used to instantiate multiple **entities**.

    ??? Note "About the `Config`"

        The `Config` is a singleton object that is used to configure the whole application,
        not only the data and scenarios.
        For more information, see the [configuration](../../advanced_features/configuration/index.md) page.

3. **User interface implementation:**
    Implement the user interface pages that will allow end-users to create, edit, and submit
    scenarios. This is typically done using the Taipy GUI components that are using
    predefined or user defined callbacks triggered when end-users interact with them.<br>
    These callbacks often use the scenario and data management APIs.
