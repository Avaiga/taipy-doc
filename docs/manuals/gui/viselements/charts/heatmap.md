## Heatmap charts

A heatmap depicts values for a main variable of interest across two axes as a grid of colored
rectangles. The axes are divided into ranges like a bar chart or histogram, and each cell’s
color gives a hint on the value of the main variable at the corresponding cell range's location.

Typical usages of heatmaps:

- Display the magnitude of a data set over two dimensions;
- In retail matrix, manufacturing diagram, and population maps;
- For marketing goals and analytics, reflecting on user behavior on specific webpages;
- ...

In order to create a heatmap in Taipy, you must set the property [*type*](../../chart/#p-type)
of the chart control to "heatmap".

### Basic Heatmap {data-source="gui:doc/examples/charts/heatmap-basic"}

This example displays a heatmap that represents the temperatures, in °C, in some cities during
a given season (of the northern hemisphere).

We define the dataset to be displayed as a simple dictionary:

```py
data = {
    "Temperatures": [[17.2, 27.4, 28.6, 21.5],
                     [5.6, 15.1, 20.2, 8.1],
                     [26.6, 22.8, 21.8, 24.0],
                     [22.3, 15.5, 13.4, 19.6]],
    "Cities": ["Hanoi", "Paris", "Rio", "Sydney"],
    "Seasons": ["Winter", "Spring", "Summer", "Autumn"]
}
```

Taipy converts the *data* dictionary into a Pandas DataFrame, where all entries
must be lists of the same size.

Here is how you would define the chart control to represent this data:

- The main variable is referenced by the [*z*](../../chart/#p-z) property.
- The two axes are referenced by the [*x*](../../chart/#p-x) and [*y*](../../chart/#p-y)
  properties.

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Cities|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="heatmap" z="Temperatures" x="Seasons" y="Cities">{data}</taipy:chart>
        ```

And here is how the resulting chart will look like in your page:

<figure>
    <img src="../heatmap_basic-d.png" class="visible-dark" />
    <img src="../heatmap_basic-l.png" class="visible-light" />
    <figcaption>Temperatures</figcaption>
</figure>

### Unbalanced Heatmap {data-source="gui:doc/examples/charts/heatmap-unbalanced"}

The example above was an example where the size of the datasets for the *x* and *y*
axes were the same.

If you needed to add another city to be represented on the *y* axis, you would need
to change the definition of the source dataset:

```py
data = [
    {
        "Temperatures": [[17.2, 27.4, 28.6, 21.5],
                         [5.6, 15.1, 20.2, 8.1],
                         [26.6, 22.8, 21.8, 24.0],
                         [22.3, 15.5, 13.4, 19.6],
                         [3.9, 18.9, 25.7, 9.8]],
        "Cities": ["Hanoi", "Paris", "Rio", "Sydney", "Washington"]
    },
    {
        "Seasons": ["Winter", "Spring", "Summer", "Autumn"]
    }
]
```

*data* is now an array of two dictionaries, where the first element's values
all have a length of 5, and where the second element's value has a length
of 4.

In order to reference which value array to use on which axes, the declaration
of the control must change slightly:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=heatmap|z=0/Temperatures|x=1/Seasons|y=0/Cities|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="heatmap" z="0/Temperatures" x="1/Seasons" y="0/Cities">{data}</taipy:chart>
        ```

Here how the data is referenced from the chart control:

- *z* is set to "0/Temperatures", indicating the column "Temperatures" of the first element
  of *data*
- *x* is set to "1/Seasons", indicating the column "Seasons" of the second element
  of *data*
- *y* is set to "0/Cities", indicating the column "Cities" of the first element
  of *data*

And the chart displays as expected:

<figure>
    <img src="../heatmap_unbalanced-d.png" class="visible-dark" />
    <img src="../heatmap_unbalanced-l.png" class="visible-light" />
    <figcaption>Temperatures</figcaption>
</figure>

### Setting the color scale {data-source="gui:doc/examples/charts/heatmap-colorscale"}

If you want to change the color scale used in the heatmap cells, you must set the *colorscale*
property of the property [*options*](../../chart/#p-options) of the chart control.<br/>
You can create an entirely custom color scale, or use one of possible predefined values, listed
in the [Colorscales](https://plotly.com/javascript/colorscales/) page of the
[Plotly.js](https://plotly.com/javascript/) documentation.

We are reusing the code of the first example, where we add a new variable to hold the
options for our chart control:

```py
options = { "colorscale": "Portland" }
```

And reference that dictionary in the [*options*](../../chart/#p-options) property of the
control:
!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Cities|options={options}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="heatmap" z="Temperatures" x="Seasons" y="Cities" options="options">{data}</taipy:chart>
        ```
<figure>
    <img src="../heatmap_colorscale-d.png" class="visible-dark" />
    <img src="../heatmap_colorscale-l.png" class="visible-light" />
    <figcaption>Specific Color Scale</figcaption>
</figure>

### Annotated Heatmap {data-source="gui:doc/examples/charts/heatmap-annotated"}

You may want to display the actual value that is represented, at the appropriate location in the heatmap.

We shall reuse the first example of this section, displaying the temperature for a given city
in a given season in the appropriate heatmap cell.

Here is the code that is needed:

```py linenums="1"
layout = {
    "annotations": [],
    "xaxis": {
        "ticks": "",
        "side": "top"
    },
    "yaxis": {
        "ticks": "",
        "ticksuffix": " "
    }
}

seasons = data["Seasons"]
cities = data["Cities"]
for city in range(len(cities)):
  for season in range(len(seasons)):
    temperature = data["Temperatures"][city][season]
    annotation = {
      "x": seasons[season],
      "y": cities[city],
      "text": f"{temperature}\N{DEGREE SIGN}C",
      "font": {
        "color": "white" if temperature < 9 or temperature > 26 else "black"
      },
      "showarrow": False
    }
    layout["annotations"].append(annotation)
```

In lines 1 to 11, we create the object that is used in the [*layout*](../../chart/#p-layout)
property of the chart.

- The *annotations* array, initialized to an empty array, is filled in the second part of
  the code (lines 13 to 27). This is where the cells content is defined;
- The *x* axis is configured to not display the axis ticks, and appear on top of the chart;
- The *y* axis is configured to not display the axis ticks either, and a space character is
  appended to the ticks label for a better result.

Lines 13 to 27 create an annotation object for every cell:

- The *x* value is set to the same of the cell's season name;
- The *y* value is set to the same of the cell's city name;
- The *text* value is set to a label that displays the temperature value, and the Celsius
  degree symbol.
- The *color* value of the *font* property is set to black or white, depending on the
  temperature value, so it appears with an appropriate contrast.

The chart definition will appear as:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=heatmap|z=Temperatures|x=Seasons|y=Cities|layout={layout}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="heatmap" z="Temperatures" x="Seasons" y="Cities" layout="layout">{data}</taipy:chart>
        ```

And the result looks like:

<figure>
    <img src="../heatmap_annotated-d.png" class="visible-dark" />
    <img src="../heatmap_annotated-l.png" class="visible-light" />
    <figcaption>Annotated Heatmap</figcaption>
</figure>

### Unequal Cell Sizes {data-source="gui:doc/examples/charts/heatmap-unequal-cell-sizes"}

You may need to specify the size of each heatmap cell, both in the horizontal and the vertical
dimensions.

Let's consider the following code:

```py linenums="1"
grid_size = 10
data = [
    {
        "z": [[0. if (row+col) % 4 == 0 else 1 if (row+col) % 2 == 0 else 0.5 for col in range(grid_size)] for row in range(grid_size)]
    },
    {
        "x": [0] + list(accumulate(np.logspace(0, 1, grid_size))),
        "y": [0] + list(accumulate(np.logspace(1, 0, grid_size)))
    }
]

axis_template = {
    "showgrid": False,
    "zeroline": False,
    "ticks": "",
    "showticklabels": False,
    "visible": False
}

layout = {
    "xaxis": axis_template,
    "yaxis": axis_template,
    "showlegend": False
}
```

Here is how you would create the control definition:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=heatmap|z=0/z|x=1/x|y=1/y|layout={layout}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="heatmap" z="0/z" x="1/x" y="1/y" layout="layout">{data}</taipy:chart>
        ```

In lines 2 to 10, we create the data that the heatmap uses:

- *z* is set to 0, 1 or 0.5 depending on which row and column we're on;
- *x* holds a series of x coordinates, growing exponentially;
- *y* holds a series of y coordinates, shrinking exponentially;

The *axis_template* variable declared on line 12 indicates the setting for our two axis: we don't want to show
any line or label.

Finally, in line 20, we create the *layout* object to set the axis properties.

The resulting chart looks like:

<figure>
    <img src="../heatmap_unequal_cell_sizes-d.png" class="visible-dark" />
    <img src="../heatmap_unequal_cell_sizes-l.png" class="visible-light" />
    <figcaption>Unequal cell sizes</figcaption>
</figure>

### Drawing on top of a heatmap {data-source="gui:doc/examples/charts/heatmap-drawing-on-top"}

You can even add another trace on top of a heatmap.

Here is an example of displaying a [Golden spiral](https://en.wikipedia.org/wiki/Golden_spiral)
of top of a heatmap that represents a Fibonacci sequence. This example was taken from the
[Plotly.js documentation](https://plotly.com/javascript/heatmaps/).

```py linenums="1"
def spiral(th):
    a = 1.120529
    b = 0.306349
    r = a * numpy.exp(-b * th)
    return (r * numpy.cos(th), r * numpy.sin(th))


(x, y) = spiral(numpy.linspace(-numpy.pi / 13, 4 * numpy.pi, 1000))

golden_ratio = (1 + numpy.sqrt(5)) / 2.  # Golden ratio
grid_x = [0, 1, 1 + (1 / (golden_ratio**4)), 1 + (1 / (golden_ratio**3)), golden_ratio]
grid_y = [0, 1 / (golden_ratio**3), 1 / golden_ratio**3 + 1 / golden_ratio**4, 1 / (golden_ratio**2), 1]

z = [
    [13, 3, 3, 5],
    [13, 2, 1, 5],
    [13, 10, 11, 12],
    [13, 8, 8, 8]
]

data = [
    {
        "z": z,
    },
    {
        "x": numpy.sort(grid_x),
        "y": numpy.sort(grid_y)
    },
    {
        "xSpiral": -x + x[0],
        "ySpiral": y - y[0],
    }
]

axisTemplate = {
    "range": [0, 2.0],
    "showgrid": False,
    "zeroline": False,
    "showticklabels": False,
    "ticks": "",
    "title": ""
}

layout = {
    "xaxis": axisTemplate,
    "yaxis": axisTemplate
}

options = {
    "showscale": False
}
```

In lines 1 to 8, we prepare the data that define the Golden spiral, stored in the *x* and *y* arrays.

Lines 10 to 12 create the arrays *grid_x* and *grid_y* that hold the cell sizes on both axes.

All these datasets are grouped in a single array called *data*, on line 21.

The *axis* dictionary create on line 35 makes it possible to remove all the drawing of the axes themselves,
including ticks and texts. It is used in the *layout* definition for both axes, in line 45 and 46.

Finally, on line 49, we create the *options* dictionary that allows the removal of the color scale next to
the heatmap.

Here is how the chart is declared in the page:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type[1]=heatmap|z[1]=0/z|x[1]=1/x|y[1]=1/y|type[2]=scatter|x[2]=2/xSpiral|y[2]=2/ySpiral|layout={layout}|options={options}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type[1]="heatmap" z[1]="0/z" x[1]="1/x" y[1]="1/y" type[2]="scatter" x[2]="2/xSpiral" y[2]="2/ySpiral" layout="layout" options="options">{data}</taipy:chart>
        ```

Note that we have create two separate traces, with two different types ("heatmap" and "scatter"). The data that
defines those two plots are retrieved from *data* using their proper index and column names.

The image that you get looks like the following:
<figure>
    <img src="../heatmap_drawing_on_top-d.png" class="visible-dark" />
    <img src="../heatmap_drawing_on_top-l.png" class="visible-light" />
    <figcaption>The Golden spiral</figcaption>
</figure>
