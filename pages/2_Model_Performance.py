import streamlit as st
import pandas as pd

st.title("🤖 Model Performance")

# Create Results Table
results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [0.68, 1.22],
    "R2 Score": [0.97, 0.91]
})

st.subheader("Model Comparison")
st.dataframe(results)

st.subheader("Best Model")
st.success("Linear Regression was selected as the best model.")

st.markdown("### Why was it selected?")
st.write("- Lower Mean Absolute Error (0.68)")
st.write("- Higher R2 Score (0.97)")
st.write("- Simpler Model with Better Generalization on this Dataset.")

st.markdown("### Interpretation")
st.info(
    "The Linear Regression Model predicts student scores more accurately than" \
    " the Random Forest model for this dataset."
)