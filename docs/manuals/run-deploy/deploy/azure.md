# Deploy on Azure

## Prerequisites

- Minimal knowledge of Azure.
- Azure CLI should be installed. Check [the official documentation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) for azure CLI installation.
- [:material-arrow-right: Running a Taipy application](../../run/index.md)


## Azure App Service

Azure App Service is a managed platform that simplifies deployment, scaling, and management of web applications. Azure Web App, a service within App Service, specialized in hosting and managing web applications. As a Python developer, you can leverage Azure Web App to easily deploy and run your Python-based web applications in a scalable and hassle-free environment.

!!! Note

    You can create Azure App Service and Azure Web App using Azure portal, VS Code, Azure Tools extension pack, or Azure CLI. Here we will focus on Azure CLI.


## Create a Web App in Azure

To host your Taipy application in Azure, you need to create an Azure App Service web app.

Login to Azure using the command:
```
az login
```

Create the web app and other necessary resources, then deploy your code to Azure using the following command:
```
az webapp up --runtime PYTHON:3.9 --sku B1 --logs
```

- The `--runtime` parameter specifies the Python version your app is running, in this case, Python 3.9.
- The `--sku` parameter defines the size (CPU, memory) and cost of the app service plan. This example uses the B1 (Basic) service plan.
- The `--logs` flag configures default logging required to enable viewing the log stream immediately after launching the web app.

You can optionally specify the `--name <app-name>` argument to provide a custom name for your app. If not provided, a name will be automatically generated.

The command may take a few minutes to complete. While it is running, it provides messages about resource group creation, App Service plan creation, app resource creation, logging configuration, and ZIP deployment. Once completed, it will display the message "You can launch the app at http://<app-name>.azurewebsites.net", which is the URL of your app.

!!! Note

    The command can also include the `--location <location-name>` argument to specify the Azure region. Use `az account list-locations` to retrieve a list of available regions for your account.

## Log Stream

Azure App Service provides a convenient feature called Log Stream, which captures all messages output to the console. This capability proves useful in diagnosing issues with your application during development and deployment. By leveraging Log Stream, you can easily monitor and analyze the logged messages to gain insights into your application's behavior.

To demonstrate this capability, let's consider the following Taipy application:
```python
import taipy as tp

if __name__ == "__main__":
    print('Starting the Taipy application')
    tp.Gui(page="# Getting started with *Taipy*").run(title="Taipy application")
```

In this example, we have a simple Taipy application that starts by printing a message to the console using the `print()` function. This message will be captured by the Azure App Service's Log Stream.

To retrieve logs from your Azure App Service web app using the Azure CLI, you need to obtain the resource group name and the app service name. Here's how you can do it:

1. Resource Group Name: You can find the resource group name associated with your Azure App Service web app through the Azure portal or by using the Azure CLI command:

   ```shell
   az appservice plan list --query "[?contains(name, '<app-service-plan-name>')].resourceGroup" --output tsv
   ```

   Replace `<app-service-plan-name>` with the name of your app service plan.

2. App Service Name: You can retrieve the app service name using the Azure CLI command:

   ```shell
   az webapp show --name <app-name> --resource-group <resource-group-name> --query name --output tsv
   ```

   Replace `<app-name>` with the name of your web app, and `<resource-group-name>` with the resource group name.

Once you have obtained the resource group name and the app service name, you can use the following steps to retrieve logs using the Azure CLI:

1. Configure Azure App Service to output logs to the App Service filesystem using the following command:

   ```shell
   az webapp log config --web-server-logging filesystem --name <app-service-name> --resource-group <resource-group-name>
   ```

   Replace `<app-service-name>` with the app service name, and `<resource-group-name>` with the resource group name.

2. Stream the logs using the following command:

   ```shell
   az webapp log tail --name <app-service-name> --resource-group <resource-group-name>
   ```

   Replace `<app-service-name>` with the app service name, and `<resource-group-name>` with the resource group name.

3. Perform actions in your Taipy application, such as refreshing the home page or making requests, to generate log messages. The log output will be displayed in the CLI, providing you with real-time log stream.

By following these steps, you can easily retrieve logs from your Azure App Service web app using the Azure CLI. This allows you to monitor and analyze the logs to diagnose any issues or unexpected behavior in your Taipy application.

The Log Stream provides a valuable way to monitor your application's output and quickly identify any issues or unexpected behavior. It helps in troubleshooting and debugging your Taipy application effectively.

Using the Log Stream feature in Azure App Service, you can conveniently view and analyze the logged messages from your Taipy application, making it easier to monitor and troubleshoot any issues that may arise.