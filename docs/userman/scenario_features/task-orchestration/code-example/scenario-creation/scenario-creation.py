import taipy as tp
from taipy import Config


def double(nb):
    return nb * 2

if __name__ == "__main__":
    # Configuring a scenario with a single task that doubles the input data node
    input_data_node_cfg = Config.configure_data_node("my_input", default_data=21)
    output_data_node_cfg = Config.configure_data_node("my_output")

    double_task_cfg = Config.configure_task(id="double_task",
                                            function=double,
                                            input=input_data_node_cfg,
                                            output=output_data_node_cfg)

    scenario_cfg = Config.configure_scenario(id="double_scenario",
                                            task_configs=[double_task_cfg])

    # Instantiating a scenario
    scenario = tp.create_scenario(scenario_cfg)

