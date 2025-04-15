#Internal libraries here
from TripManager import TripManager

#External libraries here
import streamlit as st
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "trips.json")

tripManager = TripManager(10000, "Departure", "Florida", "Miami", "05-16-2025", "05-23-2025", 2)
trips = tripManager.MainSearch() #Stores all trips returned from main search

# Load your JSON data
with open(file_path, 'r') as f:
    data = json.load(f)

# Main app title
st.title("🧳 Budget Trip Planner")

# Sidebar for selecting the destination
st.sidebar.header("Plan Your Trip")
location_names = [place["location"] for place in data]
selected_location = st.sidebar.selectbox("Choose a destination:", location_names)

# Find the selected location details
selected_place = next((place for place in data if place["location"] == selected_location), None)

# Show selections
if selected_place:
    st.sidebar.subheader("Choose Amenities")
    amenity_options = [a["name"] for a in selected_place["amenities"]]
    selected_amenities = st.sidebar.multiselect("Select amenities:", amenity_options)

    st.sidebar.subheader("Choose Entertainment")
    entertainment_options = [e["name"] for e in selected_place["entertainment"]]
    selected_entertainment = st.sidebar.multiselect("Select entertainment:", entertainment_options)

    st.sidebar.subheader("Choose Places to Stay")
    stay_options = [s["name"] for s in selected_place["places_to_stay"]]
    selected_stays = st.sidebar.multiselect("Select places to stay:", stay_options)

    st.sidebar.subheader("Choose Food Options")
    food_options = [f["name"] for f in selected_place["food"]]
    selected_food = st.sidebar.multiselect("Select food options:", food_options)

    # Main Page Output
    st.header(f"Trip Details for {selected_place['location']}, {selected_place['city']}, {selected_place['state']}")

    # 🛝 Show selected amenities (no expander!)
    st.subheader("🛝 Selected Amenities")
    if selected_amenities:
        for amenity in selected_place["amenities"]:
            if amenity["name"] in selected_amenities:
                st.write(f"• **{amenity['name']}** — {amenity['estimated_price']}")
    else:
        st.info("No amenities selected.")

    # 🎭 Show selected entertainment
    st.subheader("🎭 Selected Entertainment")
    if selected_entertainment:
        for entertainment in selected_place["entertainment"]:
            if entertainment["name"] in selected_entertainment:
                st.write(f"• **{entertainment['name']}** — {entertainment['estimated_price']}")
    else:
        st.info("No entertainment selected.")

"""
#---App Functions Separate from UI Below---#
budget
departure
destinationState
d_date
r_date
vacationers
rental

    # 🍔 Show selected food options
    st.subheader("🍔 Selected Food Options")
    if selected_food:
        for food in selected_place["food"]:
            if food["name"] in selected_food:
                st.write(f"• **{food['type']}** — {food['name']} — {food['estimated_price_per_meal']}")
    else:
        st.info("No food options selected.")
