The `JobConfig^` allows the user to
configure the Taipy behavior regarding the job executions.
Two main modes are available in Taipy : the `standalone` and the `airflow` mode (available in the enterprise
version only).

# Standalone

With the _standalone_ mode, Taipy executes the jobs on its own execution context.
You can configure the standalone mode with the following config:

```
[JOB]
mode = "standalone"
```

!!! Note

    Note that if no mode is configured, the standalone mode is used.

By default, Taipy executes each _job_ one by one, in a synchronous manner. You can ensure this behavior by setting:

```
[JOB]
mode = "standalone"
nb_of_workers = 1
```

!!! Note

    If no value is provided in the nb_of_workers setting in the configuration, Taipy will set this value to 1.

To execute the _jobs_ in parallel, you can set the number of workers to a positive integer value greater than 1.

Taipy will use multiple and asynchronous processes, and run each job in a dedicated process. The value of the
variable `nb_of_workers` represents the maximum number of processes spawned in parallel. For example,the
following configuration allows Taipy to run at most 8 jobs in parallel:

```
[JOB]
mode = "standalone"
nb_of_workers = 8
```

# Using Airflow

With the _airflow_ mode, Taipy delegates the job executions to an Airflow service. You can configure the
_airflow_ mode with the following config :

```
[JOB]
mode = "airflow"
```

## Start Airflow from Taipy

To let Taipy start the Airflow service, you can use the following configuration:

```
[JOB]
start_airflow = True
```

By default, Airflow creates a local folder `.airflow` to store its dependencies.
You can change this location with the `airflow_folder` config:

```
[JOB]
airflow_folder = "my_custom_path"
```

!!! warning "Production setting"

    Taipy starts Airflow in `standalone` mode. It is an Airflow development mode and not recommended for production.

## Use an external Airflow

By default, Taipy runs with an external Airflow. You can specify it by setting:

```
[JOB]
start_airflow = False
```

By default, Taipy is connected to Airflow on `localhost:8080`. You can change it:

```
[JOB]
hostname = "my_remote_airflow:port"
```

Taipy _jobs_ are converted in Airflow _DAG_ through the Airflow DAG Folder.
By default, this folder is `.dags`, but you can update it:

```
[JOB]
airflow_dags_folder = "/dags"
```

!!! note "Remote Airflow"

    The Airflow _Dag_ generation can only be accomplished through this folder.
    If Taipy and Airflow are not on the same machine or if Airflow uses remote workers, you must make
    sure that this folder is mounted in a shared mode.

Airflow can take time before loading _DAGS_.
In order to wait for Airflow to be ready to schedule tasks, Taipy requests the scheduling several times
until the request is actually accepted.
Depending on your Airflow configuration, you can update the number of retries:

```
[JOB]
airflow_api_retry = 10
```

Taipy authentication with Airflow is based on
[basic_auth](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#basic-authentication).
If Airflow is not started by Taipy, you should provide this configuration:

```
[JOB]
airflow_user = "user"
airflow_password = "pass"
```

!!! note "Security"

    To ensure you are not exposing your company's secrets, we recommend using
    [environment-based configuration](advanced-config.md#attribute-in-an-environment-variable)
    for `airflow_user` and `airflow_password`.

[:material-arrow-right: Next section introduces the configuration checker](config-checker.md).
