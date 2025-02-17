from taipy import Config

Config.configure_databricks_table_data_node(
    id="history_temperature",
    table_name="hist_temp",
    profile="default",
    cluster_id="0123-456789-dbscluster2",
    exposed_type="spark",
)

Config.configure_databricks_table_data_node(
    id="log_history",
    table_name="hist_log",
    profile="default",
    cluster_id="0123-456789-dbscluster2",
    exposed_type="polars",
)
