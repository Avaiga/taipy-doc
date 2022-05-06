---
title: Taipy Rest v1.0.0
language_tabs: []
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="taipy-rest">Taipy Rest v1.0.0</h1>

> Scroll down for example requests and responses.

<h1 id="taipy-rest-api">api</h1>

## get__api_v1_datanodes_{datanode_id}

> Code samples

`GET /api/v1/datanodes/{datanode_id}`

*Get a datanode*

Get a single datanode by ID

<h3 id="get__api_v1_datanodes_{datanode_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|datanode_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "datanode": {
    "config_id": "string",
    "edit_in_progress": true,
    "id": "string",
    "job_ids": [
      "string"
    ],
    "last_edit_date": "string",
    "name": "string",
    "parent_id": "string",
    "properties": {},
    "scope": "string",
    "storage_type": "string",
    "validity_days": 0,
    "validity_seconds": 0
  }
}
```

<h3 id="get__api_v1_datanodes_{datanode_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|datanode does not exist|None|

<h3 id="get__api_v1_datanodes_{datanode_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» datanode|[DataNodeSchema](#schemadatanodeschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» edit_in_progress|boolean|false|none|none|
|»» id|string|false|none|none|
|»» job_ids|[string]|false|none|none|
|»» last_edit_date|string|false|none|none|
|»» name|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» scope|string|false|none|none|
|»» storage_type|string|false|none|none|
|»» validity_days|number|false|none|none|
|»» validity_seconds|number|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_datanodes_{datanode_id}

> Code samples

`DELETE /api/v1/datanodes/{datanode_id}`

*Delete a datanode*

Delete a single datanode by ID

<h3 id="delete__api_v1_datanodes_{datanode_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|datanode_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "datanode deleted"
}
```

<h3 id="delete__api_v1_datanodes_{datanode_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|datanode does not exist|None|

<h3 id="delete__api_v1_datanodes_{datanode_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_datanodes

> Code samples

`GET /api/v1/datanodes`

*Get a list of datanodes*

Get a list of paginated datanodes

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "config_id": "string",
      "edit_in_progress": true,
      "id": "string",
      "job_ids": [
        "string"
      ],
      "last_edit_date": "string",
      "name": "string",
      "parent_id": "string",
      "properties": {},
      "scope": "string",
      "storage_type": "string",
      "validity_days": 0,
      "validity_seconds": 0
    }
  ]
}
```

<h3 id="get__api_v1_datanodes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_datanodes-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[DataNodeSchema](#schemadatanodeschema)]|false|none|none|
|»» config_id|string|false|none|none|
|»» edit_in_progress|boolean|false|none|none|
|»» id|string|false|none|none|
|»» job_ids|[string]|false|none|none|
|»» last_edit_date|string|false|none|none|
|»» name|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» scope|string|false|none|none|
|»» storage_type|string|false|none|none|
|»» validity_days|number|false|none|none|
|»» validity_seconds|number|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_datanodes

> Code samples

`POST /api/v1/datanodes`

*Create a datanode*

Create a new datanode

> Body parameter

```json
{
  "name": "string",
  "scope": 0,
  "storage_type": "string"
}
```

<h3 id="post__api_v1_datanodes-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DataNodeConfig](#schemadatanodeconfig)|false|none|

> Example responses

> 201 Response

```json
{
  "datanode": {
    "name": "string",
    "scope": 0,
    "storage_type": "string"
  },
  "msg": "datanode created"
}
```

<h3 id="post__api_v1_datanodes-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_datanodes-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» datanode|[DataNodeConfig](#schemadatanodeconfig)|false|none|none|
|»» name|string|false|none|none|
|»» scope|integer|false|none|none|
|»» storage_type|string|false|none|none|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_tasks_{task_id}

> Code samples

`GET /api/v1/tasks/{task_id}`

*Get a task*

Get a single task by ID

<h3 id="get__api_v1_tasks_{task_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|task_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "task": {
    "config_id": "string",
    "function_module": "string",
    "function_name": "string",
    "id": "string",
    "input_ids": [
      "string"
    ],
    "output_ids": [
      "string"
    ],
    "parent_id": "string"
  }
}
```

<h3 id="get__api_v1_tasks_{task_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|task does not exist|None|

