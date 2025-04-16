import streamlit as st
from datetime import date

# --- Page Title ---
st.title("😊 Vacation Budget Planner 📖")

# --- Sidebar: Budget Setup ---
st.sidebar.header("1. Budget Setup")

# Total Vacation Budget (now using text input with placeholder)
budget_input = st.sidebar.text_input("Enter your total vacation budget ($)", placeholder="e.g., 2000")

try:
    total_budget = float(budget_input) if budget_input else 0.0
except ValueError:
    total_budget = 0.0
    st.sidebar.error("❗ Please enter a valid number for the budget.")

# Remaining percentage
remaining_percentage = 100.0

# --- Sidebar: Allocate Budget ---
st.sidebar.subheader("Allocate your budget by category (%)")

if total_budget > 0:
    food_pct = st.sidebar.slider("Food (%)", 0.0, remaining_percentage, 0.0, step=0.5)
    remaining_percentage -= food_pct

    lodging_pct = st.sidebar.slider("Lodging (%)", 0.0, remaining_percentage, 0.0, step=0.5)
    remaining_percentage -= lodging_pct

    entertainment_pct = st.sidebar.slider("Entertainment (%)", 0.0, remaining_percentage, 0.0, step=0.5)
    remaining_percentage -= entertainment_pct

    airfare_pct = st.sidebar.slider("Airfare (%)", 0.0, remaining_percentage, 0.0, step=0.5)
    remaining_percentage -= airfare_pct

    spending_pct = st.sidebar.slider("Spending Money (%)", 0.0, remaining_percentage, 0.0, step=0.5)
    remaining_percentage -= spending_pct

    st.sidebar.info(f"Remaining Budget: {remaining_percentage:.1f}%")

# --- Sidebar: Trip Information ---
st.sidebar.header("2. Trip Info")

states = ["Florida", "California", "Texas", "Kentucky", "New York"]

departure_state = st.sidebar.selectbox("Departure State", states)
destination_state = st.sidebar.selectbox("Destination State", states)
destination_city = st.sidebar.text_input("Destination City", placeholder="e.g., Miami")

departure_date = st.sidebar.date_input("Departure Date", min_value=date.today())


return_date = st.sidebar.date_input("Return Date", min_value=departure_date)


vacationers = st.sidebar.number_input("Number of Vacationers", min_value=1, step=1)

# --- Validate and Show Summary on Main Page ---
if st.sidebar.button("Validate Vaccation Plan"):
    st.header("📊 Budget Allocation Summary")

    total_pct = food_pct + lodging_pct + entertainment_pct + airfare_pct + spending_pct

    if total_pct != 100:
        st.error(f"❗ Your total is {total_pct:.1f}%. Please make sure it equals 100%.")
    else:
        st.success("✅ Budget allocations are valid!")

        # Calculate dollar amounts
        food_amt = (food_pct / 100) * total_budget
        lodging_amt = (lodging_pct / 100) * total_budget
        entertainment_amt = (entertainment_pct / 100) * total_budget
        airfare_amt = (airfare_pct / 100) * total_budget
        spending_amt = (spending_pct / 100) * total_budget

        # Display budget results
        st.subheader("Your Budget Allocation:")
        st.write(f"🍴 Food: ${food_amt:.2f} ({food_pct:.1f}%)")
        st.write(f"🏨 Lodging: ${lodging_amt:.2f} ({lodging_pct:.1f}%)")
        st.write(f"🎉 Entertainment: ${entertainment_amt:.2f} ({entertainment_pct:.1f}%)")
        st.write(f"✈️ Airfare: ${airfare_amt:.2f} ({airfare_pct:.1f}%)")
        st.write(f"🛍️ Spending Money: ${spending_amt:.2f} ({spending_pct:.1f}%)")

       # Display trip info
        st.subheader("Your Trip Details:")
        st.markdown(f"""
        **📍 Departure State:** {departure_state}  
        **🏖️ Destination:** {destination_city}, {destination_state}  
        **📅 Dates:** {departure_date.strftime("%m/%d/%Y")} to {return_date.strftime("%m/%d/%Y")}  
        **🧑 Travelers:** {vacationers}
        """)
