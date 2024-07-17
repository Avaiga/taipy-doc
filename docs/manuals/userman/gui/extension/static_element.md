# Static elements

Custom static visual elements only need to define their HTML output.
These elements are called *static* because changing a `State^` variable, even if
bound to an element's property, does not impact the rendering.

Static elements are convenient when you want to display a similar item on different
pages over and over. That could, for example, be an application title or a company name.

## Declaring the extension library {data-source="gui:doc/extension/example_library/example_library.py"}

All custom elements must be declared in a subclass of `ElementLibrary^`.

You will declare this class in a dedicated Python file, where the code will look like this:

```py
from taipy.gui.extension import ElementLibrary

class ExampleLibrary(ElementLibrary):

    def __init__(self) -> None:
        # Initialize the set of visual elements for this extension library
        self.elements = { ... }

    def get_name(self) -> str:
        return "example"

    def get_elements(self) -> dict:
        return self.elements
```

At this point, two methods are overloaded:

- `get_name()` returns the name of the extension library. This is used to find visual
  elements that are declared in page contents.
- `get_elements()` returns a dictionary that associates an element name to the implementation
  on the front-end, defined in the library constructor.

## Declaring a custom visual element {data-source="gui:doc/extension/example_library/example_library.py"}

We are going to create a static custom visual element: this element will be called "fraction",
located in a new library called "example".<br/>
The element has two properties, called *numerator* and *denominator*.  This element displays the
values of its property as a fraction:

- If *numerator* is 0, the element should display "0".
- If *denominator* is 0, the element should display the infinity sign.
- In other cases, the element should display the two property values as a fraction.

The element is defined in the library's constructor as an entry of a dictionary
set as the *self.elements* data member:

```py
from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType

class ExampleLibrary(ElementLibrary):

    ...
    def __init__(self) -> None:
        ...
        self.elements = {
            "fraction": Element("numerator", {
                "numerator": ElementProperty(PropertyType.number),
                "denominator": ElementProperty(PropertyType.number)
                },
                render_xhtml=ExampleLibrary._fraction_render)
```

Our element has two numerical properties ("numerator" and "denominator"), and "numerator"
is declared as the default property.<br/>
Both those properties are declared as holding a 'number'.<br/>
The type of the property is a value among the ones defined by the `PropertyType^`
enumeration class. Because this is a static element, even if these properties were declared
as *dynamic* (where the type name is prefixed with 'dynamic_'), it would nevertheless not
reflect changes in the bound variable values.

In the declaration of a static element, the call to the
`Element.__init__()^`(`Element` constructor) must provide the *render_xhtml*
argument with a function that generates the XHTML fragment that represents
this element.

!!! note "XHTML vs. HTML"
    The definition of the element must be expressed as XHTML content, just like when the application
    creates `Html^` pages.<br/>
    You can find details on this syntax in the
    [XHTML for pages section](../pages/html.md#xhtml-is-required). In short, XHTML is a stricter
    version of HTML that is an XML application. In particular:

    - Elements **must** be properly nested.
    - Elements **must** be properly closed.
    - Attribute values **must** be properly quoted.

The rendering function for the custom visual element "fraction" is
set to a static method of the class `ExampleLibrary`, called '_fraction_render'.

Here is the definition of this static method:
```py
class ExampleLibrary(ElementLibrary):

    ...
    @staticmethod
    def _fraction_render(props: dict) -> str:
        # Get the property values
        numerator = props.get("numerator")
        denominator = props.get("denominator")
        # No denominator or numerator is 0: display the numerator
        if denominator is None or int(numerator) == 0:
            return f"<span>{numerator}</span>"
        # Denominator is zero: display infinity
        if int(denominator) == 0:
            return "<span style=\"font-size: 1.6em\">&#8734;</span>"
        # 'Normal' case
        return f"<span><sup>{numerator}</sup>/<sub>{denominator}</sub></span>"
```

This static method is invoked by Taipy GUI when the component needs to be rendered.
It receives, as a dictionary, the values of the properties for the element (where
keys are property names).

Our element library and its single element are now ready to be used.

## Using the custom visual element {data-source="gui:doc/extension/main.py"}

To create an instance of this control in our Markdown page, we just need to insert
`<|example.fraction|>` in the text.<br/>
If we were to create an HTML page, we would insert the tag: `<example:fraction/>`.

Our element library is now entirely defined.<br/>
Let us create a page that uses it:

```py
from taipy.gui import Gui
from example_library import ExampleLibrary

page="""
The fraction: <|example.fraction|numerator=355|denominator=113|>
"""

# Register the element library and run the application
Gui(page, libraries=[ExampleLibrary()]).run()
```

When the application is run, the page that is shown displays our control as expected:

<figure>
  <img src="../static1-d.png" class="visible-dark" />
  <img src="../static1-l.png" class="visible-light" />
  <figcaption>Static control</figcaption>
  </figure>

With this new visual element at our disposal, we can create a page containing
several occurrences of it.<br/>

Here is the page definition that we will use:

```
page="""
## Fraction:

No denominator: <|123|example.fraction|>

Denominator is 0: <|321|example.fraction|denominator=0|>

Regular: <|355|example.fraction|denominator=113|>
"""
```

Note that we use the first fragment of the elements' definitions to set the default property
value. These three instances cover the three use cases that we had in mind when implementing
the rendering capabilities of the element.

If we use this page definition, we get the following display:

<figure>
  <img src="../static2-d.png" class="visible-dark" />
  <img src="../static2-l.png" class="visible-light" />
  <figcaption>Different use cases</figcaption>
  </figure>

Of course, the property values used when defining the elements could have been
replaced by Python expressions. Still, because the custom element is static, changes
in Python variables used in those expressions would not impact the displayed
page.
