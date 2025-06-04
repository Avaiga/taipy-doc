from taipy import Config

historical_data_cfg = Config.configure_azure_blob_data_node(
    id="historical_data",
    azure_container_name="data_container",
    azure_blob_name="hist_data.zip",
    azure_connection_string="DefaultEndpointsProtocol=https;AccountName=foo;AccountKey=Eby8vdM02x...",
    azure_blob_parameters={
        "blob_type": "BlockBlob",
        "metadata": {
            "description": "Historical data for analysis",
            "created_by": "data_team",
        },
    },
)

log_cfg = Config.configure_azure_blob_data_node(
    id="log_history",
    azure_container_name="data_container",
    azure_blob_name="log_data.txt",
    azure_account_name="mystorageaccount",
    entra_id_client_id="00000000-0000-0000-0000-000000000000",
    entra_id_tenant_id="11111111-1111-1111-1111-111111111111",
    entra_id_client_secret="client_secret_1234567890",
    azure_blob_parameters={
        "blob_type": "BlockBlob",
        "metadata": {
            "description": "Log data of the analyses",
            "created_by": "data_team",
        },
    },
)

sales_history_cfg = Config.configure_azure_blob_data_node(
    id="sales_history",
    azure_container_name="data_container",
    azure_blob_name="sales_data.zip",
    azure_account_name="mystorageaccount",
    azure_account_key="Eby8vdM02xNOcqFlqUwJPLlmEtI6tq/K1SZFPTOtr/KBHBeksoGMGw==",
    azure_blob_parameters={
        "blob_type": "BlockBlob",
        "metadata": {
            "description": "Sales history data for analysis",
            "created_by": "data_team",
        },
    },
)
