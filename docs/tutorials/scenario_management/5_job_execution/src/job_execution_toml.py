import time

import taipy as tp
from taipy.core.config import Config


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10

if __name__=="__main__":
    Config.load("config.toml")
    Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

    scenario_cfg = Config.scenarios["my_scenario"]
    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
