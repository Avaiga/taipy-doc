# Running Taipy services

Taipy provides you three services: Taipy GUI, Taipy Rest, and Taipy Core. You can run Taipy services by calling the method _run()_ from the service instance either `Gui^`, `Rest^`, or `Core^`. You can also use `taipy.run()^` to initiate the service.

For example, you can run the GUI service with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")

    # Approach 1
    gui.run(gui, title="Taipy Demo")

    # Approach 2
    tp.run(gui, title="Taipy Demo")
```

By default, when running the Rest service, you will also start the Core service as the Rest service relies on the Core service to function:
```python
import taipy as tp

if __name__ == "__main__":
    rest = tp.Rest()

    # Approach 1
    rest.run()

    # Approach 2
    tp.run(rest)
```

The code above is the same as:
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

You can run the Core service individually with the code below:
```python
import taipy as tp

if __name__ == "__main__":
    core = tp.Core()

    # Approach 1
    core.run()

    # Approach 2
    tp.run(core)
```

# Running different Taipy services together

You can run various Taipy services together by using `taipy.run()^`.

You can run Taipy GUI along with Taipy Core together with the following code:
```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")
    core = tp.Core()

    tp.run(gui, core, title="Taipy Demo")
```

You can run all Taipy services including Taipy GUI, Taipy Rest, and Taipy Core with the code below:

```python
import taipy as tp

if __name__ == "__main__":
    gui = tp.Gui(page="# Getting started with *Taipy*")
    rest = tp.Rest()

    tp.run(gui, rest, title="Taipy Demo")
```

!!! note "As mentioned, Taipy Rest needs Taipy Core to function, when running the Taipy Rest service, Taipy Core will also run along with it. Therefore, Taipy Core will also be together with Taipy GUI and Taipy Rest in the example above."
