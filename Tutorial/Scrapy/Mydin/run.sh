#!/bin/bash

cd "${AIRFLOW_HOME}/dags/Scrapy/Mydin"
scrapy crawl grocery -O ./data/grocery.jl
