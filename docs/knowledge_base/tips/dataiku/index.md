---
title: Integrating Dataiku
category: tips
type: code
data-keywords: scenario task
short-description: A guide to integrate Dataiku with Taipy.
img: dataiku/images/dataiku.png
---

Integration with external platforms is often essential for executing tasks and functions efficiently. This article presents a comprehensive guide on integrating Dataiku with Taipy, a tool for orchestrating tasks and exploring various iterations of business problems. By integrating Dataiku projects with Taipy, users can enhance their data processing and visualization capabilities.

![Dataiku](images/dataiku.png){width=90% : .tp-image}

# Simplified Integration: Streamlining Metric Visualization

## Setting Up Your Environment

Begin by ensuring that you have the required libraries installed. You'll need `dataiku-api-client` for accessing Dataiku and `taipy-gui` for building the GUI. Install these libraries using pip:

```bash
pip install dataiku-api-client taipy pandas
```

## Connecting to Dataiku

Use the `DSSClient` from the `dataikuapi` package to establish a connection with your Dataiku instance. Replace `"http://your-dataiku-instance.com"` and `"your_api_key"` with your actual Dataiku host and API key.

```python
from dataikuapi import DSSClient

host = "http://your-dataiku-instance.com"
apiKey = "your_api_key"

client = DSSClient(host, apiKey)
```

## Retrieving Data from Dataiku

Fetch data from your Dataiku projects by iterating through the projects and collecting relevant metrics for each model. This example code retrieves metrics like AUC and organizes them into a `pandas.DataFrame`.

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
                if metric['metric']['metricType'] == "AUC":
                    value = metric['lastValues'][0]['value']
                    metrics_table.append({'Project': project_label,
                                          'ModelId': model_id['id'],
                                          'ActiveId': active_id,
                                          'MetricType': "AUC",
                                          'Value': value})
        except Exception as e:
            print(e)
            pass

metrics_df = pd.DataFrame(metrics_table)
```

## Preparing Data for Visualization

Before visualization, you may need to further prepare your data. For instance, you can concatenate certain columns to form a unique identifier or name for each entry. Here, we add a 'Name' column to our DataFrame.

```python
metrics_df['Name'] = metrics_df[['Project', 'ModelId', 'MetricType']].agg(' - '.join, axis=1)
```

## Creating and Running a Taipy Application

Define the GUI using Taipy's markdown-like syntax. This GUI will include dynamic selectors for projects and metrics, a table to display data, and a bar chart for visualizing metric values.

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



# Dataiku Projects with Taipy Scenarios

## Scenarios and Dataiku Integration

Creating and executing projects on Dataiku involves several steps, from setting up your Dataiku instance to defining and running projects. Here's a step-by-step guide on how to seamlessly integrate Dataiku projects with Taipy scenarios:

**Requirements:**

- A Dataiku Instance.

**1 - Create a Dataiku Project**

- **Navigate to Dataiku DSS:** Access the dashboard where you want to create the project.

- **Create a Project:** Click on the "New Project" button and select "Create."

- **Define Project Details:** Enter a name for your project and choose the type of project you wish to create (e.g., Visual Analysis, Data Preparation).

**2 - Define Dataiku Project Logic**

- **Prepare the Data:** Create datasets, recipes, and models required for your project in the Flow section.

- **Write Code:** Write code for data processing, analysis, or any other tasks within notebooks or custom recipes.

Here's an example of how parameters can be used in a Dataiku project to control the workflow and obtain results:

```python
# Assuming a Python code environment in Dataiku
import dataiku
import pandas as pd

# Accessing a dataset
dataset = dataiku.Dataset("my_dataset")
df = dataset.get_dataframe()

# Processing
processed_df = df[df['column'] > 100]  # Example of data processing based on a condition

# Saving results
output_dataset = dataiku.Dataset("processed_dataset")
output_dataset.write_with_schema(processed_df)
```

- **Test in Project:** Ensure that your workflow runs successfully within the project.

**3 - Integrate with Taipy**

- **API Calls or Plugins:** Use Dataiku's API or develop plugins to seamlessly integrate with Taipy scenarios for job triggering and result retrieval.

By adapting the given Dataiku API script to work with a generic data node in Taipy, you can define reading and writing functions to interact with Dataiku datasets. Then, configure a generic data node to use these functions for data handling.

Configure input and output data nodes to handle data exchange with Dataiku:

```python
# Configure input and output data nodes for Dataiku datasets
input_data_node_cfg = Config.configure_generic_data_node(
    id="input_dataiku_dataset",
    read_fct=custom_read_from_dataiku,
    read_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=custom_write_to_dataiku,
    write_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY]
)

output_data_node_cfg = Config.configure_generic_data_node(
    id="output_dataiku_dataset",
    read_fct=custom_read_from_dataiku,
    read_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=custom_write_to_dataiku,
    write_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY]
)
```

### Simplifying the Task: Triggering Dataiku Flows

With data nodes handling data autonomously, tasks now focus on action triggers, such as starting Dataiku flows. Let's assume we have a function `trigger_dataiku_flow` that initiates a specific flow within a Dataiku project:

```python
# Task function to trigger a Dataiku flow
def trigger_dataiku_flow(input_data, output_data):
    # Logic to start a specific flow in Dataiku
    # This could involve API calls to Dataiku to start a job or scenario
    pass
```

Configure a Taipy task that uses these data nodes and triggers the Dataiku flow:

```python
# Task configuration to trigger a Dataiku flow
trigger_flow_task_cfg = Config.configure_task(
    id="trigger_dataiku_flow_task",
    function=trigger_dataiku_flow,
    inputs=[input_data_node_cfg],
    outputs=[output_data_node_cfg]
)
```

### Crafting the Scenario: Orchestrating the Flow

Now, encapsulate the task within a scenario configuration to define a complete workflow, including data preparation, triggering the Dataiku flow, and post-processing:

```python
# Scenario configuration incorporating the Dataiku flow trigger task
dataiku_flow_scenario_cfg = Config.configure_scenario(
    id="dataiku_flow_scenario",
    task_configs=[trigger_flow_task_cfg]
)
```

This scenario outlines a workflow where Taipy manages the overall process, including the initiation of Dataiku flows, with data nodes autonomously handling data exchanges with Dataiku.

### Execution: Bringing It All Together

To execute the scenario, use Taipy's execution model. This initiates the configured workflow, including autonomous data exchange with Dataiku and triggering the specified flow:

```python
import taipy as tp

# Create and execute the scenario
if __name__ == "__main__":
    tp.Core().run()
    scenario = tp.create_scenario(dataiku_flow_scenario_cfg)
    scenario.submit()

    scenario = None
    scenario_md = """
<|{scenario}|scenario_selector|>

Input Dataset:

<|{scenario.input_dataiku_dataset if scenario else None}|data_node|>

Run the scenario:

<|{scenario}|scenario|>
<|{scenario}|scenario_dag|>

View all the information on output dataset here:

<|{scenario.output_dataiku_dataset if scenario else None}|data_node|>
"""

    tp.Gui(scenario_md).run()
```

This streamlined approach, where tasks focus on action triggers (like starting Dataiku flows) while data nodes manage data reading and writing, enhances the interaction between the end user and its data and models.

In conclusion, integrating Dataiku with Taipy provides a powerful solution for streamlining data processing, visualization, and workflow orchestration. By leveraging Taipy's scenario management and Dataiku's robust capabilities, organizations can enhance efficiency, scalability, and collaboration in their data workflows. This integration enables seamless interaction between Dataiku projects and Taipy, facilitating the creation and scalability data-driven applications.
