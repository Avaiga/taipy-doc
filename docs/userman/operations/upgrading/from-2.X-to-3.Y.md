---
title: Migration from 2.X to 3.Y
---

1. In Taipy GUI 3.0, the `on_action` callback signature was unified across all controls: the third
    parameter (*action*) was dropped. The *payload* dictionary parameter that used to be in fourth
    place is now in third place and contains an *action* key that is set to the action name if you
    used to use *action*.

2. In Taipy 3.0 we deprecated the **Pipeline** concept in favor of
    [**Sequence**](../../scenario_features/sdm/sequence/index.md). This also means that the
    function `configure_pipeline()` was removed from Taipy Config, making it necessary to update
    your config code. Take for instance the following configuration, built for Taipy 2.4:

    ```python title="config.py from Taipy 2.4 edition"
    from taipy import Config

    # Omitting multiply_task_cfg creation

    pipeline_cfg = Config.configure_pipeline(
        "pipeline_1",
        task_configs=[multiply_task_cfg]
    )

    scenario_cfg = Config.configure_scenario(
        "multiply_scenario",
        pipeline_configs=[pipeline_cfg]
    )
    ```

    Now, `configure_scenario()` takes task configs as parameter in place of pipeline configs, so to
    update the config above to Taipy 3.0 is just a matter of:

    ```python title="config.py from Taipy 3.0 edition"
    from taipy import Config

    # Omiting multiply_task_cfg creation

    scenario_cfg = Config.configure_scenario(
        "multiply_scenario",
        task_configs=[multiply_task_cfg]
    )
    ```

    After migrating the code, we recommend that you take advantage of `Taipy CLI`
    [migration tool](../../ecosystem/cli/migrate-entities.md) to migrate your Taipy data entities.
