from taipy import Config


def double(nb):
    return nb * 2


input_data_node_cfg = Config.configure_data_node("input",
                                                 default_data=21)
output_data_node_cfg = Config.configure_data_node("output")
task_cfg = Config.configure_task("double_task",
                                 double,
                                 input_data_node_cfg,
                                 output_data_node_cfg)

pipeline_cfg = Config.configure_pipeline("my_pipeline", [task_cfg])
