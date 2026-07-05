import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Load the student dataset
# (Using a synthetic student dataset here — swap this out for your actual CSV,
# e.g. df = pd.read_csv("student_data.csv"))
np.random.seed(42)
n = 200
df = pd.DataFrame({
    "study_hours": np.random.uniform(0, 10, n),
    "attendance": np.random.uniform(50, 100, n),
    "sleep_hours": np.random.uniform(4, 9, n),
})
df["final_score"] = (
    5 * df["study_hours"] + 0.5 * df["attendance"] + 2 * df["sleep_hours"]
    + np.random.normal(0, 5, n)
)

X = df[["study_hours", "attendance", "sleep_hours"]]
y = df["final_score"]

test_sizes = [0.1, 0.2, 0.3]
results = []

for ts in test_sizes:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=ts, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    print(f"test_size={ts}")
    print(f"  Train size: {len(X_train)}, Test size: {len(X_test)}")
    print(f"  R²: {r2:.4f}, RMSE: {rmse:.4f}\n")

    results.append((ts, len(X_train), len(X_test), r2, rmse))

best = max(results, key=lambda r: r[3])
print(f"Best split: test_size={best[0]} (R²={best[3]:.4f})")