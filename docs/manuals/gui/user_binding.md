# Binding variables

Sometimes, you will want to display information that comes from your application.<br/>
To achieve this goal, Taipy allows [visual elements](user_viselements.md)
to relate directly to your application variables, display their values, and even
change those variable values.

Consider the following application:

```py linenums="1"
from taipy.gui import Gui

x = 1234

Gui(page="""
# Hello Taipy

The variable `x` contains the value <|{x}|>.
""").run()
```

When this program runs (and a Web browser is directed to the running server), the
root page displays the value of the variable _x_, as it was defined your code.

## Expressions

Values that you can use in controls and blocks can be more than raw variable values.
You can create complete expressions, just like you would use
in the _f-string_ feature (available since Python 3).

In the code above, you could replace `<|{x}|>` by `<|{x*2}|>`, and the double of _x_
will be displayed on your page.

!!! Note "Arbitrary expressions"
        You can create complex expressions such as `|{x} and {y}|` to concatenate
        two variable values, or whatever your imagination and application requirements are.

!!! Note "Formatting"
        F-string formatting is also available in property value expressions:

        - If you have declared `pi = 3.141592653597`, then `<|Pi is {pi:.4f}|>` will
          display the text:<br/>
          `Pi is 3.1416`.
        - If you have `v = 64177`, then `<|dec:{v}, oct:{v:08o}, hex:{v:X}|>` will result
          in displaying the text:<br/>
          `dec:64177, oct:00175261, hex:FAB1`.

        Note that because HTML text gets rid of non-significant white spaces,
        right-justification format (`{string:>n}`) does not impact the resulting
        display.

## Lambda expressions

Some control properties can be assigned lambda expression to simplify the
code.

!!! abstract "TODO: provide a simple example of a lambda expression usage"
