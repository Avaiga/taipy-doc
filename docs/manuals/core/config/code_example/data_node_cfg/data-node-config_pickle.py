from taipy import Config
from datetime import datetime

date_cfg = Config.configure_pickle_data_node(
    id="date_cfg",
    default_data=datetime(2022, 1, 25))

model_cfg = Config.configure_pickle_data_node(
    id="model_cfg",
    default_path="path/to/my/model.p",
    description="The trained model")
