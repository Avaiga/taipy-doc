# To make things clear, we've opted for an AutoRegressive model instead of a pure ML model like:
# Random Forest, Linear Regression, LSTM, etc   
from statsmodels.tsa.ar_model import AutoReg
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import datetime as dt

def clean_data(initial_dataset: pd.DataFrame):
    print("     Cleaning data")
    # Convert the date column to datetime
    initial_dataset['Date'] = pd.to_datetime(initial_dataset['Date'])
    cleaned_dataset = initial_dataset.copy()
    return cleaned_dataset


def predict_baseline(cleaned_dataset: pd.DataFrame, n_predictions: int, day: dt.datetime, max_capacity: int):
    print("     Predicting baseline")
    # Select the train data
    train_dataset = cleaned_dataset[cleaned_dataset['Date'] < day]

    predictions = train_dataset['Value'][-n_predictions:].reset_index(drop=True)
    predictions = predictions.apply(lambda x: min(x, max_capacity))
    return predictions


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


def compute_metrics(historical_data, predicted_data):
    historical_to_compare = historical_data[-len(predicted_data):]['Value']
    rmse = mean_squared_error(historical_to_compare, predicted_data)
    mae = mean_absolute_error(historical_to_compare, predicted_data)
    return rmse, mae


def create_predictions_dataset(predictions_baseline, predictions_ml, day, n_predictions, cleaned_data):
    print("Creating predictions dataset...")
    
    # Create the historical dataset that will be displayed
    new_length = len(cleaned_data[cleaned_data["Date"] < day]) + n_predictions
    historical_data = cleaned_data[:new_length].reset_index(drop=True)

    create_series = lambda data, name: pd.Series([np.NaN] * (len(historical_data)), name=name).fillna({i: val for i, val in enumerate(data, len(historical_data)-n_predictions)})

    predictions_dataset = pd.concat([
        historical_data["Date"],
        historical_data["Value"].rename("Historical values"),
        create_series(predictions_ml, "Predicted values ML"),
        create_series(predictions_baseline, "Predicted values Baseline")
    ], axis=1)

    return predictions_dataset
