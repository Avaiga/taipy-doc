# Deploy on Azure

[Azure] (https://azure.microsoft.com/en-us), one of the world's leading providers of cloud services, is a very relevant choice for deploying Taipy applications. It allows developers to stay focused on their application bringing effortless scalability, monitoring and security natively. The following documentation shows how to deploy on Azure App Service and get an application into the hands of the end-user.

## Prerequisites

- Minimal knowledge of Azure.
- Azure CLI should be installed. Check [the official documentation](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) for Azure CLI installation.
- [:material-arrow-right: Running a Taipy application](../run/index.md)


## Azure App Service

[Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/) is a managed platform that simplifies web application deployment, scaling, and management. Azure Web App, a service within App Service, specializes in hosting and managing web applications. As a Python developer, you can leverage Azure Web App to quickly deploy and run your Python-based web applications in a scalable, hassle-free environment.

!!! Note

    You can create Azure App Service and Azure Web App using Azure Portal, VS Code, Azure Tools extension pack, or Azure CLI. In this section, we focus on Azure CLI.

## Prepare your application

Open a terminal and set your directory to the application folder. Ensure you have a `requirements.txt` file listing the required dependencies and your entry point Python file named `app.py` or `application.py`. These files are crucial for Azure App Service to deploy your application correctly.

Because Azure Web Application runs applications with [Gunicorn](https://gunicorn.org/), your application must be adapted to be startable by Gunicorn. To do so, you must expose an `app` object of type `Flask` as shown in the following example.

Here is the folder structure and content:
```shell
taipy@taipy:~$ ls
application.py  requirements.txt
taipy@taipy:~$ cat requirements.txt
taipy
taipy@taipy:~$ cat application.py
import taipy as tp

tp_app = tp.Gui(page="# Getting started with *Taipy*")

if __name__ == "__main__":
   # Development mode, Flask runs the application for debugging.
   tp_app.run()
else:
   # Production mode, Azure Web Application runs the application with Gunicorn.
   app = tp_app.run(run_server=False)
```

## Create a Web App in Azure

In your terminal, log in to Azure using the command:
```shell
taipy@taipy:~$ az login
```

You can now create the web application and then deploy your code using the following command:
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

- The `--runtime` parameter specifies the Python version your application is running, in this case, Python 3.9.
- The `--sku` parameter defines the size (CPU, memory) and cost of the Azure App Service plan. This example uses the B1 (Basic) service plan.
- The `--logs` flag configures the default logging required to enable viewing the log stream immediately after launching the web application.

You can optionally specify the `--name <app-name>` argument to provide a custom name for your application. If it is not provided, a name will be automatically generated.

The command may take a few minutes to complete. While running, it provides messages about the resource group and the Azure App Service names. Keep them for the next step. In the example, the resource group name is `taipy_rg_4939` and the App Service is `taipy_asp_8825`.

Once completed, it will display the message "You can launch the app at http://<application-name>.azurewebsites.net", which is the URL of your application. In the example `http://gentle-stone-7d284754337a4dcb968d392baac1ccc9.azurewebsites.net`.

## Further information

The Azure documentation provides more information about [configuration](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python), [monitoring](https://learn.microsoft.com/en-us/azure/app-service/overview-monitoring) or [logs](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs#enable-application-logging-linuxcontainer).

You can also find more information about [Azure App Service and Azure Web Application](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans).
