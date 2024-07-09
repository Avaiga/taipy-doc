from taipy import Config, Scope, Frequency

global_data_cfg = Config.configure_data_node("global_data", scope=Scope.GLOBAL)
cycle_data_cfg = Config.configure_data_node("cycle_data", scope=Scope.CYCLE)
scenario_data_cfg = Config.configure_data_node("data", scope=Scope.SCENARIO)

scenario_cfg = Config.configure_scenario("scenario",
                                         frequency=Frequency.WEEKLY,
                                         additional_data_nodes=[global_data_cfg, cycle_data_cfg, scenario_data_cfg])
