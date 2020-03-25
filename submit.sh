#!/usr/bin/env bash
python3 -m zipfile -c jobs.zip jobs/*.py
spark-submit \
    --py-files jobs.zip \
    main.py
