from airflow.models import DAG
from airflow.operators.bash import BashOperator

dag = DAG(dag_id='example_dag',
    default_args={"start_date": "2021-07-31"}
)
task01 = BashOperator(task_id='generate_random_number',
    bash_command='echo $RANDOM',
    dag=dag
)