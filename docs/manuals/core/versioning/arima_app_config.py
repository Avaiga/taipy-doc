from datetime import datetime
from taipy.config import Config, Frequency, Scope

from .arima_algorithms import train, predict

historical_data_set = Config.configure_csv_data_node(
    id="historical_data_set",
    path="./daily-min-temperatures.csv",
    scope=Scope.GLOBAL,
    cacheable=True,
)

dates_to_forecast = Config.configure_data_node(
    id="dates_to_forecast",
    scope=Scope.GLOBAL,
    default_data=[datetime(1991, 1, 1).isoformat()],
    cacheable=True,
)

arima_model = Config.configure_data_node(
    id="arima_model",
    cacheable=True,
    scope=Scope.GLOBAL,
)

forecast_values = Config.configure_excel_data_node(
    id="forecast_values",
    has_header=False,
    path="./res.xlsx",
    cacheable=True,
    scope=Scope.GLOBAL,
)

arima_training_algo = Config.configure_task(
    id="arima_training",
    input=historical_data_set,
    function=train,
    output=arima_model,
)

arima_scoring_algo = Config.configure_task(
    id="arima_scoring",
    input=[arima_model, dates_to_forecast],
    function=predict,
    output=forecast_values,
)

arima_pipeline = Config.configure_pipeline(
    id="arima_pipelines",
    task_configs=[arima_training_algo, arima_scoring_algo],
)

arima_scenario_config = Config.configure_scenario(
    id='Arima_scenario',
    pipeline_configs=[arima_pipeline],
    frequency=Frequency.DAILY,
)
