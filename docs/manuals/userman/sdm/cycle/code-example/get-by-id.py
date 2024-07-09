import taipy as tp
import my_config

# Create a scenario and the related cycle
scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

# Retrieve the parent cycle of the scenario
cycle = scenario.cycle

# Get the cycle by its id
cycle_retrieved = tp.get(cycle.id)
