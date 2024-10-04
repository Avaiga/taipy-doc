import datetime as dt

import pandas as pd

import taipy as tp
from taipy.common.config import Config


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'].dt.month == month]
    return df

if __name__ == '__main__':
    Config.load('config.toml')
    scenario_cfg = Config.scenarios["my_scenario"]

    tp.Orchestrator().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,5),
                                    name="Scenario 2022/10/5")

    scenario_1.month.write(10)

    print("Month Data Node of Scenario 1:", scenario_1.month.read())
    print("Month Data Node of Scenario 2:", scenario_2.month.read())

    scenario_1.submit()

    before_set_1 = scenario_1.is_primary
    before_set_2 = scenario_2.is_primary

    tp.set_primary(scenario_2)

    print('Scenario 1: Primary?', before_set_1, scenario_1.is_primary)
    print('Scenario 2: Primary?', before_set_2, scenario_2.is_primary)

    scenario = None
    data_node = None

    tp.Gui("""<|{scenario}|scenario_selector|>
              <|{scenario}|scenario|>
              <|{scenario}|scenario_dag|>
              <|{data_node}|data_node_selector|>""").run()
