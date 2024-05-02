from datetime import timedelta
from taipy import Config, Scope

date_cfg = Config.configure_data_node(
    id="date_cfg",
    description="The current date of the scenario",
)

model_cfg = Config.configure_data_node(
    id="model_cfg",
    scope=Scope.CYCLE,
    storage_type="pickle",
    validity_period=timedelta(days=2),
    description="Trained model shared by all scenarios",
    code=54,
)
