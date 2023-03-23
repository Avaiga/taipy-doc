# import config start
from taipy import Config
# import config end

# mssql example start
sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    table_name="sales",
    db_extra_args={"TrustServerCertificate": "yes"},
)
# mssql example end


# sqlite example start
sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_name="taipy",
    db_engine="sqlite",
    table_name="sales",
    sqlite_folder_path="database",
    sqlite_file_extension=".sqlite3",
)
# sqlite example end
