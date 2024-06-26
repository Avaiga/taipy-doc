from taipy import Config

sales_history_cfg = Config.configure_sql_table_data_node(
    id="sales_history",
    db_username="admin",
    db_password="password",
    db_name="taipy",
    db_engine="mssql",
    table_name="sales",
    db_driver="ODBC Driver 17 for SQL Server",
    db_extra_args={"TrustServerCertificate": "yes"},
)
