from taipy import Config


def double(nb):
    return nb * 2


input_data_node_cfg = Config.configure_data_node("my_input",
                                                 default_data=21)
output_data_node_cfg = Config.configure_data_node("my_output")

double_task_cfg = Config.configure_task("double_task",
                                        double,
                                        input_data_node_cfg,
                                        output_data_node_cfg,
                                        skippable=True)
