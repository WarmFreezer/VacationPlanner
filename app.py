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

st.header('st.write')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame({'first column' : [1, 2, 3, 4],
                   'second column': [10, 20, 30, 40]})
st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a DataFrame.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)