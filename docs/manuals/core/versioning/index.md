# Taipy Core Version Control

Taipy Core version control system is built to help users with:

- Developing Taipy Core applications in [development mode](./development_mode.md).
- Storing all entities of the application to an experiments, and possibly re-run the application with older entities
later on with [experiment mode](./experiment_mode.md).
- Push an experiment to production to run along with existing entities on production environment in
[production mode](./production_mode.md).

In the following sections, it is assumed that [`arima_taipy_app.py`](../arima_taipy_app.py) module contains a Taipy configuration already implemented.

!!! info "Command line arguments"

    To show all optional command line arguments for a Taipy Core application, run
    ``` console
    $ python arima_taipy_app.py --help
    ```

!!! example "A simple Taipy Core application"

    === "arima_taipy_app.py module"

        ```python
        {%
        include-markdown "./arima_taipy_app.py"
        comments=false
        %}
        ```

    === "arima_app_config.py module"

        ```python
        {%
        include-markdown "./arima_app_config.py"
        comments=false
        %}
        ```

    === "arima_algorithms.py module"

        ```python
        {%
        include-markdown "./arima_algorithms.py"
        comments=false
        %}
        ```
