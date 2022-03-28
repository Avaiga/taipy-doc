__taipy-rest__ is a python library built on top of [__taipy-core__](../about.md#taipy-core). Its purpose is to automate the use of Taipy core features by providing a runnable Flask Application exposing REST APIs.

It is particularly useful when it comes to integrating a Taipy application in a more complex IT ecosystem.


## What is a Taipy REST Api

Taipy REST Api allows developers to create, read, update, run and remove Taipy entities (including scenarios, pipelines, tasks, data nodes) through REST APIs. For more details about taipy-core entities, please refer to [Core concepts documentation](../core/concepts/index.md).

## How it works

1. Configure your __taipy-core__ application. For more details on Taipy Core configuration, please refer to the [Core configuration documentation](../core/config/index.md). 
At this stage, a `(taipy.core.config.)Config^` singleton must have been instantiated.

2. Configure __taipy-rest__ environment
    - *FLASK_ENV*: set *FLASK_ENV* to _"development"_ to set the Flask server to debug mode
    - *SECRET_KEY*: to set the secret key of the server

3. Run **taipy-rest**
