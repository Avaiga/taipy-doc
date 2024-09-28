---
title: Callbacks
category: visuals
data-keywords: gui callback
short-description: Make your multi-user graphical interface fully interactive using the on_change callback.
order: 6
img: callbacks/images/callbacks_flowchart-1.png
---
In Taipy, an `on_change` callback triggers a Python function which is executed when some application
variable is modified. This callback is used for implementing some behavior after the user
performs an action, such as dragging a slider to define the value of some parameter or typing
some text into an input box.

![Callback](images/callbacks_demo.gif){width=40% : .tp-image-border }

Note that Taipy supports various types of callbacks which serve different purposes
although this tip focuses on just one.

These callbacks are:

- *on_change*, the topic of this tip
- *on_action*
- *on_init*
- *on_navigate*
- *on_exception*

When referring to callbacks in this article, we are referring to *on_change callbacks only*,
and these alone are sufficient to build simple to complex web-apps!

That being said, let’s go through the two variations of *on_change* callbacks:

- Local (or control-bound) *on_change* callbacks; and
- Global *on_change* callbacks

# Example 1: Fahrenheit to Celsius (Local Callback)

Local callbacks are functions that are bound to a specific
[Taipy control](../../../refmans/gui/viselements/index.md#generic-controls) (a type of visual element).
This function then gets called when the user interacts with that control.
For instance, in Taipy, this may happen when a user:

1. Drags a [slider](../../../refmans/gui/viselements/generic/slider.md) control to select some number;
2. Selects a date using the [date](../../../refmans/gui/viselements/generic/date.md) control; or
3. Selects an item from the [selector](../../../refmans/gui/viselements/generic/selector.md) control

![Example 1](images/callbacks_demo_fahrenheit_to_celsius_cropped-1.gif){width=40% : .tp-image-border }

Let’s demonstrate local callbacks with a small example.
This simple app allows a user to select a temperature in degrees Fahrenheit
and automatically convert it to degrees Celsius:

```python linenums="1"
from taipy.gui import Gui, Markdown

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def update_celsius(state):
    state.celsius = fahrenheit_to_celsius(state.fahrenheit)

if __name__=="__main__":
    fahrenheit = 100
    celsius = fahrenheit_to_celsius(fahrenheit)

    md = Markdown("""
# Local Callbacks
## Fahrenheit:
<|{fahrenheit}|number|on_change=update_celsius|>

## Celsius:
<|{celsius}|number|active=False|>
    """)

    Gui(page=md).run()
```

The relevant line here is line 12, where we defined a number control using the Taipy construct
syntax. We will use this to select the temperature in degrees Fahrenheit which we wish to be
automatically converted to degrees Celsius.

The aforementioned construct consists of 3 components (bordered by the pipes):

- *{fahrenheit}*: The variable attached to this number control;
- *number*: The name of the Taipy control; and
- *on_change=update_celsius*: Sets this control’s on_change local callback to the update_celsius
    function

The update_celsius local callback function defined on line 18 receives one parameter, which we
conventionally name state.

We can use this state object within our function to access and modify the runtime variables
used in our application, which we also call state variables. Accordingly, we update celsius on
line 19.

Now, when the user interacts with the number control, the update_celsius local callback computes
and updates the state variable of celsius, displaying its new value.

# Example 2: Celsius to Kelvin (Global Callback)

The next improvement to our app is yet another simple one: add a new number control to display
the temperature in kelvin.

![Example 2](images/callbacks_demo_fahrenheit_to_celsius.gif){width=40% : .tp-image-border }

Take a look at the updated code:

```python linenums="1"
from taipy.gui import Gui, Markdown

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def update_celsius(state):
    state.celsius = fahrenheit_to_celsius(state.fahrenheit)

def on_change(state, var_name, var_value):
    if var_name == "celsius":
        state.kelvin = celsius_to_kelvin(state.celsius)

if __name__=="__main__":
    fahrenheit = 100
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)

    md = Markdown("""
# Local and Global Callbacks
## Fahrenheit:
<|{fahrenheit}|number|on_change=update_celsius|>

## Celsius:
<|{celsius}|number|active=False|>

## Kelvin:
<|{kelvin}|number|active=False|>
    """)

    Gui(page=md).run(dark_mode=False)
```

On line 22, we added a new number control to our app, which is bound to the kelvin variable. The
existing code we implemented in the previous section — which updates celsius when fahrenheit is
modified — is maintained.

Now the behavior we wish to implement here is to update the value of kelvin whenever the value
of celsius is modified.

This is a perfect use case for the global on_change callback function. Take a look at this handy
flowchart which determines the type of on_change function that would be called:

![Example 2](images/callbacks_flowchart-1.png){width=100% : .tp-image }

This flowchart visualizes the process in which Taipy determines which *on_change* function would
be called.

In this example, our update_celsius function executed the code:

```python
state.celsius = fahrenheit_to_celsius(state.fahrenheit)
```

We call this programmatically modifying the celsius variable. Looking at the flowchart above, we
know that the global on_change function would be called, if it exists.

The global callback function should have the exact name *on_change* so that Taipy automatically
recognizes it. The parameters for the global on_change function are conventionally named as follows:

1. *state*: The State object with which we can access and modify our runtime variables;
2. *var_name*: The name of the variable that was modified; and
3. *var_value*: The value of the variable that was modified

Notice that on line 33, we preceded our updates to kelvin with an if `var_name == "celsius"`
block. Within the on_change function, we almost always want to operate within an if block, to
avoid unintentionally infinitely recursion through *on_change*. Remember that programmatically
modifying kelvin or any other variables will also call the *on_change* function, though that
execution would make no changes because of our if block.

You might also have noticed that the functionality in this section could also have been
accomplished by updating kelvin using the existing update_celsius local callback — and indeed,
adding a global callback was not necessary for this particular situation. However, you may
encounter some situations where you may not be able to use local callbacks alone, so using the
global callback may be the right choice.

# Example 3: No Callbacks

Side-tracking a little from the focus of this article, it’s worth noting that this app never
actually needed callbacks! We can update the code as follows:

```python
from taipy.gui import Gui, Markdown

def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
   return celsius + 273.15

if __name__=="__main__":
    fahrenheit = 100
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)

    md = Markdown("""
# Global Callbacks
## Fahrenheit:
<|{fahrenheit}|number|>

## Celsius:
<|{fahrenheit_to_celsius(fahrenheit)}|number|active=False|>

## Kelvin:
<|{celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))}|number|active=False|>
    """)

    Gui(page=md).run()
```

Without using any callbacks, we instead simply interpolate the expression to be evaluated into
the curly braces for both the celsius and kelvin controls — much like an f-string! Since the
fahrenheit state variable is present in the expression, Taipy knows that the expression should
be reevaluated whenever fahrenheit is modified.

A drawback of this approach however is that the function fahrenheit_to_celsius is executed twice.
For a function as simple as this one, this drawback is insignificant. However, if this was a
heavy and uncacheable function, we would certainly want to avoid executing it unnecessarily.
