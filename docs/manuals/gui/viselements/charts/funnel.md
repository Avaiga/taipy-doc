## Funnel charts

Funnel charts represent a succession of values correlated between each other according to a certain order.

### Typical use of headmaps
- The data is sequential and moves through at least 4 stages.
- The number of "items" in the first stage is expected to be greater than the number in the final stage.
- To calculate potential (revenue/sales/deals/etc.) by stages.
- To calculate and track conversion and retention rates.
- To reveal bottlenecks in a linear process.
- To track a shopping cart workflow.
- To track the progress and success of click-through advertising/marketing campaigns.
- And more

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

```py
data = pd.DataFrame(
    {
        "Visit_fr_eng": [13873, 10533, 5443, 2703, 908],
        "Visit_fr_fra": [1063, 4533, 3443, 1003, 1208],
        "Visit_fr_us": [6873, 2533, 3443, 1703, 508],
        "Types": ["Website visit", "Downloads", "Potential customers", "Invoice sent", "Closed delays"],
    }
)
```
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

Huhm, We want to custom the color and style of markers

```py
marker = {
    "color": ["59D4E8", "DDB6C6", "A696C8", "67EACA", "94D2E6"],
    "line": {
        "width": [4, 2, 2, 3, 1, 1],
        "color": ["3E4E88", "606470", "3E4E88", "606470", "3E4E88"]
    }
}

options= {
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
