from data_retrieval import get_data, merge_data
from aggregation import aggregate_data

df_value, df_census, df_readmission = get_data()
# print(df_value[:5], df_census[:5], df_readmission[:5])

merged_df, census_merged_df=merge_data(df_value, df_census, df_readmission)
# print(merged_df[:5], census_merged_df[:5])

avg_code_readmission, avg_facility_readmission, updated_census_df=aggregate_data(merged_df, census_merged_df)
print(avg_code_readmission.head(), avg_facility_readmission.head(), updated_census_df.head())