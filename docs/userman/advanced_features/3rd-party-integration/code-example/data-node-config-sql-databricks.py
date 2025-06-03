import pandas as pd

import taipy as tp
from taipy import Config, Scope


def build_hist_temp_write_query(data: pd.DataFrame):
    queries = []
    for _, r in data.iterrows():
        f"INSERT INTO hist_temp (col1, col2) VALUES ({r['col1']}, {r['col2']})"
    return ";".join(queries)


def build_hist_temp_append_query(data: pd.DataFrame):
    queries = []
    for _, r in data.iterrows():
        f"INSERT INTO hist_temp (col1, col2) VALUES ({r['col1']}, {r['col2']})"
    return ";".join(queries)


def build_hist_log_write_query(data: pd.DataFrame):
    queries = []
    for _, r in data.iterrows():
        f"INSERT INTO hist_log (col1, col2) VALUES ({r['col1']}, {r['col2']})"
    return ";".join(queries)


def build_hist_log_append_query(data: pd.DataFrame):
    queries = []
    for _, r in data.iterrows():
        f"INSERT INTO hist_log (col1, col2) VALUES ({r['col1']}, {r['col2']})"
    return ";".join(queries)


dbs_sql_with_profile_dn_config = Config.configure_databricks_sql_data_node(
    id="historical_temperature",
    read_query="SELECT * FROM hist_temp",
    write_query_builder=build_hist_temp_write_query,
    append_query_builder=build_hist_temp_append_query,
    profile="default",
    cluster_id="0123-456789-dbscluster2",
    exposed_type="spark",
    scope=Scope.GLOBAL,
)

dbs_sql_with_conn_str_dn_config = Config.configure_databricks_sql_data_node(
    id="historical_log",
    read_query="SELECT * FROM hist_log",
    write_query_builder=build_hist_log_write_query,
    append_query_builder=build_hist_log_append_query,
    conn_string="sc://foo-workspace.cloud.databricks.com/;token=dapi1234567890;x-databricks-cluster-id=0301-0300-abcdefab",
    exposed_type="pandas",
)

dbs_table_dn = tp.create_global_data_node(dbs_sql_with_profile_dn_config)

dbs_table_dn.read().show(5)
