"""
The second page of the application.
Page content is imported from the page_2.md file.

Please refer to ../../userman/gui/pages for more details.
"""

from taipy.gui import Markdown, notify
import datetime as dt
import pandas as pd


scenario = None
data_node = None
day = dt.datetime(2021, 7, 26)
n_predictions = 40
max_capacity = 200
predictions_dataset = {
    "Date": [dt.datetime(2021, 7, 26)],
    "Predicted values ML": [0],
    "Predicted values Baseline": [0],
    "Historical values": [0],
}


def submission_change(state, submittable, details: dict):
    if details["submission_status"] == "COMPLETED":
        notify(state, "success", "Scenario completed!")
        state["scenario"].on_change(state, "scenario", state.scenario)
    else:
        notify(state, "error", "Something went wrong!")


def save(state):
    print("Saving scenario...")
    # Get the currently selected scenario

    # Conversion to the right format
    state_day = dt.datetime(state.day.year, state.day.month, state.day.day)

    # Change the default parameters by writing in the Data Nodes
    state.scenario.day.write(state_day)
    state.scenario.n_predictions.write(int(state.n_predictions))
    state.scenario.max_capacity.write(int(state.max_capacity))
    notify(state, "success", "Saved!")


def on_change(state, var_name, var_value):
    if var_name == "scenario" and var_value:
        state.day = state.scenario.day.read()
        state.n_predictions = state.scenario.n_predictions.read()
        state.max_capacity = state.scenario.max_capacity.read()

        if state.scenario.full_predictions.is_ready_for_reading:
            state.predictions_dataset = state.scenario.full_predictions.read()[-200:]
        else:
            state.predictions_dataset = predictions_dataset


scenario_page = Markdown("pages/scenario/scenario.md")
