import pandas as pd
from sklearn.linear_model import LinearRegression
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

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

with open(r"model\student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Trained and Saved Successfully.")