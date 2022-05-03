The `JobConfig^` allows the developer to configure the Taipy behavior for job executions. Two main modes are
available in Taipy: the `standalone` and the `airflow` mode (available in the enterprise version only).

# Standalone

With the _standalone_ mode, Taipy executes the jobs in its own execution context. You can configure the standalone
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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    ```

!!! Note

    Note that if no mode is configured, the standalone mode is used.

By default, Taipy executes each _job_ one-by-one, in a synchronous manner. You can ensure this behavior with:

=== "Python configuration"

    ```python linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone", nb_workers=1)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    nb_of_workers = "1:int"
    ```

!!! Note

    If no value is provided in the nb_of_workers setting in the configuration, Taipy will set this value to 1.

To execute the _jobs_ in parallel, you can set the number of workers to an integer value greater than 1.

Taipy will use multiple asynchronous processes, and run each job in a dedicated process. The value of the
variable `nb_of_workers` represents the maximum number of processes spawned in parallel. For example,the
following configuration allows Taipy to run at most 8 jobs in parallel:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="standalone", nb_workers=8)
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

# Using Airflow (Enterprise version only)

With the _airflow_ mode, Taipy delegates the job executions to an Airflow service. You can configure the
_airflow_ mode with the following config :

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow")
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    ```

## Starting Airflow from Taipy

To let Taipy start the Airflow service, you can use the following configuration:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=True)
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "True:bool"
    ```

By default, Airflow creates a local folder `.airflow` to store its dependencies.
You can change this location with the `airflow_folder` config:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", airflow_folder="my_custom_path")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    airflow_folder = "my_custom_path"
    ```

!!! warning "Production setting"

    Taipy starts Airflow in `standalone` mode. It is an Airflow development mode and not recommended for production.

## Using an external Airflow

By default, Taipy runs with an external Airflow. You can specify it by setting:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=False)
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "False:bool"
    ```

By default, Taipy is connected to Airflow on `localhost:8080`. You can change it by:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=False, hostname="my_remote_airflow:port")
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "False:bool"
    hostname = "my_remote_airflow:port"
    ```

Taipy _jobs_ are converted in Airflow _DAG_ through the Airflow DAG Folder.
By default, this folder is `.dags`, but you can update it by:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=False, airflow_dags_folder="/my_dag_folder")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "False:bool"
    airflow_dags_folder = "/my_dag_folder"
    ```

!!! note "Remote Airflow"

    The Airflow _Dag_ generation can only be accomplished through this folder.
    If Taipy and Airflow are not on the same machine or if Airflow uses remote workers, you must make
    sure that this folder is mounted in a shared mode.

Airflow can take time before loading _DAGS_.
In order to wait for Airflow to be ready to schedule tasks, Taipy requests the scheduling several times
until the request is actually accepted.
Depending on your Airflow configuration, you can update the number of retries:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=False, airflow_api_retry=10)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "False:bool"
    airflow_api_retry = "10:int"
    ```

Before executing a task, Airflow checks if its inputs are ready every 20 seconds by default. You can update the number of seconds between each check by:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow",airflow_sensor_poke_interval=60)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    airflow_sensor_poke_interval = "60:int"
    ```

Because Airflow executes the application code in a different directory, you must make sure that all the files used by the application are accessible by the Airflow worker. We can configure the path to the application by specifying its absolute path or relative to the Airflow folder. The default path is "" (empty string), which implies that the absolute path of the running application will be used.

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow",app_folder="/my/app/path")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    app_folder = "/my/app/path"
    ```

Taipy authentication with Airflow is based on
[basic_auth](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#basic-authentication).
If Airflow is not started by Taipy, you should provide this configuration:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", start_airflow=False, airflow_user="user", airflow_password="pass")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    start_airflow = "False:bool"
    airflow_user = "user"
    airflow_password = "pass"
    ```

!!! warning "Security"

    To ensure you are not exposing your company's confidential information, we recommend using
    [environment-based configuration](advanced-config.md#attribute-in-an-environment-variable)
    for `airflow_user` and `airflow_password`.

[:material-arrow-right: The next section introduces the configuration checker](config-checker.md).
