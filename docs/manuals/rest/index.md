# Taipy REST API

The Taipy REST package is a python library built on top of [Taipy Core](../about.md#taipy-core). Its purpose is to
automate the use of Taipy Core features by providing a runnable application exposing REST APIs.

It is particularly useful when it comes to integrating a Taipy application in a more complex IT ecosystem.


## What is a Taipy REST API

Taipy REST API allows developers to create, read, update, run and remove Taipy entities (including scenarios,
pipelines, tasks, data nodes) through REST APIs. For more details about Taipy entities, please refer to [Core
concepts documentation](../core/concepts/index.md).

## How it works

1. Configure your Taipy Core application. For more details on Taipy Core configuration, please refer to the
   [Core configuration documentation](../core/config/index.md).

2. Configure Taipy REST environment
    - _FLASK_ENV_: Can be set to _"development"_ to set the server to debug mode.
    - _SECRET_KEY_: The secret key of the server.

3. Run Taipy REST

```
import taipy as tp
rest_service = tp.Rest()
rest_service.run()
```
