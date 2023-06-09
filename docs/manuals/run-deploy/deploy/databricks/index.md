# Deploy on Databricks

!!! Note

    Taipy is currently only available with Databricks **Standard** runtimes.

!!! Warning

    We recommend using Databricks deployments for testing or demonstration purposes only.

In the current section we consider the following as prerequisites:

- Knowledge of Databricks.
- Knowledge of SSH.
- A Databricks cluster in operation.
- A Linux-based machine that can communicate with your local machine and Databricks.
- [:material-arrow-right: Running a Taipy application](../../run/index.md)

## Running your application on Databricks

The first step consist in running your Taipy application on Databricks.
Let's consider the following application:

```python linenums="1"
{%
include-markdown "../../code_sample/basic_gui_rest_app.py"
comments=false
%}
```

Connect to Databricks and run the previous code in a Databricks Notebook.

TODO: Take a better screenshot or copy/paste the output in a code snippet.

![running-taipy-application](images/running-taipy-application.png)

As you can see on the output, the Taipy application is running on the Databricks localhost (127.0.0.1:5000)
which is not exposed. The next section shows you how to expose your application.


## Exposing your application




### External access with Databricks

Databricks does not provide external access to notebooks. You can access resources from your notebooks, but the other way is blocked.

We can't change this configuration, but we can remove it using an external component as our application's entry point.

### Connecting Virtual Machine and Databricks

Since we can't connect to the Databricks, we'll use the Linux-based machine as an entry point to the Databricks. To do this, we'll use [SSH](https://www.ssh.com) which is installed by default on Databricks and Linux. It will create a tunnel between the two entities, enabling them to communicate. We'll also install Nginx on the Linux-based machine to link the request to your application.

### Configuring communication

The key point of the architecture is the communication between the Linux-based machine and Databricks. To check connectivity, we'll connect to the Linux-based device via Databricks.

On Databricks, go to compute and select your cluster.

![databricks-clusters](images/databricks-clusters.png)

Go to the "Apps" panel and select "Web Terminal". It opens a new tab with a shell.

![running-taipy-application](images/databricks-shell.png)

In this shell, enter the following command, replacing `username` and `machine-ip` with your values:
```ssh -R 8080:127.0.0.1:5000 <username>@<machine-ip>```

!!! Note

    If your SSH authentication is based on certificates, remember to upload them on Databricks.

You are now on the Linux-based machine, and the communication is verified. You may notice the option `-R 8080:127.0.0.1:5000`. This option starts [port forwarding](https://www.ssh.com/academy/ssh/tunneling-example) from the machine to Databricks. Specifically, it forwards all packets from port 8080 to port 5000 on your Databricks.

Therefore, running `curl localhost:8080` should get your application's output still running on your Databricks notebook!

![running-taipy-application](images/curl-app.png)


### Make it accessible from the outside

Communication is now established, but not from the browser's point of view. We'll install and configure Nginx on the Linux-based machine to enable browser-based communication.

First, install [Nginx](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/).

Now put the following content in `/etc/nginx/sites-enabled/default` :
```
server {
    listen 80;
    location / {
        proxy_pass http://localhost:8080;

        proxy_read_timeout  36000s;
        proxy_http_version          1.1;
        proxy_set_header            Upgrade $http_upgrade;
        proxy_set_header            Connection $connection_upgrade;
        proxy_set_header            Host $host;
        proxy_request_buffering     off;
    }
}
```

Then restart Nginx: `systemctl restart nginx`.

You should be able to access your application with your browser by doing: `http://<machine-ip>:8080`

!!! Note

    Make sure that communication between the remote machine and your browser is open.
