#%%
import pandas as pd
import numpy as np
import re
#%%
def clean_tabular_data(file == str):
    #%%
    data = pd.read_csv(file)
    # %%
    print(data.head())
    # %%
    ratings_column = data[["Value_rate",  "Cleanliness_rate", "Accuracy_rate", 
            "Communication_rate", "Location_rate", "Check-in_rate"]]
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
file = "tabular_data/AirBnBData.csv"
data = pd.read_csv(file)
# %%
data['Description'] = data["Description"].str.replace("'About this space', ", '')
data['Description'] = " ".join(map(str, data["Description"]))
for x in enumerate(data["Description"]):
    print(x)
# %%
