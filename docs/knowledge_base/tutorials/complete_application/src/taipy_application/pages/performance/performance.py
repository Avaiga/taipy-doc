from taipy.gui import Markdown

import pandas as pd
import taipy as tp

# Initial dataset for comparison
comparison_scenario = pd.DataFrame(columns=["Scenario Name",
                                            "RMSE baseline",
                                            "MAE baseline",
                                            "RMSE ML",
                                            "MAE ML"])


# Selector for metrics
metric_selector = ["RMSE", "MAE"]
selected_metric = metric_selector[0]


def compare(state):
    print("Comparing...")

    # Initialize lists for comparison
    scenario_data = []

    # Go through all the primary scenarios
    all_scenarios = sorted(tp.get_primary_scenarios(), key=lambda x: x.creation_date.timestamp())

    for scenario in all_scenarios:
        rmse_baseline, mae_baseline = scenario.metrics_baseline.read()
        rmse_ml, mae_ml = scenario.metrics_ml.read()


        # Store scenario data in a dictionary
        scenario_data.append({
            "Scenario Name": scenario.name,
            "RMSE baseline": rmse_baseline,
            "MAE baseline": mae_baseline,
            "RMSE ML": rmse_ml,
            "MAE ML": mae_ml
        })

    # Create a DataFrame from the scenario_data list
    state.comparison_scenario = pd.DataFrame(scenario_data)

performance = Markdown("pages/performance/performance.md")
