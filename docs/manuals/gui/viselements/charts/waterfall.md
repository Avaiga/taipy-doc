# Waterfall charts

Waterfall charts can display a running total as values are added or subtracted. They are used to
rapidly understand how an initial value is affected by a series of positive or negative changes.

A typical use of waterfall charts is to show how a net value is reached through gains and losses
over time.

To create a waterfall chart in Taipy, you must set the [*type*](../chart.md#p-type) property
of the chart control "waterfall".

## Key properties

| Name            | Value            | Notes   |
| --------------- | -------------------------- | ------------------ |
| [*type*](../chart.md#p-type)       | `waterfall` |  |
| [*x*](../chart.md#p-x)             | x values.   |  |
| [*y*](../chart.md#p-y)             | y values.   | Absolute or relative. |
| [*measure*](../chart.md#p-measure) | Type of value in [*y*](../chart.md#p-y). | Valid values are "absolute" or "relative". |
| [*text*](../chart.md#p-text)      | Stage names  | For the `funnelarea` type.  |
| [*options*](../chart.md#p-options)  | dictionary  | `increasing` can be used to customize how boxes representing increasing values (positive *y* values) are represented.<br/>`decreasing` can be used to customize how boxes representing decreasing values (negative *y* values) are represented.<br/>`connector` can be used to customize the graphical properties of the lines connecting the boxes. |

## Examples

### Simple waterfall chart {data-source="gui:doc/examples/charts/waterfall-simple.py"}

Waterfall charts are typically used for describing cash flow: the initial value of some deposit
and how it evolves with time.

Here is a dataset that could represent such a flow:

```py
data = {
    "Day":   ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Values": [10, -5, 20, -10, 30],
}
```

The first item of the "Values" array indicates the initial amount in the account (10, in this
example). That value is associated to the first item of the "Day" array that contains successive
day names.

The waterfall chart needs to know what the values represent (absolute or relative values). To
specify that, we need an additional array that is used as the [*measure*](../chart.md#p-measure)
property for the chart:

```py
data = {
    ...
    "Measure": ["absolute", "relative", "relative", "relative", "relative"]
}
```

The "Measure" array indicates that all values except for the first one have to be considered as
relative values (adding to or removing from the preceeding total).

Here is how the chart control could be defined:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|type=waterfall|chart|x=Day|y=Values|measure=Measure|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="waterfall" x="Day" y="Values" measure="Measure">{data}</taipy:chart>
        ```

And here is how the resulting chart would look:

<figure>
    <img src="../waterfall-simple-d.png" class="visible-dark" />
    <img src="../waterfall-simple-l.png" class="visible-light"/>
    <figcaption>Simple waterfall chart</figcaption>
</figure>

### Styling {data-source="gui:doc/examples/charts/waterfall-styling.py"}

By default, waterfall charts display values that increase the total with a green box. Red boxes
are displayed to represent values that decrease the total.<br/>
There are use cases however when this default setting does not fit your usage, such as the game
of golf: the lower the total of hits, the better. Therefore, to display the result of playing a
round of golf, we would want to display the higher scores in red, and the lower scores in green.
This is where styling comes handy.

Here is a dataset that represents the score achieved on a 9-hole golf course:

```
n_holes = 9

data = {
    # ["Hole1", "Hole2", ..., "Hole9"]
    "Hole": [f"Hole{h}" for h in range(1,n_holes+1)] + ["Score"],
    # Par for each hole
    "Par": [ 3, 4, 4, 5, 3, 5, 4, 5, 3 ] + [None],
    # Score for each hole
    "Score": [ 4, 4, 5, 4, 4, 5, 4, 5, 4 ] + [None],
}
```

The "Par" array represents the score that is expected for a given hole.<br/>
The "Score" array stores the number of strokes that were needed to complete the round.

Note that two None values are added to both arrays, after the *n_holes* values: this is because
this last "value" will not be used in our example. Instead, we display the running total which
is the difference between the actual score and the par for each hole. All those differences
are stored in another array, that we store in the *data* dictionary:

```
data["Diff"] = [data["Score"][i]-data["Par"][i] for i in range(0,n_holes)] + [None]
```

For each hole, we compute the difference between the actual score and the par. We then set the
entire array of differences, with an additional None value, to the dataset that is used by the
chart, associated to the key "Diff".<br/>
This array will be the value represented by our chart, showing, for each hole, the score relative
to the par. To indicate how to represent this array, we must add to the *data* dataset the *measure*:

```
data = {
    "M": n_holes * [ "relative" ] + ["total"]
}
```

All the values are represented as relative values (to the par) except for the last one that shows
the final score: how well or how bad was the final score, compared to the par.

To style a waterfall chart, you need to set the [*options*](../chart.md#p-options) property to a
dictionary that specifies the graphical attributes to apply to the different elements of the
chart. [TODO LINK TO waterfall options in Plotly]

Here is how we can style our chart to get the colors of the boxes reflect the real meaning of the
scores:
```py
options = {
    "decreasing": {
        "marker" : { "color": "green" }
    },
    "increasing": {
        "marker" : { "color": "red" }
    }
}
```

The "decreasing" and "increasing" keys hold dictionaries that define the color that must be used
when displaying the chart boxes.

Here is the complete definition of the chart:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|type=waterfall|chart|x=Hole|y=Diff|measure=M|options={options}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="waterfall" x="{Hole}" y="Diff" measure="{M} options="{options}">{data}</taipy:chart>
        ```

And here is what the resultin chart looks like:

<figure>
    <img src="../waterfall-styling-d.png" class="visible-dark" />
    <img src="../waterfall-styling-l.png" class="visible-light"/>
    <figcaption>Styling a waterfall chart</figcaption>
</figure>

### Hierarchical timeline {data-source="gui:doc/examples/charts/waterfall-period_levels.py"}

