import pandas as pd

def aggregate_data(merged_df, census_merged_df):
    updated_readmission_df=merged_df[["facility_id", "city", "zip_code", "payment", "value_code", "measure_name", "number_of_discharges", "excess_readmission_ratio", "number_of_readmissions"]]
    avg_code_readmission=updated_readmission_df.groupby(["facility_id"]).mean()
    avg_facility_readmission=updated_readmission_df.groupby(["value_code"]).mean()
    updated_census_df=census_merged_df[["facility_id", "city", "zip_code", "value_code", "population", "poverty_rate", "median_income"]]
    return avg_code_readmission, avg_facility_readmission, updated_census_df