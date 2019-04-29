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
    'bitshift_composition',
    default_args=default_args,
    description='example DAG to show operator relationship methods',
    catchup=False,
    schedule_interval=None)

op1 = DummyOperator(
    task_id='op1',
    dag=dag)

op2 = DummyOperator(
    task_id='op2',
    dag=dag)

# Traditionally, operator relationships are set with the set_upstream() and set_downstream() methods.
# In Airflow 1.8, this can be done with the Python bitshift operators >> and <<.
# The following four statements are all functionally equivalent:

op1.set_downstream(op2)
# op2.set_upstream(op1)

# op1 >> op2
# op2 << op1
