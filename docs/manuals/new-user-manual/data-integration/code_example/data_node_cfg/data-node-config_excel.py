from taipy import Config

class SaleRow:
    date: str
    nb_sales: int

hist_temp_cfg = Config.configure_excel_data_node(
    id="historical_temperature",
    default_path="path/hist_temp.xlsx",
    exposed_type="numpy")

hist_log_cfg = Config.configure_excel_data_node(
    id="log_history",
    default_path="path/hist_log.xlsx",
    exposed_type="modin")

sales_history_cfg = Config.configure_excel_data_node(
    id="sales_history",
    default_path="path/sales.xlsx",
    sheet_name=["January", "February"],
    exposed_type=SaleRow)
