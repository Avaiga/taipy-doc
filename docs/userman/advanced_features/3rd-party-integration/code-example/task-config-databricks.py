import pandas as pd

from taipy import Config

# Configure train input Databricks Table Data Node
train_input_table_dbs_dn_config = Config.configure_databricks_table_data_node(
    id="train_input_table_dbs",
    table_name="train_input_data",
    profile="default",
    cluster_id="0207-085400-qpwma50w",
    exposed_type="pandas",
    write_mode="overwrite",
)


def build_write_query(dataframe: pd.DataFrame):
    query = "INSERT INTO forecast_input_data VALUES"
    query += ",".join([f" ({val})" for val in dataframe["x"].tolist()])
    return query + ";"


# Configure forecast input Databricks SQL Data Node
forecast_input_sql_dbs_dn_config = Config.configure_databricks_sql_data_node(
    id="forecast_input_sql_dbs",
    read_query="SELECT * FROM forecast_input_data",
    write_query_builder=build_write_query,
    profile="default",
    cluster_id="0207-085400-qpwma50w",
    exposed_type="pandas",
)

# Configure forecast output Databricks Table Data Node
forecast_output_table_dbs_dn_config = Config.configure_databricks_table_data_node(
    id="forecast_output_table_dbs",
    table_name="forecast_output_data",
    cluster_id="0207-085400-qpwma50w",
    profile="default",
    exposed_type="pandas",
    write_mode="overwrite",
)

# Configure a Task to read from Databricks Table and write to Databricks SQL
predict_output_data = Config.configure_databricks_task(
    "run_prediction",
    "simple_linear_regression_job",
    input=[train_input_table_dbs_dn_config, forecast_input_sql_dbs_dn_config],
    output=[forecast_output_table_dbs_dn_config],
    skippable=True,
)
