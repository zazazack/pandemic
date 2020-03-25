#!/usr/bin/env bash
set -euo pipefail
IFS='\n\t'

JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export JAVA_HOME

python3 -m pip install -r requirements.txt

wget -c -P /tmp/ -i resources/urls.txt && python3 -m zipfile -e /tmp/master.zip /tmp

find /tmp/ -ipath '**covid*' -iname '*.csv' -type f -exec wc -l {} \;
./submit.sh

rm -rf samples/ && mkdir -p samples/ && mv *.csv samples/
