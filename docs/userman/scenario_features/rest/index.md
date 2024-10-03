Taipy offers a service providing a REST API on top of the scenario and data management
features. The purpose is to automate the use of these features by exposing REST APIs.

The Taipy REST APIs allows users to create, read, update, run and remove Taipy entities
(including cycles, scenarios, sequences, tasks, jobs and data nodes) through REST APIs.
For more details about Taipy entities, please refer to
[scenario and data management](../sdm/index.md).

It is particularly useful when it comes to integrating a Taipy application in a more complex IT
ecosystem.

# Running Taipy REST server

To expose the Taipy REST APIs, the Taipy REST server must first be started.

1. Configure your Taipy application. For more details on Taipy configuration, please
    refer to the [scenario configuration](../sdm/scenario/scenario-config.md) page.

2. The REST server do not require any configuration in most of the use cases. However, as an
    advanced user, you may want to configure your Taipy REST server. Indeed, Taipy REST server
    relies on [Flask](https://flask.palletsprojects.com/en/2.2.x/#). The three following Flask
    parameters are exposed by Taipy:

    - `testing` is a Boolean parameter used to run the Flask application on testing mode.
        Default value is False.
    - `env` is an optional string parameter used as the application environment.
    - `secret_key` is an optional parameter used as the application server secret key.<br>
    <br>
    These parameters can be set using the `GlobalAppConfig^` properties. Here is an example:
    ``` python
    from taipy import Config

    Config.configure_global_app(testing=True,
                                env="production",
                                secret_key="5f352379324c22463451387a0aec5d2f")
    ```

3. Finally, you can run Taipy REST server as follows:
    ``` python
    import taipy as tp

    if __name__ == "__main__":
        rest_service = tp.Rest()
        tp.run(rest_service)
    ```
    Below is the output of the previous Python code execution.
    ```
    * Serving Flask app 'taipy.rest.app' (lazy loading)
    * Environment: None
    * Debug mode: off
    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    ```

!!! note "When running the Taipy REST server, you will also run `Orchestrator^`"

!!! info "Running the REST service"

    To run the Taipy REST service with the other Taipy services, please refer to the
    [taipy.run() function](../../run-deploy/run/running_services.md) page.

# Using Taipy REST APIs

Once your Taipy REST server is up and running, the REST APIs are exposed. Any REST client can be
used to make some HTTP requests to the various APIs exposed. The exhaustive list of APIs is
available on the [REST API](../../../refmans/reference_rest/index.md) reference manual.

The following presents a simple usage example of a Taipy REST API. It shows how to retrieve all
data nodes using either the curl command line REST client or a python REST client (the
`requests` package).

!!! example

    === "Curl"
        ```shell
            curl -X GET https://localhost:5000/api/v1/datanodes/
        ```
        In this example the REST server is exposing APIs on `localhost` on the port `5000`. To
        retrieve all data nodes, we need to call the `datanodes` entry point without any
        parameter using the `GET` HTTP method.

        The output of the previous call is the list of all existing data nodes in `JSON` format.
        In the present example, we have two data nodes returned as follows:
        ``` JSON
        [{
            "last_edit_date": null,
            "scope": "Scope.SCENARIO",
            "id":"DATANODE_forecast_value_bb9b2709-baef-494f-92e5-87fbb8d11e71",
            "validity_seconds": null,
            "validity_days": null,
            "storage_type": "pickle",
            "job_ids": [],
            "version": "latest",
            "cacheable": false,
            "edit_in_progress": false,
            "name": "First forecast_value data node",
            "owner_id": "SCENARIO_my_awesome_scenario_c6e73df8-5508-41f8-a8e5-c6b1f9cd4c73",
            "config_id": "forecast_value"
        }, {
            "last_edit_date": "2022-08-04T17:12:10.973318",
            "scope": "Scope.SCENARIO",
            "id": "DATANODE_historical_data_set_bb6b2da2-5810-43a7-9e49-006bf402010f",
            "validity_seconds": null,
            "validity_days": null,
            "storage_type": "csv",
            "job_ids": [],
            "version": "latest",
            "cacheable": false,
            "edit_in_progress": false,
            "name": "historical data",
            "owner_id": "SCENARIO_my_awesome_scenario_5ed1582b-7b5c-4d62-8f7c-5c4ee9ee721a",
            "config_id": "historical_data_set"
        }]
        ```

    === "Python"
        ```python
            import requests

            response = requests.get("https://localhost:5000/api/v1/datanodes/")
        ```
        In this example the REST server is exposing APIs on `localhost` on the port `5000`. To
        retrieve all data nodes, we need to call the `datanodes` entry point without any
        parameter using the `GET` HTTP method.

        The output of the previous call is the list of all existing data nodes in `JSON` format.
        In the present example, we have two data nodes returned as follows:
        ``` JSON
        [{
            "last_edit_date": null,
            "scope": "Scope.SCENARIO",
            "id":"DATANODE_forecast_value_bb9b2709-baef-494f-92e5-87fbb8d11e71",
            "validity_seconds": null,
            "validity_days": null,
            "storage_type": "pickle",
            "job_ids": [],
            "version": "latest",
            "cacheable": false,
            "edit_in_progress": false,
            "name": "First forecast_value data node",
            "owner_id": "SCENARIO_my_awesome_scenario_c6e73df8-5508-41f8-a8e5-c6b1f9cd4c73",
            "config_id": "forecast_value"
        }, {
            "last_edit_date": "2022-08-04T17:12:10.973318",
            "scope": "Scope.SCENARIO",
            "id": "DATANODE_historical_data_set_bb6b2da2-5810-43a7-9e49-006bf402010f",
            "validity_seconds": null,
            "validity_days": null,
            "storage_type": "csv",
            "job_ids": [],
            "version": "latest",
            "cacheable": false,
            "edit_in_progress": false,
            "name": "historical data",
            "owner_id": "SCENARIO_my_awesome_scenario_5ed1582b-7b5c-4d62-8f7c-5c4ee9ee721a",
            "config_id": "historical_data_set"
        }]
        ```
