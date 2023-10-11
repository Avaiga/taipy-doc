> You can download the code for
<a href="./../src/step_09.py" download>Step 9</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 

# Subscribing to a scenario

*Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced*

To perform an action after a job status change, you can
[subscribe a function](../../../../manuals/core/entities/orchestrating-and-job-execution.md#subscribe-to-job-execution)
to a scenario. When there is a status change, this function is triggered. This feature enables the
creation of logs or specific events for the Taipy GUI.

```python
def callback_scenario_state(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever
    a job is done, it is called.
    Depending on the job and the status, it will update the message stored in a json that is then
    displayed on the GUI.

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
