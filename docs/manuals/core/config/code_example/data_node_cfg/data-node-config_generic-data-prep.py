from datetime import datetime as dt
import pandas as pd
from taipy import Config


def read_csv(path: str) -> pd.DataFrame:
    # reading a csv file, define some column types and parse a string into datetime
    custom_parser = lambda x: dt.strptime(x, "%Y %m %d %H:%M:%S")
    data = pd.read_csv(
        path,
        parse_dates=['date'],
        date_parser=custom_parser,
        dtype={
            "name": str,
            "grade": int
        }
    )
    return data


def write_csv(data: pd.DataFrame, path: str) -> None:
    # dropping not a number values before writing
    data.dropna().to_csv(path)


student_data = Config.configure_generic_data_node(
    id="student_data",
    read_fct=read_csv,
    write_fct=write_csv,
    read_fct_args=["../path/data.csv"],
    write_fct_args=["../path/data.csv"])
