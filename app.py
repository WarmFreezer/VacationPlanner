#External classes here
import streamlit as st
import plotly as py

#Classes internal to project here
import VacationData
import FlightScraper
import WebSearchAI

# creating a header text 
st.header('st.button')

# using conditional statements if and else for printing alternative messages
# the button() command accepts the label input 
if st.button('Say hello'):

    # write() command is used to write text in the app
    st.write('Hello, hi there')
else:
    st.write('Goodbye')


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