from datetime import datetime

import taipy as tp
from taipy import Frequency
from taipy import Scope
from my_functions import train, predict, plan

# Configure all six data nodes
sales_history_cfg = tp.configure_data_node(name="sales_history", scope=Scope.GLOBAL, storage_type="csv", path="my/file/path.csv")
trained_model_cfg = tp.configure_data_node(name="trained_model", scope=Scope.CYCLE)
current_month_cfg = tp.configure_data_node(name="current_month", scope=Scope.CYCLE, default_data=datetime(2020,1,1))
sales_predictions_cfg = tp.configure_data_node(name="sales_predictions", scope=Scope.CYCLE)
capacity_cfg = tp.configure_data_node(name="capacity", scope=Scope.SCENARIO)
production_orders_cfg = tp.configure_data_node(name="production_orders", scope=Scope.SCENARIO, storage_type="sql",
                                               db_username="admin",
                                               db_password="ENV[PWD]",
                                               db_name="production_planning",
                                               db_engine="mssql",
                                               read_query="SELECT * from production_order",
                                               write_table="production_order")

# Configure the three tasks
training_cfg = tp.configure_task(name="training", inputs=sales_history_cfg, train, outputs=[trained_model_cfg])
predicting_cfg = tp.configure_task(name="predicting", inputs=[trained_model_cfg, current_month_cfg], predict, outputs=sales_predictions_cfg)
planning_cfg = tp.configure_task(name="planning", inputs=[sales_predictions_cfg, capacity], plan, outputs=[production_orders_cfg])

# Configure the two pipelines
sales_pipeline_cfg = tp.configure_pipeline(name="sales", tasks=[training_cfg, predicting_cfg])
production_pipeline_cfg = tp.configure_pipeline(name="production", tasks=[planning_cfg])

# Configure the scenario
monthly_scenario_cfg = tp.configure_scenario(name="scenario_configuration",
                                             pipelines=[sales_pipeline_cfg, production_pipeline_cfg],
                                             frequency=Frequency.MONTHLY)
