from taipy import Config

read_kwargs = {"filters": [("log_level", "in", {"ERROR", "CRITICAL"})]}
write_kwargs = {"partition_cols": ["log_level"], "compression": None}

log_cfg = Config.configure_parquet_data_node(
    id="log_history",
    default_path="path/hist_log.parquet",
    engine="pyarrow", # default
    compression="snappy", # default, but overridden by the key in write_kwargs
    exposed_type="modin",
    read_kwargs=read_kwargs,
    write_kwargs=write_kwargs)
