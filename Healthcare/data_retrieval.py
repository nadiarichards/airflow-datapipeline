import pandas as pd

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
