import tempfile
import folium
from folium.folium import Map
import pandas as pd
from taipy.gui import Gui


def expose_folium(fol_map: Map):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        fol_map.save(temp_file.name)
        with open(temp_file.name, "rb") as f:
            return f.read()


eco_footprints = pd.read_csv("footprint.csv")
max_eco_footprint = eco_footprints["Ecological footprint"].max()
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)


def folium_map():
    # Create the folium map
    fol_map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
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
    ).add_to(fol_map)
    folium.LayerControl().add_to(fol_map)

    return fol_map

    
Gui.register_content_provider(Map, expose_folium)

# import taipy.gui.builder as tgb

# with tgb.Page() as page:
#     ...
#     tgb.part(content="{folium_map()}")

Gui("<|part|content={folium_map()}|height=600px|>").run()
