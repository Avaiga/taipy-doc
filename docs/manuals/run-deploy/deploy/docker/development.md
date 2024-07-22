# Prerequisites

- Minimal knowledge of Docker.
- Docker must be installed. Check [the official documentation](https://docs.docker.com/engine/install/) for docker installation.
- Docker-compose must be installed. Check [the official documentation](https://docs.docker.com/compose/install/) for docker-compose installation.

# Development Dockerfile

The following example allows you to run your application for development purpose inside a Docker container.

```
# Your Python version
FROM python:3.9

# Web port of the application
EXPOSE 5000

# Install your application
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Start up command
CMD python main.py -P 5000 -H 0.0.0.0 --debug
```

!!! note

    If you are using a SQL database based on Microsoft SQL Server, you need to add the following commands
    before installing your application:
    ```
    RUN apt-get update && apt-get install -y lsb-release && apt-get clean all
    RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    RUN curl https://packages.microsoft.com/config/debian/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
    RUN apt update && ACCEPT_EULA=Y apt install -y msodbcsql18 unixodbc-dev
    ```

Build the container using the command:
```
docker build -t my-taipy-app .
```

When the container is ready, you can run it in the background with the command:
```
docker run -p 5000:5000 -d --name my-taipy-app my-taipy-app
```
Then go on `http://localhost:5000`.

Note that the `-p` option indicates the port number binding the container and the host.


To stop the container, use the command:
```
docker stop my-taipy-app
```
You can remove the container from docker with the command:
```
docker rm my-taipy-app
```
Then you can delete the container imager with the command:
```
docker rmi my-taipy-app
```


# Simplify build with docker-compose

You can also wrap your build and run steps with `docker-compose`.

Create a `docker-compose.yml` with the following content:

```yaml
version: "3.9"
services:
  taipy:
    build: ""
    ports:
      - "5000:5000"
```

You can build and run your application with:
```
docker-compose up --build -d
```
Then go on `http://localhost:5000`.

You can clean all resources by doing: `docker-compose down --remove-orphans`.
