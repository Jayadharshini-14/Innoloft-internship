import pandas as pd

df = pd.read_csv("Day 3/students.csv")

print("Original DataFrame:")
print(df)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("Unknown")
df["Name"] = df["Name"].fillna("Unknown")

print("\nDataFrame After Filling Missing Values:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())