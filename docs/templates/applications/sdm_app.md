Taipy's scenario management application template lets you scaffold a custom Taipy
application using scenario management capabilities. It uses
[a scenario selector](./../../../refmans/gui/viselements/corelements/scenario_selector.md)
to allow end users to create, manage, and run scenarios directly from the GUI page.

# Create a Taipy application from the scenario management template

To create an application from the Taipy scenario management application template, run
`taipy create --application sdm` from the CLI, then answer a few questions to customize your application.

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

!!! info

    In the CLI, the default value for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

!!! note "Available in Taipy Enterprise edition"

    Questions 6 is only relevant to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

Each question in the CLI corresponds to a specific aspect of the application:

1. "Application root folder":
    - Specifies the root folder of the application.
    - The default value is "new_application".
2. "Application main Python file"
    - Sets the name of the main Python file (entry point) of the application.
    - The default value is "main.py".
3. "Application title":
    - Specifies the title displayed in the web application.
    - The default value is "Taipy Application".
4. "With TOML Config":
    - Specifies whether the application will use TOML configuration files, otherwise the configuration
        will be in a Python file.
    - The default value is "No".
5. "With a new Git repository":
    - Specifies whether the application will be initialized as a new Git repository.
    - The default value is "No".
6. "With Docker deployment"
    - Specifies Docker support for the application.
    - Options:
        - "No": No Docker support.
        - "For development": Add a minimal version of `Dockerfile` and `docker-compose.yml` for development.
        - "For production": Add a production-ready `Dockerfile` and `docker-compose.yml`.
    - The default value is "No".

## Run the application

To run the application, change to the newly created folder and run the application using `taipy run main.py`.

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
