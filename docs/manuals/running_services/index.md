Taipy provides you three runnable services: Taipy GUI, Taipy Rest, and Taipy Core. You can run Taipy services by
calling the method _run()_ from the service instance either `Gui^`, `Rest^`, or `Core^`. You can also use
`taipy.run()` to start the service(s).

!!! important

    As you can see in the following examples, the code to run a Taipy service is set within a `if` block checking if
    the special variable `__name__` equals to `"__main__"`. It's a standard boilerplate code that protects users from
    accidentally invoking the script when they didn't intend to. In particular the module is called when Taipy
    spawns a new Process.

    If you need to execute some code prior to start a Taipy service (like setting some variables, initializing some
    data, submitting some tasks, create a scenario) we strongly recommend to set this code within the
    `if __name__ == "__main__"` block.

## Running `Gui`

You can run the GUI service alone with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")

    # Approach 1
    gui.run(gui, title="Taipy Demo")

    # Approach 2
    tp.run(gui, title="Taipy Demo")
```

## Running `Core`

You can run the Core service alone with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    core = tp.Core()

    # Approach 1
    core.run()

    # Approach 2
    tp.run(core)
```

By starting the Core service, all configuration will be blocked from update to prepare for job execution.
To continue to configure your application, stop the Core service by running `core.stop()`.

!!! note
    On a Taipy application that uses the Taipy Core API, running the Core service is required to execute jobs.

## Running `Rest` and `Core`

By default, running the Rest service, also starts the Core service as the Rest service relies on the Core service :
```python
import taipy as tp

if __name__ == "__main__":
    rest = tp.Rest()

    # Approach 1
    rest.run()

    # Approach 2
    tp.run(rest)
```

The code above is similar as:
```python
import taipy as tp

if __name__ == "__main__":
    core = tp.Core()
    rest = tp.Rest()

    # Approach 1
    core.run()
    rest.run()

    # Approach 2
    tp.run(core, rest, title="Taipy Demo")
```

## Running `Gui` and `Core`

If you don't want to expose a REST API to manage the core entities, you can run Taipy GUI along with Taipy Core
together with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    core = tp.Core()
    gui = tp.Gui(page="# Getting started with *Taipy*")

    tp.run(gui, core, title="Taipy Demo")
```

## Running `Gui`, `Core` and `Rest`
You can run all Taipy services together by using `taipy.run()` with the code below:

```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")
    rest = tp.Rest()

    tp.run(gui, rest, title="Taipy Demo")
```

Taipy Rest relies on Taipy Core. When running the Taipy Rest service, Taipy Core will
also run along with it. Therefore, Taipy Core will run with Taipy GUI and Taipy Rest in
the previous code example.
