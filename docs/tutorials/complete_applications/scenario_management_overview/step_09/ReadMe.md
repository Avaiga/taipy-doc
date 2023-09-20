> You can download the code of this step [here](../src/step_09.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started-core/tree/develop/src).

# Subscribing to a scenario

*Time to complete: 15 minutes; Level: Advanced*

To have an action after changing a job status, we can [subscribe a function](https://docs.taipy.io/en/latest/manuals/core/entities/scheduling-and-job-execution/#subscribe-to-job-execution) to a scenario. A status change calls this function. This feature allows the creation of logs or particular events for Taipy GUI.

```python
def callback_scenario_state(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.
    Depending on the job and the status, it will update the message stored in a json that is then displayed on the GUI.

    Args:
        scenario (Scenario): the scenario of the job changed
        job (_type_): the job that has its status changed
    """
    print(scenario.name)
    if job.status == tp.core.Status.COMPLETED:
        for data_node in job.task.output.values():
            print(data_node.read())

```

A scenario can then subscribe to this callback.

```python
scenario = tp.create_scenarios(scenario_cfg)

scenario.subscribe(scenario_cfg)

scenario.submit()
```
