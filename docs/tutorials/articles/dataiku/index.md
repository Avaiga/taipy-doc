---
title: Integration with Dataiku
category: integration
data-keywords: scenario task
short-description: A guide to integrate Dataiku with Taipy.
order: 24
img: dataiku/images/dataiku.png
---

Integrating Dataiku with Taipy enhances your data analysis and processing workflows.
This connection enables users to efficiently handle, analyze, and visualize data from inside
or outside Dataiku.
The guide walks you through setting up your environment, creating an application in Dataiku DSS,
connecting to Dataiku, and fetching data for visualization within Taipy's flexible framework.

By integrating Dataiku projects with Taipy scenarios, you gain streamlined workflows for
data manipulation and scenario management. This involves creating custom functions for
interacting with Dataiku's API to read from and write to datasets, seamlessly blending
Dataiku's data processing capabilities with Taipy's task orchestration and data management.

![Dataiku](images/dataiku.png){width=70% : .tp-image}


# Simple Integration: Visualization

We'll cover how to extract and display
information from Dataiku projects. You'll be able to visualize various data and metrics from your
Dataiku projects. Remember, we'll utilize the `dataiku-api-client` for retrieving information when
building applications outside the Dataiku ecosystem. If you're following the first tutorial, you can
directly use the `dataiku` package.

## Setting Up Your Environment

Start by ensuring that you have the required libraries installed. You'll need
`dataiku-api-client` for accessing Dataiku and `taipy-gui` for building the GUI.
Install these libraries using pip:

```bash
pip install dataiku-api-client taipy
```

## Connecting to Dataiku

**Requirements:**

- A Dataiku Instance.
- A Dataiku Project.
- A knowledge of the Dataiku Python API.

Use the `DSSClient` from the `dataikuapi` package to establish a connection with
your Dataiku instance. Replace `"http://your-dataiku-instance.com"` and
`"your_api_key"` with your actual Dataiku host and API key.

```python
from dataikuapi import DSSClient

host = "HOST"
apiKey = "your_api_key"

client = DSSClient(host, apiKey)
```

## Retrieving Data from Dataiku

Fetch data from your Dataiku projects by iterating through the projects and
collecting relevant metrics for each model. This example code retrieves metrics like
AUC and organizes them into a `pandas.DataFrame`.

```python
metrics_table = []
for project_keys in client.list_project_keys():
    project = client.get_project(project_keys)
    project_label = project.get_metadata()["label"]
    for model_id in project.list_saved_models():
        model = project.get_saved_model(model_id["id"])
        try:
            active_id = model.get_active_version().get("id", None)
            metrics = model.get_metric_values(active_id)
            for metric in metrics.raw['metrics']:
                value = metric['lastValues'][0]['value']
                metrics_table.append({'Project': project_label,
                                        'ModelId': model_id['id'],
                                        'ActiveId': active_id,
                                        'MetricType': metric['metric']['metricType'],
                                        'Value': value})
        except Exception as e:
            print(e)
            pass

metrics_df = pd.DataFrame(metrics_table)
```

## Preparing Data for Visualization

Before visualization, you may need to prepare your data further. For instance, you
can concatenate certain columns to form a unique identifier or name for each entry.
Here, we add a 'Name' column to our DataFrame.

```python
metrics_df['Name'] = metrics_df[['Project', 'ModelId', 'MetricType']].agg(' - '.join, axis=1)
```

## Creating a Taipy Application

Create your own Taipy application to visualize all this information. It can
include dynamic selectors for projects and metrics, a table to display
data, and a bar chart for visualizing metric values.


