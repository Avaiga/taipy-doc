import taipy as tp
from datetime import datetime
import my_config

if __name__ == "__main__":
    scenario = tp.create_scenario(my_config.monthly_scenario_cfg,
                                creation_date=datetime(2022, 1, 1),
                                name="Scenario for January")

    # The config_id is an attribute of the scenario and equals "scenario_configuration"
    scenario.config_id
    # The creation date is the date-time provided at the creation. It equals datetime(2022, 1, 1)
    scenario.creation_date
    # The is_primary property equals `True` since it is the only scenario of the cycle.
    scenario.is_primary
    # There was no subscription, so subscribers is an empty list
    scenario.subscribers # []
    # The properties' dictionary equals {"name": "Scenario for January"}. It contains all the properties,
    # including the `name` provided at the creation
    scenario.properties # {"name": "Scenario for January"}
    # The `name` property is also exposed directly as an attribute. It equals "Scenario for January"
    scenario.name
    # the sales sequence entity is exposed as an attribute of the scenario
    sales_sequence = scenario.sales
    # the production sequence entity as well
    production_sequence = scenario.production
    # All the tasks are also exposed as attributes, including the training task entity
    training_task = scenario.training
    # The six data nodes are also exposed as attributes of the scenario.
    current_month_data_node = scenario.current_month
