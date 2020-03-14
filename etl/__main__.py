#!/usr/bin/env python
# coding: utf-8
import argparse
import logging
from pathlib import Path
from typing import Iterable

from etl import jobs
from etl.jobs import csse_covid_19_daily_reports


_LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main() -> None:
    parser = argparse.ArgumentParser(prog=__name__)
    parser.add_argument("--version", action="version", version=jobs.__version__)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("-u", "--update", action="store_true")
    parser.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()
    if args.debug:
        _LOG.setLevel(logging.DEBUG)
    if args.quiet:
        _LOG.setLevel(logging.NOTSET)
    csse_covid_19_daily_reports.run(debug=args.debug)


if __name__ == "__main__":
    main()
