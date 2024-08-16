from datetime import datetime
import taipy as tp
from taipy import Config

if __name__ == "__main__":
    # Configure data nodes with different scopes
    hist_cfg = Config.configure_csv_data_node("sales_history")
    model_cfg = Config.configure_data_node("trained_model")
    month_cfg = Config.configure_data_node("current_month")
    predictions_cfg = Config.configure_data_node("sales_predictions")
    capacity_cfg = Config.configure_data_node("capacity")
    orders_cfg = Config.configure_sql_data_node("production_orders",
                                                db_name="taipy",
                                                db_engine="sqlite",
                                                table_name="sales")

    # Configure scenarios
    scenario_cfg = Config.configure_scenario("scenario",
                                             additional_data_node_configs=[
                                                 hist_cfg,
                                                 model_cfg,
                                                 month_cfg,
                                                 predictions_cfg,
                                                 capacity_cfg,
                                                 orders_cfg])

    # Instantiate three scenarios
    # Create a scenario for January with high capacity
    jan_scenario_high = tp.create_scenario(scenario_cfg)
    jan_scenario_high.current_month.write(datetime(2024, 1, 1))  # Set the month to January 2024
    jan_scenario_high.capacity.write(10000)  # Set the capacity to 10,000 units

    # Create another scenario for January with low capacity
    jan_scenario_low = tp.create_scenario(scenario_cfg)
    jan_scenario_low.current_month.write(datetime(2024, 1, 1))  # Set the month to January 2024
    jan_scenario_low.capacity.write(500 ) # Set the capacity to 500 units

    # Create a scenario for February with low capacity
    feb_scenario_low = tp.create_scenario(scenario_cfg)
    feb_scenario_low.current_month.write(datetime(2024, 2, 1))  # Set the month )to February 2024
    feb_scenario_low.capacity.write(500)  # Set the capacity to 500 units
