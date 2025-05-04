#Author: Savanna Booten 

import streamlit as st  # streamlit is the main library for the web app
from datetime import date # date is used for date manipulation
from TripManager import TripManager # TripManager is a class that handles the trip planning logic

# Page Title
st.title("😊 Vacation Budget Planner 📖")

# Sidebar: Budget Setup
st.sidebar.header("1. Budget Setup")

# User Inputs
budget: int = 0
budget_input = st.sidebar.text_input("Enter your total vacation budget ($)", placeholder="e.g., 2000")

# Validate budget input
try:
    budget = float(budget_input) if budget_input else 0.0
except ValueError:
    budget = 0.0
    st.sidebar.error("❗ Please enter a valid number for the budget.")

# Sidebar: Trip Information 
st.sidebar.header("2. Trip Info")

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", 
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", 
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# Trip Information Inputs
departure: str = st.sidebar.selectbox("Departure State", states)
destinationState: str = st.sidebar.selectbox("Destination State", states)
destinationCity: str = st.sidebar.text_input("Destination City", placeholder="e.g., Miami")

# Dates input 
departureDate_obj = st.sidebar.date_input("Departure Date", min_value=date.today())
returnDate_obj = st.sidebar.date_input("Return Date", min_value=departureDate_obj)

# format dates to MM/DD/YYYY
departureDate: str = departureDate_obj.strftime("%m/%d/%Y")
returnDate: str = returnDate_obj.strftime("%m/%d/%Y")

# number of vacationers
vacationers: int = int(st.sidebar.number_input("Number of Vacationers", min_value=1, step=1))

# Validate and Show Summary on Main Page 
if st.sidebar.button("Validate Vacation Plan") and budget > 0:
    st.header("📊 Vacation Plan Summary")

    st.success("✅ Budget and trip information submitted successfully!")

    # Displays the users inputs
    st.markdown(f"""
    **📍 Departure State:** {departure}  
    **🏓️ Destination:** {destinationCity}, {destinationState}  
    **🗓️ Dates:** {departureDate} to {returnDate}  
    **🧑 Travelers:** {vacationers}  
    **💰 Budget:** ${budget:,.2f}
    """)

    placeholder = st.empty()

    # Show loading spinner while gathering information 
    with st.spinner("🔍 Planning your perfect trip..."):
        placeholder.info("🔄 Please wait, gathering trip data and calculating estimates...")

    with st.spinner("🔄 Gathering information may take longer due to being on a vacation..."):
        placeholder.info("Please wait, gathering trip data and calculating estimates...")

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
      
        # Trip search 
        user_trips = user_trip_manager.MainSearch()

    placeholder.success("✅ Trip planning complete! Scroll down to see your results.")

    # Display trip results in a more structured format
    st.subheader("🌿 Recommended Trip Options")
    if not user_trips:
        st.warning("No trips were found for your criteria.")
    else:
        st.success(f"Found {len(user_trips)} options within your budget of ${budget:,.2f}")

        trip_tabs = st.tabs([f"Trip Option {i+1}" for i in range(min(len(user_trips), 99))])

        # Display each trip option in a separate tab 
        for i, (tab, trip) in enumerate(zip(trip_tabs, user_trips[:99])):
            with tab:
                trip_details = trip.ToString()
                trip_days = (returnDate_obj - departureDate_obj).days

                col1, col2 = st.columns([3, 2])

                # Accommodation and Event details
                with col1:
                    if len(trip_details) > 0 and len(trip_details[0]) >= 2:
                        housing = trip_details[0]
                        st.markdown("### 🏠 Accommodation")

                        if float(housing[1]) < 0 or housing[0].strip() == "":
                            st.markdown("**Name:** Sorry, no housing available for this destination.")
                            st.markdown("**Price:** Price not available")
                            st.markdown("**Total:** N/A")
                            housing_cost = 0
                        else:
                            total_housing_cost = float(housing[1]) * trip_days
                            st.markdown(f"**Name:** {housing[0]}")
                            st.markdown(f"**Price:** ${housing[1]}/night")
                            st.markdown(f"**Total for {trip_days} nights:** ${total_housing_cost:.2f}")
                            housing_cost = total_housing_cost


                    # Event details 
                    if len(trip_details[0]) >= 4:
                        event_name = trip_details[0][2]
                        try:
                            event_cost = float(trip_details[0][3])
                        except ValueError:
                            event_cost = -1

                        st.markdown("### 🎭 Event")
                        if event_cost < 0 or event_name.strip() == "":
                            st.markdown("**Name:** No event information available.")
                            st.markdown("**Price:** Price not available")
                            st.markdown("**Total:** N/A")
                            event_cost = 0
                        else:
                            total_event_cost = event_cost * vacationers
                            st.markdown(f"**Name:** {event_name}")
                            st.markdown(f"**Price:** ${event_cost}/person")
                            st.markdown(f"**Total for {vacationers} people:** ${total_event_cost:.2f}")
                
               # Flight details 
                with col2:
                    st.markdown("### ✈️ Flights")
                    flight_cost = 0.0
                    try:
                        if len(trip_details) > 1 and len(trip_details[1]) >= 3:
                            outbound = trip_details[1]
                            st.markdown("**Outbound:**")
                            st.markdown(f"• Airline: {outbound[0]}")
                            st.markdown(f"• Depart Date: {departureDate}")
                            st.markdown(f"• Return Date: {returnDate}")
                            st.markdown(f"• Flight Price: ${outbound[3]}")
                      

                        outbound_price = float(trip_details[1][2]) if str(trip_details[1][2]).strip() != "" else 0.0
                        return_price = float(trip_details[2][2]) if str(trip_details[2][2]).strip() != "" else 0.0
                        flight_cost = (outbound_price + return_price) * vacationers
                    except (IndexError, ValueError):
                        pass  # no flight cost shown



                # Calculations for total cost
                st.markdown("### 💰 Total Cost Breakdown")
                try:
                    event_cost = 0 if 'event_cost' not in locals() else event_cost
                    flight_cost = float(outbound[3]);
                    total_cost = housing_cost + event_cost + flight_cost

                    # Display cost breakdown 
                    cost_col1, cost_col2, cost_col3, cost_col4 = st.columns(4)
                    cost_col1.metric("Accommodation", f"${housing_cost:.2f}")
                    cost_col2.metric("Events", f"${event_cost:.2f}")
                    cost_col3.metric("Flights", f"${flight_cost:.2f}")
                    cost_col4.metric("Total", f"${total_cost:.2f}")

                    # Budget bar 
                    if budget > 0:
                        budget_percentage = min(total_cost / budget * 100, 100)
                        st.progress(budget_percentage / 100)

                    # budget remaining 
                    remaining_budget = budget - total_cost
                    if remaining_budget >= 0:
                        st.success(f"✅ This trip fits within your budget with ${remaining_budget:.2f} to spare!")
                    else:
                        st.error(f"⚠️ This trip exceeds your budget by ${-remaining_budget:.2f}")

                except (IndexError, ValueError) as e:
                    st.warning(f"Unable to calculate complete cost breakdown: {e}")

                # Show raw trip details
                with st.expander("View raw trip details"):
                    for i, detail in enumerate(trip_details):
                        if i == 0:
                            st.write(f"Accommodation & Event: {detail}")
                        elif i == 1:
                            st.write(f"Outbound flight: {detail}")
                        elif i == 2:
                            st.write(f"Return flight: {detail}")
                        else:
                            st.write(detail)
