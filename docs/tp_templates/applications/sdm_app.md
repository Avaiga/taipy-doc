The scenario management template provides a foundational structure for applications requiring
scenario-based analysis and data management. It's designed to help users create, manage, and
compare different scenarios to facilitate decision-making and what-if analyses. It is ideal for
applications in forecasting, simulation, and optimization, where multiple scenarios need to be
evaluated and compared.

Out of the box, the template provides a multi-page application structure with two pages predefined:

- A scenario page to select, visualize, submit, analyze, and manage scenarios and data nodes.
- A job page to monitor and manage submissions and jobs.

<figure>
  <img src="../img/sdm_app_template_with_scenario_dark.jpeg" class="visible-dark" />
  <img src="../img/sdm_app_template_with_scenario_light.jpeg" class="visible-light"/>
  <figcaption>Out-of-the-box Taipy scenario management application</figcaption>
</figure>

The application also includes a job monitoring page to track the status of the submitted jobs.

<figure>
  <img src="../img/sdm_app_template_with_job_dark.jpeg" class="visible-dark" />
  <img src="../img/sdm_app_template_with_job_light.jpeg" class="visible-light"/>
  <figcaption>Manage jobs with the Taipy scenario management application</figcaption>
</figure>

The template provides support for a wide range of functionalities, including:

- Multi-page application structure
- Authentication support
- Scenario management
- Job monitoring
- Git repository setup
- Docker setup

# How to create an application

To create the application from the scenario management template, change to the folder in which
you want to create the application and run the command `taipy create --application sdm`. Then answer
a few questions to customize your application.

```console
$ taipy create --application sdm
[1/7] Application root folder [taipy_application]:
[2/7] Application main Python file [main.py]:
[3/7] Application title [Taipy Application]:
[4/7] With TOML Config? (No):
[5/7] With Authentication? (No):
[6/7] With a new Git repository? (No):
[7/7] Select With Docker deployment
    1 - No
    2 - For development
    3 - For production
    Choose from [1/2/3] (1):
The new Taipy application has been created at taipy_application

To start the application, change directory to the newly created folder:
    cd taipy_application

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

1. Application root folder

- Specifies the root folder of the application.
- The default value is "taipy_application".

2. Application main Python file

- Sets the name of the main Python file (entry point) of the application.
- The default value is "main.py".

3. Application title

- Specifies the title displayed in the web application.
- The default value is "Taipy Application".

4. With TOML Config

- Specifies whether the application uses TOML configuration files, otherwise the configuration
  is in generated in a Python script file.
- The default value is "No".

5. With Authentication

- Indicates whether the application includes authentication.
- If the answer is "yes" or "y", a login page and a basic setup for configuring authentication is included
  in the application.
    - A login page is created in `pages/login.py`, which uses the
      [Taipy login control](../../refmans/gui/viselements/generic/login.md).
    - A basic authentication configuration is added to the `configuration/auth_config.py` file.
      By default, the authentication uses the
      [Taipy protocol](../../userman/advanced_features/auth/authentication.md#taipy-protocol).
      You can customize the authentication method as needed.
- The default value is "No".

6. With a new Git repository

- Specifies whether the application directory should be initialized as a new Git repository.
- The default value is "No".

7. With Docker deployment

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
├──── algos/
│   ├──── __init__.py
│   └──── algos.py
│
├──── config/
│   ├──── __init__.py
│   ├──── auth_config.py
│   └──── config.py
│
├──── pages/
│   ├──── __init__.py
│   ├──── job_page/
│   ├──── scenario_page/
│   └──── root.py
│
├──── .taipyignore
├──── .gitignore
├──── docker-compose.yml
├──── Dockerfile
├──── main.py
└──── requirements.txt
```

Your application's folder structure may vary depending on the options you selected during the
creation process. Here is a brief overview of the folder structure:

- `algos/`: Contains the `algos.py` file, designed to contain various Python functions used to
    configure tasks.
- `config/`:
    - `config.py` contains the configuration for the application.
    - `auth_config.py` contains the configuration for the authentication feature.
- `pages/`: Contains the application pages.
    - `root.py` is the root page of the application, which layouts the application.
        It includes a navigation bar, and a sidebar with the
        [scenario_selector](../../refmans/gui/viselements/corelements/scenario_selector.md) and
        [data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md)
        visual elements.
    - `job_page/` contains the page for job monitoring using the
        [job_selector](../../refmans/gui/viselements/corelements/job_selector.md) visual element.
    - `scenario_page/` contains the page for scenario analysis and data management. It
        shows a scenario, its DAG, and its data nodes. It uses the
        [scenario](../../refmans/gui/viselements/corelements/scenario.md), the
        [scenario_dag](../../refmans/gui/viselements/corelements/scenario_dag.md)
        and the [data_node](../../refmans/gui/viselements/corelements/data_node.md)
        visual elements.
