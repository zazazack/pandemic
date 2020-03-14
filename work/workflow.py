#!/usr/bin/env python
# coding: utf-8
import argparse
import json
import subprocess
from pathlib import Path

import pandas as pd

DATA_DIR='./COVID-19/csse_covid_19_data/csse_covid_19_daily_reports'


def load_data(path):

    schema = {
        'Province/State': str,
        'Country/Region': str,
        'Last Update': object,
        'Confirmed': object,
        'Deaths': object,
        'Recovered': object,
        'Latitude': object,
        'Longitude': object,
    }

    df = pd.DataFrame(columns=list(schema))


    for p in Path(path).glob('*.csv'):
        other = pd.read_csv(p, warn_bad_lines=True, dtype=schema, na_filter=False)
        other['input_file'] = str(p)
        df = df.append(other)


    df['Last Update'] = pd.to_datetime(df['Last Update'])
    df['Confirmed'] = pd.to_numeric(df['Confirmed'], downcast='integer')
    df['Deaths'] = pd.to_numeric(df['Deaths'], downcast='integer')
    df['Recovered'] = pd.to_numeric(df['Recovered'], downcast='integer')

    return df


# def reconcile_record_counts(df):
#     output = subprocess.getoutput('wc -l ./data/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/*.csv')
#     line_count_wc = pd.DataFrame(
#         [
#             i.strip().split()
#             for i in output.splitlines()
#         ],
#         columns=['line_count', 'path']
#     )

#     line_count_pandas = df.groupby('path').size()

#     line_count_pandas['line_count'] = pd.to_numeric(line_count_pandas['line_count'], downcast='integer')
#     line_count_wc.dtypes
#     line_count_wc['line_count'] = pd.to_numeric(line_count_wc.line_count, downcast='integer')
#     joined = line_count_wc[:-1].join(line_count_pandas, lsuffix='_wc', rsuffix='_pd')
#     joined['delta'] = joined['line_count_pd'] - joined['line_count_wc']
#     joined.head()
#     len(joined)
#     joined.delta.sum()
#     return {
#         'wc_total': joined['line_count_wc'].sum(),
#         'padnas_total': joined['line_count_pd'].sum(),
#         'dela': joined['delta'].sum(),
#         '%': joined['delta'].sum() / joined['line_count_wc'].sum()
#     }

# df.describe().plot()
# grp_srs = df['Last Update']
# grp = df.groupby(grp_srs.dt.dayofyear)
# grp.Confirmed.describe().plot()
# grp.Recovered.describe().plot()
# grp.Deaths.describe().plot()
# df.to_csv("./csse_covid_19_daily_reports.csv")
# df.index = pd.DatetimeIndex(df['Last Update'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='workflow.py')
    parser.add_argument('-p', '--path', type=str, default='.')

    args = parser.parse_args()
#    print(subprocess.getoutput('wget --continue -P data https://github.com/CSSEGISandData/COVID-19/archive/master.zip'))
#    print(subprocess.getoutput('unzip -au -d data ./data/master.zip'))
    df = load_data(args.path)
    df.info()
    # print(json.dumps(reconcile_record_counts(df), indent='  '))
    df.to_csv('csse_covid_19_daily_reports.csv.gz')

