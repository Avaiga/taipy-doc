from taipy.core.config import Config, Scope, Frequency
import taipy as tp
import datetime as dt
import pandas as pd
import time


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    print("Wait 10 seconds")
    time.sleep(10)
    return len(df)


Config.load('config_07.toml')
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

if __name__=="__main__":
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg, creation_date=dt.datetime(2022,10,7), name="Scenario 2022/10/7")
    scenario_1.month.write(10)
    scenario_1.submit()
    scenario_1.submit()

    time.sleep(30)


if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg, creation_date=dt.datetime(2022,10,7), name="Scenario 2022/10/7")
    scenario_1.month.write(10)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)