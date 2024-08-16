import taipy as tp
import my_config

if __name__ == "__main__":
    # Create a scenario from the monthly scenario configuration
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    # Get the training task from the scenario
    training_task = scenario.training

    # Add a new sequence made of one single task: the training task
    sequence = scenario.add_sequence(name="training_sequence", tasks=[training_task])
