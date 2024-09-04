---
title: Job Execution modes
category: scenario_management
data-keywords: scenario task job submission configuration standalone cluster
short-description: Increase efficiency running your scenarios making your Job Execution asynchronous.
order: 16
img: images/icon-code.svg
---

*Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced*

[Download the code](./src/job_execution.zip){: .tp-btn target='blank' }

Taipy has [different modes](../../../userman/advanced_features/configuration/job-config.md)
to execute the code. Changing the execution mode can be useful for running multiple
tasks in parallel.

- *standalone* mode: asynchronous. Jobs can be run in parallel depending on the graph
    of execution (if *max_nb_of_workers* > 1).

- *development* mode: synchronous. The default execution mode is *development*.

We define a configuration and functions to showcase the two execution modes.

```python
# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10
```

![Configuration](images/config.svg){ width=90% : .tp-image-border }

This line of code alters the execution mode. Setting it to *standalone* makes Task
orchestration work asynchronously. In this configuration, a maximum of two tasks can
run simultaneously.

!!! warning

    In *standalone* mode, when a subprocess is spawned, the code is re-executed except
    for the code inside the `if __name__ == "__main__":` condition. This can lead to
    unexpected behavior if the code is not protected.

    Therefore, it's a good practice to protect the main code with the `if __name__ == "__main":`
    condition in your Taipy application main script. By doing this, the code will not be re-executed
    when the subprocesses are spawned.

```python
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)
```


```python
if __name__=="__main__":
    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.submit()
    scenario_2.submit()

    time.sleep(30)
```

Jobs from the two submissions are being executed simultaneously. If *max_nb_of_workers* was greater, we could run multiple scenarios at the same time and multiple tasks of a scenario at the same time.

Some options for the *submit* function exist:

- *wait*: if *wait* is True, the submission waits for the end of all the jobs (if *timeout* is not defined).

- *timeout*: if *wait* is True, Taipy waits for the end of the submission up to a certain amount of time.

```python
if __name__=="__main__":
    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
```

# Entire code

```python
import time

import taipy as tp
from taipy.core.config import Config


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10

if __name__=="__main__":
    Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

    # Configuration of Data Nodes
    input_cfg = Config.configure_data_node("my_input", default_data=21)
    intermediate_cfg = Config.configure_data_node("intermediate", default_data=21)
    output_cfg = Config.configure_data_node("my_output")

    # Configuration of tasks
    first_task_cfg = Config.configure_task("double",
                                        double,
                                        input_cfg,
                                        intermediate_cfg)

    second_task_cfg = Config.configure_task("add",
                                            add,
                                            intermediate_cfg,
                                            output_cfg)

    # Configuration of the scenario
    scenario_cfg = Config.configure_scenario(id="my_scenario",
                                            task_configs=[first_task_cfg,
                                                        second_task_cfg])

    Config.export("config.toml")

    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
```
