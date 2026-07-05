import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your student dataset
df = pd.read_csv("Day 4/student_mat.csv", sep=',')  # adjust as needed

# Target
y = df['G3']

# Features to test one at a time
features_to_test = ['studytime', 'absences', 'G1']

results = []

for feature in features_to_test:
    X = df[[feature]]  # double brackets keep it a 2D DataFrame

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    results.append({
        "feature": feature,
        "rmse": rmse,
        "r2": r2,
        "coefficient": model.coef_[0]
    })

    print(f"Feature: {feature}")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  R²: {r2:.4f}")
    print(f"  Coefficient: {model.coef_[0]:.4f}\n")

# Compare
results_df = pd.DataFrame(results).sort_values("rmse")
print("=== Ranked by RMSE (lower is better) ===")
print(results_df.to_string(index=False))

best_feature = results_df.iloc[0]["feature"]
print(f"\nBest single predictor: {best_feature}")