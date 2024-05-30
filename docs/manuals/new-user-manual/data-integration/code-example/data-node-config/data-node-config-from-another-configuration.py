from taipy import Config, Scope

products_data_cfg = Config.configure_sql_table_data_node(
    id="products_data",
    db_username="foo",
    db_password="bar",
    db_name="db",
    db_engine="mssql",
    db_host="localhost",
    db_port=1437,
    db_driver="ODBC Driver 17 for SQL Server",
    db_extra_args={"TrustServerCertificate": "yes"},
    table_name="products",
)

users_data_cfg = Config.configure_data_node_from(
    source_configuration=products_data_cfg,
    id="users_data",
    scope=Scope.GLOBAL,
    table_name="users",
)

retail_data_cfg = Config.configure_data_node_from(
    source_configuration=products_data_cfg,
    id="retail_data",
    table_name="retail_data",
)

wholesale_data_cfg = Config.configure_data_node_from(
    source_configuration=products_data_cfg,
    id="wholesale_data",
    table_name="wholesale_data",
)
