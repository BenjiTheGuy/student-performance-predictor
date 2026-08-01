import streamlit as st
import pandas as pd

st.title("📌 Feature Importance")

# Load Importance Data
importance = pd.read_csv("data/feature_importance.csv")

st.subheader("Feature Importance Table")
st.dataframe(importance)

st.subheader("Feature Importance Chart")

chart_data = importance.set_index("Feature")
st.bar_chart(chart_data)

# Explain the Top Feature
top_feature = importance.iloc[0]["Feature"]

st.success(f"The most important feature is: {top_feature}")