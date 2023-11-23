from taipy import Config
import pandas as pd

def write_query_builder(data: pd.DataFrame):
    insert_data = data[["date", "nb_sales"]].to_dict("records")
    return [
        "DELETE FROM sales",
        ("INSERT INTO sales VALUES (:date, :nb_sales)", insert_data)
    ]

sales_history_cfg = Config.configure_sql_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    read_query="SELECT * from sales",
    write_query_builder=write_query_builder,
    db_driver="ODBC Driver 17 for SQL Server",
    db_extra_args={"TrustServerCertificate": "yes"},
)
