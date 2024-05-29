from taipy import Config, Core


def build_message(name: str):
    return f"Hello {name}!"


name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])


if __name__ == "__main__":
    Core().run()

    import taipy as tp
    zinedine_scenario = tp.create_scenario(scenario_cfg)
    zinedine_scenario.input_name.write("Zinedine")
    zinedine_scenario.submit()
    print(zinedine_scenario.message.read())

    kylian_scenario = tp.create_scenario(scenario_cfg)
    kylian_scenario.input_name.write("Kylian Mbappe")
    kylian_scenario.submit()
    print(kylian_scenario.message.read())
