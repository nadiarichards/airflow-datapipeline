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

