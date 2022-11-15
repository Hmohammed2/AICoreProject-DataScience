#%%
import pandas as pd
import numpy as np
import re
<<<<<<< HEAD
import os

from macpath import join

=======
>>>>>>> refs/remotes/origin/main
#%%

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
            cleaned_string = re.sub(r"{}".format(pattern), '' ,new_string)
            print(cleaned_string)
            return cleaned_string
        else:
            raise ValueError

    def save_data():
        user_input = input("Do you want to upload your data into the cloud? (yes/no): ")
        while True:
            if user_input.lower() == "yes":
                data.to_csv('clean_tabular_data.csv')
            elif user_input.lower() == "no":
                break

# %%
if __name__ == "__main__":
    
    file = "tabular_data/AirBnBData.csv"
    
    clean_tabular_data(file)
# %%
<<<<<<< HEAD
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


=======
file = "tabular_data/AirBnBData.csv"
data = pd.read_csv(file)
# %%
data['Description'] = data["Description"].str.replace("'About this space', ", '')
data['Description'] = " ".join(map(str, data["Description"]))
for x in enumerate(data["Description"]):
    print(x)
>>>>>>> refs/remotes/origin/main
# %%
