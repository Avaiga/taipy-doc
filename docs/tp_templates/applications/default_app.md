Building a Taipy application can require a good amount of time and effort, in particular at the
beginning of a project. This can delay the time-to-market and increase development costs.

To reduce the development time, Taipy provides a simple and minimal application template which let
you create a custom application that just works out-of-the-box with a few questions.

<figure>
  <img src="../img/default_app_template_with_auth_dark.jpg" class="visible-dark" />
  <img src="../img/default_app_template_with_auth_light.jpg" class="visible-light"/>
  <figcaption>A multi-page Taipy application with authentication created by the default application template out-of-the-box</figcaption>
</figure>

This default template offers several key benefits:

- **Ease of Use**: The template is designed to be user-friendly, with a simple CLI
    interface that guides developers through the application creation process.
- **Comprehensive Features**: The template supports a wide range of functionalities, including
    multi-page support, authentication, scenario management, Rest API, Git and Docker support.
- **Accelerated Development**: By leveraging the wide range of features provided by the template,
    developers can quickly bootstrap a standard application, saving significant development time to
    focus on delivering business value more efficiently.
- **Customization**: The template provides high flexibility and customization options on application
    creation. The resulting application is also highly customizable with placeholders, allowing
    developers to tailor the application to meet specific requirements and use cases.
- **Deployment-Ready**: With support for Git and Docker, the template provides helpers for both
    development and production environments.

# How to create an application

As its name suggests, the default template is used if no template name is provided. To create the
application from the default template, change to the folder in which you want to create the
application and run `taipy create` (or `taipy create --application default`) from the CLI. Then
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

??? info "Default answers"

    In the CLI, the default answer for each question is displayed in the square brackets.
    You can provide an answer or press Enter to use the default value.

Each question in the CLI corresponds to a specific aspect of the application. The following
sections describe each question in detail.

