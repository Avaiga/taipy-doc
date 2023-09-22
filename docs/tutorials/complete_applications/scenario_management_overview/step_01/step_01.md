> You can download the code for
<a href="./../src/step_01.py" download>Step 1</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 

# Configuration and execution

*Estimated Time for Completion: 15 minutes; Difficulty Level: Beginner*

Before looking at some code examples, let’s define some basic terms Taipy Core uses. Taipy Core revolves around three major concepts.

## Three fundamental concepts in Taipy:
- [**Data Node**](../../../../manuals/core/concepts/data-node.md): is the translation of a _variable_ in Taipy. Data Nodes know how to retrieve any type of data. They can refer to: any Python object (string, int, list, dict, model, data frame, etc.), a Pickle file, a CSV file, a SQL database, etc.

- [**Task**](../../../../manuals/core/concepts/task.md): is the expression of a _function_ in Taipy.

- [**Scenarios**](../../../../manuals/core/concepts/scenario.md): is an instance of your pipelines. End-users often require modifying various parameters to reflect different business situations. Taipy Scenarios provide the framework to "run"/"execute" pipelines under different conditions/variations (i.e., data/parameters modified by the end-user).


## What is a configuration?

A [**configuration**](../../../../manuals/core/config/index.md) is a structure to define scenarios. It represents our Direct Acyclic Graph(s); it models the data sources, parameters, and tasks. Once defined, a configuration acts like a superclass; it is used to generate different instances of scenarios.


Let's create our first configuration. For this, we have two alternatives:

- Using Taipy Studio

- Or directly coding in Python.

Let’s consider the simplest possible pipeline: a single function taking two inputs: a dataset and a date to forecast and generate a prediction for the chosen date. See below:


```python
from taipy import Config
import taipy as tp
import pandas as pd

def predict(historical_temperature: pd.DataFrame, date_to_forecast: str) -> float:
    print(f"Running baseline...")
    historical_temperature['Date'] = pd.to_datetime(historical_temperature['Date'])
    historical_same_day = historical_temperature.loc[
        (historical_temperature['Date'].dt.day == date_to_forecast.day) &
        (historical_temperature['Date'].dt.month == date_to_forecast.month)
    ]
    return historical_same_day['Temp'].mean()
```

