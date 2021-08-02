from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'sla': timedelta(hours=2)
}

echo_file = """
    {% for filename in params.filenames %}
        echo "Reading {{filename}}"
    {% endfor %}
"""

with DAG(
    'Tutorial03',
    default_args=default_args,
    start_date=datetime(2021, 8, 1),
    schedule_interval='0 13 * * *'
) as dag:
# Define the tasks    
    task01 = BashOperator(
        task_id='template_task',
        bash_command=echo_file,
        params={'filenames': ['file01.txt', 'file02.txt']}
    )
    
    task01
