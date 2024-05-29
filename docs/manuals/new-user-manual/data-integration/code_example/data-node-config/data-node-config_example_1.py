from taipy import Config

date_cfg = Config.configure_data_node(
    id="date",
    description="The current date of the scenario",
)
