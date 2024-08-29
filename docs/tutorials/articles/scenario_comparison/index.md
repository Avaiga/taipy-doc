---
title: Scenario Comparison
category: scenario_management
data-keywords: scenario comparison datanode configuration
short-description: Learn best practices to compare scenarios easily.
order: 17
img: images/icon-code.svg
---

*Estimated Time for Completion: 15 minutes; Difficulty Level: Advanced*

![Configuration](images/config.svg){ width=90% : .tp-image-border }

Taipy offers a way to compare data nodes across scenarios by including a function directly in the
configuration of the scenario. This is particularly useful to visualize the differences between
scenarios and make decision upon it.

[Download the code](./src/scenario_comparison.py){: .tp-btn target='blank' }

# Comparing scenarios

**Step 1:** Declare data nodes on which the comparison functions are applied.

In this example, we want to apply a comparison to the '_revenues_' Data Node. It is indicated in
the comparators parameter of the `configure_scenario`.

```python
# Scenario configuration
scenario_cfg = Config.configure_scenario(
    id="pricing_strategy",
    task_configs=[predict_sales_task_cfg, calculate_revenue_task_cfg],
    comparators={revenue_output_cfg.id: compare_revenue}
)
```

**Step 2:** Implement the comparison function (`compare_function()`) used above.

_revenues_ is the list of the Output (*revenues*) Data Nodes from all scenarios passed in
the comparator. We iterate through it to compare scenarios.

```python
def compare_revenue(*revenues):
    scenario_names = [f"Scenario {i}" for i in range(len(revenues))]
    comparisons = {"Scenarios": scenario_names,
                   "Revenues": list(revenues)}
    return pd.DataFrame(comparisons)
```

Now, the `compare_scenarios` can be used within Taipy.

```python
if __name__ == "__main__":
    orchestrator = tp.Orchestrator()
    orchestrator.run()

    # Create scenarios with different pricing strategies
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.price_input.write(120)  # Higher price scenario
    scenario_2.price_input.write(80)   # Lower price scenario

    scenario_1.submit()
    scenario_2.submit()

    # Compare the scenarios
    comparisons = tp.compare_scenarios(scenario_1, scenario_2)
    print(comparisons)
```

Results:

```
...
{'revenue_output': {'compare_revenue':     Scenarios  Revenues
0  Scenario 0    9120.0
1  Scenario 1   11200.0}}
```

# Compare Scenario with a GUI

Taipy can then generate a GUI that compares scenarios easily. Our comparison will be shown through
a chart and a table in this case. This application can be as interactive and complete as possible.

```python
from taipy.gui import Gui
import taipy.gui.builder as tgb

with tgb.Page() as compare_page:
    tgb.text("# Compare Scenarios", mode="md")

    tgb.chart("{comparisons_revenue}", type="bar", x="Scenarios", y="Revenues")
    tgb.table("{comparisons_revenue}")

Gui(compare_page).run()
```

![Comparison GUI](images/comparison.png){ width=90% : .tp-image-border }

# Entire code

Here is the entire code to recreate the example. A GUI has been created to show the results.

```python
import numpy as np
import pandas as pd

import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config
from taipy.gui import Gui


# Simulation function to predict sales based on pricing
def predict_sales(price):
    """
    Simulate sales volume based on price.
    Elasticity affects how demand reacts to price changes.
    """
    base_demand = 100
    elasticity = -1.5

    demand = base_demand * (price / 100) ** elasticity
    return max(0, np.round(demand))  # Ensure non-negative sales volume

# Function to calculate revenue from sales volume and price
def calculate_revenue(price, sales_volume):
    return price * sales_volume

# Comparator function to compare revenue outputs
def compare_revenue(*revenues):
    scenario_names = [f"Scenario {i}" for i in range(len(revenues))]
    comparisons = {"Scenarios": scenario_names,
                   "Revenues": list(revenues)}
    return pd.DataFrame(comparisons)

if __name__=="__main__":
    # Data Node configuration
    price_input_cfg = Config.configure_data_node("price_input", default_data=100)
    sales_output_cfg = Config.configure_data_node("sales_output")
    revenue_output_cfg = Config.configure_data_node("revenue_output")

    # Task configurations
    predict_sales_task_cfg = Config.configure_task(
        id="predict_sales",
        function=predict_sales,
        input=price_input_cfg,
        output=sales_output_cfg
    )

    calculate_revenue_task_cfg = Config.configure_task(
        id="calculate_revenue",
        function=calculate_revenue,
        input=[price_input_cfg, sales_output_cfg],
        output=revenue_output_cfg
    )

    # Scenario configuration
    scenario_cfg = Config.configure_scenario(
        id="pricing_strategy",
        task_configs=[predict_sales_task_cfg, calculate_revenue_task_cfg],
        comparators={revenue_output_cfg.id: compare_revenue}
    )

    orchestrator = tp.Orchestrator()
    orchestrator.run()

    # Create scenarios with different pricing strategies
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.price_input.write(120)  # Higher price scenario
    scenario_2.price_input.write(80)   # Lower price scenario

    scenario_1.submit()
    scenario_2.submit()

    # Compare the scenarios
    comparisons = tp.compare_scenarios(scenario_1, scenario_2)
    print(comparisons)

    comparisons_revenue = comparisons["revenue_output"]['compare_revenue']

    with tgb.Page() as compare_page:
        tgb.text("# Compare Scenarios", mode="md")

        tgb.chart("{comparisons_revenue}", type="bar", x="Scenarios", y="Revenues")
        tgb.table("{comparisons_revenue}")

    Gui(compare_page).run()
```
