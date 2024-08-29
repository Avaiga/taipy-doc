# Prerequisites

- Knowledge of Docker.
- [Running a Taipy application](../../run/index.md)
- [Followed steps for development](development.md)


# Production ready Dockerfile

The following Dockerfile contains the minimum configuration settings to deploy your application to production.

This template assumes that you provide a `requirements.txt` file with all the Python
dependencies of your application and that your application entry point is the file `main.py.`

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

# Update pip
RUN python -m pip install --upgrade pip

# Install application's dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install your application
COPY . .

# Start up command
ENTRYPOINT [ "python", "main.py", "-P", "5000", "-H", "0.0.0.0", "--no-reloader" ]
```

!!! note

    If you are using a SQL database based on Microsoft SQL Server, you need to add the following commands
    before creating the user:
    ```
    RUN apt-get update && apt-get install -y lsb-release && apt-get clean all
    RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    RUN curl https://packages.microsoft.com/config/debian/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
    RUN apt update && ACCEPT_EULA=Y apt install -y msodbcsql18 unixodbc-dev
    ```

# Production ready Docker Compose

Exposing your application directly to the Internet is not recommended. Letting
[Nginx](https://nginx.org) handle the responsibility is better for security and reliability.
Consequently, besides your `docker-compose.yaml`, create a file named `nginx.conf` with
[the following content](./nginx.conf).

Then, update your `docker-compose.yaml`:
```yaml
version: "3.9"
services:
  taipy:
    build: ""
  nginx:
    image: nginx:1.25
    ports:
       - "5000:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
```

