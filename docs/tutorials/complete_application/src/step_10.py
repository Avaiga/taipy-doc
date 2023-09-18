from step_09 import *

from taipy.gui import navigate

# Our first page is the original page
# (with the slider and the chart that displays a week of the historical data)
page_data_visualization = page

# Second page: create scenarios and display results
page_scenario_manager = """
# Create your scenario

<|layout|columns=1 1 1 1|
<|
**Prediction date**\n\n <|{day}|date|not with_time|>
|>

<|
**Max capacity**\n\n <|{max_capacity}|number|>
|>

<|
**Number of predictions**\n\n<|{n_predictions}|number|>
|>

<|
<br/> <br/>\n <|Create new scenario|button|on_action=create_scenario|>
|>
|>

<|part|render={len(scenario_selector) > 0}|
<|layout|columns=1 1|
<|
## Scenario \n <|{selected_scenario}|selector|lov={scenario_selector}|dropdown|>
|>

<|
## Display the pipeline \n <|{selected_pipeline}|selector|lov={pipeline_selector}|dropdown|>
|>
|>

<|{predictions_dataset}|chart|x=Date|y[1]=Historical values|type[1]=bar|y[2]=Predicted values|type[2]=scatter|height=80%|width=100%|>
|>
"""

lov_menu = [("Data-Visualization", "Data Visualization"),
            ("Scenario-Manager", "Scenario Manager")]

# Create a menu with our pages
root_md = "<|menu|label=Menu|lov={lov_menu}|on_action=menu_fct|>"

pages = {"/":root_md,
         "Data-Visualization":page_data_visualization,
         "Scenario-Manager":page_scenario_manager}


def menu_fct(state, var_name: str, fct: str, var_value: list):
    # Change the value of the state.page variable in order to render the correct page
    navigate(state, var_value["args"][0])


if __name__ == "__main__":
    tp.Core().run()
    Gui(pages=pages).run(dark_mode=False)
