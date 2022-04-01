# Taipy's Core concepts

Taipy Core is an application builder built to help data scientists to turn their algorithms into real, customized
data-driven applications. Taipy Core provides the necessary concepts for modeling, executing, and monitoring such
algorithms. The purpose of this section if to define such concepts.

An algorithm can be seen as a succession of functions that exchange data. It can be described as an
execution graph. With Taipy one can model simple algorithms as well as more complex algorithms.

!!! example "Let's take some examples."

    === "Simple single function example"

        The following picture represents a simple algorithm made of a single _cleaning_ function processing a single input,
        the _raw data_, and returning a single output, the _cleaned data_.

        ![Simple algorithm](../pic/simple_algo.svg){ margin-left=25% width=52%}

    === "Linear example with two functions"

        The second example below is slightly more complex. The first function _cleaning_ processes a single input,
        the _raw data_, and returns some intermediate data named _cleaned data_. The second function _filtering_ reads the
        same intermediate data _cleaned data_ and returns a single output _filtered data_.

        ![Linear algorithm](../pic/linear_algo.svg)

    === "Branching example"

        The third example below introduces some complexity. As you can see on the picture below, the function
        _generating_ does not have any input. On the contrary, the function _aggregating_ takes multiple inputs and
        returns multiple outputs.

        ![Linear algorithm](../pic/branching_algo.svg)

In the next sections, the following concepts are defined:

- A [Data node](data-node.md) (the dark blue boxes) represents a dataset. It can be shared by multiple tasks as input or
  output.
- A [Task](task.md) (the orange boxes) can be seen as a function taking some data node(s) as input and returns
  some data node(s).
- A [Job](job.md) is a unique execution of a Task.
- A [Pipeline](pipeline.md) represents an algorithm made of tasks that should run together.
- A [Scenario](scenario.md) is made of one or multiple pipelines. It represents an instance of a business problem to
  solve.
- A [Cycle](cycle.md) or work cycle is a time period corresponding to an iteration of a recurrent scenario.
- A [Scope](scope.md) represents the _visibility_ of a data node in the graph of entities. It corresponds to the
  level of the 'owner' of the data node (Pipeline, Scenario, Cycle).

!!! definition "Config vs Entities"

    Among the previous concepts, data nodes, tasks, pipelines, and scenarios must be created by providing a
    configuration object.

    To differentiate the configuration objects from their runtime counterparts, they are named **_configs_**
    (`DataNodeConfig`, `TaskConfig`, `PipelineConfig`, and `ScenarioConfig`) while the runtime objects
    (`DataNode`, `Task`, `Pipeline`, and `Scenario`) are called **_entities_**.

    On this page, we provide information on the entities. More details on the configuration objects are available in
    the [configuration documentation](../config/index.md).


[:material-arrow-right: Next section introduces the data node concept](data-node.md).
