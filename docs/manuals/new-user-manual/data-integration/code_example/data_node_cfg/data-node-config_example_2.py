from datetime import timedelta
from taipy import Config, Scope

model_cfg = Config.configure_data_node(
    id="model",
    scope=Scope.CYCLE,
    storage_type="pickle",
    validity_period=timedelta(days=2),
    description="Trained model shared by scenarios from the same cycle.",
    code=54,
)
