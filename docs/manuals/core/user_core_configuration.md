
Taipy core is an application builder that converts user algorithms into a back-end application. To build such
an application with the desired behaviors, a few Taipy entities must be configured.
The taipy configuration methods can simply be imported from the Taipy main module as follows:
```python
import taipy as tp
```
The following sections shows how to configure the Taipy entities in python. Note that you can override the
python configuration using _TOML_ files. (More details on the [toml configuration](user_core_toml_configuration.md))
page.

# Data node configuration

For Taipy to instantiate a data node, it must be provided a data node configuration. A
[`DataNodeConfig`](../../reference/#taipy.config.data_node_config.DataNodeConfig) is
used to configure the various data nodes Taipy will manipulate.  To configure a new `DataNodeConfig`,
here is the list of the configurable attributes :

- The config `name` corresponds to the identifier of the data node config. It is a **mandatory** parameter
that must be unique. We strongly recommend to use lowercase alphanumeric characters, dash character '-', or
underscore character '_' (a name compatible with a python variable name).
- The `scope` attribute is from type [`Taipy.Scope`](../../reference/#taipy.data.scope.Scope).
It corresponds to the scope of the data node instantiated from the data node configuration.
The **default value** is `Scope.SCENARIO`.
- The storage `storage_type` is a parameter that corresponds to the type of storage of the data node. The
possible values are "pickle" (**the default value**), "csv", "excel", "generic", "in_memory", or "sql".
As explain in the following subsections, depending on the `storage_type`, other configuration attributes
will need to be provided in the `properties` parameter.
- Any other custom attribute can be provided through the `properties` dictionary (a description, a tag, a )
All the properties will be given to the data nodes instantiated from this data node configuration.
This `properties` dictionary is also used to configure the parameters specific to each storage type.

To configure a new data node into Taipy, the `taipy.configure_data_node` method should be used.

!!! example

    Here are a two examples of data node configurations.

    ```python
    import taipy as tp
    from taipy import Scope

    # We configure a simple data node. The name identifier is "date_cfg",
    # the scope is "SCENARIO" (default value), the storage type is "pickle" (default value),
    # and we added an optional custom description.
    date_cfg = tp.configure_data_node(name="date_cfg", description="The current date of the scenario")

    # We then add another data node configuration. The name identifier is "model_cfg", the scope is "CYCLE"
    # so the corresponding data node will be shared by all the scenarios from the same cycle,
    # the storage_type is "pickle" as well, and an optional custom description is given.
    model_cfg = tp.configure_data_node(name="model_cfg",
                                       scope=Scope.CYCLE,
                                       storage_type="pickle",
                                       description="The trained model shared by all scenarios")
    ```


### Pickle

A pickle data node is a specific data node used to model pickle data. To add a new _pickle_ data node
configuration, the `taipy.configure_pickle_data_node` method can be used. In addition to the generic
parameters described in the previous section
[Data node configuration](user_core_configuration.md#data-node-configuration), two optional
parameters can be provided.

- The `path` parameter represents the file path used by Taipy to read and write the data.
If the pickle file already exists (in the case of a shared input data node for instance), it is necessary
to provide the file path as the _path_ parameter. If no value is provided, Taipy will use an internal path
in the taipy storage folder (more details on the taipy storage folder configuration available on the
[Global configuration](user_core_configuration.md#global-configuration) documentation).

- If the `default_data` is given as parameter, the data node is automatically written with the corresponding
value. Any serializable python object can be used.

!!! example

    ```python
    import taipy as tp
    from taipy import Scope

    # We configure a simple pickle data node. The name identifier is "date_cfg",
    # the scope is "SCENARIO" (default value), and a default data is provided.
    date_cfg = tp.configure_pickle_data_node(name="date_cfg", default_data=datetime(2022, 1, 25))

    # We then add another pickle data node configuration. The name identifier is "model_cfg", the default
    # SCENARIO scope is used. Since the data node corresponds to a pre-existing pickle file, a path
    # "path/to/my/model.p" is provided and we added an optional custom description.
    model_cfg = tp.configure_pickle_data_node(name="model_cfg",
                                              path="path/to/my/model.p",
                                              description="The trained model")
    ```

!!! Note

    To configure a pickle data node, it is equivalent to use the method `taipy.configure_pickle_data_node` or
    the method `taipy.configure_data_node` with parameter `storage_type="pickle`.

### Csv

### Excel

### Generic

### In memory

### Sql


# Task configuration

# Pipeline configuration

# Scenario configuration

# Global configuration

# Job configuration

The Job configuration allows the user to configure the Taipy behavior regarding the job executions.
Two main modes are available in Taipy : the standalone and the airflow mode (available in the enterprise
version only).

### Standalone

With the _standalone_ mode, Taipy executes the jobs on its own execution context.
You can configure the standalone mode with the following config :
```
[JOB]
mode = "standalone"
```

!!! Note
    Note that the standalone mode is applied by default. If no mode is configured, the standalone mode is applied.

By default, Taipy executes each _job_ one by one in a synchronous configuration. You can ensure this behavior by
setting:
```
[JOB]
mode = "standalone"
nb_of_workers = 1
```
!!! Note
    Note that by default the number of workers is set to 1 : `nb_of_workers = 1` If no value is provided in the
    configuration, Taipy automatically sets the value to 1.

To execute the _jobs_ in parallel, you can set the number of workers to a positive integer value greater than 1.
Taipy will use multiprocessing in an asynchronous behavior, and run each job in a dedicated process. The value
of the variable `nb_of_workers` represents the maximum number of processes spawned in parallel. For example,
the following configuration will allow Taipy to run at most 8 jobs in parallel:
```
[JOB]
mode = "standalone"
nb_of_workers = 8
```

### Using Airflow

With the _airflow_ mode, Taipy delegates the job executions to an Airflow service. You can configure the
_airflow_ mode with the following config :
```
[JOB]
mode = "airflow"
```

#### Start Airflow from Taipy

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


#### Use an external Airflow

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
    If Taipy and Airflow are not on the same machine or if Airflow uses remote workers,
    you should mount this folder as shared.


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
    [environment-based configuration](user_core_toml_configuration.md#attribute-in-an-environment-variable)
    for `airflow_user` and `airflow_password`.

# Check configuration

!!! Abstract Todo

# More details
For more details on how to override the python configuration, please read the documentation on the
[:material-arrow-right: TOML configuration](user_core_toml_configuration.md)