=== "Python"
    ```python
    from taipy.gui import Gui
    import taipy.gui.builder as tgb

    selected_projects = list(metrics_df['Project'].unique())
    selected_metrics = ["AUC"]  # Initially focusing on AUC metrics.

    def show_projects(metrics_df, selected_projects, selected_metrics):
        return metrics_df[(metrics_df['Project'].isin(selected_projects)) &
                        (metrics_df['MetricType'].isin(selected_metrics))]

    with tgb.Page() as page:
        tgb.text("# Dataiku **Overview**", mode="md")

        tgb.text("**Projects**", mode="md")

        tgb.selector(
            "{selected_projects}",
            lov=list(metrics_table["Project"].unique()),
            multiple=True,
            label="Projects",
            dropdown=True,
            class_name="fullwidth",
        )

        tgb.text("**Metrics**", mode="md")

        tgb.selector(
            "{selected_metrics}",
            lov=list(metrics_table["MetricType"].unique()),
            multiple=True,
            label="Metrics",
            dropdown=True,
            class_name="fullwidth",
        )

        tgb.table(
            lambda metrics_table, selected_projects, selected_metrics: show_projects(
                metrics_table, selected_projects, selected_metrics
            ),
            filter=True,
        )

        tgb.chart(
            lambda metrics_table, selected_projects, selected_metrics: show_projects(
                metrics_table, selected_projects, selected_metrics
            ),
            x="Name",
            y="Value",
            type="bar",
        )

    Gui(md).run()
    ```

    [Download the code](./src/metrics_visualization_tgb.py){: .tp-btn target='blank' }
=== "Markdown"
    ```python
    from taipy.gui import Gui

    selected_projects = list(metrics_df['Project'].unique())
    selected_metrics = ["AUC"]  # Initially focusing on AUC metrics.

    def show_projects(metrics_df, selected_projects, selected_metrics):
        return metrics_df[(metrics_df['Project'].isin(selected_projects)) &
                        (metrics_df['MetricType'].isin(selected_metrics))]

    md = """
    # Dataiku **Overview**{: .color-primary}

    **Projects**

    <|{selected_projects}|selector|lov={list(metrics_df['Project'].unique())}|dropdown|multiple|class_name=fullwidth|label=Projects|>

    **Metrics**

    <|{selected_metrics}|selector|lov={list(metrics_df['MetricType'].unique())}|dropdown|multiple|class_name=fullwidth|label=Metrics|>

    <|{show_projects(metrics_df, selected_projects, selected_metrics)}|table|filter|>

    <|{show_projects(metrics_df, selected_projects, selected_metrics)}|chart|x=Name|y=Value|type=bar|>
    """

    Gui(md).run()
    ```

    [Download the code](./src/metrics_visualization.py){: .tp-btn target='blank' }

![Metrics Visualization](images/metrics_visualization.png){width=90% : .tp-image-border}

# Run a Dataiku pipeline from your Taipy application

The integration process involves using Dataiku's Python API to create a bridge
between Taipy and Dataiku, enabling you to trigger scenarios and manage data
workflows within your Taipy application.

Creating and executing projects on Dataiku involves several steps, from setting up
your Dataiku instance to defining and running projects.

**Requirements:**

- A Dataiku Instance.
- A Dataiku Project.
- A Dataiku Scenario that we want to run from a Taipy application
- A knowledge of the Dataiku Python API

**Integrate with Taipy**

- **API Calls or Plugins:** Use Dataiku's API or develop plugins to seamlessly
integrate with Taipy scenarios for job triggering and result retrieval.

By adapting the given Dataiku API script to work with a generic data node in Taipy,
you can define reading and writing functions to interact with Dataiku datasets.
Then, configure a generic data node to use these functions for data handling.

## Custom Dataiku Data Nodes

To adapt the given Dataiku API script to work with a generic data node in a
framework like Taipy, you would first define the reading and writing functions that
interact with your Dataiku datasets. Then, you configure a generic data node to use
these functions for data handling. The concept involves creating custom functions to
interact with Dataiku's API for reading from and writing to datasets, and then
integrating these functions into Taipy's data node configuration.

These functions will be responsible for interfacing with Dataiku's API, similar to
how you directly interacted with the Dataiku datasets in the original script.

