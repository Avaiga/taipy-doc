from taipy.config import Config, Frequency, Scope

from .arima_algorithms import train

# Config the data nodes
historical_data_set = Config.configure_csv_data_node(
    id="historical_data_set",
    path="./daily-min-temperatures.csv",
    scope=Scope.GLOBAL,
    cacheable=True,
)

arima_model = Config.configure_data_node(
    id="arima_model",
    cacheable=True,
    scope=Scope.GLOBAL,
)

# Config the training task
arima_training_algo = Config.configure_task(
    id="arima_training",
    input=historical_data_set,
    function=train,
    output=arima_model,
)

# Config the training pipeline
arima_pipeline = Config.configure_pipeline(
    id="arima_pipelines",
    task_configs=[arima_training_algo],
)

# Config the training scenario
arima_scenario_config = Config.configure_scenario(
    id='Arima_scenario',
    pipeline_configs=[arima_pipeline],
    frequency=Frequency.DAILY,
)
