from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
import sys

dag = DAG(
   dag_id = 'update_state',
   default_args={"start_date": "2019-10-01"}
)
task1 = BashOperator(
   task_id='generate_random_number',
   bash_command='echo $RANDOM',
   dag=dag
)

def python_version():
    return sys.version

task2 = PythonOperator(
   task_id='get_python_version',
   python_callable=python_version,
   dag=dag
)   
task3 = SimpleHttpOperator(
   task_id='query_server_for_external_ip',
   endpoint='https://api.ipify.org',
   method='GET',
   dag=dag
)   
task3 >> [task2, task1]
