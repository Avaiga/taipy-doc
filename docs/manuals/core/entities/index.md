# Taipy's Core entities

This documentation focuses on providing necessary information to use the Taipy Core entities, and in particular
the capabilities related to scenario management. It is assumed that the reader already knows the
[Taipy Core concepts](../concepts/index.md) described in a previous chapter.

Let’s assume also that the configuration represented in the picture below is implemented in the
module <a href="./code_example/my_config.py" download>`my_config.py`</a>.

=== "Graph representation of the scenario config"

    ![scenarios](../pic/scenarios.svg)

=== "Module my_config.py"

    ```python linenums="1"
    {%
    include-markdown "./code_example/my_config.py"
    comments=false
    %}
    ```

Please refer to the [configuration documentation](../config/index.md) to have information on how to configure a
Taipy application.

[:material-arrow-right: The next section presents the scenario creation](scenario-creation.md).
