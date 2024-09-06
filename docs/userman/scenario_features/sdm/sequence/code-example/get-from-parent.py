import taipy as tp
import my_config

if __name__ == "__main__":
    # Create a scenario from the monthly scenario configuration
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Get the sequences from the scenario
    # sequences contains two sequences, as described in the monthly
    # scenario configuration
    sequences = scenario.sequences
