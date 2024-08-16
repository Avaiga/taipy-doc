import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    tp.untag(scenario, "my_tag")
    # or
    scenario.remove_tag("a_second_tag")
