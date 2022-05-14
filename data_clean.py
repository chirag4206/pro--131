from os import access
import pandas as pd
import csv

df = pd.read_csv("merged_data.csv")
print(df.shape)

del df["Luminosity"] 
del df["Unnamed: 0"]
del df["Star_names"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
del df["Unnamed: 6"]
del df["Unnamed: 0.1"]

print(df.shape)
print(list(df))


df.to_csv("data_cleaned.csv")
