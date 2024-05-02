from taipy import Config, Scope

Config.set_default_data_node_configuration(
    storage_type="sql_table",
    db_username="username",
    db_password="p4$$w0rD",
    db_name="sale_db",
    db_engine="mssql",
    table_name="products",
    db_host="localhost",
    db_port=1437,
    db_driver="ODBC Driver 17 for SQL Server",
    db_extra_args={"TrustServerCertificate": "yes"},
    scope=Scope.GLOBAL,
)

products_data_cfg = Config.configure_data_node(id="products_data")
users_data_cfg = Config.configure_data_node(id="users_data", table_name="users")
retail_data_cfg = Config.configure_data_node(id="retail_data", storage_type="sql_table", table_name="retail_data")
wholesale_data_cfg = Config.configure_sql_table_data_node(id="wholesale_data", table_name="wholesale_data")

forecast_data_cfg = Config.configure_data_node(id="forecast_data", storage_type="csv", default_path="forecast.csv")
