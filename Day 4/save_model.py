import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load data
df = pd.read_csv("Day 4/student_mat.csv", sep=',')  # adjust filename/sep as needed

# Based on earlier feature comparison, G1 (or G1+G2) was the strongest predictor.
# Using all numeric features here since that gave the best overall RMSE/R².
numeric_df = df.select_dtypes(include='number')
X = numeric_df.drop(columns=['G3'])
y = numeric_df['G3']

feature_names = X.columns.tolist()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)
print(f"Trained model - RMSE: {rmse:.4f}, R²: {r2:.4f}")

# Save the model AND the feature names (so the next file knows the expected column order)
with open("best_model.pkl", "wb") as f:
    pickle.dump({"model": model, "features": feature_names}, f)

print("Model saved to best_model.pkl")