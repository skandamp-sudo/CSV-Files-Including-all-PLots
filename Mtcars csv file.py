import pandas as pd

df = pd.read_csv('D:\AI&ML\mtcars.csv')


print("First 5 rows of the dataset:")
print(df.head())

print("Summary statistics of the dataset:")
print(df.describe())

print("Column names of the dataset:")
print(df.columns)