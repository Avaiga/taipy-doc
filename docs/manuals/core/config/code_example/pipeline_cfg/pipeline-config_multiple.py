from taipy import Config


def double(nb):
    return nb * 2


input_data_node_cfg = Config.configure_data_node("input",
                                                 default_data=21)
intermediate_data_node_cfg = Config.configure_data_node("intermediate")
output_data_node_cfg = Config.configure_data_node("output")
first_task_cfg = Config.configure_task("first_double_task",
                                       double,
                                       input_data_node_cfg,
                                       intermediate_data_node_cfg)
second_task_cfg = Config.configure_task("second_double_task",
                                        double,
                                        intermediate_data_node_cfg,
                                        output_data_node_cfg)

other_pipeline_cfg = Config.configure_pipeline("another_pipeline",
                                               [first_task_cfg, second_task_cfg])