<h3 id="get__api_v1_tasks_{task_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» task|[TaskSchema](#schemataskschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» function_module|string|false|none|none|
|»» function_name|string|false|none|none|
|»» id|string|false|none|none|
|»» input_ids|[string]|false|none|none|
|»» output_ids|[string]|false|none|none|
|»» parent_id|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_tasks_{task_id}

> Code samples

`DELETE /api/v1/tasks/{task_id}`

*Delete a task*

Delete a single task by ID

<h3 id="delete__api_v1_tasks_{task_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|task_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "task deleted"
}
```

<h3 id="delete__api_v1_tasks_{task_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|task does not exist|None|

<h3 id="delete__api_v1_tasks_{task_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_tasks

> Code samples

`GET /api/v1/tasks`

*Get a list of tasks*

Get a list of paginated tasks

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "config_id": "string",
      "function_module": "string",
      "function_name": "string",
      "id": "string",
      "input_ids": [
        "string"
      ],
      "output_ids": [
        "string"
      ],
      "parent_id": "string"
    }
  ]
}
```

<h3 id="get__api_v1_tasks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_tasks-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[TaskSchema](#schemataskschema)]|false|none|none|
|»» config_id|string|false|none|none|
|»» function_module|string|false|none|none|
|»» function_name|string|false|none|none|
|»» id|string|false|none|none|
|»» input_ids|[string]|false|none|none|
|»» output_ids|[string]|false|none|none|
|»» parent_id|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_tasks

> Code samples

`POST /api/v1/tasks`

*Create a task*

Create a new task

> Body parameter

```json
{
  "config_id": "string",
  "function_module": "string",
  "function_name": "string",
  "id": "string",
  "input_ids": [
    "string"
  ],
  "output_ids": [
    "string"
  ],
  "parent_id": "string"
}
```

<h3 id="post__api_v1_tasks-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TaskSchema](#schemataskschema)|false|none|

> Example responses

> 201 Response

```json
{
  "msg": "task created",
  "task": {
    "config_id": "string",
    "function_module": "string",
    "function_name": "string",
    "id": "string",
    "input_ids": [
      "string"
    ],
    "output_ids": [
      "string"
    ],
    "parent_id": "string"
  }
}
```

<h3 id="post__api_v1_tasks-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_tasks-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» task|[TaskSchema](#schemataskschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» function_module|string|false|none|none|
|»» function_name|string|false|none|none|
|»» id|string|false|none|none|
|»» input_ids|[string]|false|none|none|
|»» output_ids|[string]|false|none|none|
|»» parent_id|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_tasks_submit_{task_id}

> Code samples

`POST /api/v1/tasks/submit/{task_id}`

*Execute a task*

Execute a task

<h3 id="post__api_v1_tasks_submit_{task_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|task_id|path|string|true|none|

> Example responses

> 204 Response

```json
{
  "msg": "task created",
  "task": {
    "config_id": "string",
    "function_module": "string",
    "function_name": "string",
    "id": "string",
    "input_ids": [
      "string"
    ],
    "output_ids": [
      "string"
    ],
    "parent_id": "string"
  }
}
```

<h3 id="post__api_v1_tasks_submit_{task_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|Inline|

<h3 id="post__api_v1_tasks_submit_{task_id}-responseschema">Response Schema</h3>

Status Code **204**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» task|[TaskSchema](#schemataskschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» function_module|string|false|none|none|
|»» function_name|string|false|none|none|
|»» id|string|false|none|none|
|»» input_ids|[string]|false|none|none|
|»» output_ids|[string]|false|none|none|
|»» parent_id|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_pipelines_{pipeline_id}

> Code samples

`GET /api/v1/pipelines/{pipeline_id}`

*Get a pipeline*

Get a single pipeline by ID

<h3 id="get__api_v1_pipelines_{pipeline_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pipeline_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "pipeline": {
    "config_id": "string",
    "parent_id": "string",
    "properties": {},
    "tasks": [
      "string"
    ]
  }
}
```

<h3 id="get__api_v1_pipelines_{pipeline_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|pipeline does not exist|None|

<h3 id="get__api_v1_pipelines_{pipeline_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» pipeline|[PipelineSchema](#schemapipelineschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» tasks|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_pipelines_{pipeline_id}

> Code samples

`DELETE /api/v1/pipelines/{pipeline_id}`

*Delete a pipeline*

Delete a single pipeline by ID

<h3 id="delete__api_v1_pipelines_{pipeline_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pipeline_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "pipeline deleted"
}
```

