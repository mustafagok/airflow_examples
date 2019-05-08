import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': 'user@example.com',
    'retries': 2,
}

dag = DAG(
    'no_dependency',
    default_args=default_args,
    description='example DAG without task dependencies',
    catchup=False,
    schedule_interval=None)

task_ids = ['task_A',
            'task_B',
            'task_C']

tasks = {}
for tid in task_ids:
    tasks[tid] = DummyOperator(
        task_id=tid,
        dag=dag)
