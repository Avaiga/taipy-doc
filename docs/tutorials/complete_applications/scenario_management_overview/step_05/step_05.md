> You can download the code for
<a href="./../src/step_05.py" download>Step 5</a> 
or all the steps <a href="./../src/src.zip" download>here</a>. 

# Scopes

*Time to complete: 15 minutes; Level: Intermediate*

[Scopes](../../../../manuals/core/concepts/scope.md) determine how Data Nodes are shared between cycles and scenarios. The developer may decide:

- `Scope.SCENARIO` (_default_): Having one data node for each scenario.

- `Scope.CYCLE`: Extend the scope by sharing data nodes across all scenarios of a given cycle.

- `Scope.GLOBAL`: Finally, extend the scope globally (across all scenarios of all cycles). For example, the initial/historical dataset is usually shared by all the scenarios/pipelines/cycles. It is unique in the entire application.

![](config_05.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

!!! example "Configuration"

    === "Taipy Studio"

        Modifying the scope of a Data Node is as simple as changing its Scope parameter in the configuration. 

        The configuration is taken in the previous step, so you can copy the last TOML Config file directly or take it [here](../src/config_04.toml).

        ![](config_05.gif){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

        - Change the Scope of historical_data to be global
        
        - Change the Scope of month_data and month to be Cycle
     
        - Load the new configuration in the code

    === "Python configuration"

        Modifying the scope of a Data Node is as simple as changing its Scope parameter inside the configuration.

        The configuration is taken in the previous step so you can copy the previous code directly.

        ```python
        from taipy.config import Scope, Frequency

        historical_data_cfg = Config.configure_csv_data_node(id="historical_data",
                                                         default_path="time_series.csv",
                                                         scope=Scope.GLOBAL)
        month_cfg =  Config.configure_data_node(id="month", scope=Scope.CYCLE)

        month_values_cfg = Config.configure_data_node(id="month_data",
                                                       scope=Scope.CYCLE)

        ...
        ```


Cycles are created based on the _creation_date_ of scenarios. In the example below, we force the creation_date to a given date (in real life, the actual creation date of the scenario gets used automatically).

```python
tp.Core().run()

scenario_1 = tp.create_scenario(scenario_cfg,
                                creation_date=dt.datetime(2022,10,7),
                                name="Scenario 2022/10/7")
scenario_2 = tp.create_scenario(scenario_cfg,
                               creation_date=dt.datetime(2022,10,5),
                               name="Scenario 2022/10/5")
scenario_3 = tp.create_scenario(scenario_cfg,
                                creation_date=dt.datetime(2021,9,1),
                                name="Scenario 2021/9/1")
```

Scenario 1 and 2 belong to the same Cycle: since _month_ now has a **Cycle** scope, we can define _month_ just once for both scenarios: 1 and 2.


```python
scenario_1.month.write(10)
scenario_3.month.write(9)
print("Scenario 1: month", scenario_1.month.read())
print("Scenario 2: month", scenario_2.month.read())
print("Scenario 3: month", scenario_3.month.read())
```

Results:
```
Scenario 1: month 10
Scenario 2: month 10
Scenario 3: month 9
```

Defining the _month_ of scenario 1 will also determine the _month_ of scenario 2 since they share the same Data Node. 

This is not the case for _nb_of_values_ that are of Scenario scope; each _nb_of_values_ has its own value in each scenario.

## Entire code

```python
from taipy.core.config import Config, Frequency, Scope
import taipy as tp
import datetime as dt
import pandas as pd


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    return len(df)


historical_data_cfg = Config.configure_csv_data_node(id="historical_data",
                                                 default_path="time_series.csv",
                                                 scope=Scope.GLOBAL)
month_cfg =  Config.configure_data_node(id="month", scope=Scope.CYCLE)

month_values_cfg = Config.configure_data_node(id="month_data",
                                               scope=Scope.CYCLE)
nb_of_values_cfg = Config.configure_data_node(id="nb_of_values")


task_filter_cfg = Config.configure_task(id="filter_by_month",
                                                 function=filter_by_month,
                                                 input=[historical_data_cfg,month_cfg],
                                                 output=month_values_cfg)

task_count_values_cfg = Config.configure_task(id="count_values",
                                                 function=count_values,
                                                 input=month_values_cfg,
                                                 output=nb_of_values_cfg)



scenario_cfg = Config.configure_scenario(id="my_scenario",
                                                    task_configs=[task_filter_cfg,
                                                                  task_count_values_cfg],
                                                    frequency=Frequency.MONTHLY)


if __name__ == '__main__':
    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                creation_date=dt.datetime(2022,10,5),
                                name="Scenario 2022/10/5")

    scenario_1.month.write(10)
    print("Scenario 1: month", scenario_1.month.read())
    print("Scenario 2: month", scenario_2.month.read())

    print("\nScenario 1 & 2: submit")
    scenario_1.submit()
    scenario_2.submit()
    print("Value", scenario_1.nb_of_values.read())
    print("Value", scenario_2.nb_of_values.read())
```
