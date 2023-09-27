from taipy.core.config import Config
import taipy as tp
import datetime as dt
import pandas as pd
import time

# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10


Config.load('config_07.toml')
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)


if __name__=="__main__":
    scenario_cfg = Config.scenarios['my_scenario']
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
