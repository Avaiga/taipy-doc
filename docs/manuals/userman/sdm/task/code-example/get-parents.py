import taipy as tp
import my_config

if __name__ == "__main__":
    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)

    # Retrieve a task
    task = scenario.training_cfg

    # Retrieve the parent entities of the task. The returned value is
    # {'scenarios': [Scenario 1], 'sequences': [Sequence 1]}
    parent_entities = task.get_parents()

    # Retrieve the parent entities of the task. The return value is
    # {'scenarios': [Scenario 1], 'sequences': [Sequence 1]}
    tp.get_parents(task)
