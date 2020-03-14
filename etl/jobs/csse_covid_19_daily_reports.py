import logging
import unittest
from datetime import datetime as dt
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd

_LOG = logging.getLogger(__name__)
INPUT_PATH = "./data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"
OUTPUT_PATH = "./work/csse_covid_19_daily_reports.csv.gz"

schema = {
    "Last Update": object,
    "Country/Region": str,
    "Province/State": str,
    "Latitude": object,
    "Longitude": object,
    "Confirmed": object,
    "Recovered": object,
    "Deaths": object,
    "input_file": object,
}


def extract() -> Iterable[Path]:
    for i in Path(INPUT_PATH).glob("*.csv"):
        _LOG.debug("Extracted %s" % i)
        yield Path(i)


def transform(*filepaths: Path) -> pd.DataFrame:
    for f in filepaths:
        df = pd.read_csv(
            f,
            warn_bad_lines=True,
            dtype=schema,
            na_filter=False,
            na_values="Unknown",
            keep_default_na=False,
            parse_dates=True,
            infer_datetime_format=True,
        )
        df["input_file"] = str(f)
        _LOG.debug("Loaded %s" % f)
        df["Last Update"] = pd.to_datetime(df["Last Update"])
        df["Confirmed"] = pd.to_numeric(df["Confirmed"])
        df["Deaths"] = pd.to_numeric(df["Deaths"])
        df["Recovered"] = pd.to_numeric(df["Recovered"])

        yield df


def load(*args: pd.DataFrame) -> None:
    df = pd.DataFrame(columns=list(schema))
    for other in args:
        df = df.append(other, sort=False)
    df.to_csv(OUTPUT_PATH)
    print(OUTPUT_PATH)


def run(debug: Optional[bool] = None, quiet: Optional[bool] = None) -> None:
    logging.basicConfig(level=logging.INFO)
    start = dt.now()
    if quiet:
        _LOG.setLevel(logging.NOTSET)
    elif debug:
        _LOG.setLevel(logging.DEBUG)
    _LOG.info("start=%s" % start)
    load(*transform(*extract()))
    end = dt.now()
    _LOG.info("start=%s,end=%s,duration=%s" % (start, end, end - start))
