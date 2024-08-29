---
hide:
  - toc
---
In this section, we provide details on how to instantiate `Scenario^` entities from a
`ScenarioConfig^`. They are created from the `taipy.create_scenario()^` function.

This function creates and returns a new scenario from the scenario configuration
provided as a parameter. The scenario's creation also triggers the creation of the
related entities that do not exist yet (data nodes, tasks, sequences). These entities
are created according to the configuration provided, and particularly on the scope of
the data nodes. For more details on scopes, see the
[recurrent scenario](../what-if-analysis/scenarios-and-cycles.md) page.

Three parameters can be given to the scenario creation method :

-   `config` is a mandatory parameter of type `ScenarioConfig^`. It corresponds to a scenario
    configuration (created in the module my_config.py)
-   `creation_date` is an optional parameter of type datetime.datetime. It corresponds to
    the creation date of the scenario. If the parameter is not provided, the current date-time
    is used by default.
-   The `name` parameter is optional as well. Any string can be provided as a `name`. It can
    be used to display the scenario in a user interface.

!!! Example

    === "Scenario creation without parameters"

        In this example, only the mandatory parameter config is provided. The creation_date
        is set by default to the current datetime and the name is `None`.

        ```python
        {%
        include-markdown "./code-example/scenario-creation/scenario-creation.py"
        comments=false
        %}
        ```

    === "Scenario creation with parameters"

        In this example, all the parameters are provided. The mandatory scenario config, the
        creation_date and the name.

        ```python
        {%
        include-markdown "./code-example/scenario-creation/scenario-creation-with-params.py"
        comments=false
        %}
        ```
