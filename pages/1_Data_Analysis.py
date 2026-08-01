import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Student Perfomance Analysis")

# Load Data
data = pd.read_csv("data/students.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(data)

# Summary Statistics
st.subheader("Summary Statistics")
st.write(data.describe())

# Study Hours Relationship
st.subheader("Study Hours vs Final Score")

fig, ax = plt.subplots()

ax.scatter(
    data["study_hours"],
    data["final_score"]
)

ax.set_xlabel("Study Hours")
ax.set_ylabel("Final Score")

st.pyplot(fig)

# Sleep Hours Relationship
st.subheader("Sleep Hours vs Final Score")

fig, ax = plt.subplots()

ax.scatter(
    data["sleep_hours"],
    data["final_score"]
)

ax.set_xlabel("Sleep Hours")
ax.set_ylabel("Final Score")

st.pyplot(fig)

# Previous Score Relationship
st.subheader("Previous Score vs Final Score")

fig, ax = plt.subplots()

ax.scatter(
    data["previous_score"],
    data["final_score"]
)

ax.set_xlabel("Previous Score")
ax.set_ylabel("Final Score")

st.pyplot(fig)

# Correlation Analysis

st.subheader("Feature Correlation")

correlation = data.corr()

st.write(correlation)

st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="viridis",
    ax=ax
)

st.pyplot(fig)