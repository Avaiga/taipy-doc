# Azure Blob Storage Integration

!!! note "Available in Taipy Enterprise edition"
    This section is relevant only to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

## Installation

To use the Azure Blob Storage integration, you need to install the optional package. You can do
this using pip:

```bash
pip install taipy-enterprise[azure-storage]
```

## Overview

The Azure Blob Storage integration provides the following features:

- **[Azure Blob Data Node](#azure-blob-data-node)**:
    A Taipy Data Node that represents a blob in Azure Blob Storage.
- **[Azure File-based Data Node](#azure-file-based-data-node)**:
    File-based data nodes (such as CSV, JSON, Pickle, etc.) can accept an Azure Blob URL
    as the path.

## Azure Blob Data Node

An `AzureBlobDataNode^` is a specific data node used to model data stored in Azure Blob Storage.
It is designed to read and write data from and to Azure Blob Storage.

To configure a new *Azure Blob* data node, use the `Config.configure_azure_blob_data_node()`
method. In addition to the generic parameters described in the
[data node configuration](../../scenario_features/data-integration/data-node-config.md#config-attributes)
documentation, the following parameters can be provided:

- _**azure_container_name**_: represents the Azure Blob Storage container to read from and write the data to.
- _**azure_blob_name**_: represents the Azure Blob Storage blob name to read or write.
- _**azure_connection_string**_: represents the connection string to authenticate with Azure Storage.
- _**entra_id_client_id**_: represents the Entra ID client ID for authentication. If authenticating with
    "entra_id_client_id", "entra_id_tenant_id" and "entra_id_client_secret" must also be provided.
- _**entra_id_tenant_id**_: represents the Entra ID tenant ID for authentication.
- _**entra_id_client_secret**_: represents the Entra ID client secret for authentication.
- _**azure_account_name**_: represents the Azure account name for authentication. If authenticating with
    "azure_account_name", "azure_account_key" must also be provided.
- _**azure_account_key**_: represents the Azure account key for authentication.
- _**azure_blob_parameters**_: represents additional parameters for advanced use cases.

To authenticate with Azure Blob Storage, one of the following authentication methods
must be provided:
- **Connection String**: Use the *azure_connection_string* parameter to provide the connection string
    to authenticate with Azure Blob Storage.
- **Entra ID**: Use the *entra_id_client_id*, *entra_id_tenant_id*, and *entra_id_client_secret* parameters
    to authenticate with Azure Blob Storage using Entra ID.
- **Azure Account**: Use the *azure_account_name* and *azure_account_key* parameters to authenticate
    with Azure Blob Storage using the Azure account name and key.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/data-node-config-azure.py"
    comments=false
    %}
    ```

    In lines 3-15, we configure an Azure Blob data node with the id "historical_data" pointing to
    the Azure Blob "hist_data.zip" in the "data_container" container. The credential to connect to
    Azure Blob Storage is provided through the connection string.

    In lines 17-32, we configure another Azure Blob data node with the id "log_history" pointing to
    the Azure Blob "log_data.txt" in the same "data_container" container. The credential to connect
    to Azure Blob Storage is provided through the Entra ID authentication with the client ID,
    tenant ID, and client secret.

    In line 34-47, we configure another Azure Blob data node with the id "sales_history" pointing
    to the Azure Blob "sales_data.zip" in the "data_container" container. The credential to connect
    to Azure Blob Storage is provided through the Azure account name and key.

!!! note

    To configure an Azure Blob data node, it is equivalent to using the method
    `Config.configure_azure_blob_data_node()^` or the method `Config.configure_data_node()^`
    with parameter `storage_type="azure_blob"`.

## Azure File-based Data Node

Azure Blob Storage is integrated into Taipy file-based data nodes. This means that you can
configure a file-based data node to read and write files directly from an Azure Blob using the
URL of the blob as the path. This includes `CSVDataNode^`, `ExcelDataNode^`, `JSONDataNode^`,
`PickleDataNode^`, and `ParquetDataNode^`.

To configure a file-based data node with Azure Blob Storage, you need to authenticate with Azure
Blob Storage using one of the following authentication methods:

- **Connection String**: Use the *azure_connection_string* parameter to provide the connection string
    to authenticate with Azure Blob Storage.
- **Entra ID**: Use the *entra_id_client_id*, *entra_id_tenant_id*, and *entra_id_client_secret* parameters
    to authenticate with Azure Blob Storage using Entra ID.
- **Azure Account**: Use the *azure_account_name* and *azure_account_key* parameters to authenticate
    with Azure Blob Storage using the Azure account name and key.

If none of these parameters are provided, the blob must allow access through public permissions.

!!! example

    ```python linenums="1"
    {%
    include-markdown "./code-example/data-node-config-file-based-with-azure-url.py"
    comments=false
    %}
    ```

    In lines 3-9, we configure a CSV data node with the id "historical_temperature" pointing to
    the Azure Blob "hist_temp.csv" in the "data_container" container. The credential to connect to
    Azure Blob Storage is provided through the connection string.

    In lines 11-18, we configure an Excel data node with the id "log_history" pointing to
    the Azure Blob "log_history.xlsx" in the same "data_container" container. The credential to connect
    to Azure Blob Storage is provided through the Entra ID authentication with the client ID,
    tenant ID, and client secret.

    In lines 20-27, we configure a JSON data node with the id "sales_history" pointing
    to the Azure Blob "sales.json" in the "data_container" container. The credential to connect
    to Azure Blob Storage is provided through the Azure account name and key.
