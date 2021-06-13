from data_retrieval import get_data

df_value, df_census, df_readmission, df_zipcode = get_data()
print(df_value[:5], df_census[:5], df_readmission[:5], df_zipcode[:5])