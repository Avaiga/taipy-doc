Taipy provides you three runnable services: Taipy GUI, Taipy REST, and Taipy
Orchestrator. You can run Taipy services by calling the method _run()_ from the
service instance either `Gui^`, `Rest^`, or `Orchestrator^`. You can also use
`taipy.run()` to run multiple service(s) together.

!!! note "Running from the main module"

    As you can see in the following examples, the code to run a Taipy service is
    set within a `if` block checking if the special variable `__name__` equals to
    `"__main__"`. It's a standard boilerplate code that protects users from
    accidentally invoking the script when they didn't intend to. In particular the
    module is called when Taipy spawns a new Process.

    If you need to execute some code prior to start a Taipy service (like setting
    some variables, initializing some data, submitting some tasks, create a scenario)
    we strongly recommend to set this code within the `if __name__ == "__main__"` block.

# Running all Taipy services: `Gui`, `Orchestrator` and `Rest`
You can run all Taipy services together by using `taipy.run()` with the code below:

```python linenums="1"
{%
include-markdown "../code_sample/basic_gui_rest_app.py"
comments=false
%}
```

Since Taipy REST relies on Taipy Orchestrator when running the Taipy REST service,
Taipy Orchestrator will automatically run along with it. Therefore, Taipy Orchestrator
will run with Taipy GUI and Taipy REST in the previous code example.

# Running `Gui` and `Orchestrator`

If you don't want to expose REST APIs to manage the Taipy entities, you can run Taipy
GUI along with Taipy Orchestrator together with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    orchestrator = tp.Orchestrator()
    gui = tp.Gui(page="# Getting started with *Taipy*")

    tp.run(gui, orchestrator, title="Taipy application")
```

# Running `Gui` alone

You can run the GUI service alone with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")

    tp.run(gui, title="Taipy application")  # same as gui.run(title="Taipy application")
```

# Running `Orchestrator` alone

You can run the Orchestrator service alone with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    orchestrator = tp.Orchestrator()

    tp.run(orchestrator)  # It is equivalent to orchestrator.run()
```

By starting the Orchestrator service, all configuration updates will be blocked.
To continue to configure your application, stop the Orchestrator service by running
`orchestrator.stop()`.

!!! note
    On a Taipy application, running the Orchestrator service is required to execute jobs.

# Running `Rest` and `Orchestrator`

If you don't need to run GUI, you can run Taipy Orchestrator along with Taipy REST
together. By default, running `Rest`, also runs `Orchestrator` as the REST service relies
on the Orchestrator service :

```python
import taipy as tp

if __name__ == "__main__":
    rest = tp.Rest()

    tp.run(rest)  # It is equivalent to rest.run()
```
