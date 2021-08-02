from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

default_args = {
    'sla': timedelta(hours=2)
}

with DAG(
    'BigQuery_test',
    default_args=default_args,
    start_date=datetime(2021, 8, 1),
    schedule_interval='0 0 * * *'
) as dag:
    
    task_create_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create-dataset',
        gcp_conn_id='google_cloud_default',
        dataset_id='test_dataset',
        location='asia-southeast1'
    )
    
    task_create_dataset