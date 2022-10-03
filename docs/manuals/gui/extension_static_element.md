# Static elements

Custom static visual elements are ones that only need to define their HTML output.
These elements are called *static* because changing a `State^` variable, even if
bound to an element's property, does not impact the rendering.

## Declaring the element

To declare a static element, the call to the
[`Element` constructor](Element.__init__()^) must provide the *render_xhtml*
argument with a function that generates the XHTML fragment that represents
this element.

!!! note "XHTML vs. HTML"
    XHTML is a stricter version of HTML that is an XML application. In particular,
    in XHTML:

    - Elements **must** be properly nested.
    - Elements **must** be properly closed.
    - Attribute values **must** be properly quoted.

Say that you want to create a control that displays a static string that different pages
will use over and over. That could, for example, be an application title or a company name.

We are going to create a custom visual element that does just that. This control
will be called "caption", located in a new library called "custom".<br/>
In order to create an instance of this control in our Markdown page, we
simply need to write: `<|custom.caption|>` in the Markdown text. If we were
to create an HTML page, we would insert the tag: `<custom:caption/>`.

Our control is very simple: it just needs to generate the HTML fragment
`<span>some text</span>`. So let's put some code that generates this in
the element declaration:

```py linenums="1"
from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType

class CustomLibrary(ElementLibrary):
    def get_name(self) -> str:
        return "custom"

    def get_elements(self) -> dict:
        return ({
          "caption":
            Element("text", {
              "text": ElementProperty(PropertyType.string)
              },
              render_xhtml=lambda props: "<span>The Caption</span>")
          })
```

Line 3 introduces our custom element library. We override the two methods that need
to be defined:

- `get_name()` (line 4): we return the name under which this library is identified
  in the definition of the application pages.
- `get_elements()` (line 7): we create a single custom element called "caption",
  that has a single (unused) property called "text". This property also happens
  to be the default property for this control.<br/>
  Our HTML code for this control is so simple that we could generate it from
  a lambda function assigned to the *render_xhtml* argument of the Element constructor
  (line 13). This might not be possible for more complex controls.<br/>
  Also, note that this lambda function takes an argument: *props*. This is a dictionary
  that reflects the value of each of this control's properties. We will touch on this in
  a minute.

Our element library is now entirely defined. Let us create a page that uses it:

```py linenums="1"
from taipy.gui import Gui

[... code above ...]

page="""
# Custom control

Here is my control: <|custom.caption|>
"""
gui = Gui(page)
gui.add_library(CustomLibrary())
gui.run()
```

When the application is run, the page that is shown displays our control as expected:

<figure>
  <img src="../images/extension-static1-d.png" class="visible-dark" />
  <img src="../images/extension-static1-l.png" class="visible-light" />
  <figcaption>Static control</figcaption>
  </figure>

## Using properties

So far, the text content of our control was hard-coded in the element rendering function.
A more practical use case is one where the text would reflect the value of a property.

To achieve this, we will use the property value sent to the XHTML rendering function.

Just change the lambda function that we used above to the following code:
```py
render_xhtml=lambda props: f'<span>{props.get("text", "empty")}</span>'
```

With this implementation, the text content of our control is defined by the content of the
*text* property of the control.<br/>
So we can now change our Markdown text to:
```
<|Hello|custom.caption|>
```
Note that is is equivalent yet shorter than `<|custom.caption|text=Hello|>`.

Re-running the application will produce the following page content.

<figure>
  <img src="../images/extension-static2-d.png" class="visible-dark" />
  <img src="../images/extension-static2-l.png" class="visible-light" />
  <figcaption>Using a property</figcaption>
  </figure>

Also note that we could have created a variable to store the text:
```py
text="Hello"
```

And use that variable in the Markdown definition:
```
<|{text}|custom.caption|>
```

The result would be strictly equivalent.

After the page is rendered, changing the value of this variable would not
impact the control itself.

## More complex rendering

If the rendering is more complex, then you will certainly need to perform it in a separate
function.

We can augment our example by adding another property that will impact the size
of the text.

We will create a new property called *size* that should be set to a string that can be any
value among "xs", "s", "l" and "xl". The size of the text should reflect the *size* property.

Let us improve the definition of our element library to take that into account:

```py linenums="1"
from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType

class CustomLibrary(ElementLibrary):
    def get_name(self) -> str:
        return "custom"

    def get_elements(self) -> dict:
        def render_caption(props):
            size = props.get("size", "")
            font_size=""
            if size.lower() == "xs":
              font_size=".6em"
            elif size.lower() == "s":
              font_size=".8em"
            elif size.lower() == "l":
              font_size="1.2em"
            elif size.lower() == "xl":
              font_size="1.4em"
            if font_size:
              font_size = f" style=\"font-size:{font_size}\""
            return f'<span{font_size}>{props.get("text", "empty")}</span>'
        return ({
          "caption":
            Element("text", {
              "text": ElementProperty(PropertyType.string),
              "size": ElementProperty(PropertyType.string),
              },
              render_xhtml=render_caption)
          })
```

In this new definition, the property *size* was added. It is used in the rendering
function, which is now an actual function called *render_caption*.<br/>
In the rendering function for this element (lines 8 to 21), we compute a CSS style
to apply to the span HTML element we create.

If we now replace our control fragment in the Markdown page to:
```
<|Extra small|custom.caption|size=xs|> <|Small|custom.caption|size=s|>
<|Normal|custom.caption|>
<|Large|custom.caption|size=l|> <|Extra Large|custom.caption|size=xl|>
```

We can generate the following page that shows our custom control using the two
defined properties.

<figure>
  <img src="../images/extension-static3-d.png" class="visible-dark" />
  <img src="../images/extension-static3-l.png" class="visible-light" />
  <figcaption>Slightly more complex rendering</figcaption>
  </figure>

