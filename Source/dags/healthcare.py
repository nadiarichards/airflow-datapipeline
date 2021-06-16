from core.execute import core_get_data, core_aggregate_data, core_insert_to_db
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

SCHEDULE_INTERVAL = None

default_args = {
    'owner': 'business intelligence',
    'depends_on_past': False,
    'start_date': datetime (2021, 6, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

DAG_VERSION= 'Healthcare.0'

dag = DAG(DAG_VERSION
    , default_args=default_args
    , schedule_interval=SCHEDULE_INTERVAL
    , concurrency=1
    , max_active_runs=1)

get_data = PythonOperator(
    task_id='get_data',
    python_callable=core_get_data,
    retries=0,
    provide_context=True,
    dag=dag
)

aggregation = PythonOperator(
    task_id='aggregate_data',
    python_callable=core_aggregate_data,
    retries=0,
    provide_context=True,
    dag=dag
)

