import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

data = pd.read_csv(r"data\students.csv")

X = data[
    [
        "study_hours",
        "sleep_hours",
        "previous_score"
    ]
]

y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42)
}

results = {}

# Train and Evaluate Models
for name, model in models.items():
    model.fit(X_train, y_train)\

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    results[name] = {
        "MAE": mae,
        "R2": r2
    }

    print(name)
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R2 Score: {r2:.2f}")
    print("-----------------------")

best_model = models["Linear Regression"]

with open(r"model\student_model.pkl", "wb") as file:
    pickle.dump(best_model, file)

print("Best Model Trained and Saved Successfully.")