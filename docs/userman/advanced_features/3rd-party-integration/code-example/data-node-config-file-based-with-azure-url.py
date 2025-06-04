from taipy import Config

temp_cfg = Config.configure_csv_data_node(
    id="historical_temperature",
    default_path="https://mystorageaccount.blob.core.windows.net/data_container/hist_temp.csv",
    has_header=True,
    exposed_type="numpy",
    azure_connection_string="DefaultEndpointsProtocol=https;AccountName=foo;AccountKey=Eby8vdM02x...",
)

log_cfg = Config.configure_excel_data_node(
    id="log_history",
    default_path="https://mystorageaccount.blob.core.windows.net/data_container/log_history.xlsx",
    exposed_type="pandas",
    entra_id_client_id="00000000-0000-0000-0000-000000000000",
    entra_id_tenant_id="11111111-1111-1111-1111-111111111111",
    entra_id_client_secret="client_secret_1234567890",
)

sales_history_cfg = Config.configure_json_data_node(
    id="sales_history",
    default_path="https://mystorageaccount.blob.core.windows.net/data_container/sales.json",
    azure_account_name="mystorageaccount",
    azure_account_key="Eby8vdM02xNOcqFlqUwJPLlmEtI6tq/K1SZFPTOtr/KBHBeksoGMGw==",
)
