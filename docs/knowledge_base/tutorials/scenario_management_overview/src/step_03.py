from taipy.core.config import Config
import taipy as tp
import datetime as dt
import pandas as pd


def filter_current(df):
    current_month = dt.datetime.now().month
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == current_month]
    return df

def count_values(df):
    return len(df)


historical_data_cfg = Config.configure_csv_data_node(id="historical_data",
                                                     default_path="time_series.csv")
month_values_cfg =  Config.configure_data_node(id="month_data")
nb_of_values_cfg = Config.configure_data_node(id="nb_of_values")


task_filter_cfg = Config.configure_task(id="filter_current",
                                                 function=filter_current,
                                                 input=historical_data_cfg,
                                                 output=month_values_cfg)

task_count_values_cfg = Config.configure_task(id="count_values",
                                                 function=count_values,
                                                 input=month_values_cfg,
                                                 output=nb_of_values_cfg)


scenario_cfg = Config.configure_scenario(id="my_scenario",
                                                    task_configs=[task_filter_cfg,
                                                                  task_count_values_cfg])

Config.export('config_03.toml')

if __name__ == '__main__':
    tp.Core().run()

    scenario = tp.create_scenario(scenario_cfg, creation_date=dt.datetime(2022,10,7), name="Scenario 2022/10/7")
    scenario.submit()

    print("Nb of values of scenario:", scenario.nb_of_values.read())

    data_node = None

    tp.Gui("""<|{scenario}|scenario_selector|>
              <|{scenario}|scenario|>
              <|{scenario}|scenario_dag|>
              <|{data_node}|data_node_selector|>""").run()

