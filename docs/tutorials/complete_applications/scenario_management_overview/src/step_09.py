from taipy.core.config import Config, Frequency
import taipy as tp
import datetime as dt
import time


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    print("Wait 10 seconds in add function")
    time.sleep(10)
    return nb + 10


# Configuration of Data Nodes
input_cfg = Config.configure_data_node("input", default_data=21)
intermediate_cfg = Config.configure_data_node("intermediate")
output_cfg = Config.configure_data_node("output")

# Configuration of tasks
first_task_cfg = Config.configure_task("double",
                                    double,
                                    input_cfg,
                                    intermediate_cfg)

second_task_cfg = Config.configure_task("add",
                                    add,
                                    intermediate_cfg,
                                    output_cfg)

# Configuration of the pipeline and scenario
pipeline_cfg = Config.configure_pipeline("my_pipeline", [first_task_cfg, second_task_cfg])



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


scenario_cfg = Config.configure_scenario(id="my_scenario",
                                         name="my_scenario",
                                         pipeline_configs=[pipeline_cfg])


Config.export("config_09.toml")

if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.subscribe(callback_scenario_state)

    scenario_1.submit(wait=True)
    
    tp.Rest().run()


