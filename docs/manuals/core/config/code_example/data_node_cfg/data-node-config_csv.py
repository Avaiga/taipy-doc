from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

temp_cfg = Config.configure_csv_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.csv",
    has_header=True,
    exposed_type="numpy")

log_cfg = Config.configure_csv_data_node(
    id="log_history",
    default_path="path/hist_log.csv",
    exposed_type="modin")

sales_history_cfg = Config.configure_csv_data_node(
    id="sales_history",
    default_path="path/sales.csv",
    exposed_type=SaleRow)
