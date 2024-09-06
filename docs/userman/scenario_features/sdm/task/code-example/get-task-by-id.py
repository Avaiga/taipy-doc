import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    task = scenario.training
    task_retrieved = tp.get(task.id)
    # task == task_retrieved