<h3 id="delete__api_v1_pipelines_{pipeline_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|pipeline does not exist|None|

<h3 id="delete__api_v1_pipelines_{pipeline_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_pipelines

> Code samples

`GET /api/v1/pipelines`

*Get a list of pipelines*

Get a list of paginated pipelines

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "config_id": "string",
      "parent_id": "string",
      "properties": {},
      "tasks": [
        "string"
      ]
    }
  ]
}
```

<h3 id="get__api_v1_pipelines-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_pipelines-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[PipelineSchema](#schemapipelineschema)]|false|none|none|
|»» config_id|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» tasks|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_pipelines

> Code samples

`POST /api/v1/pipelines`

*Create a pipeline*

Create a new pipeline

> Body parameter

```json
{
  "config_id": "string",
  "parent_id": "string",
  "properties": {},
  "tasks": [
    "string"
  ]
}
```

<h3 id="post__api_v1_pipelines-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PipelineSchema](#schemapipelineschema)|false|none|

> Example responses

> 201 Response

```json
{
  "msg": "pipeline created",
  "pipeline": {
    "config_id": "string",
    "parent_id": "string",
    "properties": {},
    "tasks": [
      "string"
    ]
  }
}
```

<h3 id="post__api_v1_pipelines-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_pipelines-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» pipeline|[PipelineSchema](#schemapipelineschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» tasks|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_pipelines_submit_{pipeline_id}

> Code samples

`POST /api/v1/pipelines/submit/{pipeline_id}`

*Execute a pipeline*

Execute a pipeline

<h3 id="post__api_v1_pipelines_submit_{pipeline_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pipeline_id|path|string|true|none|

> Example responses

> 204 Response

```json
{
  "msg": "pipeline created",
  "pipeline": {
    "config_id": "string",
    "parent_id": "string",
    "properties": {},
    "tasks": [
      "string"
    ]
  }
}
```

<h3 id="post__api_v1_pipelines_submit_{pipeline_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|Inline|

<h3 id="post__api_v1_pipelines_submit_{pipeline_id}-responseschema">Response Schema</h3>

Status Code **204**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» pipeline|[PipelineSchema](#schemapipelineschema)|false|none|none|
|»» config_id|string|false|none|none|
|»» parent_id|string|false|none|none|
|»» properties|object|false|none|none|
|»» tasks|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_scenarios_{scenario_id}

> Code samples

`GET /api/v1/scenarios/{scenario_id}`

*Get a scenario*

Get a single scenario by ID

<h3 id="get__api_v1_scenarios_{scenario_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scenario_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "scenario": {
    "official_scenario": true,
    "pipelines": [
      "string"
    ],
    "properties": {},
    "tags": [
      "string"
    ]
  }
}
```

<h3 id="get__api_v1_scenarios_{scenario_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|scenario does not exist|None|

<h3 id="get__api_v1_scenarios_{scenario_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» scenario|[ScenarioSchema](#schemascenarioschema)|false|none|none|
|»» official_scenario|boolean|false|none|none|
|»» pipelines|[string]|false|none|none|
|»» properties|object|false|none|none|
|»» tags|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_scenarios_{scenario_id}

> Code samples

`DELETE /api/v1/scenarios/{scenario_id}`

*Delete a scenario*

Delete a single scenario by ID

<h3 id="delete__api_v1_scenarios_{scenario_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scenario_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "scenario deleted"
}
```

<h3 id="delete__api_v1_scenarios_{scenario_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|scenario does not exist|None|

<h3 id="delete__api_v1_scenarios_{scenario_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_scenarios

> Code samples

`GET /api/v1/scenarios`

*Get a list of scenarios*

Get a list of paginated scenarios

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "official_scenario": true,
      "pipelines": [
        "string"
      ],
      "properties": {},
      "tags": [
        "string"
      ]
    }
  ]
}
```

<h3 id="get__api_v1_scenarios-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_scenarios-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[ScenarioSchema](#schemascenarioschema)]|false|none|none|
|»» official_scenario|boolean|false|none|none|
|»» pipelines|[string]|false|none|none|
|»» properties|object|false|none|none|
|»» tags|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_scenarios

> Code samples

`POST /api/v1/scenarios`

*Create a scenario*

Create a new scenario

> Body parameter

```json
{
  "official_scenario": true,
  "pipelines": [
    "string"
  ],
  "properties": {},
  "tags": [
    "string"
  ]
}
```

