from Healthcare.data_retrieval import get_data, merge_data
from Healthcare.aggregation import aggregate_data
from Healthcare.connect import create_engine_pgsql, insert_to_db

def get_data():
    df_value = pd.read_csv("../Files/clean_value_df.csv")
    df_census = pd.read_csv("../Files/final_census_df.csv")
    df_readmission = pd.read_csv("../Files/readmissions_df.csv")
    return df_value, df_census, df_readmission


def merge_data(df_value, df_census, df_readmission):
    df_value['zip_code'] = df_value['zip_code'].astype(str)
    df_census['zip_code'] = df_census['zip_code'].astype(str)
    merged_df=df_value.merge(df_readmission, how="inner", on="facility_id")
    print(merged_df.columns)
    census_merged_df=df_value.merge(df_census, how="inner", on="zip_code")
    print(census_merged_df.columns)
    return merged_df, census_merged_df

    def aggregate_data(merged_df, census_merged_df):
    updated_readmission_df=merged_df[["facility_id", "city", "zip_code", "payment", "value_code", "measure_name", "number_of_discharges", "excess_readmission_ratio", "number_of_readmissions"]]
    avg_code_readmission=updated_readmission_df.groupby(["facility_id"]).mean()
    avg_facility_readmission=updated_readmission_df.groupby(["value_code"]).mean()
    updated_census_df=census_merged_df[["facility_id", "city", "zip_code", "value_code", "population", "poverty_rate", "median_income"]]
    return avg_code_readmission, avg_facility_readmission, updated_census_df