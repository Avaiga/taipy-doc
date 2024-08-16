import taipy as tp
from my_config import monthly_scenario_cfg

if __name__ == "__main__":
    scenario = tp.create_scenario(monthly_scenario_cfg)

    tp.tag(scenario, "my_tag")
    # or
    scenario.add_tag("a_second_tag")