```python
from dataikuapi import DSSClient
import pandas as pd

# Create your own read function for your data or use this one
def read_data_from_dataiku(dataset_name, project_key, host, api_key):
    """
    Fetches a dataset from Dataiku DSS and returns it as a pandas DataFrame.

    It checks if a cached version of the dataset exists and is up-to-date before
    fetching data from Dataiku DSS. If the cached version is outdated or nonexistent,
    it fetches the data, updates the cache, and then returns the data.

    Parameters:
    - dataset_name: Name of the dataset to fetch.
    - project_key: Key of the project containing the dataset.
    - host: URL of the Dataiku DSS instance.
    - api_key: Authentication API key for Dataiku DSS.

    Returns:
    - A pandas DataFrame containing the dataset.
    """
    cache_path = f"{cache_dir}/{dataset_name}.csv"
    try:
        client = DSSClient(host, api_key)
        project = client.get_project(project_key)
        dataset = project.get_dataset(dataset_name)
        last_modified_on = dataset.get_info().info.get('timeline', {}).get('lastModifiedOn', 0)

        # Convert to datetime for comparison
        last_modified_datetime = pd.to_datetime(last_modified_on, unit='ms')

        # Check cache validity
        cache_is_valid = os.path.exists(cache_path) and \
            tp.get_entities_by_config_id(dataset_name+'_dataiku')[0].last_edit_date > last_modified_datetime

        if cache_is_valid:
            print(f"Reading {dataset_name} from cache.")
            return pd.read_csv(cache_path)

        # Fetching data from Dataiku
        columns = [column['name'] for column in dataset.get_schema()['columns']]
        data_list = list(dataset.iter_rows())
        data = pd.DataFrame(data=data_list, columns=columns)

        # Updating cache
        os.makedirs(cache_dir, exist_ok=True)
        data.to_csv(cache_path, index=False)
        print(f"Data for {dataset_name} fetched and cached.")
    except Exception as e:
        print(f"Error fetching {dataset_name} from Dataiku DSS: {e}")
        data = pd.DataFrame()  # Return an empty DataFrame in case of error

    return data


# Create your own write function for your data or use this one
def write_data_to_dataiku(data, dataset_name, project_key, host, api_key):
    """
    Writes data from a pandas DataFrame to a specified Dataiku DSS dataset.

    This function checks if the columns in the DataFrame match the target dataset's schema.
    If they match, it updates the dataset with the new data. If not, it prints a warning.

    Parameters:
    - data: pandas DataFrame containing the data to write.
    - dataset_name: Name of the dataset to update.
    - project_key: Key of the project containing the dataset.
    - host: URL of the Dataiku DSS instance.
    - api_key: Authentication API key for Dataiku DSS.
    """
    cache_path = f"{cache_dir}/{dataset_name}.csv"
    try:
        client = DSSClient(host, api_key)
        project = client.get_project(project_key)
        dataset = project.get_dataset(dataset_name)
        target_cols = [column['name'] for column in dataset.get_schema()['columns']]
        new_cols = list(data.columns)

        # Ensure column names in DataFrame match the target dataset schema
        if set(target_cols) == set(new_cols):
            os.makedirs(cache_dir, exist_ok=True)
            data.to_csv(cache_path, index=False)

            with open(cache_path, "rb") as fp:
                try:
                    # Attempt to clear the dataset and upload new file
                    dataset.clear()
                    dataset.uploaded_add_file(fp, f"{dataset_name}.csv")
                    print(f"Data successfully written to {dataset_name} in Dataiku DSS.")
                except Exception as e:
                    print(f"Failed to upload data to {dataset_name}: {e}")
        else:
            print("Column mismatch: The columns in the DataFrame do not match the target dataset's schema.")
    except Exception as e:
        print(f"An error occurred while processing {dataset_name}: {e}")

```

Now, it's time to set up your data nodes from these custom functions.
This enablies a better integration of Taipy's scenarios and data management
capabilities with Dataiku. This setup empowers you to read and write data
efficiently, track changes, and use the data node with pipelines crucial for
your application.

