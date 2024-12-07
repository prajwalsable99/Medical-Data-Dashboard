
# Medical Data Dashboard

This repository provides tools and a web application to analyze medical data, visualize patient vitals, and predict health risks using machine learning. The project aims to deliver an efficient solution for monitoring, analyzing, and predicting patient health status based on vital signs.

---

## **Directory Structure**
```
/
├── ___pycache___/
├── .ipynb_checkpoints/
├── app.py                   # Streamlit app for data visualization and prediction
├── Model-Generation.ipynb   # Jupyter notebook for training and saving the machine learning model
├── model.pkl                # Pre-trained Random Forest model for health risk prediction
├── realistic_medical_data.csv  # Sample dataset with medical vitals and health status
├── sensor_api.py            # Module for generating and simulating real-time sensor data
```

---

## **Features**
### **1. Streamlit Application (`app.py`)**
- **Patient Dashboard**: Displays patient details such as name, blood group, age, and weight.
- **Real-Time Data Visualization**: 
  - Line charts for vitals like heart rate, blood pressure, and body temperature.
  - Adjustable timeframes (last 24, 12, 6, or 1 hour).
- **Descriptive Statistics**: Summary metrics for all vitals (mean, min, max).
- **Health Risk Prediction**:
  - Input vitals to predict health status (`Critical`, `Risk`, `Healthy`) using a Random Forest classifier.

### **2. Machine Learning Model (`Model-Generation.ipynb`)**
- Trains a Random Forest Classifier using the dataset (`realistic_medical_data.csv`).
- Encodes health status labels (`Critical`, `Risk`, `Healthy`).
- Saves the model as `model.pkl` for deployment.

### **3. Sensor API (`sensor_api.py`)**
- Simulates real-time sensor data for vitals (heart rate, systolic/diastolic blood pressure, body temperature).
- Provides a patient data mock API.

---

## **How to Use**

### **1. Clone the Repository**


### **2. Install Dependencies**
Ensure you have Python 3.7 or later installed. Use `pip` to install required packages:
```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Start the Streamlit application:
```bash
streamlit run app.py
```

### **4. Access the Application**
Open your web browser and navigate to:
```
http://localhost:8501
```

---

## **File Details**

### **1. `app.py`**
The main application file that integrates:
- Sensor data visualization.
- Real-time data filtering by timeframe.
- Machine learning-based health status prediction.

### **2. `Model-Generation.ipynb`**
Jupyter notebook for:
- Data preprocessing and exploratory data analysis.
- Machine learning model training and evaluation.
- Exporting the trained model as `model.pkl`.

### **3. `sensor_api.py`**
Utility module for:
- Generating simulated time-series sensor data.
- Mocking patient details and API integration.

### **4. `realistic_medical_data.csv`**
Sample dataset with columns:
- `Heart Rate`, `Systolic BP`, `Diastolic BP`, `Temperature`, `Health Status`.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: For creating interactive dashboards and web applications.
- **scikit-learn**: For machine learning model development.
- **Pandas**: For data manipulation.
- **Matplotlib/Seaborn**: For data visualization.

---

## **Future Enhancements**
1. **Real-Time Data Integration**: Support for streaming data from IoT devices.
2. **Alerts and Notifications**: Add thresholds for vitals to notify users of health risks.
3. **Multi-Patient Support**: Extend the dashboard for monitoring multiple patients.
4. **Cloud Integration**: Deploy on cloud platforms for remote access and scalability.

---

## **Contributing**
Contributions are welcome! Please fork this repository and submit a pull request with your changes. Ensure the code is well-documented and adheres to the existing coding style.

---

Enjoy building with **Medical Data Analysis**! 🎉



