Taipy's scenario management application template leverages the scenario and data
management visual elements to speed up bootstrapping a standard application. The
resulting application exposes a user interface for scenario creation and management,
data visualization, data analysis, simulation, what-if analysis, and/or job
orchestration monitoring.

# How to create the application

To create the application from the template, change to the folder in which you want to
create the application and run the command `taipy create --application sdm`. Then answer
the few questions to customize your application.

```console
$ taipy create --application sdm
[1/6] Application root folder [taipy_application]:
[2/6] Application main Python file [main.py]:
[3/6] Application title [Taipy Application]:
[4/6] With TOML Config? (No):
[5/6] With a new Git repository? (No):
[6/6] Select With Docker deployment
    1 - No
    2 - For development
    3 - For production
    Choose from [1/2/3] (1):
New Taipy application has been created at ./taipy_application

To start the application, change directory to the newly created folder:
    cd ./taipy_application

You can then run the application as follows:
    taipy run main.py
```

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the application. The following
sections describe each question in detail.

!!! note "Available in Taipy Enterprise edition"

    Questions 6 is only relevant to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

## 1. Application root folder

- Specifies the root folder of the application.
- The default value is "new_application".

## 2. Application main Python file

- Sets the name of the main Python file (entry point) of the application.
- The default value is "main.py".

## 3. Application title

- Specifies the title displayed in the web application.
- The default value is "Taipy Application".

## 4. With TOML Config

- Specifies whether the application will use TOML configuration files, otherwise the configuration
  will be in a Python file.
- The default value is "No".

## 5. With a new Git repository

- Specifies whether the application will be initialized as a new Git repository.
- The default value is "No".

## 6. With Docker deployment

- Specifies Docker support for the application.
- Options:
    - "No": No Docker support.
    - "For development": Add a minimal version of `Dockerfile` and `docker-compose.yml` for development.
    - "For production": Add a production-ready `Dockerfile` and `docker-compose.yml`.
- The default value is "No".

# How to run the application

To run the application, change to the newly created folder and run the application using
`taipy run main.py`.

```console
$ cd ./taipy_application
$ taipy run main.py
```

If the newly created application supports Docker, you can also run the application using `docker-compose`.

```console
$ cd ./taipy_application
$ docker-compose up --build -d
```

You can now access the application in your browser at `http://localhost:5000`.
