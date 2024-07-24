import taipy as tp
import my_config

if __name__ == "__main__":
    # Create a scenario from a config
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                name="Scenario 1")

    # Retrieve a sequence
    sequence = scenario.sales_sequence_cfg

    # Retrieve the parent entities of the sequence
    parent_entities = sequence.get_parents()  # {'scenarios': [Scenario 1]}

    # Retrieve the parent entities of the sequence
    tp.get_parents(sequence)  # {'scenarios': [Scenario 1]}
