from pathlib import Path
from typing import Optional

import taipy as tp
from config import scenario_cfg
from taipy.gui import Gui, notify
import taipy.gui.builder as tgb


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
with tgb.Page() as page:
    with tgb.layout("1 4", gap="1.5rem"):

        with tgb.part():
            tgb.text("# Spark with **Taipy**", mode="md", class_name="color-primary")
            tgb.text("## Scenario", mode="md")

            tgb.scenario_selector(
                "{selected_scenario}", on_creation=scenario_on_creation
            )

            tgb.html("hr")

            tgb.text("## Scenario info", mode="md")

            tgb.scenario(
                "{selected_scenario}",
                on_submission_change=scenario_on_submission_change,
            )

        with tgb.part(render="{selected_scenario}"):
            tgb.text("## Selections", mode="md")

            with tgb.layout("1 1 1 2", gap="1.5rem"):
                tgb.selector(
                    "{selected_species}",
                    lov=lambda valid_features: valid_features["species"],
                    dropdown=True,
                    label="Species",
                )

                tgb.selector(
                    "{selected_island}",
                    lov=lambda valid_features: valid_features["island"],
                    dropdown=True,
                    label="Island",
                )

                tgb.selector(
                    "{selected_sex}",
                    lov=lambda valid_features: valid_features["sex"],
                    dropdown=True,
                    label="Sex",
                )

            tgb.html("hr")

            tgb.text("## Output", mode="md")

            tgb.text(
                lambda selected_scenario: (
                    str(selected_scenario.output.read())
                    if selected_scenario
                    and selected_scenario.output.is_ready_for_reading
                    else "Submit the scenario using the left panel."
                ),
                mode="raw",
                class_name="color-primary",
            )

            tgb.text("## Data node inspector", mode="md")

            tgb.data_node_selector("{selected_data_node}", display_cycles=False)

            tgb.text("**Data node value:**", mode="md")

            tgb.text(
                lambda selected_data_node: (
                    str(selected_data_node.read())
                    if selected_data_node and selected_data_node.is_ready_for_reading
                    else None
                )
            )

            tgb.data_node("{selected_data_node}")

            tgb.html("hr")

            with tgb.expandable("Scenario DAG"):
                tgb.scenario_dag("{selected_scenario}")


def on_change(state, var_name: str, var_value):
    if var_name == "selected_species":
        state.selected_scenario.species.write(var_value)
    elif var_name == "selected_island":
        state.selected_scenario.island.write(var_value)
    elif var_name == "selected_sex":
        state.selected_scenario.sex.write(var_value.lower())


if __name__ == "__main__":
    tp.Orchestrator().run()

    gui = Gui(page)
    gui.run(title="Spark with Taipy")
