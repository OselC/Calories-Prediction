# Calories Prediction App

A machine learning–powered web application built with **Streamlit** to predict the number of calories burned during physical activity based on physiological features.
The model is trained using a **Linear Regression pipeline** with proper preprocessing:
- Numerical features are standardized using `StandardScaler`
- Categorical features (e.g., Gender) are encoded using `OneHotEncoder`
- A `ColumnTransformer` ensures consistent data transformation during training and inference

Streamlit: https://calories-prediction-jmukbkpuqgrgzzrxwsv6rq.streamlit.app/

## 📊 Dataset
Kaggle: https://www.kaggle.com/datasets/ruchikakumbhar/calories-burnt-prediction

## ✨ Features
- Predict calories burned from:
  - Age  
  - Gender  
  - Height  
  - Weight  
  - Exercise Duration  
  - Heart Rate  
  - Body Temperature  
- End-to-end ML pipeline (preprocessing + model) saved and loaded with `joblib`
- Interactive user interface built with Streamlit
- Real-time prediction with a single click

## 🛠 Tech Stack
- Python  
- Scikit-learn (Linear Regression, Pipeline, ColumnTransformer)  
- Streamlit  
- Pandas, NumPy  
- Joblib  

Evaluation metrics:
- MAE  
- RMSE  
- R² Score  

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py


