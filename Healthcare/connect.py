import pandas as pd
from sqlalchemy import create_engine

def create_engine_pgsql():
    rds_connection_string = "postgres:3411@localhost:5432/airflow_pipeline_project"
    engine = create_engine(f'postgresql://{rds_connection_string}')
    return engine

def insert_to_db(engine, df, table_name):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)