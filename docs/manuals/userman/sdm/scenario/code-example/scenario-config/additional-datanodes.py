from taipy import Config, Scope

data_node_cfg = Config.configure_data_node("data", scope=Scope.GLOBAL)
scenario_cfg = Config.configure_scenario("scenario_with_one_data_node",
                                         additional_data_nodes=[data_node_cfg])
