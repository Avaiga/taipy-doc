from taipy import Config, Frequency, Scope
import taipy as tp
from datetime import datetime

# Configure data nodes with different scopes
hist_cfg = Config.configure_csv_data_node("sales_history", scope=Scope.GLOBAL)
model_cfg = Config.configure_data_node("trained_model", scope=Scope.CYCLE)
month_cfg = Config.configure_data_node("current_month", scope=Scope.CYCLE)
predictions_cfg = Config.configure_data_node("sales_predictions", scope=Scope.CYCLE)
capacity_cfg = Config.configure_data_node("capacity", scope=Scope.SCENARIO)
orders_cfg = Config.configure_sql_data_node("production_orders",
                                            scope=Scope.SCENARIO,
                                            db_name="taipy",
                                            db_engine="sqlite",
                                            table_name="sales")

# Configure scenarios
scenario_cfg = Config.configure_scenario("scenario", frequency=Frequency.MONTHLY,
                                         additional_data_node_configs=[
                                             hist_cfg,
                                             model_cfg,
                                             month_cfg,
                                             predictions_cfg,
                                             capacity_cfg,
                                             orders_cfg])

# Instantiate three scenarios
jan_scenario_high = tp.create_scenario(scenario_cfg, datetime(2024, 1, 1))
jan_scenario_low = tp.create_scenario(scenario_cfg, datetime(2024, 1, 1))
feb_scenario_low = tp.create_scenario(scenario_cfg, datetime(2024, 2, 1))
