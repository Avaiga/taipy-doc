from taipy.core.config import Config, Frequency
import taipy as tp
import datetime as dt
import pandas as pd


def filter_by_month(df, month):
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == month]
    return df

def count_values(df):
    return len(df)


Config.load('config_04.toml')

if __name__ == '__main__':
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,7),
                                    name="Scenario 2022/10/7")
    scenario_2 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2022,10,5),
                                    name="Scenario 2022/10/5")

    scenario_1.month.write(10)
    scenario_2.month.write(10)

    print("Month Data Node of Scenario 1", scenario_1.month.read())
    print("Month Data Node of Scenario 2", scenario_2.month.read())

    scenario_1.submit()
    scenario_2.submit()


    print("Scenario 1 before", scenario_1.is_primary)
    print("Scenario 2 before", scenario_2.is_primary)

    tp.set_primary(scenario_2)

    print("Scenario 1 after", scenario_1.is_primary)
    print("Scenario 2 after", scenario_2.is_primary)


    scenario_3 = tp.create_scenario(scenario_cfg,
                                    creation_date=dt.datetime(2021,9,1),
                                    name="Scenario 2022/9/1")
    scenario_3.month.write(9)
    scenario_3.submit()

    print("Is scenario 3 primary?", scenario_3.is_primary)

    data_node = None
    scenario = None


    tp.Gui("""<|{scenario}|scenario_selector|>
              <|{scenario}|scenario|>
              <|{scenario}|scenario_dag|>
              <|{data_node}|data_node_selector|>""").run()
