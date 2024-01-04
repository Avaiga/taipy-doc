## Integrate Third-Party Components

In the world of web development, it's often necessary to integrate third-party components 
into your applications. These components could range from interactive visualizations to 
videos or other web pages. This article will demonstrate how to effectively include 
external resources, focusing on embedding a Folium Map into a web application.

![Part illustration](part_illustration.png){width=100%}

## Example: Embedding a Folium Map

Let's delve into a practical example of how to integrate a Folium Map into a web 
application. Folium is a powerful visualization tool used for representing various maps, 
finding applications in energy studies, cost analysis, and network analysis.

![Folium Map](folium_map.png){width=100%}

In our scenario, we have a Python application that processes recruitment data, performs 
analysis, and generates a Folium Map using 
[Folium](https://python-visualization.github.io/folium/), a Python library for creating interactive maps.

Here's a code snippet creating a Folium object:

```python
import folium
import pandas as pd

eco_footprints = pd.read_csv("footprint.csv")
max_eco_footprint = eco_footprints["Ecological footprint"].max()
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)

def folium_map():
    # Create the folium map
    map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
    folium.Choropleth(
        geo_data=political_countries_url,
        data=eco_footprints,
        columns=("Country/region", "Ecological footprint"),
        key_on="feature.properties.name",
        bins=(0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, max_eco_footprint),
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name="Ecological footprint per capita",
        name="Countries by ecological footprint per capita",
    ).add_to(map)
    folium.LayerControl().add_to(map)

    return map
```

[Get the CSV file](./footprint.csv){: .tp-btn target='blank'}


## Integrating the Folium Map

To integrate this *map* object into our web application, we need to create the HTML 
version of this object. Here is the code that achieves this:

```python
import tempfile

def expose_folium(map):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        map.save(temp_file.name)
        with open(temp_file.name, "rb") as f:
            return f.read()
```

In this code, the function *expose_folium()* converts a Folium object (*map*) to HTML, a 
mandatory step in integrating any third-party component into your application.

The *map* object is transformed into HTML, and then we proceed to define two callback 
functions, namely, *on_user_content()* and *on_init()*. The *on_init()* callback serves 
as a fundamental Taipy callback that is triggered when a new user connects to the 
application. On the other hand, the *on_user_content()* function is designed to return 
the HTML content to be rendered, while the *get_user_content_url()* function is invoked 
to obtain the URL for rendering the HTML content.

```python
uc_url = None

def on_user_content(state, path: str, query: dict):
    return expose_folium(folium_map())

def on_init(state):
    state.uc_url = get_user_content_url(state, "val", {"name": "param"})
```

Finally, we can embed the Folium Map within our web application using the following 
`part` component:

```
<|part|page={uc_url}|>
```

You can adjust the layout by changing its width and height. This element seamlessly 
integrates the Folium Map into your web app.

[Get the entire code](./example.py){: .tp-btn target='blank'}

## Conclusion

Incorporating third-party components into your web applications is a powerful technique 
that can greatly enhance user experience. You can achieve this by converting external 
content into HTML and seamlessly integrating it into your web app.

This article demonstrated how to embed a Folium Map using this method. This approach 
also ensures that the integrated content doesn't interfere with your page and provides a 
secure user experience.

# Entire Code

```python
import tempfile
import folium
import pandas as pd
from taipy.gui import Gui, get_user_content_url

eco_footprints = pd.read_csv("footprint.csv")
max_eco_footprint = eco_footprints["Ecological footprint"].max()
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)

def folium_map():
    # Create the folium map
    map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
    folium.Choropleth(
        geo_data=political_countries_url,
        data=eco_footprints,
        columns=("Country/region", "Ecological footprint"),
        key_on="feature.properties.name",
        bins=(0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, max_eco_footprint),
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name="Ecological footprint per capita",
        name="Countries by ecological footprint per capita",
    ).add_to(map)
    folium.LayerControl().add_to(map)

    return map

def expose_folium(map):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        map.save(temp_file.name)
        with open(temp_file.name, "rb") as f:
            return f.read()


uc_url = None

def on_user_content(state, path: str, query: dict):
    return expose_folium(folium_map())

def on_init(state):
    state.uc_url = get_user_content_url(state, "val", {"name": "param"})

example = "<|part|page={uc_url}|height=800px|>"

Gui(example).run()
```