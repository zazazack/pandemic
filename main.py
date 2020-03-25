#!/usr/bin/env python
# coding: utf-8
from jobs import (
    csse_covid_19_daily_reports,
    csse_covid_19_time_series,
    publichealth_harriscountytx_gov,
)

if __name__ == "__main__":
    csse_covid_19_daily_reports.run()
    csse_covid_19_time_series.run()
    publichealth_harriscountytx_gov.run()
