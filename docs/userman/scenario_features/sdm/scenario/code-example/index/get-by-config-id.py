import taipy as tp
import my_config

if __name__ == "__main__":
    # Create 2 scenarios.
    scenario_1 = tp.create_scenario(my_config.monthly_scenario_cfg)
    scenario_2 = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get all monthly scenarios by config id, this will return a list of 2 scenarios just created.
    all_monthly_scenarios = tp.get_entities_by_config_id("scenario_configuration")