<h3 id="post__api_v1_scenarios-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ScenarioSchema](#schemascenarioschema)|false|none|

> Example responses

> 201 Response

```json
{
  "msg": "scenario created",
  "scenario": {
    "official_scenario": true,
    "pipelines": [
      "string"
    ],
    "properties": {},
    "tags": [
      "string"
    ]
  }
}
```

<h3 id="post__api_v1_scenarios-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_scenarios-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» scenario|[ScenarioSchema](#schemascenarioschema)|false|none|none|
|»» official_scenario|boolean|false|none|none|
|»» pipelines|[string]|false|none|none|
|»» properties|object|false|none|none|
|»» tags|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_scenarios_submit_{scenario_id}

> Code samples

`POST /api/v1/scenarios/submit/{scenario_id}`

*Execute a scenario*

Execute a scenario

<h3 id="post__api_v1_scenarios_submit_{scenario_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scenario_id|path|string|true|none|

> Example responses

> 204 Response

```json
{
  "msg": "scenario created",
  "scenario": {
    "official_scenario": true,
    "pipelines": [
      "string"
    ],
    "properties": {},
    "tags": [
      "string"
    ]
  }
}
```

<h3 id="post__api_v1_scenarios_submit_{scenario_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|Inline|

<h3 id="post__api_v1_scenarios_submit_{scenario_id}-responseschema">Response Schema</h3>

Status Code **204**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|
|» scenario|[ScenarioSchema](#schemascenarioschema)|false|none|none|
|»» official_scenario|boolean|false|none|none|
|»» pipelines|[string]|false|none|none|
|»» properties|object|false|none|none|
|»» tags|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_cycles_{cycle_id}

> Code samples

`GET /api/v1/cycles/{cycle_id}`

*Get a cycle*

Get a single cycle by ID

<h3 id="get__api_v1_cycles_{cycle_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cycle_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "cycle": {
    "creation_date": "string",
    "end_date": "string",
    "frequency": "string",
    "id": "string",
    "name": "string",
    "properties": {},
    "start_date": "string"
  }
}
```

<h3 id="get__api_v1_cycles_{cycle_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|cycle does not exist|None|

<h3 id="get__api_v1_cycles_{cycle_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» cycle|[CycleResponse](#schemacycleresponse)|false|none|none|
|»» creation_date|string|false|none|none|
|»» end_date|string|false|none|none|
|»» frequency|string|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» properties|object|false|none|none|
|»» start_date|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_cycles_{cycle_id}

> Code samples

`DELETE /api/v1/cycles/{cycle_id}`

*Delete a cycle*

Delete a single cycle by ID

<h3 id="delete__api_v1_cycles_{cycle_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cycle_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "cycle deleted"
}
```

<h3 id="delete__api_v1_cycles_{cycle_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|cycle does not exist|None|

<h3 id="delete__api_v1_cycles_{cycle_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_cycles

> Code samples

`GET /api/v1/cycles`

*Get a list of cycles*

Get a list of paginated cycles

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "creation_date": "string",
      "end_date": "string",
      "frequency": "string",
      "name": "string",
      "properties": {},
      "start_date": "string"
    }
  ]
}
```

<h3 id="get__api_v1_cycles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_cycles-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[CycleSchema](#schemacycleschema)]|false|none|none|
|»» creation_date|string|false|none|none|
|»» end_date|string|false|none|none|
|»» frequency|string|false|none|none|
|»» name|string|false|none|none|
|»» properties|object|false|none|none|
|»» start_date|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_cycles

> Code samples

`POST /api/v1/cycles`

*Create a cycle*

Create a new cycle

> Body parameter

```json
{
  "creation_date": "string",
  "end_date": "string",
  "frequency": "string",
  "name": "string",
  "properties": {},
  "start_date": "string"
}
```

<h3 id="post__api_v1_cycles-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CycleSchema](#schemacycleschema)|false|none|

> Example responses

> 201 Response

```json
{
  "cycle": {
    "creation_date": "string",
    "end_date": "string",
    "frequency": "string",
    "name": "string",
    "properties": {},
    "start_date": "string"
  },
  "msg": "cycle created"
}
```

<h3 id="post__api_v1_cycles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_cycles-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» cycle|[CycleSchema](#schemacycleschema)|false|none|none|
|»» creation_date|string|false|none|none|
|»» end_date|string|false|none|none|
|»» frequency|string|false|none|none|
|»» name|string|false|none|none|
|»» properties|object|false|none|none|
|»» start_date|string|false|none|none|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_jobs_{job_id}

> Code samples

`GET /api/v1/jobs/{job_id}`

*Get a job*

Get a single job by ID

<h3 id="get__api_v1_jobs_{job_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|job_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "job": {
    "callables": {
      "module": "string",
      "name": "string"
    },
    "task_name": "string"
  }
}
```

