import pickle
import joblib
from sklearn.preprocessing import MinMaxScaler
import numpy as np

rf_model = joblib.load("model/car_sales_rf_model.pkl")
def prediction_cancer(features):
    predictions = rf_model.predict([features])
    return predictions[0]