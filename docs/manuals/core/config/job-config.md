The `JobConfig^` allows the developer to configure the Taipy behavior for job executions. Two main modes are
available in Taipy: the `standalone` mode and the `development` mode.


# Development mode

With the _development_ mode, the jobs are synchronously executed one by one. The jobs are directly executed
in the main thread at the submission. Note that with the _development_ mode, the submit method waits for the
jobs to be finished before to return. Please refer to the
[submit entity](../entities/scheduling-and-job-execution.md#submit-a-scenario-pipeline-or-task) section to
the see how to submit jobs.

It is particularly handy to test a job execution and/or investigate an issue in the function
executed.

The _development_ mode can be activated with the following config:

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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "development"
    ```

!!! Note

    Note that if no mode is configured, the development mode is used.

# Standalone mode

!!! Warning

    We do not encourage using standalone mode in an interactive Python environment such as Jupyter
    Notebook or iPython. However, if you find the need for it, please note that when using the
    standalone mode in an interactive environment context, the function to be provided to a task
    configuration must be defined in a separate Python module (or a .py file) and not in the
    interactive platform. For reference, please visit:
    [multiprocessing - Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers)

With the _standalone_ mode, a `Job^` runs in its own execution context, in an asynchronous manner.
At the submission, the job is queued. It is dequeued in a different thread and sent to a dedicated process to be
executed.
Note that with the _standalone_ mode, the submit method in not blocking and returns after the job is queued.
It means the submit method can return before the job finishes or even before it is dequeued. Please refer to
the [submit entity](../entities/scheduling-and-job-execution.md#submit-a-scenario-pipeline-or-task) section
to the see how to submit jobs.

You can configure the _standalone_ mode with the following config:

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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    ```

To execute multiple `Job^`s simultaneously, you can set the _nb_of_workers_ to an integer value greater
than 1. That starts each `Job^` in a dedicated process with _nb_of_workers_ as the limit of concurrent
processes that can run simultaneously.

For example, the following configuration will allow Taipy to run up to eight `Job^`s simultaneously:

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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    nb_of_workers = "8:int"
    ```

!!! Note

    If no value is provided in the _nb_of_workers_ setting in the configuration, Taipy will set this value to 1.

[:material-arrow-right: The next section introduces the configuration checker](config-checker.md).
