#!/bin/bash

microk8s helm3 delete airflow \
--namespace airflow
microk8s helm3 repo rm apache-airflow
microk8s kubectl delete ns airflow
microk8s kubectl delete -f pv_dags.yaml
microk8s ctr images rm $(microk8s ctr images ls name~='airflow' | awk {'print $1'})
