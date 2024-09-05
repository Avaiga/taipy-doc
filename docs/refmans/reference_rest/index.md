---
hide:
    - toc
---
Taipy can expose REST APIs so an external application can send and receive data to and from any
Taipy application. Taipy REST Server must first be started. (See the
[REST User Manual](../../userman/scenario_features/rest/index.md) to learn how to run the `Rest^` server).

Once the taipy REST server is running, any REST client can make some HTTP requests to the various
APIs exposed.

All the APIs are exposed at the following base url: `http://<HOST>:<PORT>/api/v1/` where
`<HOST>` and `<PORT>` are placeholders to be replaced respectively by the application host and
the application port. The various entry points are grouped by domain (data node, task, sequence,
scenario, cycle, job, auth). Each domain corresponds to a specific path:

- The APIs related to authentication and authorization are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/auth/`. Here is the exhaustive list of all entrypoints for
    [auth](apis_auth.md).
- The APIs related to cycles are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/cycles/`. Here is the exhaustive list of all entrypoints for
    [cycles](apis_cycle.md).
- The APIs related to data nodes are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/datanodes/`. Here is the exhaustive list of all entrypoints
    for [data nodes](apis_datanode.md).
- The APIs related to job and orchestration are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/jobs/`. Here is the exhaustive list of all entrypoints for
    [jobs](apis_job.md).
- The APIs related to sequences are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/sequences/`. Here is the exhaustive list of all entrypoints
    for [sequences](apis_sequence.md).
- The APIs related to scenarios are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/scenarios/`. Here is the exhaustive list of all entrypoints
    for [scenarios](apis_scenario.md).
- The APIs related to tasks are grouped under the base url <br>
    `http://<HOST>:<PORT>/api/v1/tasks/`. Here is the exhaustive list of all entrypoints for
    [tasks](apis_task.md).

Note that all the schemas are described in this [schemas](schemas.md) section.
