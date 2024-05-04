The `JobConfig^` allows the developer to configure the Taipy behavior for job executions. There are three modes
available in Taipy: the *standalone* mode, the *development* mode, and the *cluster* mode


# Development mode

With the *development* mode, the jobs are synchronously executed one by one. The jobs are directly executed
in the main thread at the submission. Note that with the *development* mode, the submit method waits for the
jobs to be finished before returning. Please refer to the
[submit entity](../entities/orchestrating-and-job-execution.md#submit-a-scenario-sequence-or-task) section
on how to submit jobs.

It is particularly handy to test a job execution and/or investigate an issue in the function
executed.

The *development* mode can be activated with the following config:

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

!!! note

    Note that if no mode is configured, the development mode is used.

# Standalone mode

!!! warning

    We do not encourage using standalone mode in an interactive Python environment such as Jupyter
    Notebook or iPython. However, if you find the need for it, please note that when using the
    standalone mode in an interactive environment context, the function to be provided to a task
    configuration must be defined in a separate Python module (or a .py file) and not in the
    interactive platform. For reference, please visit:
    [multiprocessing - Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers)

With the *standalone* mode, a `Job^` runs in its own execution context, in an asynchronous manner.
At the submission, the job is queued. It is dequeued in a different thread and sent to a dedicated process to be
executed.
Note that with the *standalone* mode, the submit method is not blocking and returns after the job is queued.
It means the submit method can return before the job finishes or even before it is dequeued. Please refer to
the [submit entity](../entities/orchestrating-and-job-execution.md#submit-a-scenario-sequence-or-task) section
on how to submit jobs.

You can configure the *standalone* mode with the following config:

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

To execute multiple `Job^`s simultaneously, you can set the *max_nb_of_workers* to an integer value greater
than 1. That starts each `Job^` in a dedicated process with *max_nb_of_workers* as the limit of concurrent
processes that can run simultaneously.

!!! note

    The default value of *max_nb_of_workers* is 2.

For example, the following configuration will allow Taipy to run up to eight `Job^`s simultaneously:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone", max_nb_of_workers=8)
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    max_nb_of_workers = "8:int"
    ```

# Cluster mode

!!! warning "Available in Taipy Enterprise edition"

    This section is relevant only to the Enterprise edition of Taipy.

The *cluster* mode is designed to make a Taipy application executes jobs on a remote cluster of
distributed workers. The number of machines available in the cluster is unlimited, so the
application becomes fully scalable horizontally. It can also be adjusted dynamically depending on
some load metric.

With the *cluster* mode, a `Job^` asynchronously runs in its own environment. At the submission,
the job is queued in a RabbitMQ queue. When there is a worker available, the job is dequeued and
sent to the worker environment to be executed.

Note that with the *cluster* mode, the submit method is not blocking and returns after the job is queued.
It means the submit method can return before the job finishes or even before it is dequeued. Please refer to
the [submit entity](../entities/orchestrating-and-job-execution.md#submit-a-scenario-sequence-or-task) section
on how to submit jobs.

You can configure the *cluster* mode with the following config:

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="cluster")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "cluster"
    ```

To set up a worker environment, some requirements must be met:

- The worker environment must have access to the same Taipy application as the main environment.
- The worker environment must have the same Python environment as the main environment.
- The worker environment must have access to the same RabbitMQ server as the main environment.
- The worker environment must have access to the data of the data nodes as the main environment.
  This includes:
  - The shared drive(s) containing the data for file-based data nodes.
  - The database server(s) containing the data for database-based data nodes.

To start the worker service in the worker environment, you can use the following command:

```console
$ taipy run-worker --application-path /path/to/your/taipy/application
```
where you can provide the path to the Taipy application. The default path is the current working directory.
The worker service will start and listen to the RabbitMQ queue for incoming jobs.

!!! note "Number of worker environments"

    The number of active worker environments limits the number of concurrent jobs that can run simultaneously.

    If there is no worker available, the job is queued in the RabbitMQ queue until a worker is available.

[:material-arrow-right: The next section introduces the configuration checker](config-checker.md).
