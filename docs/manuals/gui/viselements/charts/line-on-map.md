### Maps with lines

Lines on maps can show distance between geographic points or be contour lines (isolines, isopleths, or isarithms).

In this example, we create a line between New York City and London.
```py
# First, we define start and end points
data = {
    "lat": [40.7127, 51.5072],
    "lon": [-74.0059, 0.1275],
}

layout = {
    "title": 'London to NYC Great Circle',
    "showlegend": False,
    "geo": {
        "resolution": 50,
        "showland": True,
        "showocean": True,
        "landcolor": '663004',
        "oceancolor": '34a1eb',
        "projection": {
            "type": 'equirectangular'
        },
        "coastlinewidth": 2,
        "lataxis": {
            "range": [20, 60],
            "showgrid": True,
            "tickmode": 'linear',
            "dtick": 10
        },
        "lonaxis": {
            "range": [-100, 20],
            "showgrid": True,
            "tickmode": 'linear',
            "dtick": 20
        }
    }
}
# Style the connect line.
lineOpts = {
    "width": 5,
    "color": '0bf507'
}
```
About geo configuration in layout, you can check [here](https://plotly.com/javascript/reference/layout/geo/#layout-geo)

!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=scattergeo|mode=lines|lat=lat|lon=lon|line={lineOpts}|layout={layout}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="scattergeo" mode="lines" lat="lat" lon="lon" line="lineOpts" layout="layout">{data}</taipy:chart>
        ```
<figure>
    <img src="map-with-line-dark.png" class="visible-dark" />
    <img src="map-with-line.png" class="visible-light" />
    <figcaption>Maps with lines</figcaption>
</figure>

### Maps with Bubbles

Maps with bubbles can associate quantities with geographic location

We will use this chart to visualize the populations of all cities in US in 2014.
```py
data = pandas.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
scale = 50000
data['citysize'] = data['pop'].apply(lambda p: p / scale)
data['hovertext'] = data.apply(lambda r: f"{r['name']} pop {r['pop']}", axis=1)

opts = {
    'locationmode': 'USA-states',
    'hoverinfo': 'text',
}
# We define bubble size based on city size
marker_opt = {
    'size': 'citysize',
    "line": {
        "color": '14ba2d',
        "width": 2
    }
}

layout = {
    'title': '2014 US City Populations',
    'showlegend': False,
    'geo': {
        'scope': 'usa',
        'projection': {
            'type': 'albers usa'
        },
        'showland': True,
        'landcolor': 'e3e3e3',
        'subunitwidth': 1,
        'countrywidth': 1,
        'subunitcolor': '660000'
    },
}
```
!!! example "Page content"

    === "Markdown"

        ```
        <|{data}|chart|type=scattergeo|mode=lines|lat=lat|lon=lon|line={lineOpts}|layout={layout}|>
        ```
  
    === "HTML"

        ```html
        <taipy:chart type="scattergeo" mode="lines" lat="lat" lon="lon" line="lineOpts" layout="layout">{data}</taipy:chart>
        ```
We can see top crowed cities: New York, Los Angeles and Chicago
<figure>
    <img src="map-with-bubbles-dark.png" class="visible-dark" />
    <img src="map-with-bubbles.png" class="visible-light" />
    <figcaption>Maps with bubbles</figcaption>
</figure>
