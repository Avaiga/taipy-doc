# Taipy application with Airflow

!!! important
    This feature is limited to the Enterprise version only. <br>
    For more information, contact us at [taipy.io](https://www.taipy.io).

## Prerequisites

- Minimal knowledge of Docker.
- Docker should be installed. Check [the official documentation](https://docs.docker.com/engine/install/) for Docker
  installation.
- Docker-compose should be installed. Check [the official documentation](https://docs.docker.com/compose/install/)
  for docker-compose installation.
- [:material-arrow-right: Had done the Getting-Started](standalone.md)

## Airflow and Taipy in the same container

To run Airflow and Taipy in the same container, you must install the Airflow dependencies in the container itself.
Replace your Dockerfile with the following:
```
# Your Python version
FROM python:3.9

# Web port of the application
EXPOSE 5000

# Install your application
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install pip install 'apache-airflow==2.2.3' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.9.txt"

# Startup command
CMD python my-app.py
```

Then you should specify Airflow as the scheduler in your configuration.
```
[JOB]
mode = "airflow"
hostname = "http://localhost:8080"
```

## Airflow and Taipy in different containers

The Apache Airflow community provides an official
[docker-compose file](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html). However, Taipy requires
a custom version of this file, that should be downloaded from [this link](docker-compose.yml.md). Download this file
and copy it next to your main application file.

!!! important "Docker-compose minimal version"
    Make sure that the version is later than `1.29`.

### Custom image

To run your application, you must provide to Airflow a custom image that contains all the Airflow dependencies.
Everything is already packaged in this [Dockerfile](Dockerfile.md). Download it and copy it next to the main
application source file.

Update your configuration with the parameters below to allow communication between Airflow and Taipy.
```
[TAIPY]
storage_folder = "/app/data"

[JOB]
mode = "airflow"
hostname = "http://airflow-webserver:8080"
airflow_api_retry = 100
airflow_dags_folder="/app/dags"
airflow_user="airflow"
airflow_password="airflow"
```

!!! warning "If you run on Linux"
    You should first run the following commands ([For more information click here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#setting-the-right-airflow-user)):
    ```
    mkdir -p ./dags ./logs ./plugins
    echo -e "AIRFLOW_UID=$(id -u)\n_PIP_ADDITIONAL_REQUIREMENTS=taipy-core" > .env
    ```


Before you run your application, you must create the Airflow database using the following command:
```
docker-compose up airflow-init
```
Then, you can run your application by doing:
```
docker-compose up -d --build
```

You can access the Airflow server at `http://0.0.0.0:8080/home`. The default value for both the username and the
password are `airflow`. Please note that in some instances the initialization of Airflow can be lengthy, the server
URL may not be available for several minutes.

If your application has a Taipy user interface, you can connect to it at `http://0.0.0.0:5000`.

You can clean all resources by doing:
```
docker-compose down --volumes --remove-orphans
```
