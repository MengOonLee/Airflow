#!/bin/bash

docker build . --no-cache --pull \
-f ~/Work/Airflow/Build/Docker/Dockerfile \
-t darklemon/airflow:latest

docker push darklemon/airflow:latest

echo -e "AIRFLOW_UID=$(id -u)" > .env

echo -e "AIRFLOW_IMAGE_NAME=darklemon/airflow:latest" >> .env

docker compose up airflow-init
