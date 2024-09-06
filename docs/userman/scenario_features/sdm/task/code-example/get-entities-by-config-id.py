import taipy as tp
import my_config

if __name__ == "__main__":
    # Create 2 scenarios, which will also create 2 trainig tasks.
    scenario_1 = tp.create_scenario(my_config.monthly_scenario_cfg)
    scenario_2 = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get all training tasks by config id, this will return a list of 2 training tasks
    # created alongside the 2 scenarios.
    all_training_tasks = tp.get_entities_by_config_id("training")
