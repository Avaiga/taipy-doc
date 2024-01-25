---
title: Job Execution modes
category: tutorials
type: code
data-keywords: scenario task job submission configuration standalone cluster
short-description: Increase efficiency running your scenarios making your Job Execution asynchronous.
---
> You can download the code
<a href="/job_execution.py" download>here</a>. Here is the
<a href="/job_execution_toml.py" download>Python version</a>
with the
<a href="/config.toml" download>TOML file</a>
.

# Executing jobs

*Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced*

Taipy has [different ways](../../../manuals/core/config/job-config.md) to execute the code.
Changing the execution mode can be useful for running multiple tasks in parallel.

- _standalone_ mode: asynchronous. Jobs can be run in parallel depending on the graph of execution (if _max_nb_of_workers_ > 1).

- _development_ mode: synchronous. The default execution mode is _development_.

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

![Configuration](config.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

This line of code alters the execution mode. Setting it to *standalone* makes Taipy Core work asynchronously.
In this configuration, a maximum of two tasks can run simultaneously.

```python
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)
```


```python
if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.submit()
    scenario_2.submit()

    time.sleep(30)
```

Jobs from the two submissions are being executed simultaneously. If `max_nb_of_workers` was greater, we could run multiple scenarios at the same time and multiple tasks of a scenario at the same time.

Some options for the _submit_ function exist:

- _wait_: if _wait_ is True, the submission waits for the end of all the jobs (if _timeout_ is not defined).

- _timeout_: if _wait_ is True, Taipy waits for the end of the submission up to a certain amount of time.

```python
if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
```

# Entire code


```python
from taipy.core.config import Config
import taipy as tp
import datetime as dt
import pandas as pd
import time

# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10

Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

# Configuration of Data Nodes
input_cfg = Config.configure_data_node("input", default_data=21)
intermediate_cfg = Config.configure_data_node("intermediate", default_data=21)
output_cfg = Config.configure_data_node("output")

# Configuration of tasks
first_task_cfg = Config.configure_task("double",
                                       double,
                                       input_cfg,
                                       intermediate_cfg)

second_task_cfg = Config.configure_task("add",
                                        add,
                                        intermediate_cfg,
                                        output_cfg)

# Configuration of scenario
scenario_cfg = Config.configure_scenario(id="my_scenario",
                                         task_configs=[first_task_cfg,
                                                       second_task_cfg])

Config.export("config_07.toml")

if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
```
