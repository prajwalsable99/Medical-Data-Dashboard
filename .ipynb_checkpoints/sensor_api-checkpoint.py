

import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import joblib
# Function to generate random sensor data
def generate_sensor_data(hours, freq='1T'):
    end_time = datetime.now()
    start_time = end_time - timedelta(hours= hours)
    time_range = pd.date_range(start=start_time, end=end_time, freq=freq)
    data = {
        'timestamp': time_range,
        'heart_rate': np.random.randint(60, 100, size=len(time_range)),  # Heart rate in bpm
        'systolic_bp': np.random.randint(110, 140, size=len(time_range)),  # Systolic blood pressure in mmHg
        'diastolic_bp': np.random.randint(70, 90, size=len(time_range)),  # Diastolic blood pressure in mmHg
        'body_temp': np.random.uniform(36.5, 37.5, size=len(time_range))  # Body temperature in °C
    }
    df= pd.DataFrame(data)  
    df['body_temp']=df['body_temp'].apply(int)
    df['timestamp']= pd.to_datetime( df['timestamp'])
    return df




def get_patient_data(patient_id=1):

    return {

        "name": "John doe",
        "profile_pic": 'https://cdn.pixabay.com/photo/2018/11/08/23/52/man-3803551_640.jpg',
        "blood_group": "A+",
        "age":33,
        "weight": 72,
        "Address":"Street:  1, Parvati Nivas, Chandavarkar Rd, Opp Dattani Trade Centre, Borivali (west)",
        "contact":"+91 7517780448",
        "mail":"jdoe123@gmail.com"
        
    }


model=joblib.load('model.pkl')
def getPrediction(heart_rate  ,systolic_bp  ,diastolic_bp , body_temp):
    return model.predict([[heart_rate  ,systolic_bp  ,diastolic_bp , body_temp]])
