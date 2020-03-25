# pandemic

Extract COVID-19 data to $PWD

## Prerequisites

- Linux/Unix Shell
- Java==1.8
- Python>=3.6.8

## Install

    git clone https://github.com/.../pandemic
    cd ./pandemic

## Usage

### Etl

    ./run.sh

### Add new jobs

    mv my_new_job.py ./jobs
    echo 'jobs.my_new_job.run()\n' >> main.py
