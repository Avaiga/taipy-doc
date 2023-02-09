# Advanced topics

Taipy exposes advanced features that the Plotly library provides. This section
demonstrates some of those features, when they are needed and how to use them
in your Taipy application.

## Multiple traces with different dataset sizes {data-source="gui:doc/examples/charts/advanced-unbalanced-datasets.py"}

The [*Adding a trace*](basics.md#adding-a-trace) example explained how to create multiple
traces on the same chart.<br/>
However, a strong limitation was that all series have to have the same size.<br/>
This limitation is due to the technical nature of a Pandas DataFrame, which must
have all its columns holding the same number of items.

To allow for plotting series of different sizes, we set the [*data*](../chart.md#p-data)
property of the chart control to an array of dictionaries (converted to Pandas
DataFrames internally): each dictionary that holds different series that must all
be the same size to be used in the chart control, but different dictionaries in the
*data* array may have different sizes.<br/>
The data column names must then be prefixed by their index in the data array (starting
at index 0) followed by a slash: "1/value" indicates the key (or the column) called "value"
in the second element of the array set to the [*data*](../chart.md#p-data) property of the
chart control.

Here is an example that demonstrates this. We want to plot two different data sets that
represent the same function (x squared) on two different intervals.

- The first trace is very coarse, with a data point at every other *x* unit between -10 and
  10.
- The second trace is far more detailed, with ten data points between each *x* unit,
  on the interval [-4, 4].

Here is the code that does just that:

```py
# The first data set uses the x interval [-10..10],
# with one point at every other unit
x1_range = [x*2 for x in range(-5, 6)]

# The second data set uses the x interval [-4..4],
# with ten point between every unit
x2_range = [x/10 for x in range(-40, 41)]

# Definition of the two data sets
data = [
    # Coarse data set
    {
        "x": x1_range,
        "Coarse": [x*x for x in x1_range]
    },
    # Fine data set
    {
        "x": x2_range,
        "Fine": [x*x for x in x2_range]
    }
]
```

As you can see, the array *data* has two elements:

- At index 0: A dictionary that has two properties: "x" is set to the array
  [-10, -8, ..., 8, 10], which is the *x* range for the coarse plot, and "y"
  is the series of all these values, squared.<br/>
  Both these arrays hold 11 elements.
- At index 1: A dictionary that has two properties: "x" is set to the array
  [-4.0, -3.9, ..., 3.9, 4.0], which is the *x* range for the fine plot, and
  "y" is the series of all these values, squared, just like in the first
  element.<br/>
  Both these arrays hold 81 elements.

To use these series in the chart control, the [*x*](../chart.md#p-x) and
[*y*](../chart.md#p-y) properties must indicate which trace they refer to and be
set with the indexed data set syntax as shown below:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x[1]=0/x|y[1]=0/Coarse|x[2]=1/x|y[2]=1/Fine|>
        ```

    === "HTML"

        ```html
        <taipy:chart x[1]="0/x" y[1]="0/Coarse" x[2]="1/x" y[2]="1/Fine">
            {data}</taipy:chart>
        ```

Trace number 1 (the Coarse trace) is defined by *x[1]* and *y[1]*, and uses
the series *data[0]\["x"\]* and *data[0]\["Coarse"\]*;<br/>
Trace number 2 (the Fine trace) is defined by *x[2]* and *y[2]*, and uses
the series *data[1]\["x"\]* and *data[1]\["Fine"\]*.

Here is what the resulting plot looks like:

<figure>
    <img src="../advanced-unbalanced-datasets-d.png" class="visible-dark" />
    <img src="../advanced-unbalanced-datasets-l.png" class="visible-light"/>
    <figcaption>Unbalanced data sets</figcaption>
</figure>

## Adding annotations {data-source="gui:doc/examples/charts/advanced-annotations.py"}

You can add text annotations on top of a chart using the *annotations* property of
the dictionary set to the [*layout*](../chart.md#p-layout) property of the chart
control.<br/>
These annotations can be connected to an arrow that points to an exact location in
the chart coordinates system, and have many customization capabilities. You may
look at the documentation on the
[annotations](https://plotly.com/javascript/reference/#layout-annotations) documentation
page on Plotly's website.

Here is an example demonstrating how you can add annotations to your chart controls:


```py
# Function to plot: x^3/3 - x
def f(x):
    return x*x*x/3-x

# x values: [-2.2, ..., 2.2]
x = [(x-10)/4.5 for x in range(0, 21)]

data = {
    "x": x,
    # y: [f(-2.2), ..., f(2.2)]
    "y": [f(x) for x in x]
}

layout = {
    # Chart title
    "title": "Local extrema",
    "annotations": [
        # Annotation for local maximum (x = -1)
        {
            "text": "Local <b>max</b>",
            "font": {
                "size": 20
            },
            "x": -1,
            "y": f(-1)
        },
        # Annotation for local minimum (x = 1)
        {
            "text": "Local <b>min</b>",
            "font": {
                "size": 20
            },
            "x": 1,
            "y": f(1),
            "xanchor": "left"
        }
    ]
}
```

The important part is the definition of the *layout* object, the rest of the code being
very standard.<br/>
You can see how we create a dictionary for every annotation we want to add, including the
text information, location, font setting, etc.

Adding the annotations to the chart control is a matter of setting the
[*layout*](../chart.md#p-layout) property of the chart control to that object:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|layout={layout}|>
        ```

    === "HTML"

        ```html
        <taipy:chart layout="{layout}">{data}</taipy:chart>
        ```

Here is how the annotated chart control shows on the page:

<figure>
    <img src="../advanced-annotations-d.png" class="visible-dark" />
    <img src="../advanced-annotations-l.png" class="visible-light"/>
    <figcaption>Text annotations</figcaption>
</figure>

## Adding shapes {data-source="gui:doc/examples/charts/advanced-shapes.py"}

Shapes can be rendered on top of a chart at defined locations.<br/>
To create shapes, you must add shape descriptors to the *shapes* property of
the dictionary set to the [*layout*](../chart.md#p-layout) property of the chart
control.<br/>
The documentation for shape descriptors can be found in the
[shapes documentation](https://plotly.com/javascript/reference/#layout-shapes)
page on Plotly's website.

Here is some code that creates shapes on top of a chart control:

```py
# Function to plot: x^3/3-x
def f(x):
    return x*x*x/3-x

# x values: [-2.2, ..., 2.2]
x = [(x-10)/4.5 for x in range(0, 21)]

data = {
    "x": x,
    # y: [f(-2.2), ..., f(2.2)]
    "y": [f(x) for x in x]
}

shape_size = 0.1

layout = {
    "shapes": [
        # Shape for local maximum (x = -1)
        {
            "x0": -1-shape_size,
            "y0": f(-1)-2*shape_size,
            "x1": -1+shape_size,
            "y1": f(-1)+2*shape_size,
            "fillcolor": "green",
            "opacity": 0.5
        },
        # Shape for local minimum (x = 1)
        {
            "x0": 1-shape_size,
            "y0": f(1)-2*shape_size,
            "x1": 1+shape_size,
            "y1": f(1)+2*shape_size,
            "fillcolor": "red",
            "opacity": 0.5
        }
    ]
}
```

The part you should be looking at is the setting of the property *shapes* in
the *layout* dictionary: each shape is defined as a dictionary that holds all
the parameters that configure how and where to render it.<br/>
Note how we indicate the size of the shape, using the *shape_size* variable.

Here is the definition of the chart control:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|layout={layout}|>
        ```

    === "HTML"

        ```html
        <taipy:chart layout="{layout}">{data}</taipy:chart>
        ```

And here is what the resulting chart looks like:

<figure>
    <img src="../advanced-shapes-d.png" class="visible-dark" />
    <img src="../advanced-shapes-l.png" class="visible-light"/>
    <figcaption>Shapes on chart</figcaption>
</figure>

## Tracking selection {data-source="gui:doc/examples/charts/advanced-selection.py"}

The chart control has the [*selected*](../chart.md#p-selected) property
that can be used to track data point selection in the chart control.<br/>
This property is dynamic and indexed; the bound variable holds an array of point
indexes. It is updated when the user selects points on the chart.

Here is some code that calculates the mean of the values of the selected points of
a chart control:

```py
# x = [0..20]
x = list(range(0, 21))

data = {
    "x": x,
    # A list of random values within [1, 10]
    "y": [random.uniform(1, 10) for _ in x]
}

layout = {
    # Force the Box select tool
    "dragmode": "select",
    # Remove all margins around the plot
    "margin": {"l":0,"r":0,"b":0,"t":0}
}

config = {
    # Hide Plotly's mode bar
    "displayModeBar": False
}

selected_indices = []

mean_value = 0.

def on_change(state, var, val):
    if var == "selected_indices":
        state.mean_value = numpy.mean([data["y"][idx] for idx in val]) if len(val) else 0
```

The part you should be looking at is the use of the default callback property [*on_change*](../../callbacks.md#variable-value-change):
it detects the changes in *selected_indices* and calculates the mean, which updates
the text in the title.

We also create two objects (*layout* and *config*) used to remove the mode
bar above the chart and force the Box select tool.

Here is the definition of the chart and text controls:

!!! example "Page content"

    === "Markdown"

        ```
        ## Mean of <|{len(selected_indices)}|raw|> selected points: <|{mean_value}|format=%.2f|raw|>

        <|{data}|chart|selected={selected_indices}|layout={layout}|plot_config={config}|>
        ```

    === "HTML"

        ```html
        <h2>Mean of
          <taipy:text raw="true">{len(selected_indices)}</taipy:text>
          selected points:
          <taipy:text format="%.2f" raw="true">{mean_value}</taipy:text>
          </h2>

        <taipy:chart selected="{selected_indices}" layout="{layout}"
            plot_config="{config}">{data}</taipy:chart>
        ```

And here is what the resulting page looks like:

<figure>
    <img src="../advanced-selection-d.png" class="visible-dark" />
    <img src="../advanced-selection-l.png" class="visible-light"/>
    <figcaption>Data points selection</figcaption>
</figure>

<!--- TODO: when range tracking works.. say... better
## Tracking range changes {data-source="gui:doc/examples/charts/advanced-range-tracking.py"}

You can be notified when the visible range of the chart is changed. That happens when the
user zooms or pans the chart content using the Zoom or Pan tools.

Here is some code that shows you how to listen to range changes:

```py
# Random data points along the [0..20] x axis
x = list(range(0, 21))
y = [random.uniform(1, 20) for _ in x]

data = {
    "x": x,
    "y": y
}

def range_changed(state, x1, x2, x3):
    print(f"state={state} x1={x1} x2={x2} x3={x3}")
```

[TODO]

!!! example "Page content"

    === "Markdown"

        ```
        [TODO]
        ```

    === "HTML"

        ```html
        [TODO]
        ```

[TODO]
--->
