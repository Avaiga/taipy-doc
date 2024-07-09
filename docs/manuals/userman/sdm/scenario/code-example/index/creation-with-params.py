import taipy as tp
import my_config
from datetime import datetime

scenario = tp.create_scenario(config=my_config.monthly_scenario_cfg,
                              creation_date=datetime(2022, 1, 1),
                              name="Scenario for January")
