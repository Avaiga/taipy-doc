Building a Taipy application with multiple complex scenarios usually requires a significant amount of time and effort. This can delay the time-to-market and increase development costs.

To reduce the developer hours and resources needed, Taipy provides a scenario management application template, which leverages Taipy visual elements to speed up bootstrapping a standard application. This template offers several key benefits:

- **Accelerated Development**: By leveraging scenario and data management visual elements, developers can quickly bootstrap a standard application, saving significant development time to focus on delivering business value more efficiently.
- **Comprehensive Features**: The template supports a wide range of functionalities, including data visualization, data analysis, simulation, what-if analysis, and job orchestration monitoring, providing a comprehensive solution for various use cases.
- **Customization**: The template is highly customizable with pre-built placeholders for various components, allowing developers to tailor the application to meet specific requirements and use cases.
- **Deployment-Ready**: With support for Docker deployment and integration with Taipy Enterprise Edition, the template is suitable for both development and production environments.

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
- The default value is "taipy_application".

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
│   └──── config.py
│
├──── pages/
│   ├──── __init__.py
│   ├──── job_page/
│   ├──── scenario_page/
│   └──── root.py
│
├──── .taipyignore
├──── docker-compose.yml
├──── Dockerfile
├──── main.py
└──── requirements.txt
```

Your application's folder structure may vary depending on the options you selected during the creation process. Here is a brief overview of the key components:

- *algos/*: Contains the *algos.py* file, which is designed to contain various Python functions used to configure tasks. You can add your tasks' functions here, and they will be imported into the main application file.
- *config/*: Contains the *config.py* file, where you can put your application's configuration. The configuration will be imported into the main application file.
- *pages/*: Contains the pages of the application.
    - *root.py* is the root page of the application, which layouts the application, including the navigation bar, and a sidebar that has [scenario_selector](../../refmans/gui/viselements/corelements/scenario_selector.md) and [data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md) visual elements.
    - *job_page/* contains the page for job orchestration management via the [job_selector](../../refmans/gui/viselements/corelements/job_selector.md) visual element.
    - *scenario_page/* contains the page for scenario management that displays the information stored in the selected scenario and the DAG via [scenario](../../refmans/gui/viselements/corelements/scenario.md) and  [scenario_dag](../../refmans/gui/viselements/corelements/scenario_dag.md) visual elements, as well as displays the information for the selected data node via the [data_node](../../refmans/gui/viselements/corelements/data_node.md) visual element.
- *.taipyignore*: Specifies files to be protected when running the web server. Please refer to the [Taipy documentationProtect private files](../../userman/run-deploy/run/protect_files.md) for more information.
- *docker-compose.yml* and *Dockerfile*: The Docker configuration for building the application Docker image.
- *main.py*: The main Python file of the application.
- *requirements.txt*: Contains the Python dependencies required by the application.

# Customize the application

Everything in the generated application can be updated to fit your specific application. This includes the code, configuration files, and any other resources. Specifically, in the **algos/** and **config/** folders, there are placeholders that you can customize precisely to your use case.

<!-- TODO: Explain that some parts are strongly use case dependent and identified as placeholders and are probably a good piece of code to focus on.   -->

## Customizing the tasks' functions

The *algos/* folder contains the *algos.py* file, which is designed to contain various Python functions used to configure tasks. The functions are strongly use-case dependent, for example, cleaning data, performing analysis, or running simulations, among other tasks.

In the *algos.py* file, the `clean_data()` method is provided as a placeholder. You can edit/replace the placeholder method `clean_data()` and add your tasks' functions here.

```python title="algos/algos.py"
def clean_data(df, replacement_type):
    df = df.fillna(replacement_type)
    return df

def analyze_data(df):
    ...
    return analysis_results
```

To configure tasks using these functions, make sure to update the import statements in the *algos/\_\_init\_\_.py* file.

```python title="algos/__init__.py"
from .algos import clean_data, analyze_data
```

Then when [customizing the configuration](#customizing-the-configuration), you can import these functions and use them to configure various tasks for your application.

!!! note "Updating the folder and file names"

    If you decide to rename the *algos.py* file or the *algos/* folder, make sure to update the import statements in the *algos/\_\_init\_\_.py* file and any other import statements.

## Customizing the configuration

The *config/config.py* file contains the `configure()` method, which will be called in the main application file to configure the application.

If your answer to the ["With TOML Config"](#4-with-toml-config) question was "No" (as default), the placeholder configuration will be stored in the `configure()` method [as Python code](../../userman/advanced_features/configuration/advanced-config.md#python-code-configuration). Import the added functions from the *algos/algos.py* file and use them to configure the tasks.

```python title="config/config.py"

from algos import clean_data, analyze_data

def configure():
    ...
```

If your answer to the ["With TOML Config"](#4-with-toml-config) question was "Yes", the placeholder configuration will be stored in `config.toml` file. Update the `config.toml` file to configure the application to your specific use case, or you can use [Taipy Studio](../../userman/ecosystem/studio/index.md) for generating a TOML file that can be loaded in the `configure()` method.

!!! note "Loading the TOML configuration"

    If you have a different name for the TOML file, make sure to update the file name in the `configure()` method.

 Customizing the pages

The *pages/* folder contains the pages of the application. You can customize the content of the pages to fit your specific application requirements, as well as customize the layout and visual elements.

*pages/root.py* defines the layout the application, including the navigation bar, and a sidebar. Here, you can customize the [layout](../../refmans//gui/viselements/generic/layout.md), [scenario_selector](../../refmans/gui/viselements/corelements/scenario_selector.md), and [data_node_selector](../../refmans/gui/viselements/corelements/data_node_selector.md) visual elements to fit your application's design.

In *pages/job_page/job_page.py*, you can customize the [job_selector](../../refmans/gui/viselements/corelements/job_selector.md) visual element, which lists all jobs of the application and allows users to select and manage them.

In *pages/scenario_page/scenario_page.py*, you can customize the [scenario](../../refmans/gui/viselements/corelements/scenario.md), [scenario_dag](../../refmans/gui/viselements/corelements/scenario_dag.md), and [data_node](../../refmans/gui/viselements/corelements/data_node.md) visual elements to display the information of the selected scenario and data node, as well as modifying the `notify_on_submission()` method to handle the notification of a scenario's submission.

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
