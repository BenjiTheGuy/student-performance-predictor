import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load Data
data = pd.read_csv("data/students.csv")

X = data[
    [
        "study_hours",
        "sleep_hours",
        "previous_score"
    ]
]

y = data["final_score"]

# Train Random Forest
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Get Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(by="Importance", ascending=False)

print(importance)

# Save Results
importance.to_csv("data/feature_importance.csv", index=False)

print("Feature Importance Saved!")