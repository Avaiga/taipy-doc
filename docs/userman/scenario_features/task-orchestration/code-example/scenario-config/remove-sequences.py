from taipy import Config

scenario_cfg = Config.configure_scenario("my_scenario",
                                         task_configs=[add_task_cfg_1,
                                                       add_task_cfg_2,
                                                       multiply_task_cfg_1,
                                                       multiply_task_cfg_2],
                                         sequences={"add_sequence": [add_task_cfg_1, add_task_cfg_2],
                                                    "multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})

scenario_cfg.remove_sequences(["add_sequence", "multiply_sequence"])
