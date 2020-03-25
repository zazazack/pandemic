from pathlib import Path
import pandas as pd


def run():
    path = Path("/tmp/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/")
    files = [
        "time_series_19-covid-Confirmed.csv",
        "time_series_19-covid-Recovered.csv",
        "time_series_19-covid-Deaths.csv",
    ]
    df = pd.DataFrame(
        columns=["Province/State", "Country/Region", "Lat", "Long", "Date"]
    )
    for f in files:
        other = pd.read_csv(path.joinpath(f),)
        other = other.melt(
            id_vars=["Province/State", "Country/Region", "Lat", "Long"],
            var_name="Date",
            value_name=(path / f).stem,
        )
        other['input_file_path'] = (path / f).as_posix()
        df = pd.merge(df, other, how="outer")
    df.to_csv(f"{__name__}.csv", index_label="ix")


if __name__ == "__main__":
    run()
