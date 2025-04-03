"""
import streamlit as st
#import plotly as py

# creating a header text 
st.header('st.button')

# using conditional statements if and else for printing alternative messages
# the button() command accepts the label input 
if st.button('Say hello'):

    # write() command is used to write text in the app
    st.write('Hello, hi there')
else:
    st.write('Goodbye')

"""

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

# Using object notation
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