![](config_01.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

- Three Data Nodes are being configured ('historical_temperature', 'date_to_forecast' and 'predictions'). All the input Data Nodes will be written before the submission of the pipeline. The task links the three Data Nodes through the Python function *predict*. The submission write the input ('predictions'). 


!!! example "Configuration"

    === "Taipy Studio"

        **Alternative 1:** Configuration using Taipy Studio

        By watching the animation below, you can see how this configuration gets created using Taipy Studio. In fact, Taipy Studio is an editor of a TOML file specific to Taipy. It lets you edit and view a TOML file that will be used in our code.

        <video controls width="400">
            <source src="/step_01/config_01.mp4" type="video/mp4">
        </video>


        To use this configuration in our code (`main.py` for example), we must load it and retrieve the `scenario_cfg`. This `scenario_cfg` is the basis to instantiate our scenarios.

        ```python
        Config.load('config_01.toml')

        # my_scenario is the id of the scenario configured
        scenario_cfg = Config.scenarios['my_scenario']
        ```

    === "Python configuration"

        **Alternative 2:** Configuration using Python Code

        Here is the code to configure a simple scenario.

        ```python
        # Configuration of Data Nodes
        historical_temperature_cfg = Config.configure_data_node("historical_temperature")
        date_to_forecast_cfg = Config.configure_data_node("date_to_forecast")
        predictions_cfg = Config.configure_data_node("predictions")

        # Configuration of tasks
        predictions_cfg = Config.configure_task(id="predict",
                                                function=predict,
                                                input=[historical_temperature_cfg, date_to_forecast_cfg],
                                                output=predictions_cfg)

        # Configuration of scenario
        scenario_cfg = Config.configure_scenario(id="my_scenario", 
                                                            task_configs=[predictions_cfg])
        ```

The configuration is done! Let's use it to create scenarios and submit them.

First, launch Taipy Core in your code (`tp.Core().run()`). Then, you can play with Taipy: 

- create scenarios,

- submit them,

- write your data nodes,

- read your data nodes.

Creating a scenario (`tp.create_scenario(<Scenario Config>)`) creates all its related entities (_tasks_, _Data Nodes_, etc). These entities are being created thanks to the previous configuration. Still, no scenario has been run yet. `tp.submit(<Scenario>)` is the line of code that runs all the scenario-related pipelines and tasks.

```python
# Run of the Core
tp.Core().run()

# Creation of the scenario and execution
scenario = tp.create_scenario(scenario_cfg)
scenario.historical_temperature.write(data)
scenario.date_to_forecast.write(dt.datetime.now())
tp.submit(scenario)

print("Value at the end of task", scenario.output.read())
```

Results:

```
[2022-12-22 16:20:02,740][Taipy][INFO] job JOB_predict_... is completed.
Value at the end of task 23.45
```    

## Gui-Core visual elements

Add these few lines to the code of your script. This creates a web application to:

- select scenarios you created,

- create new ones,

- submit them,

- see the configuration used by the scenario.

```python
def save(state):
    # write values of Data Node to submit scenario
    state.scenario.historical_temperature.write(data)
    state.scenario.date_to_forecast.write(state.date)
    tp.gui.notify(state, "s", "Saved! Ready to submit")

date = None
scenario_md = """
<|{scenario}|scenario_selector|>
<|{date}|date|on_change=save|active={scenario}|>
<|{scenario}|scenario|>
<|{scenario}|scenario_dag|>

<|Refresh|button|on_action={lambda s: s.assign("scenario", scenario)}|>
<|{scenario.predictions.read() if scenario else ''}|>
"""

tp.Gui(scenario_md).run()
```

The [Gui-Core visual elements](../../../../manuals/gui/corelements/data_node.md_template) let you add visual elements for the Taipy backend. This way, creating a web application corresponding to your backend has never been simpler.

![](demo.gif){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

## Entire code

```python
from taipy import Config
import taipy as tp
import pandas as pd


data = pd.read_csv("https://raw.githubusercontent.com/Avaiga/taipy-getting-started-core/develop/src/daily-min-temperatures.csv")



# Normal function used by Taipy
def predict(historical_temperature: pd.DataFrame, date_to_forecast: str) -> float:
    print(f"Running baseline...")
    historical_temperature['Date'] = pd.to_datetime(historical_temperature['Date'])
    historical_same_day = historical_temperature.loc[
        (historical_temperature['Date'].dt.day == date_to_forecast.day) &
        (historical_temperature['Date'].dt.month == date_to_forecast.month)
    ]
    return historical_same_day['Temp'].mean()

# Configuration of Data Nodes
historical_temperature_cfg = Config.configure_data_node("historical_temperature")
date_to_forecast_cfg = Config.configure_data_node("date_to_forecast")
predictions_cfg = Config.configure_data_node("predictions")

# Configuration of tasks
predictions_cfg = Config.configure_task("predict",
                                        predict,
                                        [historical_temperature_cfg, date_to_forecast_cfg],
                                        predictions_cfg)

# Configuration of scenario
scenario_cfg = Config.configure_scenario(id="my_scenario", 
                                                    task_configs=[predictions_cfg])


if __name__ == '__main__':
    # Run of the Core
    tp.Core().run()

    # Creation of the scenario and execution
    scenario = tp.create_scenario(scenario_cfg)
    scenario.historical_temperature.write(data)
    scenario.date_to_forecast.write(dt.datetime.now())
    tp.submit(scenario)

    print("Value at the end of task", scenario.predictions.read())

    def save(state):
        state.scenario.historical_temperature.write(data)
        state.scenario.date_to_forecast.write(state.date)
        tp.gui.notify(state, "s", "Saved! Ready to submit")

    date = None
    scenario_md = """
<|{scenario}|scenario_selector|>
<|{date}|date|on_change=save|active={scenario}|>
<|{scenario}|scenario|>
<|{scenario}|scenario_dag|>

<|Refresh|button|on_action={lambda s: s.assign("scenario", scenario)}|>
<|{scenario.predictions.read() if scenario else ''}|>
"""

    tp.Gui(scenario_md).run()
``` 
    