```python
from taipy import Config, Scope
import os

cache_dir = ".cache_dataiku"
os.makedirs(cache_dir, exist_ok=True)

# Configuration Constants
HOST = "HOST"
API_KEY = "API"
PROJECT_KEY = "PROJECT_KEY"
SCENARIO_ID = "SCENARIO_ID"
INPUT_DATASET_NAME = "input"
OUTPUT_DATASET_NAME = "output"

response_cfg = Config.configure_data_node(id="response")

# Taipy Configuration for Dataiku integration
input_dataiku_cfg = Config.configure_generic_data_node(
    id=INPUT_DATASET_NAME + "_dataiku",
    read_fct=read_data_from_dataiku,
    read_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=write_data_to_dataiku,
    write_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    scope=Scope.GLOBAL
)

output_dataiku_cfg = Config.configure_generic_data_node(
    id=OUTPUT_DATASET_NAME + "_dataiku",
    read_fct=read_data_from_dataiku,
    read_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=write_data_to_dataiku,
    write_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    scope=Scope.GLOBAL
)
```

## Triggering Dataiku scenarios

With data nodes handling data autonomously, tasks now focus on action triggers, such
as starting Dataiku scenarios. Let's assume we have a function
`trigger_dataiku_scenario` that initiates a specific scenario within a Dataiku
project:

```python
def run_dataiku_scenario():
    """Executes a specified Dataiku scenario."""
    try:
        client = DSSClient(HOST, API_KEY)
        project = client.get_project(PROJECT_KEY)
        scenario = project.get_scenario(SCENARIO_ID)
        scenario.run_and_wait()
        return scenario
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
```

Configure a Taipy task that uses these data nodes and triggers the Dataiku scenario:

```python
# Task configuration to trigger a Dataiku scenario
trigger_scenario_task_cfg = Config.configure_task(
    id="trigger_dataiku_scenario_task",
    function=run_dataiku_scenario,
    input=[],
    output=[response_cfg]
)
```

## Configuring the Scenario

Now, encapsulate the task within a scenario configuration to define a complete
scenario, including data preparation, triggering the Dataiku scenario, and
post-processing:

```python
# Scenario configuration incorporating the Dataiku scenario trigger task
dataiku_scenario_cfg = Config.configure_scenario(
    id="dataiku_scenario",
    task_configs=[trigger_scenario_task_cfg],
    additional_data_node_configs=[input_dataiku_cfg, output_dataiku_cfg]
)
```

This scenario outlines a scenario where Taipy manages the overall process,
including the initiation of Dataiku scenarios, with data nodes autonomously handling
data exchanges with Dataiku.

## Execution: Bringing It All Together

To execute the scenario, use Taipy's execution model. This initiates the configured
scenario, including autonomous data exchange with Dataiku and triggering the
specified scenario:

=== "Python"
    ```python
    import taipy as tp

    # Create and execute the scenario
    if __name__ == "__main__":
        tp.Orchestrator().run()
        scenario = tp.create_scenario(dataiku_scenario_scenario_cfg)

        scenario = None
        with tgb.Page() as scenario_page:
            with tgb.layout("1 1"):
                tgb.scenario_selector("{scenario}")
                tgb.scenario("{scenario}")
            tgb.job_selector()

            with tgb.layout("1 1"):
                with tgb.part():
                    tgb.text("Input Dataset:")
                    tgb.data_node("{scenario.input_dataiku if scenario else None}")
                with tgb.part():
                    tgb.text("Output Dataset:")
                    tgb.data_node("{scenario.output_dataiku if scenario else None}")

            tgb.scenario_dag("{scenario}")


        tp.Gui(scenario_page).run()
    ```

    [Download the code](./src/scenario_dataiku_tgb.py){: .tp-btn target='blank' }

