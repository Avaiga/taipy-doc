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
    Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

    # Configuration of Data Nodes
    input_cfg = Config.configure_data_node("my_input", default_data=21)
    intermediate_cfg = Config.configure_data_node("intermediate", default_data=21)
    output_cfg = Config.configure_data_node("my_output")

    # Configuration of tasks
    first_task_cfg = Config.configure_task("double",
                                        double,
                                        input_cfg,
                                        intermediate_cfg)

    second_task_cfg = Config.configure_task("add",
                                            add,
                                            intermediate_cfg,
                                            output_cfg)

    # Configuration of the scenario
    scenario_cfg = Config.configure_scenario(id="my_scenario",
                                            task_configs=[first_task_cfg,
                                                        second_task_cfg])

    Config.export("config.toml")

    tp.Orchestrator().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
