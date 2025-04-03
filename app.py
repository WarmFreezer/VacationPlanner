



import streamlit as st
import plotly as py
import pandas as pd
import numpy as np
import altair as alt

st.header('Creating a UI')
st.write('This is not out UI finle design')
st.write('Creating place holder for UI')

st.write('Hello, *World!* :vacation mode:')

st.write(1234)

df = pd.DataFrame({'1st column' : [1, 2, 3, 4],
                   '2nd column': [10, 20, 30, 40]})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


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