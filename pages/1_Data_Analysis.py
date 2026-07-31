import streamlit as st
import pandas as pd

st.title("Student Perfomance Analysis")

# Load Data
data = pd.read_csv("data/students.csv")

st.subheader("Dataset Preview")

st.dataframe(data)

st.subheader("Study Hours vs Final Score")

st.scatter_chart(
    data,
    x="study_hours",
    y="final_score"
)

st.subheader("Sleep Hours vs Final Score")

st.scatter_chart(
    data,
    x="sleep_hours",
    y="final_score"
)

st.subheader("Previous Score vs Final Score")

st.scatter_chart(
    data,
    x="previous_score",
    y="final_score"
)