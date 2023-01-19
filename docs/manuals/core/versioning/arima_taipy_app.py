import taipy.core as tp
from arima_app_config import arima_scenario_config

tp.Core().run()

scenario = tp.create_scenario(arima_scenario_config)

tp.submit(scenario)
