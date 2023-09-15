import taipy as tp
from taipy import Config, Core

################################################################
#                  Configure your application                  #
################################################################


def build_message(name):
    return f"Hello {name}!"


# A first data node configuration represents a name
name_data_node_cfg = Config.configure_data_node(id="input_name")
# A second data node configuration represents the message to print
message_data_node_cfg = Config.configure_data_node(id="message")
# The task represents the build_message function
build_msg_task_cfg = Config.configure_task("build_msg", build_message, name_data_node_cfg, message_data_node_cfg)
# The scenario represent the whole execution graph
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

if __name__ == "__main__":
    ################################################################
    #            Instantiate the Core service and run it           #
    ################################################################
    Core().run()

    ################################################################
    #               Manage your scenarios and data nodes           #
    ################################################################
    zinedine_scenario = tp.create_scenario(scenario_cfg)
    kylian_scenario = tp.create_scenario(scenario_cfg)

    zinedine_scenario.input_name.write("Zinedine")
    zinedine_scenario.submit()
    print(zinedine_scenario.message.read())

    kylian_scenario.input_name.write("Kylian Mbappe")
    kylian_scenario.submit()
    print(kylian_scenario.message.read())
