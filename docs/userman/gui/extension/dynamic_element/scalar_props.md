# Scalar properties

In this section, we will add a dynamic custom element to the custom element library, which we
started to create in the
[Static Elements](../static_element.md#declaring-the-extension-library)
section.

This dynamic element will be using a property that holds a scalar value.<br/>
The role of this visual element is to display a string where each letter is displayed
with a different color.

If a Python variable is bound to this property, the code can change this variable value,
and the front-end would immediately reflect the new string content.

## Declaring the element {data-source="gui:doc/extension/example_library/example_library.py"}

Starting from the code mentioned above, here is how you would declare this new element:

```python hl_lines="8 15-17"
from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType

class ExampleLibrary(ElementLibrary):
    def __init__(self) -> None:
        self.elements = {
            # A dynamic element that decorates its value
            "label": Element("value", {
                "value": ElementProperty(PropertyType.dynamic_string)
                },
                # The name of the React component (ColoredLabel) that implements this custom
                # element, exported as ExampleLabel in front-end/src/index.ts
                react_component="ExampleLabel")
            }

    def get_scripts(self) -> list[str]:
        # Only one JavaScript bundle for this library.
        return ["example_library/front-end/dist/exampleLibrary.js"]
```

The two highlighted sections must be detailed:

- The "label" element has a single property called "value".<br/>
  The type of this property is `PropertyType.dynamic_string`, indicating that it
  represents a string value, and that it is dynamic.
- The `(ElementLibrary.)get_scripts()^` is overloaded to return an array of paths
  to JavaScript module files that Taipy GUI will load at run time.<br/>
  In our situation, the custom element library is entirely defined in a single
  module file ('exampleLibrary.js') and needs no dependent module.


## Creating the React component {data-source="gui:doc/extension/example_library/front-end/src/ColoredLabel.tsx"}

Here is the entire implementation of the React component that our element relies on:

```ts
import React from "react";
import { useDynamicProperty } from "taipy-gui";

interface ColoredLabelProps {
  value?: string;
  defaultValue: string;
}

// Sequence of colors
const colorWheel = ["#FF0000", "#A0A000", "#00FF00", "#00A0A0", "#0000FF", "#A000A0"]
// The array of styles using these colors
const colorStyles = colorWheel.map(c => ({ color: c }))

// ColoredLabel component definition
const ColoredLabel = (props: ColoredLabelProps) => {
  // The dynamic property that holds the text value
  const value = useDynamicProperty(props.value, props.defaultValue, "");
  // Empty text? Returning null produces no output.
  if (!value) {
    return null;
  }
  // Create a <span> element for each letter with the proper style.
  // Note that React needs, in this situation, to set the 'key' property
  // with a unique value for each <span> element.
  return (
    <>
      {value.split("").map((letter, index) => (
        <span key={"key" + index} style={colorStyles[index % 6]}>{letter}</span>
      ))}
    </>
  )
}

export default ColoredLabel;
```
We use the
[`useDynamicProperty()`](../../../../refmans/reference_guiext/functions/useDynamicProperty.md)
hook provided by the Taipy GUI Extension API to retrieve the value of the dynamic
property. This hook returns the latest updated value.<br/>

It takes three parameters:

- *value*: The bound value, coming from the *props* of the component;
- *defaultValue* The default value, coming from the *props* of the component;
- *defaultStatic* The default static value.

## Using the element in the application {data-source="gui:doc/extension/main.py"}

The demonstration Python script provided in Taipy GUI has the following content:

```
label = "Here is some text"

page = """
## Custom label:

Colored text: <|{label}|example.label|>
"""
```

We can see how the *label* property of the control is bound to the Python variable
*label*,using the default property syntax.

When you run this application, the page displays the element like this:

<figure>
    <img src="../scalar1-d.png" class="visible-dark"  width="80%"/>
    <img src="../scalar1-l.png" class="visible-light" width="80%"/>
    <figcaption>Colored Label</figcaption>
</figure>

To demonstrate the dynamic aspect of this property, let's add a button on the page that,
when pressed, appends a random alphanumeric character to the *label* variable.

In the Markdown definition of the page, we add a button:
```
<|Add a character|button|id=addChar|>
```

And implement the `on_action` callback to react to the user pressing this button:
```py
def on_action(state, id):
  if id == "addChar":
    # Add a random character to the end of 'label'
    state.label += random.choice(string.ascii_letters)
```

If the user click the button a few times, this is what the page would look like:

<figure>
    <img src="../scalar2-d.png" class="visible-dark"  width="80%"/>
    <img src="../scalar2-l.png" class="visible-light" width="80%"/>
    <figcaption>With trailing random characters</figcaption>
</figure>
