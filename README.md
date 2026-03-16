# ⚡ Energy Consumption Prediction using Machine Learning

A Machine Learning regression project that predicts building energy consumption based on environmental and operational factors such as temperature, humidity, occupancy, HVAC usage, and lighting usage.

The project also includes a Streamlit web application deployed on Streamlit Cloud for interactive predictions.

## 🚀 Live Demo

### Streamlit App:
👉 https://energyconsumptionpredictionmodel-bgfso5vvorr7mjhp5yegeh.streamlit.app/

## 📌 Project Overview

Energy consumption forecasting helps improve energy efficiency, cost optimization, and sustainability in buildings.

This project uses Machine Learning Regression (Random Forest) to estimate energy consumption using various input features.

## 📊 Dataset Features

The dataset includes the following variables:

| Feature | Description |
|--------|-------------|
| Timestamp | Date and time of observation |
| Temperature | Ambient temperature |
| Humidity | Humidity level |
| SquareFootage | Size of the building |
| Occupancy | Number of occupants |
| HVACUsage | HVAC system usage |
| LightingUsage | Lighting energy usage |
| RenewableEnergy | Renewable energy generation |
| DayOfWeek | Day of the week |
| Holiday | Whether it is a holiday |
| EnergyConsumption | Target variable (energy usage) |
## 🧠 Machine Learning Model

Algorithm used:

### Random Forest Regressor

Why Random Forest?

- Handles nonlinear relationships well

- Robust to outliers

- Works well with tabular datasets

- Requires minimal feature scaling

## 🔎 Exploratory Data Analysis (EDA)

EDA was performed to understand patterns in the dataset:

### Key analyses included:

- Energy consumption distribution

- Temperature vs energy consumption

- HVAC usage impact

- Occupancy vs energy demand

- Correlation heatmap

- Hourly energy consumption patterns

### EDA notebook:
```
notebooks/eda_analysis.ipynb
```
## 🏗 Project Structure
```
energy_consumption_prediction_model
│
├── app
│   └── streamlit_app.py        # Streamlit web application
│
├── data
│   └── Energy_consumption.csv  # Dataset
│
├── models
│   └── energy_model.pkl        # Trained ML model
│
├── notebooks
│   └── eda_analysis.ipynb      # Exploratory Data Analysis
│
├── src
│   ├── preprocess.py           # Data preprocessing pipeline
│   ├── train_model.py          # Model training script
│   └── predict.py              # Prediction utilities
│
├── requirements.txt
├── runtime.txt
└── README.md
```
## ⚙️ Installation

### Clone the repository:
```
git clone https://github.com/yourusername/energy_consumption_prediction_model.git
cd energy_consumption_prediction_model
```
Install dependencies:
```
pip install -r requirements.txt
```
## 🧪 Train the Model

Run the training script:
```
python src/train_model.py
```
This will generate:
```
models/energy_model.pkl
```
## 💻 Run the Streamlit App

Start the application:
```
streamlit run app/streamlit_app.py
```
The app will open in your browser.

## 🧾 Model Evaluation

Model performance metric used:

### R² Score

The model achieved a strong predictive performance for estimating building energy consumption.

## 🛠 Technologies Used

- Python

- Pandas

- NumPy

- Scikit-learn

- Matplotlib

- Seaborn

- Joblib

- Streamlit

## 🌍 Deployment

The application is deployed using:

### Streamlit Cloud

Deployment steps:

1. Push project to GitHub

2. Connect repository to Streamlit Cloud

3. Select app/streamlit_app.py

4. Deploy

## 📈 Future Improvements

### Potential improvements:

- Hyperparameter tuning

- Advanced feature engineering

- XGBoost / LightGBM models

- Real-time data integration

- Dashboard visualization

## 👨‍💻 Author

### Shani Yadav

Machine Learning Enthusiast | Data Science Learner
