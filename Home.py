import streamlit as st
import pickle
import pandas as pd

with open(r"model/student_model.pkl", 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Student Predictor", page_icon="📚")

st.title("📚 Student Performance Predictor")

st.write("Enter a student's study hours, sleep hours, and previous score" \
" to predict the expected final score."
)

study_hours = st.slider("Study Hours", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
previous_score = st.slider("Previous Score", 0, 100, 50)

if st.button("Predict"):
    prediction = model.predict([
        [
            study_hours,
            sleep_hours,
            previous_score
        ]
    ])

    st.success(f"Predicted Final Score: {prediction[0]:.2f}%")

st.subheader('Model Information')
st.write('Model: Linear Regression')
st.write('Features used:')
st.write('- Study Hours')
st.write('- Sleep Hours')
st.write('- Previous Score')

col1, col2 = st.columns(2)

with col1:
    st.metric('MAE', '0.68')

with col2:
    st.metric('R² Score', '0.97')