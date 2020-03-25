import pandas as pd

url = "http://publichealth.harriscountytx.gov/Resources/2019-Novel-Coronavirus"


def run():
    df, *rest = pd.read_html(url, header=0, attrs={"id": "covidtable"})
    df.to_csv(f"{__name__}.csv", index_label="ix")


if __name__ == "__main__":
    run()
