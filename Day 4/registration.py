import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your student dataset
df = pd.read_csv("Day 4/student_mat.csv", sep=',')  # adjust filename/separator as needed

# Select ALL numeric columns as features
numeric_df = df.select_dtypes(include='number')

# Target is G3, features are every other numeric column
X = numeric_df.drop(columns=['G3'])
y = numeric_df['G3']

feature_names = X.columns.tolist()
print("Features used:", feature_names)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

print(f"\nRMSE: {rmse:.4f}")
print(f"R² score: {r2:.4f}")

# Predict for a new student of your choice
# Build a single-row DataFrame with the same feature columns, in the same order
new_student = pd.DataFrame([{
    col: X[col].mean() for col in feature_names  # start from average values
}])

# Customize a few values for "your" student
# (edit these to match columns actually in your dataset, e.g. studytime, absences, G1, G2)
if 'studytime' in new_student.columns:
    new_student['studytime'] = 4      # studies a lot
if 'absences' in new_student.columns:
    new_student['absences'] = 2       # rarely absent
if 'G1' in new_student.columns:
    new_student['G1'] = 15            # did well on first grade
if 'G2' in new_student.columns:
    new_student['G2'] = 16            # did well on second grade

predicted_grade = model.predict(new_student)[0]
print(f"\nPredicted G3 for new student: {predicted_grade:.2f}")