#!/bin/bash

microk8s helm3 repo add apache-airflow https://airflow.apache.org
microk8s helm3 repo update

microk8s kubectl create namespace airflow
microk8s kubectl create -f pv_dags.yaml
microk8s kubectl create -f pvc_dags.yaml
