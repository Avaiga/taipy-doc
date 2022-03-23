# REST Interface


The following API endpoints can be used to programmatically create, retrieve and delete a Cycle, Scenario, Pipeline, Task, Datanode:

## Cycle
- POST api/v1/cycles/...
- GET api/v1/cycles
- GET api/v1/cycles/:id
- DELETE api/v1/cycles/:id

## Scenario
- POST api/v1/scenarios?config_id=:config_id
- GET api/v1/scenarios
- GET api/v1/scenarios/:id
- DELETE api/v1/scenarios/:id

## Pipeline
- POST api/v1/pipelines?config_id=:config_id
- GET api/v1/pipelines
- GET api/v1/pipelines/:id
- DELETE api/v1/pipelines/:id

## Task
- POST api/v1/tasks?config_id=:config_id
- GET api/v1/tasks
- GET api/v1/tasks/:id
- DELETE api/v1/tasks/:id

## Datanode
- POST api/v1/datanodes?config_id=:config_id
- GET api/v1/datanodes
- GET api/v1/datanodes/:id
- DELETE api/v1/datanodes/:id


## Example

### GET all scenarios

```
# Example request
$ curl http://127.0.0.1:5000/api/v1/scenarios

# Example response
[
    {
        "creation_date": "2022-03-23T13:52:50.916249",
        "pipelines": [
            "PIPELINE_pipeline_bc6d9663-fbf8-48c5-b5be-7c81252616e2"
        ],
        "properties": {},
        "id": "SCENARIO_scenario_d0fef5f3-5c57-42b8-98ef-7f9deb472c04",
        "official_scenario": true,
        "cycle": "CYCLE_Frequency.MONTHLY_2022-03-23T135250.913339_583640ee-4460-45ae-83eb-dbed861a847d",
        "subscribers": [],
        "tags": []
    }
]
```

### GET Scenario by id

```
# Example request
$ curl http://127.0.0.1:5000/api/v1/scenarios/SCENARIO_scenario_d0fef5f3-5c57-42b8-98ef-7f9deb472c04

# Example response
{
    "creation_date": "2022-03-23T13:52:50.916249",
    "pipelines": [
        "PIPELINE_pipeline_bc6d9663-fbf8-48c5-b5be-7c81252616e2"
    ],
    "properties": {},
    "id": "SCENARIO_scenario_d0fef5f3-5c57-42b8-98ef-7f9deb472c04",
    "official_scenario": true,
    "cycle": "CYCLE_Frequency.MONTHLY_2022-03-23T135250.913339_583640ee-4460-45ae-83eb-dbed861a847d",
    "subscribers": [],
    "tags": []
}
```

### POST Scenario by config_id

```
# Example request
$ curl -X POST http://127.0.0.1:5000/api/v1/scenarios?config_id=scenario

# Example response
{
    "msg": "scenario created",
    "scenario": {
        "creation_date": "2022-03-23T14:22:48.015778",
        "pipelines": [
            "PIPELINE_pipeline_259c29a3-c620-4161-8949-383717d4fa4a"
        ],
        "properties": {},
        "id": "SCENARIO_scenario_464fa322-0a26-4de7-a2c7-5407f939c7cb",
        "official_scenario": false,
        "cycle": "CYCLE_Frequency.MONTHLY_2022-03-23T135250.913339_583640ee-4460-45ae-83eb-dbed861a847d",
        "subscribers": [],
        "tags": []
    }
}
```

### DELETE Scenario by id
```
# Example request
$ curl -X DELETE http://127.0.0.1:5000/api/v1/scenarios/SCENARIO_scenario_acb80aef-0bc1-40c4-9286-f14974fd8a30

# Example response
{
    "msg": "scenario SCENARIO_scenario_acb80aef-0bc1-40c4-9286-f14974fd8a30 deleted"
}
```
