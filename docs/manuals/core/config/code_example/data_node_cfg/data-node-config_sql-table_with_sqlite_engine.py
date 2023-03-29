from taipy import Config

sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_name="taipy",
    db_engine="sqlite",
    table_name="sales",
    sqlite_folder_path="database",
    sqlite_file_extension=".sqlite3",
)
