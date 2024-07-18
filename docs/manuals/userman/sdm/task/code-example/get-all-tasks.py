import taipy as tp
import my_config

# Creating a scenario from a config
scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

# Access all the tasks from the scenario
scenario.tasks

# Access the sequence 'sales' from the scenario and
# then access all the tasks from the sequence
sequence = scenario.sales
sequence.tasks
