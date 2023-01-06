import pandas as pd


def train(sales_history: pd.DataFrame):
    print("Running training")
    return "TRAINED_MODEL"


def predict(model, current_month):
    print("Running predicting")
    return "SALES_PREDICTIONS"


def plan(sales_predictions, capacity):
    print("Running planning")
    return "PRODUCTION_ORDERS"


def compare(previous_month_prediction, current_month_prediction):
    print("Comparing previous month and current month sale predictions")
    return "COMPARISION_RESULT"
