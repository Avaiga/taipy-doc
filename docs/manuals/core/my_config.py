from datetime import datetime

import taipy as tp
from my_functions import plan, predict, train
from taipy import Frequency, Scope

# Configure all six data nodes
sales_history_cfg = tp.configure_data_node(
    id="sales_history", scope=Scope.GLOBAL, storage_type="csv", path="my/file/path.csv"
)
trained_model_cfg = tp.configure_data_node(id="trained_model", scope=Scope.CYCLE)
current_month_cfg = tp.configure_data_node(id="current_month", scope=Scope.CYCLE, default_data=datetime(2020, 1, 1))
sales_predictions_cfg = tp.configure_data_node(id="sales_predictions", scope=Scope.CYCLE)
capacity_cfg = tp.configure_data_node(id="capacity", scope=Scope.SCENARIO)
production_orders_cfg = tp.configure_data_node(
    id="production_orders",
    scope=Scope.SCENARIO,
    storage_type="sql",
    db_username="admin",
    db_password="ENV[PWD]",
    db_name="production_planning",
    db_engine="mssql",
    read_query="SELECT * from production_order",
    write_table="production_order",
)

# Configure the three tasks
training_cfg = tp.configure_task(id="training", inputs=sales_history_cfg, function=train, outputs=[trained_model_cfg])
predicting_cfg = tp.configure_task(
    id="predicting", inputs=[trained_model_cfg, current_month_cfg], function=predict, outputs=sales_predictions_cfg
)
planning_cfg = tp.configure_task(
    id="planning", inputs=[sales_predictions_cfg, capacity_cfg], function=plan, outputs=[production_orders_cfg]
)

# Configure the two pipelines
sales_pipeline_cfg = tp.configure_pipeline(id="sales", tasks=[training_cfg, predicting_cfg])
production_pipeline_cfg = tp.configure_pipeline(id="production", tasks=[planning_cfg])

# Configure the scenario
monthly_scenario_cfg = tp.configure_scenario(
    id="scenario_configuration", pipelines=[sales_pipeline_cfg, production_pipeline_cfg], frequency=Frequency.MONTHLY
)
