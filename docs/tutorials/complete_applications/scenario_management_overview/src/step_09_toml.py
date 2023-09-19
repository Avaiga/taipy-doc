from taipy.core.config import Config, Scope, Frequency
import taipy as tp
import datetime as dt
import pandas as pd
import time


Config.load('config_09.toml')
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    print("Wait 10 seconds")
    time.sleep(10)
    return len(df)


def callback_scenario_state(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.
    Depending on the job and the status, it will update the message stored in a json that is then displayed on the GUI.

    Args:
        scenario (Scenario): the scenario of the job changed
        job (_type_): the job that has its status changed
    """
    print(scenario.name)
    if job.status.value == 7:
        for data_node in job.task.output.values():
            print(data_node.read())


if __name__=="__main__":
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg, creation_date=dt.datetime(2022,10,7), name="Scenario 2022/10/7")
    scenario_1.subscribe(callback_scenario_state)

    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)