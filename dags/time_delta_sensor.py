import datetime
import airflow
from airflow import DAG
from airflow.models import Variable
from airflow.sensors.time_delta_sensor import TimeDeltaSensor

# get time delta sensor parameters
time_delta_args = Variable.get('time_delta_sensors', deserialize_json=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': 'user@example.com',
    'retries': 2,
}

dag = DAG(
    'time_delta_sensor',
    default_args=default_args,
    description='example DAG to test time delta sensor',
    catchup=False,
    schedule_interval='0 0 * * *')

wait_test = TimeDeltaSensor(
    task_id='wait_test',
    delta=datetime.timedelta(hours=time_delta_args['test']['hours'],
                             minutes=time_delta_args['test']['minutes']),
    dag=dag)
