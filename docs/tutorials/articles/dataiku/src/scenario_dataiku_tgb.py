# Import necessary libraries
from dataikuapi import DSSClient
import pandas as pd
import taipy as tp
from taipy import Config, Scope
import taipy.gui.builder as tgb
import os

cache_dir = ".cache_dataiku"
os.makedirs(cache_dir, exist_ok=True)


# Configuration Constants
HOST = "HOST"
API_KEY = "API_KEY"
PROJECT_KEY = "PROJECT_KEY"
SCENARIO_ID = "SCENARIO_ID"
INPUT_DATASET_NAME = "input"
OUTPUT_DATASET_NAME = "output"


# Custom functions for interacting with Dataiku datasets
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
        last_modified_on = (
            dataset.get_info().info.get("timeline", {}).get("lastModifiedOn", 0)
        )

        # Convert to datetime for comparison
        last_modified_datetime = pd.to_datetime(last_modified_on, unit="ms")

        # Check cache validity
        cache_is_valid = (
            os.path.exists(cache_path)
            and tp.get_entities_by_config_id(dataset_name + "_dataiku")[
                0
            ].last_edit_date
            > last_modified_datetime
        )

        if cache_is_valid:
            print(f"Reading {dataset_name} from cache.")
            return pd.read_csv(cache_path)

        # Fetching data from Dataiku
        columns = [column["name"] for column in dataset.get_schema()["columns"]]
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
        target_cols = [column["name"] for column in dataset.get_schema()["columns"]]
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
                    print(
                        f"Data successfully written to {dataset_name} in Dataiku DSS."
                    )
                except Exception as e:
                    print(f"Failed to upload data to {dataset_name}: {e}")
        else:
            print(
                "Column mismatch: The columns in the DataFrame do not match the target dataset's schema."
            )
    except Exception as e:
        print(f"An error occurred while processing {dataset_name}: {e}")


# Function to run a Dataiku scenario
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


response_cfg = Config.configure_data_node(id="response")

# Taipy Configuration for Dataiku integration
input_dataiku_cfg = Config.configure_generic_data_node(
    id=INPUT_DATASET_NAME + "_dataiku",
    read_fct=read_data_from_dataiku,
    read_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=write_data_to_dataiku,
    write_fct_args=[INPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    scope=Scope.GLOBAL,
)

output_dataiku_cfg = Config.configure_generic_data_node(
    id=OUTPUT_DATASET_NAME + "_dataiku",
    read_fct=read_data_from_dataiku,
    read_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    write_fct=write_data_to_dataiku,
    write_fct_args=[OUTPUT_DATASET_NAME, PROJECT_KEY, HOST, API_KEY],
    scope=Scope.GLOBAL,
)

# Scenario and task configuration in Taipy
trigger_scenario_task_cfg = Config.configure_task(
    id="trigger_dataiku_scenario_task",
    function=run_dataiku_scenario,
    input=[],
    output=[response_cfg],
)

dataiku_scenario_cfg = Config.configure_scenario(
    id="dataiku_scenario",
    task_configs=[trigger_scenario_task_cfg],
    additional_data_node_configs=[input_dataiku_cfg, output_dataiku_cfg],
)


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

# Main execution block with GUI setup
if __name__ == "__main__":
    tp.Orchestrator().run()
    scenario = tp.create_scenario(dataiku_scenario_cfg)
    # Run the GUI
    tp.Gui(scenario_page).run(title="Dataiku Integration")
