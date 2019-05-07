import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': 'example@mail.com',
    'retries': 2,
}

dag = DAG(
    'trigger_rule',
    default_args=default_args,
    description='example DAG for showing trigger rules',
    catchup=False,
    schedule_interval=None)

task_1_A = DummyOperator(
    task_id='task_1_A',
    dag=dag)

task_1_B = BashOperator(
    task_id='task_1_B',
    bash_command='sleep 60',
    dag=dag)

task_2 = DummyOperator(
    task_id='task_2',
    trigger_rule='one_success',
    dag=dag)

[
    task_1_A,
    task_1_B
] >> task_2
