from taipy import Config
import json


class SaleRow:
    date: str
    nb_sales: int


class SaleRowEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SaleRow):
            return {
                '__type__': "SaleRow",
                'date': obj.date,
                'nb_sales': obj.nb_sales}
        return json.JSONEncoder.default(self, obj)


class SaleRowDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self,
                                  object_hook=self.object_hook,
                                  *args,
                                  **kwargs)

    def object_hook(self, d):
        if d.get('__type__') == "SaleRow":
            return SaleRow(date=d['date'], nb_sales=d['nb_sales'])
        return d


sales_history_cfg = Config.configure_json_data_node(
    id="sales_history",
    path="path/sales.json",
    encoder=SaleRowEncoder,
    decoder=SaleRowDecoder)
