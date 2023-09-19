> You can download the code of this step [here](../src/step_08.py) or all the steps [here](https://github.com/Avaiga/taipy-getting-started-core/tree/develop/src).

# Step 8: Scenario comparison

This step reuses the configuration provided in the previous step except for the [scenario configuration](https://docs.taipy.io/en/latest/manuals/core/entities/scenario-cycle-mgt/#compare-scenarios).

![](config_08.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

Taipy provides a mechanism to compare scenarios by providing a function directly into the scenario's configuration.

## Step 1: The first step consists in declaring on which data nodes to apply the comparison functions:

Taipy can compare Data Nodes. In this example, we want a comparison applied to the '_output_' Data Node. It is indicated in the comparators parameter of the `configure_scenario()`.

```python
scenario_cfg = Config.configure_scenario(id="multiply_scenario",
                                        name="my_scenario",
                                        pipeline_configs=[pipeline_cfg],
                                        comparators={output_data_node_cfg.id: compare_function},
                                        frequency=Frequency.MONTHLY)
```
## Step 2: Implement the comparison function (`compare_function()`) used above.

_data_node_results_ is the list of the Output Data Nodes from all scenarios passed in the comparator. We iterate through it to compare scenarios.

```python
def compare_function(*data_node_results):
    compare_result= {}
    current_res_i = 0
    for current_res in data_node_results:
        compare_result[current_res_i]={}
        next_res_i = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_i} with result {next_res_i}")
            compare_result[current_res_i][next_res_i] = next_res - current_res
            next_res_i += 1
        current_res_i += 1
    return compare_result
```

Now, the `compare_scenarios()` can be used within Taipy.

```python
tp.Core().run()

scenario_1 = tp.create_scenario(scenario_cfg)
scenario_2 = tp.create_scenario(scenario_cfg)


print("\nScenario 1: submit")
scenario_1.submit()
print("Value", scenario_1.output.read())

print("\nScenario 2: first submit")
scenario_2.submit()
print("Value", scenario_2.output.read())


print(tp.compare_scenarios(scenario_1, scenario_2))
```

## Taipy Rest

Taipy Rest allows the user to navigate through the entities of the application but also create and submit scenarios. Taipy Rest commands are referenced [here](https://docs.taipy.io/en/latest/manuals/reference_rest/).

```python
tp.Rest().run()
```