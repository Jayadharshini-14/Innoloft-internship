import pandas as pd

# Create a DataFrame with 5 students
data = {
    "Name": ["Jaya", "Anu", "Rahul", "Priya", "Karthik"],
    "Age": [19, 20, 18, 21, 19],
    "City": ["Chennai", "Coimbatore", "Madurai", "Salem", "Trichy"],
    "Marks": [85, 45, 72, 90, 38]
}

df = pd.DataFrame(data)

# Print first 5 rows
print("First 5 Rows:")
print(df.head())

# Print shape
print("\nShape:")
print(df.shape)

# Print data types
print("\nData Types:")
print(df.dtypes)

# Add a new column 'Result'
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Print updated DataFrame
print("\nUpdated DataFrame:")
print(df)