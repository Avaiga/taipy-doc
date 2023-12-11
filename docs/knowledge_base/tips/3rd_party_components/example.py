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

Gui("<|part|page={uc_url}|height=600px|>").run(port=2534, debug=True)