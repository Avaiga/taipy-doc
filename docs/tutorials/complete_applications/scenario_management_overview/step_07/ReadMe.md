> You can download the code of this step [here](../src/step_07.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started-core/tree/develop/src).

# Step 7: Execution modes

Taipy has [different ways](https://docs.taipy.io/en/latest/manuals/core/config/job-config/) to execute the code. Changing the execution mode can be useful for running multiple tasks in parallel.
- _standalone_ mode: asynchronous. Jobs can be run in parallel depending on the graph of execution if _max_nb_of_workers_ > 1.
- _development_ mode: synchronous.

In this step, we define a new configuration and functions to showcase the two execution modes.

```python
# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10
```

![](config_07.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }



This line of code will change the execution mode (the default execution mode is _development_). Changing it to _standalone_ will make Taipy Core asynchronous. Here a maximum of two tasks will be able to run concurrently.

```python
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)
```


```python
if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_1.submit()

    time.sleep(30)
```

Jobs from the two submissions are being executed simultaneously. If `max_nb_of_workers` was greater, we could run multiple scenarios at the same time and multiple tasks of a scenario at the same time.

Some options for the [_submit_](https://docs.taipy.io/en/latest/manuals/reference/taipy.core.Scenario/#taipy.core.scenario.scenario.Scenario.submit) function exist:
- _wait_: if _wait_ is True, the submit is synchronous and will wait for the end of all the jobs (if _timeout_ is not defined).
- _timeout_: if _wait_ is True, Taipy will wait for the end of the submission up to a certain amount of time.

```python
if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
```
