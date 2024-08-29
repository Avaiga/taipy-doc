---
hide:
  - toc
---
Taipy provides a checking mechanism to validate if your configuration is correct.

You can trigger the check by calling:
```python linenums="1"
from taipy import Config

Config.check()
```

The `Config.check()^` method returns a collector of issues. Each issue corresponds to an inconsistency in
the configuration attached to an issue level (`INFO`, `WARNING`, `ERROR`). `Config.check()^` raises an
exception if at least one issue collected has the `ERROR` level.

!!! info
    The `Config.check()^` is automatically called when the Orchestrator service is run.

Here is the list of the possible issues that the checker could return:

- A `WARNING` issue is created if the `repository_type` property is populated in the `CoreSection^` with an
  unsupported repository value.
- An `ERROR` issue is created if the `storage_type` and the `scope` properties of any `DataNodeConfig^` are not
  provided with a correct value.
- Depending on the `storage_type` value of a `DataNodeConfig^`, an `ERROR` issue is created if a specific required
  property is missing.
- An `ERROR` issue is created if one of the `inputs` and `outputs` parameters of a `TaskConfig^` does not correspond
  to a `DataNodeConfig` or a list of `DataNodeConfig^`.
- A `WARNING` issue is created if a `TaskConfig^` has no input and no output.
- An `ERROR` issue is created if any `DataNodeConfig^` of the `inputs` or `outputs` has the same name as one of the
  attributes or properties of the `TaskConfig^`.
- An `ERROR` issue is created if the `function` parameter of a `TaskConfig^` is not a callable function.
- An `ERROR` issue is created if one of the tasks provided in the `sequences` parameters does not does not exist in
  the corresponding list of tasks in `tasks` parameter of the `ScenarioConfig^`.
- An `ERROR` issue is created if a `ScenarioConfig^` has no task configuration defined.
- An `ERROR` issue is created if any item of a `ScenarioConfig^` task list does not 
  correspond to a `TaskConfig^`.
- A `ERROR` issue is created if any additional data node of a `ScenarioConfig^` does not
  correspond to a `DataNodeConfig^`.
- An `ERROR` issue is created if any `DataNodeConfig^` or `TaskConfig^` or sequence of the `ScenarioConfig^` has the same name as
  one of the attributes or properties of the `ScenarioConfig^`.
- An `ERROR` issue is created if the `frequency` parameter of a `ScenarioConfig^` has an incorrect `Frequency^` value.
- An `ERROR` issue is created if the value of `comparators` property of a `ScenarioConfig^` is not a dictionary, with each key is a data node id and the value is a callable function.
- An `ERROR` issue is created if any data node, task, or sequence of a `ScenarioConfig^` has the same configuration id
  with another one in the same `ScenarioConfig^`.
- If the `JobConfig^` has been configured with multiple workers, an `ERROR` issue is created if an "in_memory"
  `DataNodeConfig^` is defined.
- An `ERROR` issue is created if the `migration_function` parameter of a `MigrationConfig^` is not a callable function.
- An `ERROR` issue is created if the `target_version` parameter of a `MigrationConfig^` is not a valid production
  version.
- An `INFO` issue is created if no `MigrationConfig^` is defined to migrate entities from an old production version
  to the next.
- An `ERROR` issue is created if any additional property of any configuration has the same name as one of the attributes
  of the configuration class.
