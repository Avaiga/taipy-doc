---
hide:
  - navigation
---

# Getting Started with Taipy

Dive into Taipy with this beginner-friendly guide. Learn to install, configure, and deploy your first application with ease.

## Installation with pip

1. **Prerequisites**: Ensure you have Python (version 3.8 or higher) and [pip](https://pip.pypa.io) installed.
2. **Installation Command**: Run the following in your terminal or command prompt:
``` console
$ pip install taipy
```

!!! info "Other installation options"

    For alternative installation methods or if you're lacking Python or pip, refer to the [installation page](../installation/index.md).

## Your First Taipy Scenario

A Taipy *Scenario* models pipeline executions. Think of it as an execution graph, typically a Directed Acyclic Graph (DAG), with tasks or functions sharing data. The complexity of your scenario is all up to you.

Let's craft a basic "Hello World" scenario:

![Hello World Example](hello_world.svg){width=50%}

The graph involves:
- An input data node named *name*.
- A task, *build_message*, that processes the *name* data node and outputs a *message* data node.

### Setting It Up

1. **Configuration**: Set up the execution graph with the following Python code:

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
- Lines 8-9 configure the data nodes, *input_name* and *message*.
- Line 10 configures a task called *build_msg* associated with the *build_message()*
  function, specifying the input and output data nodes.
- Finally, line 11 configures the execution graph of the scenario providing 
  the previously configured task.

2. **Core Service Initialization**: The Core service processes the configuration of the previous step to set up the scenario management feature.

```python linenums="1"
from taipy import Core

if __name__ == "__main__":
    Core().run()
```

3. **Scenario & Data Management**: With the Core service up and running, you can create
and manage scenarios, submit task graphs for execution, and access data nodes:

```python linenums="1"
import taipy as tp

hello_scenario = tp.create_scenario(scenario_cfg)
hello_scenario.input_name.write("Taipy")
hello_scenario.submit()
print(hello_scenario.message.read())
```

- In line 3, method `tp.create_scenario()` instantiates the new scenario name *hello_scenario* 
from the scenario configuration built before.

- Line 4, sets the input data node *input_name* of *hello_scenario* with the string value "Taipy" 
using the `write()` method.

- Line 5 submits the *hello_scenario* for execution, which triggers the creation and execution of 
a job. This job reads the input data node, passes the value to the *build_message()* function, 
and writes the result to the output data node.

- Line 6 reads and prints the output data node *message* written by the execution of the scenario 
*hello_scenario*.

For convenience, grab the entire code for this example:
<a href="./hello_world_scenario.py" download>`hello_world_scenario.py`</a>

Expected Output:
``` console
[2023-02-08 20:19:35,062][Taipy][INFO] job JOB_build_msg_9e5a5c28-6c3e-4b59-831d-fcc8b43f882e is completed.
Hello Taipy!
```

## A Glimpse into creating a GUI

While we used the Python APIs of Taipy to manage our scenario, it typically integrates
with a graphical interface, also built using Taipy, for end-user interactions. Here's a
basic GUI set up for our "Hello World" scenario:

```python
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

For the full example with the user interface code, download:
<a href="./hello_world.py" download>`hello_world.py`</a>

TO DO: explain the code above and result below

![GUI Result](result.png){width=50%}


---

For deeper dives and more intricate use cases, check out our [Tutorials](../tutorials/index.md), [Demos](../demos/index.md), or [Manuals](../manuals/index.md).