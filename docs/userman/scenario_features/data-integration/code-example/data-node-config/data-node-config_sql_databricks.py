import pandas as pd

from taipy import Config


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


Config.configure_databricks_sql_data_node(
    id="historical_temperature",
    read_query="SELECT * FROM hist_temp",
    write_query_builder=build_hist_temp_write_query,
    append_query_builder=build_hist_temp_append_query,
    profile="default",
    cluster_id="0123-456789-dbscluster2",
    exposed_type="spark",
)

Config.configure_databricks_sql_data_node(
    id="historical_log",
    read_query="SELECT * FROM hist_log",
    write_query_builder=build_hist_log_write_query,
    append_query_builder=build_hist_log_append_query,
    profile="default",
    cluster_id="my_cluster_id",
    exposed_type="pandas",
)
