import taipy as tp
import my_config

if __name__ == "__main__":
    # Create a scenario
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                name="Monthly scenario")
    # Get the sequence created along with the scenario
    sales_sequence = scenario.sales_sequence
    sales_sequence.name = "Sequence for sales prediction"

    # There was no subscription, so subscribers is an empty list
    sales_sequence.subscribers # []

    # The properties dictionary equals {"name": "Sequence for sales prediction"}. It
    # contains all the properties, including the `name` provided at the creation
    sales_sequence.properties # {"name": "Sequence for sales prediction"}

    # The `name` property is also exposed directly as an attribute. It
    # equals "Sequence for sales prediction"
    sales_sequence.name

    # The training task entity is exposed as an attribute of the sequence
    training_task = sales_sequence.training

    # The predicting task entity as well
    predicting_task = sales_sequence.predicting

    # The data nodes are also exposed as attributes of the sequence.
    current_month_data_node = sales_sequence.current_month
