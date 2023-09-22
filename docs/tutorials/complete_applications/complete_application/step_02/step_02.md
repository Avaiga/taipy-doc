> The full code is available
<a href="./../src/src.zip" download>here</a>.

# Algorithms used

The application contains functions for different tasks, such as cleaning data, making baseline predictions, 
using machine learning (ML) for predictions, calculating metrics, and generating a dataset to display the predictions.

The function `clean_data` handles the task of cleaning the initial 
dataset. It does this by converting the 'Date' column into datetime 
format. It takes an initial DataFrame as input and provides a cleaned copy of that DataFrame as output.

```python
def clean_data(initial_dataset: pd.DataFrame):
    print("     Cleaning data")
    initial_dataset['Date'] = pd.to_datetime(initial_dataset['Date'])
    cleaned_dataset = initial_dataset.copy()
    return cleaned_dataset
```


## Predictions:
	
`predict_baseline()` and `predict_ml()` returns prediction values from the cleaned 
DataFrame (`cleaned_dataset`), the number of predictions to make (`n_predictions`), a 
specific date (`day`), and a maximum capacity value (`max_capacity`).

First, they pick the training dataset up to the date mentioned. After that, they perform certain calculations or adjustments to make predictions. 
These predictions must not surpass the maximum limit.

```python
def predict_baseline(cleaned_dataset: pd.DataFrame, n_predictions: int, day: dt.datetime, max_capacity: int):
    print("     Predicting baseline")
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
```

`compute_metrics()` calculates some metrics about the predictions.

```python
def compute_metrics(historical_data, predicted_data):
    historical_to_compare = historical_data[-len(predicted_data):]['Value']
    rmse = mean_squared_error(historical_to_compare, predicted_data)
    mae = mean_absolute_error(historical_to_compare, predicted_data)
    return rmse, mae
```

## Output dataset
	
`create_predictions_dataset()` creates a predictions dataset for visualization purposes. It 
takes the predicted baseline values (`predictions_baseline`), ML predicted values 
(`predictions_ml`), a specific date (`day`), the number of predictions to make
(`n_predictions`), and the cleaned dataset (`cleaned_data`).The function returns a DataFrame 
containing the date, historical values, ML predicted values, and baseline predicted values.


```python
def create_predictions_dataset(predictions_baseline, predictions_ml, day, n_predictions, cleaned_data):
    ....

    # Columns : [Date, Historical values, Predicted values (ml and baseline)]
    predictions_dataset = pd.concat([temp_df["Date"],
                                    historical_values,
                                    predicted_values_ml,
                                    predicted_values_baseline], axis=1)
    
    return predictions_dataset
```

## Entire code (algorithms/algorithms.py)
	
Chaining all the functions together can be represented as a following graph:

```python
# For the sake of clarity, we have used an AutoRegressive model rather than a pure ML model such as:
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

    # Set arbitrarily the time window for the chart as 5 times the number of predictions
    window = 5 * n_predictions

    # Create the historical dataset that will be displayed
    new_length = len(cleaned_data[cleaned_data["Date"] < day]) + n_predictions
    temp_df = cleaned_data[:new_length]
    temp_df = temp_df[-window:].reset_index(drop=True)

    # Create the series that will be used in the concat
    historical_values = pd.Series(temp_df["Value"], name="Historical values")
    predicted_values_ml = pd.Series([np.NaN] * len(temp_df), name="Predicted values ML")
    predicted_values_ml[-len(predictions_ml):] = predictions_ml 
    predicted_values_baseline = pd.Series([np.NaN] * len(temp_df), name="Predicted values Baseline")
    predicted_values_baseline[-len(predictions_baseline):] = predictions_baseline

    # Create the predictions dataset
    # Columns : [Date, Historical values, Predicted values]
    predictions_dataset = pd.concat([temp_df["Date"],
                                    historical_values,
                                    predicted_values_ml,
                                    predicted_values_baseline], axis=1)
    
    return predictions_dataset
```