<h3 id="get__api_v1_jobs_{job_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|job does not exist|None|

<h3 id="get__api_v1_jobs_{job_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» job|[JobSchema](#schemajobschema)|false|none|none|
|»» callables|[Callable](#schemacallable)|false|none|none|
|»»» module|string|false|none|none|
|»»» name|string|false|none|none|
|»» task_name|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## delete__api_v1_jobs_{job_id}

> Code samples

`DELETE /api/v1/jobs/{job_id}`

*Delete a job*

Delete a single job by ID

<h3 id="delete__api_v1_jobs_{job_id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|job_id|path|integer|true|none|

> Example responses

> 200 Response

```json
{
  "msg": "job deleted"
}
```

<h3 id="delete__api_v1_jobs_{job_id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|job does not exist|None|

<h3 id="delete__api_v1_jobs_{job_id}-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get__api_v1_jobs

> Code samples

`GET /api/v1/jobs`

*Get a list of jobs*

Get a list of paginated jobs

> Example responses

> 200 Response

```json
{
  "results": [
    {
      "callables": {
        "module": "string",
        "name": "string"
      },
      "task_name": "string"
    }
  ]
}
```

<h3 id="get__api_v1_jobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="get__api_v1_jobs-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» results|[[JobSchema](#schemajobschema)]|false|none|none|
|»» callables|[Callable](#schemacallable)|false|none|none|
|»»» module|string|false|none|none|
|»»» name|string|false|none|none|
|»» task_name|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__api_v1_jobs

> Code samples

`POST /api/v1/jobs`

*Create a job*

Create a new job

> Body parameter

```json
{
  "callables": {
    "module": "string",
    "name": "string"
  },
  "task_name": "string"
}
```

<h3 id="post__api_v1_jobs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[JobSchema](#schemajobschema)|false|none|

> Example responses

> 201 Response

```json
{
  "job": {
    "callables": {
      "module": "string",
      "name": "string"
    },
    "task_name": "string"
  },
  "msg": "job created"
}
```

<h3 id="post__api_v1_jobs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="post__api_v1_jobs-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» job|[JobSchema](#schemajobschema)|false|none|none|
|»» callables|[Callable](#schemacallable)|false|none|none|
|»»» module|string|false|none|none|
|»»» name|string|false|none|none|
|»» task_name|string|false|none|none|
|» msg|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Callable">Callable</h2>
<!-- backwards compatibility -->
<a id="schemacallable"></a>
<a id="schema_Callable"></a>
<a id="tocScallable"></a>
<a id="tocscallable"></a>

```json
{
  "module": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|module|string|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_CycleResponse">CycleResponse</h2>
<!-- backwards compatibility -->
<a id="schemacycleresponse"></a>
<a id="schema_CycleResponse"></a>
<a id="tocScycleresponse"></a>
<a id="tocscycleresponse"></a>

```json
{
  "creation_date": "string",
  "end_date": "string",
  "frequency": "string",
  "id": "string",
  "name": "string",
  "properties": {},
  "start_date": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|creation_date|string|false|none|none|
|end_date|string|false|none|none|
|frequency|string|false|none|none|
|id|string|false|none|none|
|name|string|false|none|none|
|properties|object|false|none|none|
|start_date|string|false|none|none|

<h2 id="tocS_CycleSchema">CycleSchema</h2>
<!-- backwards compatibility -->
<a id="schemacycleschema"></a>
<a id="schema_CycleSchema"></a>
<a id="tocScycleschema"></a>
<a id="tocscycleschema"></a>

```json
{
  "creation_date": "string",
  "end_date": "string",
  "frequency": "string",
  "name": "string",
  "properties": {},
  "start_date": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|creation_date|string|false|none|none|
|end_date|string|false|none|none|
|frequency|string|false|none|none|
|name|string|false|none|none|
|properties|object|false|none|none|
|start_date|string|false|none|none|

<h2 id="tocS_DataNodeConfig">DataNodeConfig</h2>
<!-- backwards compatibility -->
<a id="schemadatanodeconfig"></a>
<a id="schema_DataNodeConfig"></a>
<a id="tocSdatanodeconfig"></a>
<a id="tocsdatanodeconfig"></a>

```json
{
  "name": "string",
  "scope": 0,
  "storage_type": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|scope|integer|false|none|none|
|storage_type|string|false|none|none|

<h2 id="tocS_DataNodeSchema">DataNodeSchema</h2>
<!-- backwards compatibility -->
<a id="schemadatanodeschema"></a>
<a id="schema_DataNodeSchema"></a>
<a id="tocSdatanodeschema"></a>
<a id="tocsdatanodeschema"></a>

```json
{
  "config_id": "string",
  "edit_in_progress": true,
  "id": "string",
  "job_ids": [
    "string"
  ],
  "last_edit_date": "string",
  "name": "string",
  "parent_id": "string",
  "properties": {},
  "scope": "string",
  "storage_type": "string",
  "validity_days": 0,
  "validity_seconds": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config_id|string|false|none|none|
|edit_in_progress|boolean|false|none|none|
|id|string|false|none|none|
|job_ids|[string]|false|none|none|
|last_edit_date|string|false|none|none|
|name|string|false|none|none|
|parent_id|string|false|none|none|
|properties|object|false|none|none|
|scope|string|false|none|none|
|storage_type|string|false|none|none|
|validity_days|number|false|none|none|
|validity_seconds|number|false|none|none|

<h2 id="tocS_JobSchema">JobSchema</h2>
<!-- backwards compatibility -->
<a id="schemajobschema"></a>
<a id="schema_JobSchema"></a>
<a id="tocSjobschema"></a>
<a id="tocsjobschema"></a>

```json
{
  "callables": {
    "module": "string",
    "name": "string"
  },
  "task_name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|callables|[Callable](#schemacallable)|false|none|none|
|task_name|string|false|none|none|

<h2 id="tocS_PaginatedResult">PaginatedResult</h2>
<!-- backwards compatibility -->
<a id="schemapaginatedresult"></a>
<a id="schema_PaginatedResult"></a>
<a id="tocSpaginatedresult"></a>
<a id="tocspaginatedresult"></a>

```json
{
  "next": "string",
  "pages": 0,
  "prev": "string",
  "total": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|next|string|false|none|none|
|pages|integer|false|none|none|
|prev|string|false|none|none|
|total|integer|false|none|none|

<h2 id="tocS_PipelineSchema">PipelineSchema</h2>
<!-- backwards compatibility -->
<a id="schemapipelineschema"></a>
<a id="schema_PipelineSchema"></a>
<a id="tocSpipelineschema"></a>
<a id="tocspipelineschema"></a>

```json
{
  "config_id": "string",
  "parent_id": "string",
  "properties": {},
  "tasks": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config_id|string|false|none|none|
|parent_id|string|false|none|none|
|properties|object|false|none|none|
|tasks|[string]|false|none|none|

<h2 id="tocS_ScenarioSchema">ScenarioSchema</h2>
<!-- backwards compatibility -->
<a id="schemascenarioschema"></a>
<a id="schema_ScenarioSchema"></a>
<a id="tocSscenarioschema"></a>
<a id="tocsscenarioschema"></a>

```json
{
  "official_scenario": true,
  "pipelines": [
    "string"
  ],
  "properties": {},
  "tags": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|official_scenario|boolean|false|none|none|
|pipelines|[string]|false|none|none|
|properties|object|false|none|none|
|tags|[string]|false|none|none|

<h2 id="tocS_TaskSchema">TaskSchema</h2>
<!-- backwards compatibility -->
<a id="schemataskschema"></a>
<a id="schema_TaskSchema"></a>
<a id="tocStaskschema"></a>
<a id="tocstaskschema"></a>

```json
{
  "config_id": "string",
  "function_module": "string",
  "function_name": "string",
  "id": "string",
  "input_ids": [
    "string"
  ],
  "output_ids": [
    "string"
  ],
  "parent_id": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|config_id|string|false|none|none|
|function_module|string|false|none|none|
|function_name|string|false|none|none|
|id|string|false|none|none|
|input_ids|[string]|false|none|none|
|output_ids|[string]|false|none|none|
|parent_id|string|false|none|none|
