# Line charts

Line plots are a widely-used representation that connects distinct
data points, showing trends.

The [Basic concepts](basics.md) section already shows a handful of examples
showing line charts. This section focuses on customizations that are
relevant to this type of chart only.

## Key properties

| Name            | Value           | Notes   |
| --------------- | ------------------------- | ------------------ |
| [*mode*](../chart.md#p-mode)      | `lines`          | Overrides the default `lines+markers` |
| [*x*](../chart.md#p-x)            | x values           |  |
| [*y*](../chart.md#p-y)            | y values           |  |
| [*line*](../chart.md#p-line)      | Style for the line |  |
| [*color*](../chart.md#p-color)  | Color for the line  |  |
| [*text*](../chart.md#p-text)  | Text to display  |  |

## Examples

### Styling lines {data-source="gui:doc/examples/charts/line-style.py"}

You can style plots using the [*line[]*](../chart.md#p-line) and
[*color[]*](../chart.md#p-color) properties.

Say we have captured daily temperature measurements: the mean, maximum
and minimum values for every day. This data set can easily be stored in a
dictionary that Taipy will convert to a Pandas DataFrame:
```py
data = {
    "Date": pandas.date_range("<start-date>", periods=100, freq="D"),
    "Temp°C": [-15,-12.9,...100 records total...,7.2,10.2],
    "Min": [-22,-19.7,...100 records total...,2.7,6.5],
    "Max": [-8.6,-8.2,...100 records total...,12.,13.5]
}
```

We want to customize the style of the different traces so the chart
is easier to read. We will display the 'Max' trace in red, the 'Min'
trace in blue and apply a dash style to the 'regular' temperature
plot.

Here is the definition of the chart control:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|mode=lines|x=Date|y[1]=Temp°C|y[2]=Min|y[3]=Max|line[1]=dash|color[2]=blue|color[3]=red|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart mode="lines" x="Date" y[1]="Temp°C" y[2]="Min" y[3]="Max"
                     line[1]="dash" color[2]="blue" color[3]="red">{data}</taipy:chart>
        ```

The page now shows the following chart:

<figure>
    <img src="../line-style-d.png" class="visible-dark" />
    <img src="../line-style-l.png" class="visible-light"/>
    <figcaption>Styling a line chart</figcaption>
</figure>

### Text above plot {data-source="gui:doc/examples/charts/line-texts.py"}

It is sometimes useful to provide textual information on top of a plot.
Here is how to do that in the context of a line chart.

We want to display the index of the relevant week at the approximate location of a
temperature data point.<br/>
We can use the [*text[]*](../chart.md#p-text) property to do just that: a text will
be displayed at the relevant (*x*, *y*) location.

We can reuse the dataset of the example above and add a column to
the data dictionary, holding the week number as a text:
```py
data = {
...
"WeekN": [f"W{i//7}" if i%7==0 else None for i in range(0, 100)]
...
}
```
Note that this new column (*WeekN*) is mainly filled with None values: we only add text
information on Sundays.

Let us use this column as a source for displaying text in our chart:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x=Date|y[1]=Temp°C|y[2]=Max|mode[2]=text|text[2]=WeekN|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart x="Date" y[1]="Temp°C"
                     mode[2]="text" y[2]="Max" text[2]="WeekN">{data}</taipy:chart>
        ```

We use the [*mode[]*](../chart.md#p-mode) indexed property to indicate that, for
the second trace, we want to display the text itself.<br/>
This definition allows the display of the texts contained in the 'WeekN'
column (the *text[2]*) property at the *y* coordinate indicated in the
'Max' column (the *y[2]*), as raw text (the *mode[2]* property).

Here is the resulting chart:

<figure>
    <img src="../line-text-d.png" class="visible-dark" />
    <img src="../line-text-l.png" class="visible-light"/>
    <figcaption>Line and text</figcaption>
</figure>
