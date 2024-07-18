from taipy import Config

scenario_cfg = Config.configure_scenario("my_scenario",
                                         task_configs=[add_task_cfg_1,
                                                       add_task_cfg_2,
                                                       multiply_task_cfg_1,
                                                       multiply_task_cfg_2])

scenario_cfg.add_sequences({"add_sequence": [add_task_cfg_1, add_task_cfg_2]})
scenario_cfg.add_sequences({"multiply_sequence": [multiply_task_cfg_1, multiply_task_cfg_2]})
