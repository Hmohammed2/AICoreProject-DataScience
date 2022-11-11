#%%
import pandas as pd
import numpy as np
import re
import os

from macpath import join

#%%
file = pd.read_csv("tabular_data/AirBnbData.csv")
# %%
print(file.head())
# %%
ratings_column = file[["Value_rate",  "Cleanliness_rate", "Accuracy_rate", 
        "Communication_rate", "Location_rate", "Check-in_rate"]]
# %%
dropped_rows = ratings_column.dropna(0, inplace=False)
# %%
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
        
        print(df.isna().sum()) # Checks to see if its already been filled
# %%
def remove_rows_with_missing_ratings(*args):
    for df in args:
        if isinstance(df, pd.DataFrame):
            for column in df:
                if df[column].isna().sum() > 1:
                    dropped_rows = df[column].dropna(0, inplace=True)
                else:
                    print("Column has no missing values!")
        else:
            raise ValueError
    
    print(dropped_rows.isna().sum())
# %%
# def combine_description_strings():
# %%
new_string = file['Description'].str.replace("About this space", '')
# file['Description'] = file['Description'].str.replace("About this space", "")
# %%
# %%
new_string = [item for item in new_string if item != '']
# %%
print(new_string)
# %%
joined_string = " ".join(map(str, new_string))
print(joined_string)
# %%
"" in joined_string
# %%
print(joined_string)
# %%
updated_string = re.sub(r'('',\s)+', '', joined_string)
print(updated_string)
# %%


# %%
