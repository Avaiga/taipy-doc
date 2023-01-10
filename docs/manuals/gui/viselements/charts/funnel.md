## Funnel charts

TODO
Funnel charts represent a succession of values correlated between each other according to a certain order.

### Typical use of headmaps
- The data is sequential and moves through at least 4 stages. If you have less than 4, you can use pie chart or stacked bar chart.
- The number of "items" in the first stage is expected to be greater than the number in the final stage.
- To calculate potential (revenue/sales/deals/etc.) by stages.
- To calculate and track conversion and retention rates.
- To reveal bottlenecks in a linear process.
- To track a shopping cart workflow.
- To track the progress and success of click-through advertising/marketing campaigns.
- And more

In order to create a funnel chart in Taipy, you must set the property type of the chart control to "funnel".
### Basic Funnel chart

Here is an example of how to use a visits funnel that counts number of visits through stages: "Website visit" > "Downloads" > "Potential customers" > "Invoice sent" > "Closed delays".

```py
data = pd.DataFrame(
    {
        "Visits": [13873, 10533, 5443, 2703, 908],
        "Types": ["Website visit", "Downloads", "Potential customers", "Invoice sent", "Closed delays"],
    }
)
```
- The main value is referenced by x property, in this example, we focus on the number of visits.
- The axis label is referenced by y property.

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x=Visits|y=Types|type=funnel|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="funnel" x="Visits" y="Types">{data}</taipy:chart>
        ```
<figure>
    <img src="funnel-chart-dark.png" class="visible-dark" />
    <img src="funnel-chart.png" class="visible-light" />
    <figcaption>Basic Funnel chart</figcaption>
</figure>

### Funnel chart with multi traces

With above example, we want to know where the number of visits comes from. 
We assume that the visits come from England, France and US. So we create data for each country.
```py
data = pd.DataFrame(
    {
        # Data for England
        "Visit_fr_eng": [13873, 10533, 5443, 2703, 908],
        # Data for France
        "Visit_fr_fra": [7063, 4533, 3443, 1003, 1208],
        # Data for US
        "Visit_fr_us": [6873, 2533, 3443, 1703, 508],
        "Types": ["Website visit", "Downloads", "Potential customers", "Invoice sent", "Closed delays"],
    }
)
```
- x[index] stands for each country data.
- y for the type that we want to filter
- name[index] is the label of each country that is shown on the chart.
!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x[1]=Visit_fr_eng|x[2]=Visit_fr_fra|x[3]=Visit_fr_us|y=Types|name[1]=England|name[2]=France|name[3]=US|type=funnel|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="funnel" x[1]="Visit_fr_fra" x[2]="Visit_fr_eng" x[3]="Visit_fr_us" y="Types" name[1]="England" name[2]="France" name[3]="US">{data}</taipy:chart>
        ```
<figure>
    <img src="funnel-chart-multi-traces-dark.png" class="visible-dark" />
    <img src="funnel-chart-multi-traces.png" class="visible-light" />
    <figcaption>Funnel chart with multi traces</figcaption>
</figure>

### Funnel chart with custom markers

For the first example, we want something colorful, so we put some custom markers into Taipy chart.

```py
marker = {
    # We define colors for each type: "Website visit", "Downloads", "Potential customers", "Invoice sent" and "Closed delays". We have 5 types, so we have to define 5 items for each attribute.
    "color": ["59D4E8", "DDB6C6", "A696C8", "67EACA", "94D2E6"],
    # This is the border around the rectangle of each type
    "line": {
        # The border width
        "width": [4, 2, 2, 3, 1],
        # The border color
        "color": ["3E4E88", "606470", "3E4E88", "606470", "3E4E88"]
    }
}

options= {
    # the connector is the line between 2 rectangles, yes, we can change its'styles too.
    "connector": {
        "line": {
            "color": "royalblue",
            "dash": "dot",
            "width": 5
        }
    }
}
```
!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|x=Visits|y=Types|type=funnel|marker={marker}|options={options}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="funnel" x="Visits" y="Types" marker="marker" options="options">{data}</taipy:chart>
        ```
<figure>
    <img src="funnel-chart-custom-markers-dark.png" class="visible-dark" />
    <img src="funnel-chart-custom-markers.png" class="visible-light" />
    <figcaption>Funnel chart with custom markers</figcaption>
</figure>
