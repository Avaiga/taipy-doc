__taipy-rest__ provides a Flask Api built on top of __taipy-core__ for you to use Taipy via a REST Api.

This project is meant to be used as a complement for __taipy-core__ and its goal is to enable automation through REST APIs of processes built on taipy.


## What is a Taipy REST Api

Taipy REST Api allows developers to create, read, update, run and remove Taipy entities (including scenarios, pipelines, tasks, data nodes) through REST APIs. For more details about taipy-core entities, please refer to [Core concepts documentation](../core/concepts/index.md).

## How it works

1. Create and provide **taipy-rest** with a Taipy config. [(Details and examples for creating configs)](../core/config/index.md)

2. Configure __taipy-rest__ environment
    - *FLASK_ENV*: set *FLASK_ENV* to _"development"_ to set the Flask server to debug mode
    - *SECRET_KEY*: to set the secret key of the server
    - *SQLALCHEMY_DATABASE_URI*: to set the URI to a SQL database
    - *TAIPY_SETUP_FILE*: to set the path to the Taipy config file

3. Run **taipy-rest**
