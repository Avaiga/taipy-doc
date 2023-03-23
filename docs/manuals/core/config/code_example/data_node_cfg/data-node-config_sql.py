# import config start
from taipy import Config
import pandas as pd
# import config end


# mssql example start
def write_query_builder(data: pd.DataFrame):
    insert_data = list(
        data[["date", "nb_sales"]].itertuples(index=False, name=None))
    return [
        "DELETE FROM sales",
        ("INSERT INTO sales VALUES (?, ?)", insert_data)
    ]


sales_history_cfg = Config.configure_sql_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    read_query="SELECT * from sales",
    write_query_builder=write_query_builder,
    db_extra_args={"TrustServerCertificate": "yes"},
)
# mssql example end


# sqlite example start
sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_name="taipy",
    db_engine="sqlite",
    read_query="SELECT * from sales",
    write_query_builder=write_query_builder,
    sqlite_folder_path="database",
    sqlite_file_extension=".sqlite3",
)
# sqlite example end
