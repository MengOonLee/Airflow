#!/bin/bash

microk8s kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
