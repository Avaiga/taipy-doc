import datetime as dt
import pandas as pd

from taipy import Config, Scope, Frequency

from algorithms.algorithms import *

path_to_csv = "data/dataset.csv"

# Datanodes (3.1)
## Input Data Nodes
initial_dataset_cfg = Config.configure_data_node(id="initial_dataset",
                                                 storage_type="csv",
                                                 path=path_to_csv,
                                                 scope=Scope.GLOBAL)

# We assume the current day is the 26th of July 2021.
# This day can be changed to simulate multiple executions of scenarios on different days
day_cfg = Config.configure_data_node(id="day", default_data=dt.datetime(2021, 7, 26))

n_predictions_cfg = Config.configure_data_node(id="n_predictions", default_data=40)

max_capacity_cfg = Config.configure_data_node(id="max_capacity", default_data=200)

## Remaining Data Nodes
cleaned_dataset_cfg = Config.configure_data_node(id="cleaned_dataset",
                                                 scope=Scope.GLOBAL)

predictions_baseline_cfg = Config.configure_data_node(id="predictions_baseline")
predictions_ml_cfg = Config.configure_data_node(id="predictions_ml")

full_predictions_cfg = Config.configure_data_node(id="full_predictions")

metrics_baseline_cfg = Config.configure_data_node(id="metrics_baseline")
metrics_ml_cfg = Config.configure_data_node(id="metrics_ml")

# Functions (3.2)

# Tasks (3.3)
clean_data_task_cfg = Config.configure_task(id="task_clean_data",
                                            function=clean_data,
                                            input=initial_dataset_cfg,
                                            output=cleaned_dataset_cfg,
                                            skippable=True)


predict_baseline_task_cfg = Config.configure_task(id="predict_baseline",
                                                  function=predict_baseline,
                                                  input=[cleaned_dataset_cfg, n_predictions_cfg, day_cfg,
                                                         max_capacity_cfg],
                                                  output=predictions_baseline_cfg)

predict_ml_task_cfg = Config.configure_task(id="task_predict_ml",
                                            function=predict_ml,
                                            input=[cleaned_dataset_cfg,
                                                   n_predictions_cfg, day_cfg,
                                                   max_capacity_cfg],
                                            output=predictions_ml_cfg)


metrics_baseline_task_cfg = Config.configure_task(id="task_metrics_baseline",
                                            function=compute_metrics,
                                            input=[cleaned_dataset_cfg,
                                                   predictions_baseline_cfg],
                                            output=metrics_baseline_cfg)

metrics_ml_task_cfg = Config.configure_task(id="task_metrics_ml",
                                            function=compute_metrics,
                                            input=[cleaned_dataset_cfg,
                                                   predictions_ml_cfg],
                                            output=metrics_ml_cfg)


full_predictions_task_cfg = Config.configure_task(id="task_full_predictions",
                                            function=create_predictions_dataset,
                                            input=[predictions_baseline_cfg,
                                                   predictions_ml_cfg,
                                                  day_cfg,
                                                  n_predictions_cfg,
                                                  cleaned_dataset_cfg],
                                            output=full_predictions_cfg)


# Configure our scenario which is our business problem.
scenario_cfg = Config.configure_scenario(id="scenario",
                                         task_configs=[clean_data_task_cfg,
                                                        predict_baseline_task_cfg,
                                                        predict_ml_task_cfg,
                                                        metrics_baseline_task_cfg,
                                                        metrics_ml_task_cfg,
                                                        full_predictions_task_cfg],
                                         frequency=Frequency.WEEKLY)
