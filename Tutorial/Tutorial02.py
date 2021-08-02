from datetime import datetime, timedelta
from time import sleep
from airflow.models import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'sla': timedelta(hours=2)
}

def print_func():
    print("This goes in the logs!")
    
def sleep_func(length_of_time):
    sleep(length_of_time)

with DAG(
    'Tutorial02',
    default_args=default_args,
    start_date=datetime(2021, 8, 1),
    schedule_interval='0 0 * * *'
) as dag:
# Define the tasks    
    task01 = PythonOperator(
        task_id='print',
        python_callable=print_func
    )
    task02 = PythonOperator(
        task_id='sleep',
        python_callable=sleep_func,
        op_kwargs={'length_of_time': 5}
    )
    
    task01 >> task02