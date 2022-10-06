import datetime
import pytz
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.bash import BashOperator

tz=pytz.timezone("Asia/Kuala_Lumpur")

yesterday = datetime.datetime.combine(
    datetime.datetime.now(tz=tz) - datetime.timedelta(1),
    datetime.datetime.min.time())

with DAG(
    dag_id="tutorial",
    start_date=yesterday,
    schedule_interval="@daily"
    ) as dag:

    t1 = BashOperator(
        task_id="echo",
        bash_command="echo $PWD"
    )
    t2 = EmailOperator(
        task_id='send_email',
        conn_id='sendgrid_default',
        to='darklemon2000@gmail.com',
        subject="EmailOperator test for SendGrid",
        html_content="This is a test message sent through SendGrid."
    )
    t1 >> t2
