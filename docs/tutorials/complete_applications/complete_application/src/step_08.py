from step_07 import *

# Initial variables
## Initial variables for the scenario   
day = dt.datetime(2021, 7, 26)
n_predictions = 40
max_capacity = 200

page_scenario_manager = page + """
# Change your scenario

**Prediction date**\n\n <|{day}|date|not with_time|>

**Max capacity**\n\n <|{max_capacity}|number|>

**Number of predictions**\n\n<|{n_predictions}|number|>

<|Save changes|button|on_action={submit_scenario}|>

Select the pipeline
<|{selected_pipeline}|selector|lov={pipeline_selector}|> <|Update chart|button|on_action={update_chart}|>

<|{predictions_dataset}|chart|x=Date|y[1]=Historical values|type[1]=bar|y[2]=Predicted values|type[2]=scatter|height=80%|width=100%|>
"""


def create_scenario():
    global selected_scenario

    print("Creating scenario...")
    scenario = tp.create_scenario(scenario_cfg)

    selected_scenario = scenario.id

    tp.submit(scenario)


def submit_scenario(state):
    print("Submitting scenario...")
    # Get the selected scenario: in this current step a single scenario is created then modified here.
    scenario = tp.get(selected_scenario)

    # Conversion to the right format
    state_day = dt.datetime(state.day.year, state.day.month, state.day.day)

    # Change the default parameters by writing in the datanodes
    scenario.day.write(state_day)
    scenario.n_predictions.write(int(state.n_predictions))
    scenario.max_capacity.write(int(state.max_capacity))

    # Execute the pipelines/code
    tp.submit(scenario)

    # Update the chart when we change the scenario
    update_chart(state)


def update_chart(state):
    # Select the right scenario and pipeline
    scenario = tp.get(selected_scenario)
    pipeline = scenario.pipelines[state.selected_pipeline]
    # Update the chart based on this pipeline
    update_predictions_dataset(state, pipeline)


if __name__ == "__main__":
    global selected_scenario
    tp.Core().run()
    # Creation of a single scenario
    create_scenario()
    Gui(page=page_scenario_manager).run(dark_mode=False)
