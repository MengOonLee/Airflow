#!/bin/bash

docker build . --no-cache --pull \
-f Dockerfile \
-t darklemon/airflow:latest

docker push darklemon/airflow:latest

microk8s helm3 upgrade \
--install airflow apache-airflow/airflow \
--namespace airflow \
-f override.yaml

docker rmi darklemon/airflow:latest
docker rmi apache/airflow:latest