=== "Markdown"
    ```python
    import taipy as tp

    # Create and execute the scenario
    if __name__ == "__main__":
        tp.Orchestrator().run()
        scenario = tp.create_scenario(dataiku_scenario_scenario_cfg)

        scenario = None
        scenario_md = """
    <|1 1|layout|
    <|{scenario}|scenario_selector|>

    <|{scenario}|scenario|>
    |>

    <|job_selector|>

    <|1 1|layout|
    Input Dataset:
    <|{scenario.input_dataiku if scenario else None}|data_node|>

    Output Dataset:
    <|{scenario.output_dataiku if scenario else None}|data_node|>
    |>

    <|{scenario}|scenario_dag|>
    """

        tp.Gui(scenario_md).run()
    ```

    [Download the code](./src/scenario_dataiku.py){: .tp-btn target='blank' }

![Dataiku Scenario](images/scenario_dataiku.png){width=90% : .tp-image-border}

This approach, where tasks focus on action triggers (like starting
Dataiku scenarios) while data nodes manage data reading and writing, enhances the
interaction between the end user and its data and models.


# Taipy Application in Dataiku DSS

We'll begin by developing an application directly within Dataiku DSS. This approach allows you to
utilize the comprehensive dataiku package, packed with powerful features, and seamlessly integrate
your Taipy application into your existing ecosystem.

!!! warning "Taipy Application in Dataiku DSS"
    This has some limitations when it comes to publishing the application as a web
    app. Creating a web application through Code Studio sometimes results in an
    unexpected failure.

## Prerequisites:
- Ensure that [Code Studios](https://knowledge.dataiku.com/latest/code/work-environment/tutorial-first-code-studio.html) is enabled for your instance.
- You must have a [Code Environment](https://doc.dataiku.com/dss/latest/code-envs/index.html) with Taipy installed and Python version 3.9 or higher.

## Step-by-Step Guide:

First, log in to your Dataiku DSS instance and create a new project or enter an existing project.

### Create a new "Code Studio"

- Navigate to "Code Studios"

![Step 3 Image](images/code_studio.png){width=50% : .tp-image-border}


- Click on "+ NEW CODE STUDIO".

- Follow the link in the description for templates.

![Step 4 Image](images/new_code_studio.png){width=50% : .tp-image-border}

### Add a template to Code Studio:

- Create a new template by clicking on "+ CREATE CODE STUDIO TEMPLATE".

You can either name your new template or import one using the dropdown arrow next to the button.

- Configure your Code Studio:

   - Go to "Definition".

    ![Definition](images/definition.png){width=90% : .tp-image-border}

   - Add three blocks:

     - **Code Environment**: Select the Code Environment where Taipy is installed.

     - **Visual Studio Code**: Enable the "Launch for Webapps" option.

     - **Entrypoint**: Add a label (e.g., "taipy"), enable both "Launch for Webapps" and "Expose port".

     Specify an "Exposed port label" (e.g., "taipy") and the exposed port (5000, the default port for Taipy).

   ![Step 6 Image](images/blocks.png){width=90% : .tp-image-border}

- Save and Build your template

Then, return to Code Studios to create a Code Studio using this template, which should now appear in the list.

### Use the template in your Code Studio

- Launch the studio and begin creating your first Taipy application.

- In the run settings, use:

```python
<Gui>.run(..., base_url="/code-studios/<PROJECT_NAME>/<CODE_STUDIO_ID>/<EXPOSED_PORT>/")
```

The exposed port should be 5000, as set in the Entrypoint block. You can find these details easily in the URL:

![URL Details Image](images/url_details_image.png){width=90% : .tp-image-border}

### Access your application

- Navigate to the Taipy tab in Code Studio.

![Application Tab Image](images/application_tab_image.png){width=90% : .tp-image-border}

- Refresh the port and you should see your application live.

![Application Refresh](images/application_resfresh.png){width=90% : .tp-image-border}

In conclusion, integrating Dataiku with Taipy provides a powerful
solution for data processing, visualization, and scenario orchestration.
By leveraging Taipy's scenario management and Dataiku's robust capabilities,
organizations can enhance efficiency, scalability, and collaboration in their data
scenarios. This integration enables seamless interaction between Dataiku
projects and Taipy, facilitating the creation and scalability data-driven
applications.
