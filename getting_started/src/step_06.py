# For the sake of clarity, we have used an AutoRegressive model rather than a pure ML model such as:
# Random Forest, Linear Regression, LSTM, etc   
from statsmodels.tsa.ar_model import AutoReg

from taipy import Config

from step_04 import *
from step_03 import cleaned_dataset_cfg, n_predictions_cfg, day_cfg, max_capacity_cfg, predictions_cfg, pd, dt


# This is the function that will be used by the task
def predict_ml(cleaned_dataset: pd.DataFrame, n_predictions: int, day: dt.datetime, max_capacity: int):
    print("     Predicting with ML")
    # Select the train data
    train_dataset = cleaned_dataset[cleaned_dataset["Date"] < day]

    # Fit the AutoRegressive model
    model = AutoReg(train_dataset["Value"], lags=7).fit()

    # Get the n_predictions forecasts
    predictions = model.forecast(n_predictions).reset_index(drop=True)
    predictions = predictions.apply(lambda x: min(x, max_capacity))
    return predictions


# Create the task configuration of the predict_ml function.
## We use the same input and ouput as the previous predict_baseline task but we change the funtion
predict_ml_task_cfg = Config.configure_task(id="predict_ml",
                                            function=predict_ml,
                                            input=[cleaned_dataset_cfg, n_predictions_cfg, day_cfg, max_capacity_cfg],
                                            output=predictions_cfg)

# Create the new pipeline that will clean and predict with the ml model
ml_pipeline_cfg = Config.configure_pipeline(id="ml", task_configs=[clean_data_task_cfg, predict_ml_task_cfg])

# Configure our scenario which is our business problem.
scenario_cfg = Config.configure_scenario(id="scenario", pipeline_configs=[baseline_pipeline_cfg, ml_pipeline_cfg])

# The configuration is now complete

if __name__ == "__main__":
    # Create the scenario
    scenario = tp.create_scenario(scenario_cfg)
    # Execute it
    tp.submit(scenario)

    # Get the resulting scenario
    ## Print the predictions of the two pipelines (baseline and ml)
    print("\nBaseline predictions\n", scenario.baseline.predictions.read())
    print("\nMachine Learning predictions\n", scenario.ml.predictions.read())
