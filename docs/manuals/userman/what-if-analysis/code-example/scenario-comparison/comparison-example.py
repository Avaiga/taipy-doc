import pandas as pd
import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config
from taipy.gui import Gui


def compare_revenue(*sales_predictions):
    unit_price = 9.99
    scenario_names = [f"Scenario {i}" for i in range(len(sales_predictions))]
    revenues = {"Scenarios": scenario_names,
                "Revenues": [sales * unit_price for sales in sales_predictions]}
    return pd.DataFrame(revenues)

if __name__ == "__main__":
    # Configure scenario
    weather_cfg = Config.configure_data_node("weather")
    sales_cfg = Config.configure_data_node("sales")
    scenario_cfg = Config.configure_scenario("scenario",
                                             additional_data_node_configs=[weather_cfg, sales_cfg],
                                             comparators={sales_cfg.id: compare_revenue})

    # Instantiate multiple scenarios and populate data
    # Create a scenario with sunny weather
    sunny = tp.create_scenario(scenario_cfg)
    sunny.weather.write("SUNNY")  # Set the weather to sunny
    sunny.sales.write(1000)  # Set the sales to

    # Create another scenario with a cloudy weather
    cloudy = tp.create_scenario(scenario_cfg)
    cloudy.weather.write("CLOUDY")  # Set the weather to cloudy
    cloudy.sales.write(800)  # Set the sales to

    # Create another scenario with a rainy weather
    rainy = tp.create_scenario(scenario_cfg)
    rainy.weather.write("RAINY")  # Set the weather to rainy
    rainy.sales.write(250)  # Set the sales to

    # Compare the scenarios on sales data node with the compare_revenue comparator
    revenues = tp.compare_scenarios(sunny, cloudy, rainy)[sales_cfg.id]["compare_revenue"]

    # Create a user interface
    with tgb.Page() as compare_page:
        tgb.chart("{revenues}", type="bar", x="Scenarios", y="Revenues")
        tgb.table("{revenues}")

    Gui(compare_page).run()