- `.taipyignore`: Specifies files to be protected when running the web server. Please refer to the
    [Protect private files](../../userman/run-deploy/run/protect_files.md) page for more
    information.
- `docker-compose.yml` and `Dockerfile`: The Docker configuration for building and running the
    application as a Docker container.
- `main.py`: The main Python file of the application.
- `requirements.txt`: Contains the Python dependencies required by the application.

# How to customize the application

Everything in the generated application can be updated to fit your needs. It includes
the Python code, the configuration files, and any other resources. Specifically, in
the `algos/` and `config/` folders, there are placeholders that you can customize
precisely to your use case.

## Tasks' functions

The `algos/` folder contains the `algos.py` file, designed to contain various Python
functions used to configure tasks. The functions are strongly use-case dependent,
for example, cleaning data, performing analysis, or running simulations, among other
tasks.

In the `algos.py` file, the *clean_data()* function is provided as a placeholder. You can
edit or replace the function body and add your tasks' functions here.

```python title="algos/algos.py"
def clean_data(df, replacement_type):
    df = df.fillna(replacement_type)
    return df

def analyze_data(df):
    ...
    return analysis_results
```

To configure tasks using these functions, make sure to update the import statements in
the `algos/\_\_init\_\_.py` file.

```python title="algos/__init__.py"
from .algos import clean_data, analyze_data
```

Then when [customizing the configuration](#configuration), you can
import these functions and use them to configure various tasks for your application.

??? note "Renaming generated folders or files"

    If you decide to rename the `algos.py` file or the `algos/` folder, make sure to
    update the import statements in the `algos/\_\_init\_\_.py` file and any other
    import statements.

## Configuration

The `config/config.py` file contains the *configure()* function, which is called in the main
application file to configure the application.

If your answer to the ["With TOML Config"](#4-with-toml-config) question is "No"
(the default), the placeholder configuration is stored in the *configure()* function
[as Python code](../../userman/advanced_features/configuration/advanced-config.md#python-code-configuration).
Import the added functions from the `algos/algos.py` file and use them to configure the tasks.

```python title="config/config.py"

from algos import clean_data, analyze_data

def configure():
    ...
```

If your answer to the ["With TOML Config"](#4-with-toml-config) question is "Yes" or "y",
the placeholder configuration is stored in `config.toml` file. Update the
`config.toml` file to configure the application to your specific use case, or you can
use [Taipy Studio](../../userman/ecosystem/studio/index.md) for generating a TOML
file that can be loaded in the *configure()* function.

!!! note "Loading the TOML configuration"

    If you have a different name for the TOML file, make sure to update the file name in the
    *configure()* function.

## Authentication

For the authentication feature, the `config/auth_config.py` file is designed to contain the
configuration of the authentication protocol.

By default, the authentication uses the
[Taipy protocol](../../userman/advanced_features/auth/authentication.md#taipy-protocol). You can
customize the authentication protocol by editing the placeholder list of users and roles, or use a
different supported protocols.

The role required to access the admin page is defined by the *admin_page_filter* filter variable
which is a `AnyOf^` instance. By default, the *filters* only allow "TAIPY_ADMIN" role to access the
admin page. You can customize the filter to allow other roles to access the admin page.

```python title="config/auth_config.py"

...
admin_page_filter = AnyOf(filters=["TAIPY_ADMIN"], success="admin", failure="login")
```

## Pages

The `pages/` folder contains the application pages. You can customize the
content of the pages to fit your specific requirements, as well as customize
the grid layout of the application and the visual elements.

`pages/root.py` defines the layout of the application, including the navigation bar,
and a sidebar. Here, you can customize the [layout](../../refmans//gui/viselements/generic/layout.md),
the [scenario_selector](../../refmans/gui/viselements/corelements/scenario_selector.md), and
the [data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md).

In `pages/job_page/job_page.py`, you can customize the
[job_selector](../../refmans/gui/viselements/corelements/job_selector.md) visual element, which
lists all jobs of the application and allows users to select and manage them.

In `pages/scenario_page/scenario_page.py`, you can customize the
[scenario](../../refmans/gui/viselements/corelements/scenario.md),
the [scenario_dag](../../refmans/gui/viselements/corelements/scenario_dag.md), and the
[data_node](../../refmans/gui/viselements/corelements/data_node.md) visual elements to display
the information of the selected scenario and data node, as well as modifying the
*notify_on_submission()* function to handle the notification of a scenario's submission.

# How to run the application

To run the application, change to the newly created folder and run the application using
`taipy run main.py`.

```console
$ cd taipy_application
$ taipy run main.py
```

If the newly created application supports Docker, you can also run the application using `docker-compose`.

```console
$ cd taipy_application
$ docker-compose up --build -d
```

You can now access the application in your browser at `http://localhost:5000`.
