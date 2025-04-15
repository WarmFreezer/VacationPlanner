



import streamlit as st
from urllib3 import add_stderr_logger
import plotly as py
import pandas as pd
import numpy as np
import altair as alt


st.header('Creating a UI')
st.write('This is not our UI finle design')
st.write('Creating place holder for UI')



# creating a side bar
add_selectbox = st.sidebar.selectbox(
    "Where would you like to travel to",
    ("Example 1", "Example 2", "Example 3")



)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


# adding a slide bar
# Example 1
st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')



st.header('Services:')

option = st.selectbox(
     'Select the service you want',
     ('Service 1', 'Service 2', 'Service 3'))

st.write('You chose the following service ', option)


st.header('multiselect')

options = st.multiselect(
     'What are your top choices',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)


# map 
df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,
        "col2": np.random.randn(1000) / 50 + -122.4,
        "col3": np.random.randn(1000) * 100,
        "col4": np.random.rand(1000, 4).tolist(),
    }
)

st.map(df, latitude="col1", longitude="col2", size="col3", color="col4")


"""
#---App Functions Separate from UI Below---#
budget 
departure
destinationState
d_date
r_date
vacationers
rental

flightData #List for departing flights which need to be passed to WebSearchAI to find an itinerary on the destination city (Odd indexes should be departing flights)
vacationData #List for vacation info which will be combined with flightData to creat a list of trip objects
tripList #Will need to define a new object based on all departing flights, not returning ones
"""