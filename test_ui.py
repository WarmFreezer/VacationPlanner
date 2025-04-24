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

    # Display trip results in a more structured format
    st.subheader("🌿 Recommended Trip Options")
    if not user_trips:
        st.warning("No trips were found for your criteria.")
    else:
        st.success(f"Found {len(user_trips)} options within your budget of ${budget:,.2f}")
        
        # Create tabs for each trip option (up to 10 to avoid overwhelming the UI)
        trip_tabs = st.tabs([f"Trip Option {i+1}" for i in range(min(len(user_trips), 10))])
        
        # Display each trip in its own tab
        for i, (tab, trip) in enumerate(zip(trip_tabs, user_trips[:10])):
            with tab:
                trip_details = trip.ToString()
                
                # Calculate trip duration
                trip_days = (returnDate_obj - departureDate_obj).days
                
                # Split into columns for better layout
                col1, col2 = st.columns([3, 2])
                
                with col1:
                    # Format accommodation details
                    if len(trip_details) > 0 and len(trip_details[0]) >= 2:
                        housing = trip_details[0]
                        total_housing_cost = float(housing[1]) * trip_days
                        
                        st.markdown("### 🏠 Accommodation")
                        st.markdown(f"**Name:** {housing[0]}")
                        st.markdown(f"**Price:** ${housing[1]}/night")
                        st.markdown(f"**Total for {trip_days} nights:** ${total_housing_cost:.2f}")
                    
                    # Format event details
                    if len(trip_details) > 0 and len(trip_details[0]) >= 4:
                        event_name = trip_details[0][2]
                        event_cost = float(trip_details[0][3])
                        total_event_cost = event_cost * vacationers
                        
                        st.markdown("### 🎭 Event")
                        st.markdown(f"**Name:** {event_name}")
                        st.markdown(f"**Price:** ${event_cost}/person")
                        st.markdown(f"**Total for {vacationers} people:** ${total_event_cost:.2f}")
                
                with col2:
                    # Format flight details
                    st.markdown("### ✈️ Flights")
                    
                    # Departure flight
                    if len(trip_details) > 1 and len(trip_details[1]) >= 3:
                        outbound = trip_details[1]
                        st.markdown("**Outbound:**")
                        st.markdown(f"• Airline: {outbound[0]}")
                        st.markdown(f"• Date: {outbound[1]}")
                        st.markdown(f"• Price: ${outbound[2]}")
                    
                    # Return flight
                    if len(trip_details) > 2 and len(trip_details[2]) >= 3:
                        return_flight = trip_details[2]
                        st.markdown("**Return:**")
                        st.markdown(f"• Airline: {return_flight[0]}")
                        st.markdown(f"• Date: {return_flight[1]}")
                        st.markdown(f"• Price: ${return_flight[2]}")
                    
                    # Calculate and display total flight cost
                    if len(trip_details) > 2:
                        flight_cost = (float(trip_details[1][2]) + float(trip_details[2][2])) * vacationers
                        st.markdown(f"**Total flight cost for {vacationers} people:** ${flight_cost:.2f}")
                
                # Calculate and display total trip cost
                st.markdown("### 💰 Total Cost Breakdown")
                try:
                    housing_cost = float(trip_details[0][1]) * trip_days
                    event_cost = float(trip_details[0][3]) * vacationers if len(trip_details[0]) >= 4 else 0
                    flight_cost = (float(trip_details[1][2]) + float(trip_details[2][2])) * vacationers if len(trip_details) > 2 else 0
                    
                    total_cost = housing_cost + event_cost + flight_cost
                    
                    # Create a cost breakdown using columns
                    cost_col1, cost_col2, cost_col3, cost_col4 = st.columns(4)
                    cost_col1.metric("Accommodation", f"${housing_cost:.2f}")
                    cost_col2.metric("Events", f"${event_cost:.2f}")
                    cost_col3.metric("Flights", f"${flight_cost:.2f}")
                    cost_col4.metric("Total", f"${total_cost:.2f}")
                    
                    # Budget comparison progress bar
                    budget_percentage = min(total_cost / budget * 100, 100)
                    st.progress(budget_percentage/100)
                    
                    remaining_budget = budget - total_cost
                    if remaining_budget >= 0:
                        st.success(f"✅ This trip fits within your budget with ${remaining_budget:.2f} to spare!")
                    else:
                        st.error(f"⚠️ This trip exceeds your budget by ${-remaining_budget:.2f}")
                    
                except (IndexError, ValueError) as e:
                    st.warning(f"Unable to calculate complete cost breakdown: {e}")
                    
                # Option to view raw data
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
