#%%
import pandas as pd
import numpy as np
import re

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
def combine_description_strings(column, pattern):
    if isinstance(column, pd.Series):
        new_string = " ".join(map(str, column))
        print(re.findall(f'r"{pattern}"', new_string))
        cleaned_string = re.sub(f'r"{pattern}"', '' ,new_string)
        print(cleaned_string)
        return cleaned_string
    else:
        raise ValueError
# %%
type(file["Description"])
# %%
