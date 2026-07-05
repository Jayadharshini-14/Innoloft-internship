import pandas as pd

df = pd.read_csv("Day 3/student_mat.csv", sep=",")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 3 rows:")
print(df.tail(3))

print("\nInternet access count:")
print(df["internet"].value_counts())