!!! note "Available in Taipy Enterprise edition"

    Questions 5 and 9 are only relevant to the [Taipy Enterprise Edition](https://taipy.io/enterprise)

    [Contact us](https://taipy.io/book-a-call){: .tp-btn .tp-btn--accent target='blank' }

## 1. Application root folder

- Specifies the root folder of the application.
- The default value is "taipy_application".

## 2. Application main Python file

- Sets the name of the main Python file (entry point) of the application.
- The default value is "main.py".

## 3. Application title

- Specifies the title displayed in the web application.
- The default value is "Taipy Application".

## 4. With multi-pages

- Specifies whether the application is a single-page or multi-page.
- For a multi-page application, enter the page names separated by spaces. If left blank, the
  application will default to single page.
    - The page names must be valid Python identifiers.
    - Once the application is created, all pages will be created in the `pages` folder as empty
      pages. You can add content to the pages as needed.
- The default value is an empty string, which creates a single-page application.

## 5. With Authentication

- Indicates whether the application includes authentication.
- If yes, a login page and a basic setup for for configuring authentication will be included
  in the application.
    - A login page will be created at `pages/login.py`, which uses the
      [Taipy login control](../../refmans/gui/viselements/generic/login.md).
    - A basic authentication configuration will be added to the `configuration/auth_config.py` file.
      By default, the authentication will use the
      [Taipy protocol](../../userman/advanced_features/auth/authentication.md#taipy-protocol).
      You can customize the authentication method as needed.
- The default value is "No".

## 6. With scenario management

- Specifies whether the application uses scenario management.
- If yes:
    - The Taipy `Orchestrator^` service will be included to handle job orchestration and version
      management.
    - A scaffold configuration file will be created at `configuration/config.py`. You can put your
      application's configuration here and it will be imported to the main application file.
    - A scaffold `algorithms/algorithms.py` file will be created, which is designed to contain the
      various Python functions used to configure tasks. You can add your tasks' functions here and
      they will be imported to the main application file.
- The default value is "No".

## 7. With a Rest API

- Specifies whether the application uses Taipy Rest.
- If yes, the Taipy `Rest^` service will be included in the application.
- The default value is "No".

## 8. With a new Git repository

- Specifies whether the application will be initialized as a new Git repository.
- The default value is "No".

## 9. With Docker deployment

- Specifies Docker support for the application.
- Options:
    - "No": No Docker support.
    - "For development": Add a minimal version of `Dockerfile` and `docker-compose.yml` for development.
    - "For production": Add a production-ready `Dockerfile` and `docker-compose.yml`.
- The default value is "No".

# Application description

The generated application has the following folder structure:

```plaintext
taipy_application/
├──── algorithms/
│   ├──── __init__.py
│   └──── algorithms.py
│
├──── configuration/
│   ├──── __init__.py
│   ├──── auth_config.py
│   └──── config.py
│
├──── pages/
│   ├──── __init__.py
│   ├──── admin/
│   ├──── login/
│   ├──── page_custom/
│   └──── root.py
│
├──── docker-compose.yml
├──── Dockerfile
├──── main.py
└──── requirements.txt
```

Your application's folder structure may vary depending on the options you selected during the
creation process. Here is a brief overview of the key components:

- *algorithms/*: Contains the *algorithms.py* file, designed to contain various Python functions
    used to configure tasks for the scenario management feature.
- *configuration/*: Contains the configuration for the application. The configuration will
    be imported to the main application file.
    - *config.py* contains the configuration for the scenario management feature.
    - *auth_config.py* contains the configuration for the authentication feature.
- *pages/*: Contains the application pages if the application is multi-page.
    - *root.py* is the root page of the application, which includes the
        [navigation bar](../../refmans/gui/viselements/generic/navbar.md) visual element.
    - *login/* contains the login page for the authentication feature using the
        [login](../../refmans/gui/viselements/generic/login.md) visual element.
    - *admin/* contains an example admin page for the authentication feature that only authenticated
        users with the "TAIPY_ADMIN" role can access.
- *docker-compose.yml* and *Dockerfile*: The Docker configuration for building and running the
    application as a Docker container.
- *main.py*: The main Python file of the application.
- *requirements.txt*: Contains the Python dependencies required by the application.

# Customizing the application

Everything in the generated application can be updated to precisely fit your needs. It includes
the Python code, the configuration files, placeholders, and any other resources.

## Customizing the scenario management feature

For the scenario management feature, the *algorithms/algorithms.py* file is designed to contain the
various Python functions used to configure tasks. The functions are strongly use-case dependent, for
example, cleaning data, performing analysis, or running simulations, among other tasks.

Edit the placeholder functions with your specific functions. The functions will be imported by the
*algorithms/\_\_init\_\_.py* file.

```python title="algorithms/algorithms.py"
def clean_data(df, replacement_type):
    df = df.fillna(replacement_type)
    return df
```

The *configuration/config.py* file is designed to contain the configuration of the application.
Import the functions from the *algorithms* folder and edit the placeholder with your specific
configuration.

```python title="configuration/config.py"
from algorithms import clean_data

from taipy import Config

initial_dataset_config = Config.configure_csv_data_node("initial_dataset", scope=Scope.CYCLE)
replacement_type_config = Config.configure_data_node("replacement_type", default_data="NO VALUE")
cleaned_dataset_config = Config.configure_csv_data_node("cleaned_dataset")
clean_data_task_config = Config.configure_task(
    "clean_data",
    function=clean_data,
    input=[initial_dataset_config, replacement_type_config],
    output=cleaned_dataset_config,
)
scenario_config = Config.configure_scenario("scenario_configuration", task_configs=[clean_data_task_config])
```

For more information about configuring scenarios, please refer to
[Data node config](../../userman/scenario_features/data-integration/data-node-config.md) and
[Scenario config](../../userman/scenario_features/task-orchestration/scenario-config.md).

The configuration can then be imported to the main application file. Uncomment the placeholder in
the main file to use the configuration for the scenario management feature.

```python title="main.py"
    ...
    orchestrator = Orchestrator()
    orchestrator.run()
    # #############################################################################
    # PLACEHOLDER: Create and submit your scenario here                           #
    #                                                                             #
    # Example:                                                                    #
    # from configuration import scenario_config                                   #
    # scenario = tp.create_scenario(scenario_config)                              #
    # scenario.submit()                                                           #
    # Comment, remove or replace the previous lines with your own use case        #
    # #############################################################################
```

## Customize the authentication feature

For the authentication feature, the *configuration/auth_config.py* file is designed to contain the
configuration of the authentication protocol.

By default, the authentication will use the
[Taipy protocol](../../userman/advanced_features/auth/authentication.md#taipy-protocol). You can
customize the authentication protocol by editing the placholder list of users and roles, or use a
different supported protocols.

The role required to access the admin page is defined by the `admin_page_filter` variable by the
`AnyOf^` filter.

## Customizing the pages

If the application is single-page, the homepage content is in the main Python file. You can edit
the content of the homepage placeholder to fit your specific application requirements.

If the application is multi-page, the *pages/* folder contains the application pages. You can
customize the content of each page:

- *pages/root.py* is the root page of the application. Here, you can customize the navigation bar
    of the application with the [navbar](../../refmans//gui/viselements/generic/navbar.md) visual
    element.
- For the authentication feature, *pages/login/* contains the login page for the authentication
    feature, and *pages/admin/* contains the page that only authenticated users with the
    "TAIPY_ADMIN" role can access. You can customize the login page with the
    [login](../../refmans/gui/viselements/generic/login.md) visual element.
- If you provide an answer to the [question 4](#4-with-multi-pages), the pages you specified will
    be created in the *pages/* folder and are imported automatically in the *pages/\_\_init\_\_.py*
    file. You can customize the content of each page as needed.

# How to run the application

To run the application, change to the newly created folder and run the application using the
`taipy run main.py` command.

```console
$ cd ./taipy_application
$ taipy run main.py
```

If the newly created application supports Docker, you can also run the application using the
`docker-compose` command.

```console
$ cd ./taipy_application
$ docker-compose up --build -d
```

You can now access the application in your browser at `http://localhost:5000`.
