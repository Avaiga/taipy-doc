from taipy import Config
from datetime import datetime

class DailyMinTemp:
    def __init__(self, Date : datetime=None, Temp : float=None):
        self.Date = Date
        self.Temp = Temp

    def encode(self):
        return {
            "date": self.Date.isoformat(),
            "temperature": self.Temp,
        }

    @classmethod
    def decode(cls, data):
        return cls(
            datetime.fromisoformat(data["date"]),
            data["temperature"],
        )

historical_data_cfg = Config.configure_mongo_collection_data_node(
    id="historical_data",
    db_username="admin",
    db_password="pa$$w0rd",
    db_name="taipy",
    collection_name="historical_data_set",
    custom_document=DailyMinTemp,
)
