# Callbacks

Callbacks are functions that are created in the application that are
invoked in response to user actions in generated pages or other events that the
Web browser requires that the application handles.

Every callback function receives a `State^` object as its first parameter.<br/>
This object reflects the state of the application variables, for a given end-user:
your application may be used simultaneously by different users connected to the
same Web server (note that setting the _single_client_ configuration parameter to
False - as explained in the
[Configuration](configuration.md#configuring-the-gui-instance) section - prevents
multiple users from connecting to your application simultaneously, but you still rely
on the `State^` object to access the application variables that are represented in your
user interfaces).<br/>
When visual elements use application variables (see the [Binding](binding.md)
section), the `State` class is provided an accessor to these variables, both
for reading and writing.

## Variable value change

Some controls (such as [`input`](viselements/input.md) or [`slider`](viselements/slider.md))
let the user modify the value they hold.  
In order to control what that _new value_ is and decide whether to use
it as such, a callback function is called in the application when the user
activates the control in order to change its value.

!!! example

    ```py
    from taipy.gui import Gui

    md = """
    # Hello Taipy

    The variable `x` is here: <|{x}|slider|>.
    """

    x = 50

    def on_change(state, var, val):
        if var == "x":
            print(f"'x' was changed to: {val}")

    Gui(page=md).run()
    ```

In the function body, you can check the new value of the variable and decide
what to do with it: potentially triggering some other code to propagate the
side effects of the new variable value.

In order to reset the value displayed at this point, one can simply change
the variable value, using the `state` variable (or any other variable name
that the `State` instance has been set to) prefix when referring to that variable.
In our example, that would be `state.x`.

!!! note "Control-specific on_change callback"
    All the controls that allow users to impact the variables they rely on let
    you specify a specific _on_change_ callback. This is done using the
    _on_change_ property of each control.<br/>
    That makes it easier to organize your application code in situations where
    there are many controls to handle, where a single _on_change_ function would
    become very large.

    In the code above, you could isolate the _on_change_ function for the slider
    control using its _on_change_ property:
    ```py
    ... 
    md = """
    # Hello Taipy

    The variable `x` is here: <|{x}|slider|on_change=on_slider_change|>.
    """

    ...

    def on_slider_change(state):
        print(f"'x' was changed to: {state.x}")

    ...
    ```
    You would not have to check the variable name anymore (although the callback function
    still receives it) since you know that _on_slider_change_, in this case, will be
    invoked _only_ when the user interacts with the slider.

## Actions

Controls like buttons don't notify of any value change. Instead, they use callbacks to notify
the application that the user has activated those controls somehow.

!!! example
    ```py
    from taipy import Gui

    md = """
    # Hello Taipy

    Press <|THIS|button|> button.
    """

    def on_action(state, id, action):
        print("The button was pressed!")

    Gui(page=md).run()
    ```

The default behavior for these controls is to call the `on_action` function within your
code, if there is one.

## Initialize a new connection

When a client connects to your application, the `on_init()` callback is invoked so you can
set variables to appropriate values, depending on the application state at this point.

A new connection will make Taipy GUI try to locate a global `on_init()` function, and
invoke this function providing the client's `State^`, where you can
specify timely values in your application variables.

Here is how an `on_init()` function could be used to initialize a connection-specific variable.
Here this variable would represent the date and time when the connection occurs:

```py
from datetime import datetime

connection_datetime = None
def on_init(state: State):
    state.connection_datetime = datetime.now()
```

## Long-running callbacks

In some cases, the code that runs as a result of invoking a callback may take a long
time. The browser expects some response when the work required by the callback is
performed. However, in the context of a client-server application such as the ones built with
Taipy GUI, tasks that take a long time may result in a timeout in the communication between
the server (the Python application) and the client (the Web browser connected to it).

Taipy GUI provides a way to update the user interface while the server is still working on
the requested tasks asynchronously.

Here is how to set up such asynchronous communication with Taipy GUI.

Say a callback is triggered, where your application needs to perform some heavy task,
consuming time. Say this task is implemented in the `heavy_function()` function.<br/>
In a callback triggered by the user interface, we want to create a thread, run our
task, then refresh the visual elements according to the results, or send notifications
to the client's browser.

Here is how this can be achieved:
```py linenums="1"
from taipy.gui import get_state_id, notify
from threading import Thread

gui = Gui(...)

def heavy_function_done(state: State):
    # Now the State can be used to update the user interface
    notify(state, "info", "The heavy task was done!")

def heavy_function_in_thread(state_id: str, ...other_args...):
    heavy_function(...other_args...)
    invoke_callback(gui, state_id, heavy_function_done)

def on_action(state: State, ...):
    notify(state, "info", "Heavy task started...", duration=3000)
    # Execute the heavy task, in a new thread
    thread = Thread(target=heavy_function_in_thread,
                    args=[get_state_id(state), ...other_args...])
    thread.start()
```

Line 14 introduces the declaration of a callback function, that would typically be
executed when the user activates a control. This is where we want to run the time-consuming task defined in the function *heavy_function()*`. However, because we know this
will take time, we will execute it in another thread and let the application carry on
its regular execution.<br/>
Note that in *on_action()*, we can use *state* to update variables or notify the user interface.
Typically, in this situation, we may want to deactivate the button that triggered the callback
so that the user cannot request the execution twice until the task was actually performed.

In line 10, we define the function that gets executed in the external thread. The first
thing to do is to invoke *heavy_function()* (with whatever parameters it needs).
When the function is done, we want to update the graphical user interface that the work
was performed. This is where `invoke_callback()^` is used: the code requests that the
function **heavy_function_done()* is invoked. The `State^` will be provided by Taipy, using
the state identifier that was provided in *state_id*.

The actual update of the user interface (including, potentially, the re-activation of the
control that triggered the callback in the first place) is performed in *heavy_function_done()*,
defined at line 6. Any code that needs a `State^` object (to update a variable or send a
notification to the user) can be used safely.

## Exception handling

Because the user interface may invoke your own Python code using callbacks, exceptions
may be raised in the user code. Taipy GUI provides a way to notify the application of
such situations, so you can control what to do to reflect the application state.

When a user callback raises an exception, the global `on_exception()` callback is invoked.

Here is an example of an exception handling callback that would provide valuable
information in the user interface should a problem occur:

```py
def on_exception(state: State, function_name: str, ex: Exception)
    state.status_text = f"A problem occured in {function_name}"
```

## Navigation callback

You can control the behavior of your application when the user navigates from one
page to another. You would typically use that functionality when a page should not
be exposed to a user under a given condition but instead display another fallback
page.

Here is an example of how to use that callback:<br/>
Imagine an application that can display results of some sort on the page "results".
If results are not ready for some reason, when navigating to the result page should
be prevented, and the user should be switched to another page instead:

```py linenums="1"
results_ready = False

def on_navigate(state: State, page_name: str): str
    if page_name == "results" and not state.results_ready:
        return "no_results"
    return page_name
```
Line 1 initializes the variable *results_ready* to False, indicating that at this point,
there are no results ready to be displayed yet.

In line 4, we check if the requested page is the "results" page and if there are no
results yet to be shown. In that situation, the callback function returns "no_results",
which is the name of the page that should be displayed instead.
