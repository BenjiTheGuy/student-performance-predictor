Student Performance Predictor

## LIVE DEMO

[Open the App](https://student-performance-predictor-4t4xhuu2rwucuibmonlbc7.streamlit.app/)

A simple machine learning web application that predicts a student's final score based on input labels:

- Study hours
- Sleep hours
- Previous score

Technologies Used:

- Python
- pandas
- scikit-learn
- Streamlit

Features:

- Train a linear regression model
- Save and load the trained model
- Interactive web interface
- Display prediction results
- Show model evaluation metrics

Model Performance:

- Mean Absolute Error (MAE): 0.68
- R² Score: 0.97

Run Locally:

- pip install -r requirements.txt
- streamlit run app.py

Project Structure:

StudentPerformancePredictor/
│
├── Home.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
├── data/
├── model/
└── venv/
