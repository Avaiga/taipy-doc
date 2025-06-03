import taipy as tp
from taipy import Config, Scope

dbs_table_with_profile_dn_config = Config.configure_databricks_table_data_node(
    id="history_temperature",
    table_name="hist_temp",
    profile="default",
    cluster_id="0123-456789-dbscluster2",
    exposed_type="pandas",
)

dbs_table_with_conn_str_dn_config = Config.configure_databricks_table_data_node(
    id="log_history",
    table_name="hist_log",
    conn_string="sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab",
    scope=Scope.GLOBAL,
)

dbs_table_dn = tp.create_global_data_node(dbs_table_with_conn_str_dn_config)

dbs_table_dn.read().show(5)
