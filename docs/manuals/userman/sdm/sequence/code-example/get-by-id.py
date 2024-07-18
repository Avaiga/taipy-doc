import taipy as tp
import my_config

scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
sequence = scenario.sales_sequence

sequence_retrieved = tp.get(sequence.id)
