# Callbacks

Callbacks are functions that you create in your application that are meant to be
invoked in response to user actions in generated pages or other events that the
Web browser requires that the application takes care of.

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
Because you may want to control what that _new value_ is and decide whether to use
it as such or not, a callback function is called in your application when the user
activates the control to change its value.

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

Once in your function body, you can check the new value for the variable and decide
what to do with it: maybe you will need to trigger some other code to propagate the
side effects of the new variable value.

Suppose you need to reset the value displayed at this moment. In that case, you can change
the variable value, assuming you use the `state` variable (or any other variable
name you have assigned for the `State` instance) prefix when referring to that variable.
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
    from taipy.gui import Gui

    md = """
    # Hello Taipy

    Press <|THIS|button|> button.
    """

    def on_action(state, id, action):
        print("The button was pressed!")

    Gui(page=md).run()
    ```

The default behavior for these controls is to call the `on_action` function within your code,
if there is one.
