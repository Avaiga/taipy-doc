import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task_1 = scenario.predicting  # "predicting" is the config_id of the task
    sequence = scenario.sales
    task_2 = sequence.predicting  # "predicting" is the config_id of the task
    # task_1 == task_2
