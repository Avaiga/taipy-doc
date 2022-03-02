from datetime import datetime

import pandas as pd


def train(sales_history: pd.DataFrame):
    print("running training")
    return "TRAINED_MODEL"


def predict(model, current_month):
    print("running predicting")
    return "SALES_PREDICTIONS"


def plan(sales_predictions, capacity):
    print("running planning")
    return "PRODUCTION_ORDERS"


