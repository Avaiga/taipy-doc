from datetime import datetime

import pandas as pd

from taipy import Config, Frequency, Scope


def write_orders_plan(data: pd.DataFrame):
    insert_data = data[["date", "product_id", "number_of_products"]].to_dict("records")
    return ["DELETE FROM orders", ("INSERT INTO orders VALUES (:date, :product_id, :number_of_products)", insert_data)]


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
    return "COMPARISON_RESULT"


# Configure all six data nodes
sales_history_cfg = Config.configure_csv_data_node(
    id="sales_history", scope=Scope.GLOBAL, default_path="path/sales.csv"
)
trained_model_cfg = Config.configure_data_node(id="trained_model", scope=Scope.CYCLE)
current_month_cfg = Config.configure_data_node(id="current_month", scope=Scope.CYCLE, default_data=datetime(2020, 1, 1))
sales_predictions_cfg = Config.configure_data_node(id="sales_predictions", scope=Scope.CYCLE)
capacity_cfg = Config.configure_data_node(id="capacity")
orders_cfg = Config.configure_sql_data_node(
    id="orders",
    db_username="admin",
    db_password="ENV[PWD]",
    db_name="production_planning",
    db_engine="mssql",
    read_query="SELECT orders.ID, orders.date, products.price, orders.number_of_products FROM orders INNER JOIN products ON orders.product_id=products.ID",
    write_query_builder=write_orders_plan,
    db_driver="ODBC Driver 17 for SQL Server",
)

# Configure the three tasks
training_cfg = Config.configure_task("training", train, sales_history_cfg, [trained_model_cfg])
predicting_cfg = Config.configure_task(
    id="predicting", function=predict, input=[trained_model_cfg, current_month_cfg], output=sales_predictions_cfg
)
planning_cfg = Config.configure_task(
    id="planning", function=plan, input=[sales_predictions_cfg, capacity_cfg], output=[orders_cfg]
)

# Configure the scenario
monthly_scenario_cfg = Config.configure_scenario(
    id="scenario_configuration",
    task_configs=[training_cfg, predicting_cfg, planning_cfg],
    frequency=Frequency.MONTHLY,
    comparators={sales_predictions_cfg.id: compare},
    sequences={"sales": [training_cfg, predicting_cfg], "production": [planning_cfg]},
)
