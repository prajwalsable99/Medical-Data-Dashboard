# Take the data generated from this code below

import pandas as pd
import numpy as np
from datetime import datetime,timedelta

# Function to generate random sensor data
def generate_sensor_data(start_time, end_time, freq='1T'):
    time_range = pd.date_range(start=start_time, end=end_time, freq=freq)
    data = {
        'timestamp': time_range,
        'heart_rate': np.random.randint(60, 100, size=len(time_range)),  # Heart rate in bpm
        'systolic_bp': np.random.randint(110, 140, size=len(time_range)),  # Systolic blood pressure in mmHg
        'diastolic_bp': np.random.randint(70, 90, size=len(time_range)),  # Diastolic blood pressure in mmHg
        'body_temp': np.random.uniform(36.5, 37.5, size=len(time_range))  # Body temperature in °C
    }
    return pd.DataFrame(data)

# Generate data for one day
# start_time = datetime.datetime(2024, 8, 8, 0, 0)
# end_time = datetime.datetime(2024, 8, 8, 23, 59)

# Generate data for last 24 hours
end_time = datetime.now()
start_time = end_time - timedelta(hours=24)

sensor_data = generate_sensor_data(start_time, end_time)

# Display the first few rows of the generated data
print(sensor_data.head())

# Save the data to a CSV file
sensor_data.to_csv('sensor_data_last_24hrs.csv', index=False)

# •	Timestamp Generation: We generate timestamps for every minute (freq='1T') within the specified date range.
# •	Heart Rate: Random values between 60 and 100 bpm.
# •	Systolic Blood Pressure: Random values between 110 and 140 mmHg.
# •	Diastolic Blood Pressure: Random values between 70 and 90 mmHg.
# •	Body Temperature: Random values between 36.5 and 37.5 °C.

# Imagine that a sensor data has been generated and proceed
# Design and implement an end-to-end IoT solution for a healthcare product that monitors patient vitals in real-time, provides predictive analytics for early detection of health issues, and ensures secure data transmission and storage. The solution should include the following components:
