from taipy import Config
import taipy as tp
import taipy.gui.builder as tgb
import pandas as pd
import datetime as dt


data = pd.read_csv("https://raw.githubusercontent.com/Avaiga/taipy-getting-started-core/develop/src/daily-min-temperatures.csv")


# Normal function used by Taipy
def predict(historical_temperature: pd.DataFrame, date_to_forecast: dt.datetime) -> float:
    print(f"Running baseline...")
    historical_temperature["Date"] = pd.to_datetime(historical_temperature["Date"])
    historical_same_day = historical_temperature.loc[
        (historical_temperature["Date"].dt.day == date_to_forecast.day) &
        (historical_temperature["Date"].dt.month == date_to_forecast.month)
    ]
    return historical_same_day["Temp"].mean()

Config.load("config.toml")

if __name__ == "__main__":
    scenario_cfg = Config.scenarios["my_scenario"]

    # Run of the Orchestrator
    tp.Orchestrator().run()

    # Creation of the scenario and execution
    scenario = tp.create_scenario(scenario_cfg)
    scenario.historical_temperature.write(data)
    scenario.date_to_forecast.write(dt.datetime.now())
    tp.submit(scenario)

    print("Value at the end of task", scenario.predictions.read())

    def save(state):
        state.scenario.historical_temperature.write(data)
        state.scenario.date_to_forecast.write(state.date)
        state.refresh("scenario")
        tp.gui.notify(state, "s", "Saved! Ready to submit")

    date = None
    with tgb.Page() as scenario_page:
        tgb.scenario_selector("{scenario}")
        tgb.text("Select a Date")
        tgb.date("{date}", on_change=save, active="{scenario}")

        tgb.text("Run the scenario")
        tgb.scenario("{scenario}")
        tgb.scenario_dag("{scenario}")

        tgb.text("View all the information on your prediction here")
        tgb.data_node("{scenario.predictions}")

    tp.Gui(scenario_page).run()
