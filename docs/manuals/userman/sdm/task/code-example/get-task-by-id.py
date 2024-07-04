import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
task = scenario.training
task_retrieved = tp.get(task.id)
# task == task_retrieved
