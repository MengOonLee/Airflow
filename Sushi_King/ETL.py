import os
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.utils.dates import days_ago
# from airflow.providers.apache.beam.operators.beam import BeamRunPythonPipelineOperator
# from airflow.providers.google.cloud.operators.dataflow import DataflowConfiguration
from airflow.providers.google.cloud.operators.dataflow import DataflowCreatePythonJobOperator
# from airflow.providers.google.cloud.hooks.dataflow import DataflowJobStatus
# from airflow.providers.google.cloud.sensors.dataflow import DataflowJobStatusSensor

os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/opt/airflow/dags/.GCP_SA/mlee-claritas-bigdata-poc.json'

default_args = {
    'sla': timedelta(hours=2)
}

with DAG(
    'ETL',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='0 0 * * *',
    tags=['Sushi_King']
) as dag:
    
    mssql_bq = DataflowCreatePythonJobOperator(
        task_id='mssql_bq',
        py_file='/opt/airflow/dags/Sushi_King/__main__.py',
        py_options=[],
        job_name='{{task.task_id}}',
        options={
            'driver_file': '/opt/airflow/dags/Sushi_King/connect_driver.json',
            'customer_sql_file': '/opt/airflow/dags/Sushi_King/SQL/Customer.sql',
            'temp_location': 'gs://claritas-bigdata-poc-temp/',
            'experiment': 'use_runner_v2',
            'sdk_container_image': 'gcr.io/claritas-bigdata-poc/sushi_king/etl:0.0.1'
        },
        py_requirements=['apache-beam[gcp]==2.31.0', 'pymssql==2.2.2'],
        py_interpreter='python3',
        py_system_site_packages=False,
        project_id='claritas-bigdata-poc',
        location='asia-southeast1'
    )
    
    mssql_bq
#     mssql_bq = DataflowCreatePythonJobOperator(
#         task_id='mssql_bq',
#         py_file='/opt/airflow/dags/Sushi_King/test.py',
#         py_options=[],
#         job_name='{{task.task_id}}',
#         options={
#             'driver_file': '/opt/airflow/dags/Sushi_King/connect_driver.json',
#             'customer_sql_file': '/opt/airflow/dags/Sushi_King/SQL/Customer.sql',
#             'temp_location': 'gs://claritas-bigdata-poc-temp/',
#         },
#         py_requirements=['pymssql==2.2.2', 'apache-beam[gcp]==2.31.0'],
#         py_interpreter='python3',
#         py_system_site_packages=False,
#         project_id='claritas-bigdata-poc',
#         location='asia-southeast1',
#         wait_until_finished=False
#     )
    
#     mssql_bq = BeamRunPythonPipelineOperator(
#         task_id='mssql-bq',
#         runner='DataflowRunner',
#         py_file='/opt/airflow/dags/Sushi_King/test.py',
#         py_options=[],
#         pipeline_options={
#             "driver_file": "/opt/airflow/dags/Sushi_King/connect_driver.json",
#             "customer_sql_file": "/opt/airflow/dags/Sushi_King/SQL/Customer.sql",
#             "tempLocation": "gs://claritas-bigdata-poc-temp/"
#         },
#         py_requirements=['apache-beam[gcp]==2.31.0', 'pymssql==2.2.2'],
#         py_interpreter='python3',
#         py_system_site_packages=False,
#         dataflow_config=DataflowConfiguration(
#             job_name='{{task.task_id}}',
#             project_id='claritas-bigdata-poc',
#             location='asia-southeast1',
#             wait_until_finished=False
#         )
#     )
    
#     dataflow_status = DataflowJobStatusSensor(
#         task_id='dataflow_status',
#         job_id="{{task_instance.xcom_pull('mssql_bq')['job_id']}}",
#         expected_statuses={DataflowJobStatus.JOB_STATE_DONE},
#         project_id='claritas-bigdata-poc',
#         location='asia-southeast1'
#     )
    
#     mssql_bq >> dataflow_status