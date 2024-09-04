In this section, we explore how to benefit from data processing and task orchestration
submitting Taipy *Scenarios*.

# What is a Scenario?

Taipy provides the key concept of `Scenario^`. Among other functionalities,
a *scenario* provides the functionalities for modeling, executing and monitoring algorithms.
It models an algorithm as an execution graph (a Directed Acyclic Graph or DAG) to solve
a data science problem. The execution graph can be seen as a succession of functions
(or `Task^`) that exchange data (or `DataNode^`). Scenarios can range from simple to
highly complex.

!!! example "Let's take some examples."

    === "Simple single function example"

        The following picture represents a simple scenario made of a single *cleaning*
        task processing a single input data node, the *raw data*, and returning a single
        output data node, the *cleaned data*.

        <figure class="tp-center">
        <img src="img/index/simple-algo.svg" class="visible-dark" width="400">
        <img src="img/index/simple-algo.svg" class="visible-light" width="400">
        <figcaption>Simple scenario</figcaption>
        </figure>

    === "Linear example with two functions"

        The second example below is slightly more complex. The first task *cleaning*
        processes a single input data node, the *raw data*, and returns some intermediate
        data node named *cleaned data*. The second task *filtering* reads the same
        intermediate data node *cleaned data* and returns a single output data node
        named *filtered data*.

        <figure class="tp-center">
        <img src="img/index/linear-algo.svg" class="visible-dark" width="600"/>
        <img src="img/index/linear-algo.svg" class="visible-light" width="600"/>
        <figcaption>Linear scenario</figcaption>
        </figure>

    === "Branching example"

        The third example below introduces some complexity. As you can see in the picture
        below, the task *generating* does not have any input. On the contrary, the task
        *aggregating* takes multiple inputs and returns multiple outputs.

        <figure class="tp-center">
        <img src="img/index/branching-algo.svg" class="visible-dark" width="800"/>
        <img src="img/index/branching-algo.svg" class="visible-light" width="800"/>
        <figcaption>Branching scenario</figcaption>
        </figure>

- A `DataNode^` (the dark blue boxes) represents a reference to a dataset or a parameter
    set. For more details, please refer to the [data integration](../data-integration/index.md)
    section.<br/>
    A data node can be shared by multiple tasks as input or output.
- A `Task^` (the orange boxes) can be seen as a function receiving data node(s) as input
    and returning data node(s) as output.

# Why use Scenarios?

Using Taipy for data processing and task execution offers several distinct advantages
that cater to the needs of data scientists and developers aiming to build robust,
production-ready applications with ease for their end-users. Here are some key benefits:

1. **Easy to configure:**
    No matter how complex your problem may be, defining execution graphs as scenarios, tasks,
    and data nodes is simple. For more details on how to configure scenarios, see the
    [scenario configuration](scenario-config.md) page. <br>
    Taipy Studio, an extension for [Visual Studio Code](https://code.visualstudio.com/),
    enhances the user experience by providing a graphical editor to build a scenario configuration.
    <br>
    For more details, see the [Taipy Studio](../../ecosystem/studio/index.md) page.

2. **Efficient Orchestration and execution**:
    Taipy already implements utility methods to create, manage, submit your scenarios.
    With support for parallelism, remote execution, horizontal scalability, and skippable
    tasks, your end-users can run their data processing pipelines smoothly and quickly while
    minimizing resource costs. <br>
    For more details on how to create, submit and manage scenarios,
    see the [scenario creation](scenario-creation.md), [scenario submission](scenario-submission.md),
    [scenario management](../sdm/scenario/index.md) pages.

3. **Taipy visual elements**:
    Benefit from a comprehensive set of visual elements to empower end users just in one line
    of code. Manage, display, edit, and submit scenarios in a user-friendly graphical interface.
    <br>
    For more details, see the [visual elements](vizelmts.md) page.<br>

4.  **Integration with existing Tools:**
    Integrate seamlessly with any Python library or any external model such as
    [Scikit learn](https://scikit-learn.org/),
    [MLlib](https://spark.apache.org/docs/latest/ml-guide.html),
    [XGBoost](https://xgboost.readthedocs.io/en/stable/),
    [TensorFlow](https://www.tensorflow.org/),
    [OpenML](https://www.openml.org/), [Hugging Face](https://huggingface.co/), etc.
    Any Python function can be used as a Taipy *task*, and any data source can be used as
    a *data node*.

# How to use Scenarios?

A `Scenario^` is instantiated from a `ScenarioConfig^`, which encapsulates the execution graph
definition. To create and submit scenarios, you need to:

1. **Configure a scenario:**
    Configuring a scenario for Task execution is done using the `Config.configure_scenario()^`
    method and consists in defining the scenario structure and the execution graph. For that
    the data nodes and tasks must have been configured using `Config.configure_data_node()^`
    and `Config.configure_task()^` methods.
    <br>
    For more details, see the [scenario configuration](scenario-config.md) page.

2. **Create a scenario:**
    Instantiating a scenario from its configuration is done programmatically with the
    `create_scenario()^` function. When a scenario is instantiated, related tasks and data nodes
    are instantiated from their configurations as well.
    For more details, see the [scenario creation](scenario-creation.md) page.<br>
    Typically, this step is done by an end-user using the graphical interface built with
    [Taipy GUI](../../gui/index.md). In particular, the
    [scenario selector](../../../refmans/gui/viselements/corelements/scenario_selector.md) natively includes a
    scenario creation capability.

3. **Submit a scenario for execution:**
    Submitting a scenario for an execution is done programmatically through the `submit()^`
    method. <br>
    For more details, see the [scenario submission](scenario-submission.md) page.<br>
    Typically, this step is done by an end-user using the graphical interface built with
    [Taipy GUI](../../gui/index.md). The [scenario viewer](../../../refmans/gui/viselements/corelements/scenario.md) is
    designed for this purpose.


!!! example

    === "Hello world"

        Please refer to the [hello world](hello-world.md) page to get a didactic example.

    === "Complete example"

        The following code shows a complete example of how to create a scenario configuration
        and submit it for execution. It consists of creating a dumb function named "do_nothing"
        and used to configure a scenario. The scenario configuration is then used to instantiate
        a scenario and submit it for execution.

        ```python linenums="1"
        {%
        include-markdown "./code-example/index/complete-example.py"
        comments=false
        %}
        ```
        Here is the
        <a href="./code-example/index/complete-example.py" download>complete python code</a>
        corresponding to the example.

    === "With user interface"

        The following code shows a complete example of how to have a quick user interface for
        scenario execution. It consists of creating a dumb function named "identity" and used
        to create a scenario configuration. A user interface is created with three controls
        allowing to create and execute scenarios.

        ```python linenums="1"
        {%
        include-markdown "./code-example/index/example-with-gui.py"
        comments=false
        %}
        ```
        Here is the
        <a href="./code-example/index/example-with-gui.py" download>complete python code</a>
        corresponding to the example.
