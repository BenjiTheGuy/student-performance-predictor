import pickle

with open(r"model\student_model.pkl", "rb") as file:
    model = pickle.load(file)

study_hours = 5
sleep_hours = 7
previous_score = 75

prediction = model.predict([
    [
        study_hours,
        sleep_hours,
        previous_score
    ]
])

print(f"Predicted Score: {prediction[0]:.2f}")