from taipy.core.config import Config
import taipy as tp
import datetime as dt
import pandas as pd


def filter_current(df):
    current_month = dt.datetime.now().month
    df['Date'] = pd.to_datetime(df['Date']) 
    df = df[df['Date'].dt.month == current_month]
    return df

def count_values(df):
    return len(df)


Config.load('config_03.toml')

if __name__ == '__main__':
    # my_scenario is the id of the scenario configured
    scenario_cfg = Config.scenarios['my_scenario']

    tp.Core().run()

    scenario = tp.create_scenario(scenario_cfg, creation_date=dt.datetime(2022,10,7), name="Scenario 2022/10/7")
    scenario.submit()

    print("Nb of values of scenario:", scenario.nb_of_values.read())

    data_node = None

    tp.Gui("""<|{scenario}|scenario_selector|>
              <|{scenario}|scenario|>
              <|{scenario}|scenario_dag|>
              <|{data_node}|data_node_selector|>""").run()

