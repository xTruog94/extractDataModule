import pandas as pd
import os
import requests

def get_columns(df):
    return df.columns

def read_data(data_url="tmp/final.xls"):
    extension = data_url.split(".")[-1]
    if extension =="csv":
        return pd.read_csv(data_url)
    return pd.read_excel(data_url)

def extract_data(column_requires, data_url="tmp/final.xls"):
    res = {}
    df = read_data(data_url)
    columns = get_columns(df)
    if any([x not in columns for x in column_requires]):
        return {"error":"Columns must exist"}
    else:
        for column in column_requires:
            res[column] = df[column].values.tolist()
        return res