from taipy.core.config import Config, Scope, Frequency
import taipy as tp
import datetime as dt
import pandas as pd


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    return len(df)


Config.load('config_06.toml')

# my_scenario is the id of the scenario configured
scenario_cfg = Config.scenarios['my_scenario']

if __name__ == '__main__':
    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                creation_date=dt.datetime(2022,10,5),
                                name="Scenario 2022/10/5")
    scenario_3 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2021,9,1),
                                    name="Scenario 2022/9/1")


    # scenario 1 and 2 belongs to the same cycle
    scenario_1.month.write(10)

    scenario_1.submit()

    # first task has already been executed by scenario 1
    # because scenario 2 shares the same data node for this task
    scenario_2.submit()

    # every task has already been executed so everything will be skipped
    scenario_2.submit()

    # scenario 3 has no connection to the other scenarios so everything will be executed
    scenario_3.month.write(9)
    scenario_3.submit()

    # changing an input data node will make the task be reexecuted
    print("Scenario 3: change in historical data")
    scenario_3.historical_data.write(pd.read_csv('time_series_2.csv'))
    scenario_3.submit()

