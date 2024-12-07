# import modules
import streamlit as st
from sensor_api import generate_sensor_data,get_patient_data
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import seaborn as sns
#App data starts here

@st.cache_data  # 👈 Add the caching decorator
def load_data():
    sensor_data = generate_sensor_data(hours=25)
    patient_data=get_patient_data()
    return sensor_data,patient_data
sensor_data,patient_data=load_data()


my_params=[ 'timestamp','heart_rate'  ,'systolic_bp'  ,'diastolic_bp' , 'body_temp' ]


# Generate data for last x hours

data_time_range=datetime.now()-timedelta(24)

# Save the data to a CSV file
# sensor_data.to_csv('sensor_data_last_24hrs.csv', index=False)


# print(sensor_data.head())


# app gui starts here-----------------------------------------------
st.logo(
        "https://cdn.pixabay.com/photo/2021/11/20/03/17/doctor-6810751_1280.png",
        
    )

with st.sidebar:
    

  
    st.header("Medical Portal")

   
        
    st.divider()
    st.image(patient_data['profile_pic'],width=100)
    st.write("Name ")
    st.markdown(f"{patient_data["name"]}")
    
    st.divider()
    st.write("Address ")
    st.markdown(f"{patient_data["Address"]}")
    st.divider()

  
    st.write("Contact")
    st.markdown(f"{patient_data['contact']}")
    st.markdown(f"{patient_data['mail']}")
    st.divider()

  
        
    
       







# Title
st.title("Medical Portal !!!")
# st.line_chart(data=sensor_data,  x='timestamp', y='heart_rate',  use_container_width=True)



st.divider()



    
c1, c2,c3 = st.columns(3,vertical_alignment='center')
with c1:
            st.metric(label="Blood Group", value=patient_data['blood_group'],  delta_color="inverse")
with c2:
            st.metric(label="Age", value=patient_data['age'] )
with c3:
            st.metric(label="Weight", value=patient_data['weight'], delta=-2, )


st.divider()


st.header("Statistics")
time_frame= ["last 24 hours","last 12 hours","last 6 hours","last 1 hour"]


time_selectbox = st.selectbox("Select data ",time_frame)
# st.write("You selected:", time_selectbox)

if time_selectbox==time_frame[0] :
        data_time_range=datetime.now()-timedelta(hours=24)
        # print(data_time_range)
        # sensor_data_to_plot=sensor_data[sensor_data['timestamp'] >= data_time_range]
elif time_selectbox==time_frame[1] :
        data_time_range=datetime.now()-timedelta(hours=12)
        # print(data_time_range)
        # sensor_data_to_plot=sensor_data[sensor_data['timestamp'] >= data_time_range]
elif time_selectbox==time_frame[2] :
        data_time_range=datetime.now()-timedelta(hours=6)
        # print(data_time_range)
        # sensor_data_to_plot=sensor_data[sensor_data['timestamp'] >= data_time_range]
elif time_selectbox==time_frame[3] :
        data_time_range=datetime.now()-timedelta(hours=1)
        # sensor_data_to_plot=sensor_data[sensor_data['timestamp'] >= data_time_range]
        # print(data_time_range)
        
sensor_data_to_plot=sensor_data[sensor_data['timestamp'] >= data_time_range]


tab1, tab2, tab3,tab4 = st.tabs(my_params[1:])

with tab1:
    st.header(my_params[1])
    st.line_chart(data=sensor_data_to_plot,  x='timestamp', y=my_params[1],  use_container_width=True)
with tab2:
    st.header(my_params[2])
    st.line_chart(data=sensor_data_to_plot,  x='timestamp', y=my_params[2],  use_container_width=True)
with tab3:
    st.header(my_params[3])
    st.line_chart(data=sensor_data_to_plot,  x='timestamp', y=my_params[3],  use_container_width=True)
with tab4:
    st.header(my_params[4])
    st.line_chart(data=sensor_data_to_plot,  x='timestamp', y=my_params[4],  use_container_width=True)


# sensor_data.describe()['heart_rate']['mean']
st.divider()

st.table(sensor_data_to_plot[my_params[1:]].describe().T[['mean','min','max']])



