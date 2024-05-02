from taipy import Config

hist_temp_cfg = Config.configure_json_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.json",
)
