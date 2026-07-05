import pandas as pd

# Function to generate EDA report
def eda_report(df):
    print("=" * 50)
    print("EDA REPORT")
    print("=" * 50)

    # Shape
    print("\nShape:")
    print(df.shape)

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Numeric summary
    print("\nNumeric Columns Summary:")
    print(df.describe())

    # Object columns value counts
    print("\nValue Counts for Object Columns:")
    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        print(f"\nColumn: {col}")
        print(df[col].value_counts())

    print("=" * 50)


# Test on first CSV
df1 = pd.read_csv("Day 3/student_mat.csv")
print("\nREPORT FOR student_mat.csv")
eda_report(df1)

# Test on second CSV
df2 = pd.read_csv("Day 3/students.csv")
print("\nREPORT FOR students.csv")
eda_report(df2)