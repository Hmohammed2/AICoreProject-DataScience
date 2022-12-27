import pandas as pd
import numpy as np
import re

def set_default_feature_values(*dfs):
    for df in dfs:
        if isinstance(df, pd.DataFrame):
            for column in df:
                if df[column].isna().sum() > 1:
                    featured_columns = df[column].fillna(1, inplace=True)
                else:
                    print("Column has no missing values!")
        else:
            raise ValueError  
        
    print(df.isna().sum()) # Checks to see if its already been filled

    return featured_columns

def remove_rows_with_missing_ratings(*args):
    for df in args:
        if isinstance(df, pd.DataFrame):
            for column in df:
                if df[column].isna().sum() > 1:
                    dropped_rows = df[column].dropna(0, inplace=False)
                else:
                    print("Column has no missing values!")
        else:
            raise ValueError
    
    print(dropped_rows.isna().sum())

    return dropped_rows

def combine_description_strings(column, pattern):
    if isinstance(column, pd.Series):
        new_string = " ".join(map(str, column))
        cleaned_string = re.sub(r"{}".format(pattern), '' ,new_string)
        print(cleaned_string)
        return cleaned_string
    else:
        raise ValueError

def save_data(data):
    user_input = input("Do you want to save your data? (yes/no): ")
    while True:
        if user_input.lower() == "yes":
            data.to_csv('clean_tabular_data.csv')
        elif user_input.lower() == "no":
            break

def clean_tabular_data(read_data: str):

    data = pd.read_csv("tabular_data/AirBnbData.csv")
    ratings_column = data[["Value_rate", "Cleanliness_rate", "Accuracy_rate", 
       "Communication_rate", "Location_rate", "Check-in_rate"]]