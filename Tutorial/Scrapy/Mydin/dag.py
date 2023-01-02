import os
import datetime
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time())

with DAG(
    dag_id="Mydin_scrapy",
    default_args={
        "email": ["darklemonlee@yahoo.co.uk"],
        "email_on_failure": True
    },
    start_date=yesterday,
    schedule_interval="@daily",
    tags=["Test"]
) as dag:
    
    grocery = BashOperator(
        task_id="grocery",
        bash_command=dedent("""
            cd ${AIRFLOW_HOME}/dags/Scrapy/Mydin
            scrapy crawl grocery -O {{ params.filename }}_{{ ds_nodash }}.jl
        """),
        params={
            "filename": "./data/grocery"
        }
    )
