> You can download the code 
<a href="/scenario_comparison.py" download>here</a>. 

*Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced*

![Configuration](config.svg){ width=700 style="margin:auto;display:block;border: 4px solid rgb(210,210,210);border-radius:7px" }

Taipy offers a way to compare data nodes across scenarios by including a function directly in the configuration of the scenario.

## Step 1: The first step consists in declaring on which data nodes to apply the comparison functions:

In this example, we want to apply a comparison to the '_output_' Data Node. It is indicated in the comparators parameter of the `configure_scenario`.

```python
scenario_cfg = Config.configure_scenario(id="multiply_scenario",
                                         name="my_scenario",
                                         tasks_configs=[first_task_cfg,
                                                        second_task_cfg],
                                         comparators={output_data_node_cfg.id: compare_function},)
```
## Step 2: Implement the comparison function (`compare_function()`) used above.

_data_node_results_ is the list of the Output Data Nodes from all scenarios passed in the comparator. We iterate through it to compare scenarios.

```python
def compare_function(*data_node_results):
    compare_result = {}
    current_res_i = 0
    for current_res in data_node_results:
        compare_result[current_res_i] = {}
        next_res_i = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_i} with result {next_res_i}")
            compare_result[current_res_i][next_res_i] = next_res - current_res
            next_res_i += 1
        current_res_i += 1
    return compare_result
```

Now, the `compare_scenarios` can be used within Taipy.

```python
tp.Core().run()

scenario_1 = tp.create_scenario(scenario_cfg)
scenario_2 = tp.create_scenario(scenario_cfg)

scenario_1.submit()
scenario_2.submit()

print(tp.compare_scenarios(scenario_1, scenario_2))
```

Results:

```
...
{'output': {'compare_function': {0: {0: 0, 1: -4}, 1: {0: 4, 1: 0}}}}
```

# Entire code

```python
from taipy.core.config import Config, Frequency
import taipy as tp


# Normal function used by Taipy
def double(nb):
    return nb * 2

def add(nb):
    return nb + 10


# Configuration of Data Nodes
input_cfg = Config.configure_data_node("input", default_data=21)
intermediate_cfg = Config.configure_data_node("intermediate")
output_cfg = Config.configure_data_node("output")

# Configuration of tasks
first_task_cfg = Config.configure_task("double",
                                    double,
                                    input_cfg,
                                    intermediate_cfg)

second_task_cfg = Config.configure_task("add",
                                    add,
                                    intermediate_cfg,
                                    output_cfg)



def compare_function(*data_node_results):
    # example of function
    compare_result = {}
    current_res_i = 0
    for current_res in data_node_results:
        compare_result[current_res_i] = {}
        next_res_i = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_i} with result {next_res_i}")
            compare_result[current_res_i][next_res_i] = next_res - current_res
            next_res_i += 1
        current_res_i += 1
    return compare_result


scenario_cfg = Config.configure_scenario(id="multiply_scenario",
                                         name="my_scenario",
                                         task_configs=[first_task_cfg, second_task_cfg],
                                         comparators={output_cfg.id: compare_function})


if __name__=="__main__":
    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.input.write(10)
    scenario_2.input.write(8)

    scenario_1.submit()
    scenario_2.submit()
    
    print(tp.compare_scenarios(scenario_1, scenario_2))
```