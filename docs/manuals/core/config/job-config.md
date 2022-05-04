The `JobConfig^` allows the developer to configure the Taipy behavior for job executions. Two main modes are
available in Taipy: the `standalone` and the `airflow` mode (available in the enterprise version only).

# Standalone

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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    ```

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

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "standalone"
    nb_of_workers = "1:int"
    ```

!!! Note

    If no value is provided in the nb_of_workers setting in the configuration, Taipy will set this value to _1_.

To execute multiple `Job^` in simultaneously, you can set the **nb_of_workers** to an integer value greater than 1. That
starts each `Job^` in a dedicated process with **nb_of_workers** as the limit of concurrent processes that can run
simultaneously.

For example, the following configuration will allow Taipy to run up till eight `Job^` in simultaneously:

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

By default, Taipy is connected to Airflow on [localhost:8080](http://localhost:8080). You can change it by:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", hostname="my_remote_airflow:port")
    ```

=== "TOML configuration "

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    hostname = "my_remote_airflow:port"
    ```

Taipy `Job^` are converted in Airflow _DAG_ through the Airflow DAG Folder.
By default, this folder is _.dags_, but you can update it by:

=== "Python configuration"

    ```python  linenums="1"
    from taipy import Config

    Config.configure_job_executions(mode="airflow", airflow_dags_folder="/my_dag_folder")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
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

    Config.configure_job_executions(mode="airflow", airflow_api_retry=10)
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
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

    Config.configure_job_executions(mode="airflow", airflow_user="user", airflow_password="pass")
    ```

=== "TOML configuration"

    ```python linenums="1"
    from taipy import Config

    Config.load("config.toml")
    ```

    ```toml linenums="1" title="config.toml"
    [JOB]
    mode = "airflow"
    airflow_user = "user"
    airflow_password = "pass"
    ```

!!! warning "Security"

    To ensure you are not exposing your company's confidential information, we recommend using
    [environment-based configuration](advanced-config.md#attribute-in-an-environment-variable)
    for `airflow_user` and `airflow_password`.

[:material-arrow-right: The next section introduces the configuration checker](config-checker.md).
