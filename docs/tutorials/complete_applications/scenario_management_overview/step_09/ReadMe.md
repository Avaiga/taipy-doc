> You can download the code of this step [here](../src/step_09.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started-core/tree/develop/src).

# Step 9: Scenario subscription

This step reuses the configuration provided in step 7 except for the scenario configuration. To have an action after changing a job status, we can [subscribe a function](https://docs.taipy.io/en/latest/manuals/core/entities/scheduling-and-job-execution/#subscribe-to-job-execution) to a scenario. A status change will call this function. This feature allows the creation of logs or particular events for Taipy GUI.

```python
def callback_scenario(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.

    Args:
        scenario (Scenario): the scenario of the job changed
        job (_type_): the job that has its status changed
    """
    print("Name:", scenario.name)
    if job.status.value == 7:
        for data_node in job.task.output.values():
            print(data_node.read())

```

A scenario can then subscribe to this callback.

```python
scenario = tp.create_scenarios(scenario_cfg)

scenario.subscribe(scenario_cfg)

scenario.submit()
```
