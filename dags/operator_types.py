import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': 'user@example.com',
    'retries': 2,
}

dag = DAG(
    'operator_types',
    default_args=default_args,
    description='example DAG to show operator types',
    catchup=False,
    schedule_interval=None)

bash_op = BashOperator(
    task_id='bash_op',
    bash_command='echo bash_operator',
    dag=dag)

python_op = PythonOperator(
    task_id='python_op',
    python_callable=lambda: print('Hello World!'),
    dag=dag)

email_op = EmailOperator(
    task_id='email_op',
    to='user@example.com',
    subject='Airflow Email Operator Example',
    html_content='<p>Airflow <b>Email Operator</b> Example Mail Body</p>',
    mime_charset='utf-8',
    dag=dag)

dummy_op = DummyOperator(
    task_id='dummy_op',
    dag=dag)

bash_op >> python_op
email_op >> dummy_op
