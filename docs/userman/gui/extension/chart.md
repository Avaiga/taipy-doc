In this section, we’ll dive into creating and integrating charts using [`Plotly`](https://plotly.com/graphing-libraries/) in our extension library.
Charts are invaluable for visualizing data, offering clear and interactive insights that enhance the user experience.
We’ll walk through the steps to implement different types of charts, configure their properties,
and seamlessly embed them into your application.

## Prerequisites

Before you start creating charts, ensure you have the following prerequisites:

- **Install the necessary libraries:** To use [Plotly.js with React](https://plotly.com/javascript/react/),
you’ll need to install the [`react-plotly.js`](https://github.com/plotly/react-plotly.js) library.

  ```bash
  $ npm install react-plotly.js plotly.js
  ```

!!! note "Using TypeScript"
    When using TypeScript, you’ll need to install the type definitions for Plotly.js as well.

    ```bash
    $ npm install --dev @types/react-plotly.js
    ```

## Declaring the element {data-source="gui/extension/example_library/example_library.py#L69"}

To create an element that holds a chart, you need to define it in the extension library:

```python title="example_library.py"
from taipy.gui.extension import Element, ElementLibrary, ElementProperty, PropertyType

class ExampleLibrary(ElementLibrary):
    def __init__(self) -> None:
        # Initialize the set of visual elements for this extension library
        self.elements = {
            "dashboard": Element(
                "data",
                {
                    "data": ElementProperty(PropertyType.dict),
                    "layout": ElementProperty(PropertyType.dict),
                },
            )
        }
```

The detailed explanation of the code is as follows:

- The *dashboard* element includes two properties: *data* and *layout*.
- The *data* property has the type `PropertyType.dict^`, meaning it holds a dictionary of data.
- The *layout* property has the type `PropertyType.dict^`, meaning it holds a dictionary of layout properties.

## Creating the React component {data-source="gui/extension/example_library/front-end/src/Dashboard.tsx"}

The React component for the *dashboard* element is defined as follows:

```tsx title="Dashboard.tsx"
import React, { useMemo } from "react";
import { useDynamicJsonProperty, } from "taipy-gui";

import Plot from "react-plotly.js";
import { Data, Layout } from "plotly.js";

interface DashboardProps {
    data?: string;
    defaultData?: string;
    layout?: string;
    defaultLayout?: string;
}

const Dashboard = (props: DashboardProps) => {
    const value = useDynamicJsonProperty(props.data, props.defaultData || "", {} as Partial<Data>);
    const dashboardLayout = useDynamicJsonProperty(props.layout, props.defaultLayout || "", {} as Partial<Layout>);

    // Using useMemo to avoid re-rendering the component when the data changes
    const data = useMemo(() => {
        if (Array.isArray(value)) {
            return value as Data[];
        }
        return [] as Data[];
    }, [value]);

    const baseLayout = useMemo(() => {
        const layout = {
            ...dashboardLayout,
        };
        return layout as Partial<Layout>;
    }, [dashboardLayout]);

    return (
        <div>
            <Plot data={data} layout={baseLayout} />
        </div>
    );
};

export default Dashboard;
```

The detailed explanation of the code is as follows:

- The **Dashboard** component accepts two props: *data* and *layout*.
- The [`useDynamicJsonProperty()`](../../../refmans/reference_guiext/functions/useDynamicJsonProperty.md) hook is used to handle dynamic properties. It accepts the following arguments:

    - *data*: The dynamic property that holds the data for the chart.
    - *defaultData*: The default value for the *data* property.
    - *layout*: The dynamic property that holds the *layout* properties for the chart.
    - *defaultLayout*: The default value for the *layout* property.

- The **Plot** component utilizes the [`react-plotly.js`](https://github.com/plotly/react-plotly.js) library to render the chart. It accepts two attributes:

    - *data*: An array of data objects to define the chart's datasets.
    - *layout*: An object specifying the layout of the chart.

For more information on how to use `react-plotly.js`, refer to the official documentation [here](https://github.com/plotly/react-plotly.js).



## Exporting the React component {data-source="gui/extension/example_library/front-end/src/index.ts"}

When the component is entirely defined, it must be exported by the library's JavaScript bundle.
This is done by adding the `export` directive in the file `<project_dir>/<package_dir>front-end/src/index.ts`.

```ts title="index.ts"
import Dashboard from "./Dashboard";

export { Dashboard };
```

## Configuring the webpack configuration {data-source="gui/extension/example_library/front-end/webpack.config.js#L39"}

To bundle the React component, you must configure the webpack configuration file.
Since Plotly.js is a JavaScript library, you need to include JavaScript in the webpack’s *resolve.extensions* setting.

```js title="webpack.config.js"
module.exports = {
    // ...
    resolve: {
        extensions: [".ts", ".tsx", ".js"],
    },
    // ...
};
```

After configuring the webpack file, you can build the library as mentioned in the [Building the front-end module](dynamic_element/index.md#building-the-front-end-module) section.

## Using the element {data-source="gui/extension/dashboard.py"}

To use the *dashboard* element in a Python script, you can follow the example below:

```python title="dashboard.py"
set1 = {
    "x": [1, 2, 3, 4, 4, 4, 8, 9, 10],
    "type": "box",
    "name": "Set 1"
}

set2 = {
    "x": [2, 3, 3, 3, 3, 5, 6, 6, 7],
    "type": "box",
    "name": "Set 2"
}

data = [set1, set2]

layout = {
    "title": {
        "text": "Horizontal Box Plot"
    }
}

page = """
<|{data}|dashboard|layout={layout}|>
"""
```

In this example, we define two traces and a layout for an horizontal box plot.
When you run the script, the *dashboard* element will display like this:

<figure>
    <img src="../dashboard.png" alt="Horizontal Box Plot">
    <figcaption>Horizontal Box Plot</figcaption>
</figure>
