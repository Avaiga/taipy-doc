from taipy.core.config import Config, Frequency
import taipy as tp
import datetime as dt
import pandas as pd


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    return len(df)


historical_data_cfg = Config.configure_csv_data_node(id="historical_data",
                                                     default_path="time_series.csv")
month_cfg =  Config.configure_data_node(id="month")
month_values_cfg =  Config.configure_data_node(id="month_data")
nb_of_values_cfg = Config.configure_data_node(id="nb_of_values")


task_filter_cfg = Config.configure_task(id="filter_by_month",
                                                 function=filter_by_month,
                                                 input=[historical_data_cfg, month_cfg],
                                                 output=month_values_cfg)

task_count_values_cfg = Config.configure_task(id="count_values",
                                                 function=count_values,
                                                 input=month_values_cfg,
                                                 output=nb_of_values_cfg)

pipeline_cfg = Config.configure_pipeline(id="my_pipeline",
                                         task_configs=[task_filter_cfg,
                                                       task_count_values_cfg])

scenario_cfg = Config.configure_scenario(id="my_scenario",
                                         pipeline_configs=[pipeline_cfg],
                                         frequency=Frequency.MONTHLY)

Config.export('config_04.toml')

if __name__ == '__main__':
    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,5),
                                    name="Scenario 2022/10/5")

    # scenario 1 and 2 belongs to the same cycle so I can define the cycle_metadata just once for
    # scenario 1 and 2 because cycle_metadata has a Cycle scope
    scenario_1.month.write(10)
    scenario_2.month.write(10)

    print("Month Data Node of Scenario 1", scenario_1.month.read())
    print("Month Data Node of Scenario 2", scenario_2.month.read())

    scenario_1.submit()
    scenario_2.submit()

    print("Scenario 1 before", scenario_1.is_primary)
    print("Scenario 2 before", scenario_1.is_primary)

    tp.set_primary(scenario_2)

    print("Scenario 1 after", scenario_1.is_primary)
    print("Scenario 2 after", scenario_1.is_primary)

    scenario_3 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2021,9,1),
                                    name="Scenario 2022/9/1")
    scenario_3.month.write(9)
    scenario_3.submit()

    print("Is scenario 3 primary?", scenario_3.is_primary)
