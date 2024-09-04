### app/main.py
from pathlib import Path
from typing import Optional

import taipy as tp
from config import scenario_cfg
from taipy.gui import Gui, notify


valid_features: dict[str, list[str]] = {
    "species": ["Adelie", "Chinstrap", "Gentoo"],
    "island": ["Torgersen", "Biscoe", "Dream"],
    "sex": ["Male", "Female"],
}

selected_species = valid_features["species"][0]
selected_island = valid_features["island"][0]
selected_sex = valid_features["sex"][0]

selected_scenario: Optional[tp.Scenario] = None

data_dir = Path(__file__).with_name("data")
data_dir.mkdir(exist_ok=True)


def scenario_on_creation(state, id, payload):
    _ = payload["config"]
    date = payload["date"]
    label = payload["label"]
    properties = payload["properties"]

    # Create scenario with selected configuration
    scenario = tp.create_scenario(scenario_cfg, creation_date=date, name=label)
    scenario.properties.update(properties)

    # Write the selected GUI values to the scenario
    scenario.species.write(state.selected_species)
    scenario.island.write(state.selected_island)
    scenario.sex.write(state.selected_sex.lower())
    output_csv_file = data_dir / f"{scenario.id}.csv"
    scenario.output_csv_path.write(str(output_csv_file))

    notify(state, "S", f"Created {scenario.id}")

    return scenario


def scenario_on_submission_change(state, submittable, details):
    """When the selected_scenario's submission status changes, reassign selected_scenario to force a GUI refresh."""

    state.selected_scenario = submittable


selected_data_node = None

main_md = """
<|layout|columns=1 4|gap=1.5rem|

<lhs|part|
# Spark with **Taipy**{: .color-primary}

## Scenario

<|{selected_scenario}|scenario_selector|on_creation=scenario_on_creation|>

----------

## Scenario info

<|{selected_scenario}|scenario|on_submission_change=scenario_on_submission_change|>

|lhs>

<rhs|part|render={selected_scenario}|

## Selections

<selections|layout|columns=1 1 1 2|gap=1.5rem|

<|{selected_species}|selector|lov={valid_features["species"]}|dropdown|label=Species|>

<|{selected_island}|selector|lov={valid_features["island"]}|dropdown|label=Island|>

<|{selected_sex}|selector|lov={valid_features["sex"]}|dropdown|label=Sex|>

|selections>

----------

## Output

**<|{str(selected_scenario.output.read()) if selected_scenario and selected_scenario.output.is_ready_for_reading else 'Submit the scenario using the left panel.'}|text|raw|class_name=color-primary|>**

## Data node inspector

<|{selected_data_node}|data_node_selector|display_cycles=False|>

**Data node value:**

<|{str(selected_data_node.read()) if selected_data_node and selected_data_node.is_ready_for_reading else None}|>

<br/>

----------

## DAG

<|Scenario DAG|expandable|
<|{selected_scenario}|scenario_dag|>
|>

|rhs>

|>
"""


def on_change(state, var_name: str, var_value):
    if var_name == "selected_species":
        state.selected_scenario.species.write(var_value)
    elif var_name == "selected_island":
        state.selected_scenario.island.write(var_value)
    elif var_name == "selected_sex":
        state.selected_scenario.sex.write(var_value.lower())


if __name__ == "__main__":
    tp.Orchestrator().run()

    gui = Gui(main_md)
    gui.run(title="Spark with Taipy")
