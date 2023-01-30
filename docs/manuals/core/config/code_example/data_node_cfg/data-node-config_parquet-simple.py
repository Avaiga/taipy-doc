from taipy import Config

temp_cfg = Config.configure_parquet_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.parquet")
