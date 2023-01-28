import csv
from typing import List
from taipy import Config


def read_csv(path: str, delimiter: str = ",") -> str:
    with open(path, newline=' ') as csvfile:
        data = csv.reader(csvfile, delimiter=delimiter)
    return data


def write_csv(data: List[str], path: str, delimiter: str = ","):
    headers = ["country_code", "country"]
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)


csv_country_data_cfg = Config.configure_generic_data_node(
    id="csv_country_data",
    read_fct=read_csv,
    write_fct=write_csv,
    read_fct_params=["../path/data.csv", ";"],
    write_fct_params=["../path/data.csv", ";"])
