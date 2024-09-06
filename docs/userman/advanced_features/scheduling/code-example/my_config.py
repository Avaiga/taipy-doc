from taipy import Config


def build_message(name: str):
    return f"Hello {name}!"


name_data_node_cfg = Config.configure_data_node(id="input_name", default_data="Zinedine")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])
