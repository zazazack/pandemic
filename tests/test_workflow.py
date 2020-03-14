import unittest
from pathlib import Path

import pandas as pd

from etl.jobs import csse_covid_19_daily_reports

class TestCsseCovid19DailyReports(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_extract(self):
        result = csse_covid_19_daily_reports.extract()
        self.assertIsInstance(next(result), Path)

    def test_transform(self):
        result = csse_covid_19_daily_reports.transform(*csse_covid_19_daily_reports.extract())
        self.assertTrue(isinstance(next(result), pd.DataFrame))

    def test_run(self):
        result = csse_covid_19_daily_reports.run()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
