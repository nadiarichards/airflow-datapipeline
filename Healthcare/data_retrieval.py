import pandas as pd

def get_data():
    df_value = pd.read_csv("../Files/clean_value_df.csv", nrows=100)
    df_census = pd.read_csv("../Files/final_census_df.csv", nrows=100)
    df_readmission = pd.read_csv("../Files/readmissions_df.csv", nrows=100)
    df_zipcode = pd.read_csv("../Files/zipcode_lat_lng.csv", nrows=100)
    return df_value.head(50), df_census.head(50), df_readmission.head(50), df_zipcode.head(50)

# print(get_data())
# df_value, df_census, df_readmission, df_zipcode = get_data()
# print(df_value[:5], df_census[:5], df_readmission[:5], df_zipcode[:5])