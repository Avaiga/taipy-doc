## Prerequisites

- Knowledge of Docker.
- [Prepare your application for deployment](../prepare-taipy-for-deployment.md)
- [Followed steps for development](development.md)


## Production ready Dockerfile

The following Dockerfile contains minimum configuration for put your application in production.

This template assumes that you provide a `requirements.txt` file with all your dependencies.
Please, update the Docker command `CMD` with corresponding file name and Flask app of your application
as describe in [prepare your application for deployment](../prepare-taipy-for-deployment.md).

```
# Your Python version
FROM python:3.9 as taipy

# Web port of the application
EXPOSE 5000

# Create taipy user for security
RUN groupadd -r taipy && useradd -r -m -g taipy taipy
USER taipy

# Go to the dedicated folder and add the python corresponding folder in PATH
WORKDIR /home/taipy
ENV PATH="${PATH}:/home/taipy/.local/bin"

# Update pip and install Gunicorn with a suitable worker
RUN python -m pip install --upgrade pip
RUN python -m pip install gunicorn gevent-websocket

# Install your application
COPY . .
RUN python -m pip install -r requirements.txt

# Start up command
ENTRYPOINT [ "gunicorn", "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "--bind=0.0.0.0:5000", "--timeout", "1800" ]
CMD [ "<main>:<app>" ]
```

!!! Note

    If you are using a `SQLDataNode^` with a Microsoft SQL Server, you need to add the following commands
    before creating the user:
    ```
    RUN apt-get update && apt-get install -y lsb-release && apt-get clean all
    RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    RUN curl https://packages.microsoft.com/config/debian/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
    RUN apt update && ACCEPT_EULA=Y apt install -y msodbcsql18 unixodbc-dev
    ```

## Production ready Docker Compose

It is not recommended to expose Gunicorn to the Internet. It is better to let [Nginx](https://nginx.org)
handle [this responsibility](https://docs.gunicorn.org/en/stable/deploy.html).

Beside your `docker-compose.yaml`, create a file named `nginx.conf` with
[the following content](https://docs.taipy.io/en/latest/manuals/deployment/docker/nginx.conf).

Then, update your `docker-compose.yaml`:
```yaml
version: "3.9"
services:
  taipy:
    build: ""
  nginx:
    image: nginx:1.23
    ports:
       - "5000:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
```

!!! Warning

    We cannot guarantee that our Dockerfile, Docker Compose and their components do not contain security issues.
