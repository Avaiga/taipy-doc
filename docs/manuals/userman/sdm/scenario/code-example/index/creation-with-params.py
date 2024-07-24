import taipy as tp
import my_config
from datetime import datetime

if __name__ == "__main__":
    scenario = tp.create_scenario(config=my_config.monthly_scenario_cfg,
                                creation_date=datetime(2022, 1, 1),
                                name="Scenario for January")
