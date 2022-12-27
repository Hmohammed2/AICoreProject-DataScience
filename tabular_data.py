import pandas as pd
import numpy as np
import re

def set_default_feature_values(*dfs):
    for df in dfs:
        if isinstance(df, pd.DataFrame):
            for column in df:
                if df[column].isna().sum() > 1:
                    df[column].fillna(1, inplace=True)
                else:
                    print("Column has no missing values!")
        else:
            raise ValueError  
    
def remove_rows_with_missing_ratings(*args):
    for df in args:
        if isinstance(df, pd.DataFrame):
            for column in df:
                if df[column].isna().sum() > 1:
                    df[column].dropna(0, inplace=True)
                else:
                    print("Column has no missing values!")
        else:
            raise ValueError
 
def combine_description_strings(column):
    if isinstance(column, pd.Series):
        new_string = " ".join(map(str, column))
        cleaned_string = re.sub(r"'About this space', " , '' ,new_string)
        column = cleaned_string
        return column
    else:
        raise ValueError

def save_data(data):
    user_input = input("Do you want to save your data? (yes/no): ")
    while True:
        if user_input.lower() == "yes":
            data.to_csv('clean_tabular_data.csv')
            break
        elif user_input.lower() == "no":
            break

def clean_tabular_data(read_data: str):

    data = pd.read_csv("tabular_data/AirBnbData.csv")

    ratings_column = data[["Value_rate", "Cleanliness_rate", "Accuracy_rate", 
       "Communication_rate", "Location_rate", "Check-in_rate"]]
    descriptions_column = data["Description"]
    feature_columns = data[["guests", "beds", "bathrooms", "bedrooms"]]
    
    remove_rows_with_missing_ratings(ratings_column)
    data["Description"] = combine_description_strings(descriptions_column)
    set_default_feature_values(feature_columns)
    save_data(data)


if __name__ == "__main__":

    string_data = "tabular_data/AirBnbData.csv"

    # clean_tabular_data(string_data) 

    data = pd.read_csv(string_data)

    new_column = combine_description_strings(data["Description"])

    print(new_column)