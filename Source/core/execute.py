from Healthcare.data_retrieval import get_data, merge_data
from Healthcare.aggregation import aggregate_data
from Healthcare.connect import create_engine_pgsql, insert_to_db

def core_get_data(**kwargs):
    task_instance =kwargs['ti']
    df_value, df_census, df_readmission = get_data()
    merged_df, census_merged_df=merge_data(df_value, df_census, df_readmission)
    task_instance.xcom_push(key='merged_df', value=merged_df)
    task_instance.xcom_push(key='census_merged_df', value=census_merged_df)

def core_aggregate_data(**kwargs):
    task_instance = kwargs['ti']
    merged_df = task_instance.xcom_pull(key='merged_df', task_ids ='get_data')
    census_merged_df = task_instance.xcom_pull(key='census_merged_df', task_ids ='get_data')
    avg_code_readmission, avg_facility_readmission, updated_census_df=aggregate_data(merged_df, census_merged_df)
    task_instance.xcom_push(key='avg_code_readmission', value=avg_code_readmission)
    task_instance.xcom_push(key='avg_facility_readmission', value=avg_facility_readmission)
    task_instance.xcom_push(key='updated_census_df', value=updated_census_df)
    
def core_insert_to_db(**kwargs):
    task_instance = kwargs['ti']
    engine=create_engine_pgsql()
    avg_code_readmission=task_instance.xcom_pull(key='avg_code_readmission', task_ids='aggregate_data')
    avg_facility_readmission=task_instance.xcom_pull(key='avg_facility_readmission', task_ids='aggregate_data')
    updated_census_df=task_instance.xcom_pull(key='updated_census_df', task_ids='aggregate_data')
    insert_to_db(engine, avg_code_readmission, 'avg_readmissions')
    insert_to_db(engine, avg_facility_readmission, 'avg_valuecode_readmissions')
    insert_to_db(engine, updated_census_df, 'hospitals_census')