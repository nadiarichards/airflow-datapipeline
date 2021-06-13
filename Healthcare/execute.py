from data_retrieval import get_data, merge_data
from aggregation import aggregate_data

df_value, df_census, df_readmission = get_data()
# print(df_value[:5], df_census[:5], df_readmission[:5])

merged_df, census_merged_df=merge_data(df_value, df_census, df_readmission)
# print(merged_df[:5], census_merged_df[:5])

