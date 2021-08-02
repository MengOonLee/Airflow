from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'sla': timedelta(hours=2)
}

with DAG(
    'parallel_dag',
    default_args=default_args,
    start_date=datetime(2021, 8, 1),
    schedule_interval='@daily'
) as dag:
    
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )
    
    task_2 = BashOperator(
        task_id='task_2',
        bash_command='sleep 3'
    )
    
    task_3 = BashOperator(
        task_id='task_3',
        bash_command='sleep 3'
    )
    
    task_4 = BashOperator(
        task_id='task_4',
        bash_command='sleep 3'
    )
    
    task_1 >> [task_2, task_3] >> task_4