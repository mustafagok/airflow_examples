import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': 'example@mail.com',
    'retries': 2,
}

dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='simple DAG',
    catchup=False,
    schedule_interval=None)

# a simple DAG consist of three tasks: A, B, and C.
# task A has to run successfully before task B can run, but task C can run anytime.

# Maybe A prepares data for B to analyze while C sends an email.
# Or perhaps A monitors your location so B can open your garage door while C turns on your house lights.

# part 1 is equivalent to part 2

# region part 1

task_ids = ['task_A',
            'task_B',
            'task_C']

tasks = {}
for t in task_ids:
    tasks[t] = DummyOperator(
        task_id=t,
        dag=dag)

tasks['task_A'] >> tasks['task_B']

# endregion

# region part 2

# task_A = DummyOperator(
#     task_id='task_A',
#     dag=dag)
#
# task_B = DummyOperator(
#     task_id='task_B',
#     dag=dag)
#
# task_C = DummyOperator(
#     task_id='task_C',
#     dag=dag)
#
# task_A >> task_B

# endregion
