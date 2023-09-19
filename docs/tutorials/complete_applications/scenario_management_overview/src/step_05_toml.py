from taipy.core.config import Config, Frequency, Scope
import taipy as tp
import datetime as dt
import pandas as pd


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    return len(df)

Config.load('config_05.toml')

if __name__ == '__main__':
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                creation_date=dt.datetime(2022,10,5),
                                name="Scenario 2022/10/5")
    scenario_3 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2021,9,1),
                                    name="Scenario 2021/9/1")


    scenario_1.month.write(10)
    print("Scenario 1: month", scenario_1.month.read())
    print("Scenario 2: month", scenario_2.month.read())

    print("\nScenario 1: submit")
    scenario_1.submit()
    print("Value", scenario_1.nb_of_values.read())


    print("\nScenario 2: first submit")
    scenario_2.submit()
    print("Value", scenario_2.nb_of_values.read())
    print("Scenario 2: second submit")
    scenario_2.submit()
    print("Value", scenario_2.nb_of_values.read())


    print("\nScenario 3: submit")
    scenario_3.month.write(9)
    scenario_3.submit()
    print("Value", scenario_3.nb_of_values.read())


    print("Scenario 3: change in historical data")
    scenario_3.historical_data.write(pd.read_csv('time_series_2.csv'))
    scenario_3.submit()
    print("Value", scenario_3.nb_of_values.read())