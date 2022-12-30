The `JobConfig^` allows the developer to configure the Taipy behavior for job executions. Two main modes are
available in Taipy: the `standalone` and the `development` mode (available for debugging).

# Standalone mode

!!! Warning

    We do not encourage using standalone mode in an interactive Python environment such as Jupyter Notebook or iPython. However, if you find the need for it, please note that when using the standalone mode in an interactive environment context, the function to be provided to a task configuration must be defined in a separated Python module (or a .py file) and not in the interactive platform. For reference, please visit:[multiprocessing — Process-based parallelism — Python 3.11.1 documentation](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers)

With the _standalone_ mode, Taipy executes the `Job^` in its own execution context. You can configure the standalone
mode with the following config:

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ``toml linenums="1" title="config.toml"     [JOB]     mode = "standalone"     ``

!!! Note

    Note that if no mode is configured, the standalone mode is used.

By default, Taipy executes each `Job^` one-by-one, in a synchronous manner. You can ensure this behavior with:

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone", nb_of_workers=1)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ``toml linenums="1" title="config.toml"     [JOB]     mode = "standalone"     nb_of_workers = "1:int"     ``

!!! Note

    If no value is provided in the_nb_of_workers_ setting in the configuration, Taipy will set this value to 1.

To execute multiple `Job^` simultaneously, you can set the _nb_of_workers_ to an integer value greater than 1. That
starts each `Job^` in a dedicated process with _nb_of_workers_ as the limit of concurrent processes that can run
simultaneously.

For example, the following configuration will allow Taipy to run up to eight `Job^` simultaneously:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone", nb_of_workers=8)
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ``toml linenums="1" title="config.toml"     [JOB]     mode = "standalone"     nb_of_workers = "8:int"     ``

# Development mode

With the _development_ mode, the jobs are executed one by one in a synchronous way. This is particularly useful to
test a job execution and or investigate an issue. The _development_ mode can be activated with the following config :

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="development")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ``toml linenums="1" title="config.toml"     [JOB]     mode = "development"     ``

[:material-arrow-right: The next section introduces the configuration checker](config-checker.md).
