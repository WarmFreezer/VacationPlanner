import streamlit as st
from datetime import date
from TripManager import TripManager

# --- Page Title ---
st.title("😊 Vacation Budget Planner 📖")

# --- Sidebar: Budget Setup ---
st.sidebar.header("1. Budget Setup")

# User Inputs
budget: int = 0
budget_input = st.sidebar.text_input("Enter your total vacation budget ($)", placeholder="e.g., 2000")

try:
    budget = float(budget_input) if budget_input else 0.0
except ValueError:
    budget = 0.0
    st.sidebar.error("❗ Please enter a valid number for the budget.")

# --- Sidebar: Trip Information ---
st.sidebar.header("2. Trip Info")

states = ["Florida", "California", "Texas", "Kentucky", "New York"]

departure: str = st.sidebar.selectbox("Departure State", states)
destinationState: str = st.sidebar.selectbox("Destination State", states)
destinationCity: str = st.sidebar.text_input("Destination City", placeholder="e.g., Miami")

departureDate_obj = st.sidebar.date_input("Departure Date", min_value=date.today())
returnDate_obj = st.sidebar.date_input("Return Date", min_value=departureDate_obj)

departureDate: str = departureDate_obj.strftime("%m/%d/%Y")
returnDate: str = returnDate_obj.strftime("%m/%d/%Y")

vacationers: int = int(st.sidebar.number_input("Number of Vacationers", min_value=1, step=1))

# --- Validate and Show Summary on Main Page ---
if st.sidebar.button("Validate Vacation Plan") and budget > 0:
    st.header("📊 Vacation Plan Summary")

    st.success("✅ Budget and trip information submitted successfully!")

    st.markdown(f"""
    **📍 Departure State:** {departure}  
    **🏖️ Destination:** {destinationCity}, {destinationState}  
    **📅 Dates:** {departureDate} to {returnDate}  
    **🧑 Travelers:** {vacationers}  
    **💰 Budget:** ${budget:,.2f}
    """)

    # Use dynamic user inputs to create TripManager
    user_trip_manager = TripManager(
        budget=budget,
        departure=departure,
        destinationState=destinationState,
        destinationCity=destinationCity,
        departureDate=departureDate,
        returnDate=returnDate,
        vacationers=vacationers
    )

    user_trips = user_trip_manager.MainSearch()

    st.subheader("🌿 Recommended Trip Options (Based on Your Input)")
    if not user_trips:
        st.warning("No trips were found for your criteria.")
    else:
        for i, trip in enumerate(user_trips):
            st.markdown(f"### ✈️ Trip {i+1}")
            trip_details = trip.ToString()
            for detail in trip_details:
                st.write(f"• {detail}")


# --- Hardcoded Example (Preserved from Original Code) ---
st.subheader("🛠️ Hardcoded Example Trips (for Testing)")
tripManager = TripManager(10000, "Departure", "Florida", "Miami", "06/15/2025", "06/21/2025", 1)
trips = tripManager.MainSearch()

print(len(trips))

for trip in trips:
    trip = trip.ToString()
    for tripAttributes in trip:
        st.write(tripAttributes)

