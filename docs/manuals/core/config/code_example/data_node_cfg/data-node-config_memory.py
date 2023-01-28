from taipy import Config
from datetime import datetime

date_cfg = Config.configure_in_memory_data_node(
    id="date",
    default_data=datetime(2022, 1, 25))
