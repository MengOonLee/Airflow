from datetime import datetime, timedelta
from time import sleep
from airflow.models import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'sla': timedelta(hours=2)
}

def branch_test(**kwargs):
    if int(kwargs['ds_nodash']) % 2 == 0:
        return 'even_day_task'
    else:
        return 'odd_day_task'

with DAG(
    'Tutorial04',
    default_args=default_args,
    start_date=datetime(2021, 7, 30),
    schedule_interval='@daily'
) as dag:
    
    # Define the tasks
    start_task = BashOperator(
        task_id='start',
        bash_command='echo START'
    )
    branch_task = BranchPythonOperator(
        task_id='branch',
        provide_context=True,
        python_callable=branch_test
    )
    even_day_task = BashOperator(
        task_id='even_day_task',
        bash_command='echo EVEN day'
    )
    odd_day_task = BashOperator(
        task_id='odd_day_task',
        bash_command='echo ODD day'
    )
    
    start_task >> branch_task >> even_day_task
    branch_task >> odd_day_task