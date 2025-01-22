Taipy default application template is a simple, minimal template that lets you create a custom Taipy
application with a few questions.

## Create a Taipy application from the default template

To create an application from the Taipy default application template, run `taipy create` from the
CLI or specify the application template name by running `taipy create --application default`, then
answer a few questions to customize your application.

```console
$ taipy create --application default
[1/9] Application root folder [taipy_application]:
[2/9] Application main Python file [main.py]:
[3/9] Application title [Taipy Application]:
[4/9] With multi-pages?
        Enter the page names separated by a space ():
[5/9] With Authentication? (No):
[6/9] With scenario management? (No):
[7/9] With a Rest API? (No):
[8/9] With a new Git repository? (No):
[9/9] Select With Docker deployment
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

    Questions 5 and 9 are only relevant to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

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
4. "With multi-pages"
    - Specifies whether the application is a single-page or multi-page.
    - For a multi-page application, enter the page names separated by spaces. If left blank, the
    application will default to single page.
    - The names must be valid Python identifiers.
5. "With Authentication"
    - Indicates whether the application includes authentication.
    - If yes, a login page and a basic setup for for configuring authentication will be included
    in the application.
    - The default value is "No".
6. "With scenario management"
    - Specifies whether the application uses scenario management.
    - If yes, the `Orchestrator^` service will be included to handle job orchestration and version management.
    - The default value is "No".
7. "With a Rest API":
    - Specifies whether the application uses Taipy Rest.
    - If yes, the Taipy Rest API service will be included in the application.
    - The default value is "No".
8. "With a new Git repository":
    - Specifies whether the application will be initialized as a new Git repository.
    - The default value is "No".
9. "With Docker deployment"
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
