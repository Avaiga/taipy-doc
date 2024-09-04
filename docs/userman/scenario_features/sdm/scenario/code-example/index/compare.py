import taipy as tp
from datetime import datetime
from my_config import monthly_scenario_cfg

if __name__ == "__main__":
    tp.Orchestrator().run()

    previous_month_scenario = tp.create_scenario(monthly_scenario_cfg)
    previous_month_scenario.current_month.write(datetime(2020, 1, 1))
    previous_month_scenario.submit()

    current_month_scenario = tp.create_scenario(monthly_scenario_cfg)
    current_month_scenario.current_month.write(datetime(2020, 2, 1))
    current_month_scenario.submit()

    tp.compare_scenarios(previous_month_scenario,
                        current_month_scenario,
                        data_node_config_id="sales_predictions")
