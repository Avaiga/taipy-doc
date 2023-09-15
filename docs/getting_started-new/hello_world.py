import taipy as tp
from taipy import Config, Core, Gui


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

################################################################
#                     Design your interface                    #
################################################################

hello_scenario = None
input_name = "Taipy"
message = None


def submit_scenario(state):
    state.hello_scenario.input_name.write(state.input_name)
    state.hello_scenario.submit(wait=True)
    state.message = hello_scenario.message.read()

page = """
Name: <|{input_name}|input|>

<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

if __name__ == "__main__":
    ################################################################
    #            Instantiate the Core service and run it           #
    ################################################################
    Core().run()

    ################################################################
    #               Manage your scenarios and data nodes           #
    ################################################################
    hello_scenario = tp.create_scenario(scenario_cfg)

    ################################################################
    #            Instantiate the Gui service and run it            #
    ################################################################

    Gui(page).run()

