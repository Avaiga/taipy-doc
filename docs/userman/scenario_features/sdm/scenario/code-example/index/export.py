import taipy as tp
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    tp.export(scenario.id, output_path="./monthly_scenario.zip", override=True, include_data=True)
    # or
    scenario.export(output_path="./monthly_scenario_2.zip", override=True, include_data=True)
