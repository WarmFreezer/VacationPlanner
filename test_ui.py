
import streamlit as st
import plotly as py

# creating a header text 
st.header('st.button')

# using conditional statements if and else for printing alternative messages
# the button() command accepts the label input 
if st.button('Say hello'):

    # write() command is used to write text in the app
    st.write('Hello, hi there')
else:
    st.write('Goodbye')