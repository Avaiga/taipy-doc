# Deploy on Azure

## Prerequisites

- Minimal knowledge of Azure.
- Azure CLI should be installed. Check [the official documentation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) for azure CLI installation.
- [:material-arrow-right: Running a Taipy application](../../run/index.md)


## Azure App Service

Azure App Service is a managed platform that simplifies deployment, scaling, and management of web applications. Azure Web App, a service within App Service, specialized in hosting and managing web applications. As a Python developer, you can leverage Azure Web App to easily deploy and run your Python-based web applications in a scalable and hassle-free environment.

!!! Note

    You can create Azure App Service and Azure Web App using Azure portal, VS Code, Azure Tools extension pack, or Azure CLI. Here we will focus on Azure CLI.

## Prepare your application

Open a terminal and go in the application folder. Ensure you have a `requirements.txt` file listing the required dependencies and your entrypoint Python file named `app.py` or `application.py`. These files are crucial for Azure App Service to correctly deploy your application.

!!! Note

   This naming convention is standard but you can [overwrite it](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python).

Here the folder structure:
```shell
taipy@taipy:~$ ls
application.py  requirements.txt
taipy@taipy:~$ cat requirements.txt
taipy
taipy@taipy:~$ cat application.py
import taipy as tp

app = tp.Gui(page="# Getting started with *Taipy*")

if __name__ == "__main__":
   # Development mode, Flask runs the application for debugging.
   app.run()
else:
   # Production mode, Azure Web Application runs the application with [Gunicorn](https://gunicorn.org/).
   app = app.run(run_server=False)
```

## Create a Web App in Azure

In your terminal, login to Azure using the command:
```shell
taipy@taipy:~$ az login
```

Still in your terminal, you can create the web app then deploy your code using the following command:
```shell
taipy@taipy:~$ az webapp up --runtime PYTHON:3.9 --sku B1 --logs
The webapp 'gentle-stone-7d284754337a4dcb968d392baac1ccc9' doesn't exist
Creating Resource group 'taipy_rg_4939' ...
Resource group creation complete
Creating AppServicePlan 'taipy_asp_8825' ...
Creating webapp 'gentle-stone-7d284754337a4dcb968d392baac1ccc9' ...
Configuring default logging for the app, if not already enabled
Creating zip with contents of dir /home/taipy ...
Getting scm site credentials for zip deployment
Starting zip deployment. This operation can take a while to complete ...
Deployment endpoint responded with status code 202
You can launch the app at http://gentle-stone-7d284754337a4dcb968d392baac1ccc9.azurewebsites.net
Configuring default logging for the app, if not already enabled
```

- The `--runtime` parameter specifies the Python version your app is running, in this case, Python 3.9.
- The `--sku` parameter defines the size (CPU, memory) and cost of the app service plan. This example uses the B1 (Basic) service plan.
- The `--logs` flag configures default logging required to enable viewing the log stream immediately after launching the web app.

You can optionally specify the `--name <app-name>` argument to provide a custom name for your app. If not provided, a name will be automatically generated.

The command may take a few minutes to complete. While it is running, it provides messages about the ressource group and the App Service. Keep then for the next step. In the example, the resource group name is `taipy_rg_4939` and the App Service is `taipy_asp_8825`.

Once completed, it will display the message "You can launch the app at http://<app-name>.azurewebsites.net", which is the URL of your app. In the example `http://gentle-stone-7d284754337a4dcb968d392baac1ccc9.azurewebsites.net`.

!!! Note

    The command can also include the `--location <location-name>` argument to specify the Azure region. Use `az account list-locations` to retrieve a list of available regions for your account.


## Further information

The Azure documentation provide more information about [configuration](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python), [monitoring](https://learn.microsoft.com/en-us/azure/app-service/overview-monitoring) or [logs](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs#enable-application-logging-linuxcontainer).

You can also find more information about [Azure App Service and Azure Web Application](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans).
