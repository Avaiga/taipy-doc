# Accessing the library assets

Say we want to display a small image next to the text. That would be useful in the situation where we apply
our *caption* control to represent a company name along with its logo.

## Declaring the element

In HTML, you would create an `img` tag, where the source URL is set to the path of the image.<br/>
However, in order to protect the application from attacks, Taipy provides the method
`ElementLibrary.get_resource()` that let the application filter what resources are requested, and return the
actual files according to the application setting.

```py 
class DemoLibrary(ElementLibrary):
    elts = {
        "image": Element(
            "src",
            {
                "src": ElementProperty(PropertyType.string),
                "alt": ElementProperty(PropertyType.string),
            },
            react_component="DemoImage",
        ),
    }

    def get_name(self) -> str:
        return "demo_library"

    def get_elements(self) -> dict:
        return DemoLibrary.elts

    def get_scripts(self) -> list[str]:
        # Only one JavaScript bundle for this library.
        return ["demo_lib/frontend/dist/demo.js"]

    def get_resource(self, name: str) -> Path: # <--- This is the method we are interested in.
        return super().get_resource(name)
```
`get_resource()` introduces us two parameters:
- `name` is the path of the resource requested by the application.
- `return` is the path of the resource that will be sent to the application which is the path of the file.

## Creating the React component

Our Library is now ready to be used in the application. Let's create a react element that will display the image.

```jsx
import React from 'react'

interface DemoImageProps {
    src?: string;
    alt?: string;
}

export default function DemoImage(props: DemoImageProps) {
  return <img src={props.src} alt={props.alt} />
}
```
Component's name must match the name of the `react_component` property of the `image` element.

## Using the element in the application

Now we can use the `image` element in our page.

```py
md = """
# Image test

<|demo_library.image|src=https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png|alt=Google Logo|>
"""

a_gui = Gui(md)

Gui.add_library(DemoLibrary())
a_gui.run()
```

The result is the following:
![Image test](./images/image_test.png)