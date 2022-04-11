## Line charts

Line plots are a widely-used representation that connects distinct
data points, showing trends.

The [Basics](basics.md) section already shows a handful of examples
showing line charts. This section focuses on customizations that are
relevant for this type of charts only.

### Styling lines

You can style plots using the _line[]_ and _color[]_ properties.

Say we have captured temperature measurements every day: the mean, maximum
and minimum values for every day. This data set can easily be stored in a
Pandas Data Frame:
```py
data = pd.DataFrame(
  {
    "Date": pd.date_range("<start-date>", periods=100, freq="D"),
    "Temp°C": [-15,-12.9,...100 records total...,7.2,10.2],
    "Min": [-22,-19.7,...100 records total...,2.7,6.5],
    "Max": [-8.6,-8.2,...100 records total...,12.,13.5]
  }
)
```

We want to customize the style of the different traces, so the chart
is easier to read. We will display the 'Max' trace in red, the 'Min'
trace in blue, and apply a dash style to the 'regular' temperature
plot.

Here is the definition of the chart control:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x=Date|y[1]=Temp°C|y[2]=Min|y[3]=Max|mode=lines|line[1]=dash|color[2]=blue|color[3]=red|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart x="Date" y[1]="Temp°C" y[2]="Min" y[3]="Max" mode="lines"
                     line[1]="dash" color[2]="blue" color[3]="red">{data}</taipy:chart>
        ```

The page now shows the following chart:

![Styling a line chart](line1.png)

### Text above plot

It is sometimes useful to provide textual information on top of a plot.
Here is how to do that in the context of a line chart.

We want to display, at the approximate location of a temperature data point,
the index of the week we are plotting the data.

We can reuse the dataset of the example above, and add a column to
the DataFrame, holding the week number as a text:
```py
data = pd.DataFrame({
...
"WeekN": [f"W{i//7}" if i%7==0 else None for i in range(0, 100)]
...
})
```
Note that this new column (_WeekN_) is mainly filled with None values.

Let us use this column as a source for displaying text in our chart:

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x=Date|y[1]=Temp°C|y[2]=Max|text[2]=WeekN|mode[2]=text|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart x="Date" y[1]="Temp°C"
                     y[2]="Max" text[2]="WeekN" mode[2]="text">{data}</taipy:chart>
        ```

This definition will allow to display the texts contained in the 'WeekN'
column (the _text[2]_) property, at the _y_ coordinate indicated in the
'Max' column (the _y[2]_), as raw text (the _mode[2]_ property).

Here is the resulting chart:

![Plotting x squared](line2.png)

!!! tip "Faint text"
    You may find that your texts don't appear as clearly as they should.
    Plotly actually applies a low opacity to individual plot items to
    bring the opacity at a maximum value when the item is selected.

    If you have this problem and want to work it out, you can enforce a higher
    opacity value by default for all the text elements of your charts by adding
    the following lines to your application style sheets:
    ```css
    .textpoint text {
        fill-opacity: 0.9 !important;
    }
    ```
