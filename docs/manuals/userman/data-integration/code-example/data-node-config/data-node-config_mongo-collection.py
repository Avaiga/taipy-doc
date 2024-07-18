from taipy import Config

historical_data_cfg = Config.configure_mongo_collection_data_node(
    id="historical_data",
    db_username="admin",
    db_password="pa$$w0rd",
    db_name="taipy",
    collection_name="historical_data_set",
)
