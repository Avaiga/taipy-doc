---
hide:
  - navigation
---

# Getting Started with Taipy

Welcome to Taipy! This guide will show you how to install Taipy and create your first application.

## Install Taipy with pip

To begin with Taipy, ensure you have Python installed (version 3.8 or higher) along with
[pip](https://pip.pypa.io). Once you have these prerequisites, open your terminal or command 
prompt and run the following command to get the latest stable version of Taipy downloaded and 
installed:

``` console
$ pip install taipy
```

!!! info "Other installation options"
    
    You can find additional instructions on the [installation page](../installation/index.md) 
    if you require different ways to install Taipy or don't have Python or pip installed.


## First Taipy Scenario 
Taipy introduces the concept of a *Scenario* to model pipeline executions. A *Scenario* consists 
of an execution graph, often represented as a Directed Acyclic Graph (DAG), where tasks (or 
functions) exchange data. You can make your scenario as easy or as complicated as you want, 
depending on what you need.

For your first scenario, we'll create a simple "Hello World" example to show you the 
configuration process. Here's a picture of the scenario's execution graph, which has two data 
nodes (blue boxes) and one task (orange box):

![hello world example](hello_world.svg){width=50%}

This involves a single input data node called *name*. Afterward, a task called *build_message* 
takes the first initial data node and returns a second data node called *message*.

Building the corresponding Taipy application requires three easy steps.

### Configuration

The first step involves configuring the execution graph. This includes 
configuring data nodes, tasks, and scenario itself. 
Use the following Python code:

```python linenums="1"
from taipy import Config


def build_message(name: str):
    return f"Hello {name}!"


name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])
```

- Lines 4-5 define the function that the task will use during execution.
- Lines 8-9 configure the two data nodes, *input_name* and *message*.
- Line 10 configures a task called *build_msg* associated with the *build_message()*
  function, specifying the input and output data nodes.
- Finally, line 11 configures the execution graph of the scenario providing 
  the previously configured task.

### Core service run

The Core service processes the configuration made in the previous step to set up the scenario 
management feature.

Include the following code in your Python script:

```python linenums="1"
from taipy import Core

if __name__ == "__main__":
    Core().run()
```
- Line 3 is standard boilerplate code to ensure your script runs only from the main module, 
preventing accidental execution. It is strongly recommended to include it.

- Line 4 instantiates and runs a Core service.

### Scenario creation and data access

With the Taipy Core service up and running, you can create and manage scenarios, submit 
task graphs for execution, and access data nodes. Here's a code snippet to illustrate  
these actions:
```python linenums="1"
import taipy as tp

hello_scenario = tp.create_scenario(scenario_cfg)
hello_scenario.input_name.write("Taipy")
hello_scenario.submit()
print(hello_scenario.message.read())
```

In line 3, method `tp.create_scenario()` instantiates the new scenario name *hello_scenario* 
from the scenario configuration built before.

Line 4, sets the input data node *input_name* of *hello_scenario* with the string value "Taipy" 
using the `write()` method.

Line 5 submits the *hello_scenario* for execution, which triggers the creation and execution of 
a job. This job reads the input data node, passes the value to the *build_message()* function, 
and writes the result to the output data node.

Line 6 reads and prints the output data node *message* written by the execution of the scenario 
*hello_scenario*.

Putting all together the pieces, you can download the entire Python code for the example
from this link: <a href="./hello_world_scenario.py" download>`hello_world_scenario.py`</a>

And here is the expected output:
``` console
[2023-02-08 20:19:35,062][Taipy][INFO] job JOB_build_msg_9e5a5c28-6c3e-4b59-831d-fcc8b43f882e is completed.
Hello Taipy!
```

## Graphical Interface

In the previous step, you used Taipy Python APIs to access, edit, and submit a scenario.
This interaction is typically integrated into Python functions that get triggered by end-user 
actions in a graphical interface built using Taipy. 

In this section, we suggest a basic graphical interface for interacting with the previously created 
scenario. Use the following Python code:
``` python
from taipy import Gui

hello_scenario = None
input_name = "Taipy"
message = None


def submit_scenario(state):
    state.hello_scenario.input_name.write(state.input_name)
    state.hello_scenario.submit(wait=True)
    state.message = hello_scenario.message.read()

page = """
Name: <|{input_name}|input|>

<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

if __name__ == "__main__":
    Core().run()
    hello_scenario = tp.create_scenario(scenario_cfg)
    Gui(page).run()
```

TODO: explain the code above and result below

![result](result.png){width=50%}

Combining both the scenario and the Gui parts, you can download the entire Python code for the 
example from the link:
<a href="./hello_world.py" download>`hello_world.py`</a>

That covers the fundamental steps to begin with Taipy. For more realistic 
use cases and advanced features, refer to the 
[Tutorials](../tutorials/index.md), [demos](../demos/index.md), or 
[manuals](../manuals/index.md) pages.
