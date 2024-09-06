from datetime import datetime
import taipy as tp
from taipy import Config, Orchestrator, Gui, Scope
import pandas as pd

# Creating a data node variable to be bound to the visual element
data_node = None

if __name__ == "__main__":
    # Creating various data sources. A CSV file (out.csv), an integer parameter and a datetime object
    pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}).to_csv("out.csv")
    parameter, date = 15, datetime.now()

    # Configure global data nodes to integrate previous data
    ds_cfg = Config.configure_csv_data_node(id="dataset", scope=Scope.GLOBAL, default_path="out.csv")
    parameter_cfg = Config.configure_data_node(id="parameter", scope=Scope.GLOBAL, default_data=parameter)
    date_cfg = Config.configure_data_node(id="date", scope=Scope.GLOBAL, default_data=date)

    # Instantiate the three data nodes
    Orchestrator().run()
    tp.create_global_data_node(ds_cfg)
    tp.create_global_data_node(parameter_cfg)
    tp.create_global_data_node(date_cfg)

    # Running the GUI service with a data node selector and a data node viewer
    page = ("<|{data_node}|data_node_selector|>"
            "<|{data_node}|data_node|>")
    Gui(page=page).run()
