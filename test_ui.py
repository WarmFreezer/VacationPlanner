
import streamlit as st

# --- Page Title ---
st.title(" Vacation Budget Planner")

# --- Sidebar: Budget Setup ---
st.sidebar.header("1. Budget Setup")

# Total Vacation Budget (now using text input with placeholder)
budget_input = st.sidebar.text_input("Enter your total vacation budget ($)", placeholder="e.g., 2000")

# Make sure budget_input is a valid number before converting
try:
    total_budget = float(budget_input) if budget_input else 0.0
except ValueError:
    total_budget = 0.0
    st.sidebar.error("❗ Please enter a valid number for the budget.")

# Initialize remaining percentage
remaining_percentage = 100.0

# --- Sidebar: Allocate Budget ---
st.sidebar.subheader("Allocate your budget by category (%)")

if total_budget > 0:
    food_pct = st.sidebar.slider("Food (%)", min_value=0.0, max_value=remaining_percentage, value=0.0, step=0.5)
    remaining_percentage -= food_pct

    lodging_pct = st.sidebar.slider("Lodging (%)", min_value=0.0, max_value=remaining_percentage, value=0.0, step=0.5)
    remaining_percentage -= lodging_pct

    entertainment_pct = st.sidebar.slider("Entertainment (%)", min_value=0.0, max_value=remaining_percentage, value=0.0, step=0.5)
    remaining_percentage -= entertainment_pct

    airfare_pct = st.sidebar.slider("Airfare (%)", min_value=0.0, max_value=remaining_percentage, value=0.0, step=0.5)
    remaining_percentage -= airfare_pct

    spending_pct = st.sidebar.slider("Spending Money (%)", min_value=0.0, max_value=remaining_percentage, value=0.0, step=0.5)
    remaining_percentage -= spending_pct

    st.sidebar.info(f"Remaining Budget: {remaining_percentage:.1f}%")

    # --- Validate Percentages ---
    total_pct = food_pct + lodging_pct + entertainment_pct + airfare_pct + spending_pct

    if st.sidebar.button("Validate Budget Allocation"):
        st.header("Budget Allocation Summary")

        if total_pct > 100:
            st.error(f"❗ You allocated {total_pct:.1f}%, which is more than 100%. Please adjust.")
        elif total_pct < 100:
            st.error(f"❗ You allocated {total_pct:.1f}%, which is less than 100%. Please adjust.")
        else:
            st.success("✅ Budget allocations are valid!")

            # Calculate dollar amounts
            food_amt = (food_pct / 100) * total_budget
            lodging_amt = (lodging_pct / 100) * total_budget
            entertainment_amt = (entertainment_pct / 100) * total_budget
            airfare_amt = (airfare_pct / 100) * total_budget
            spending_amt = (spending_pct / 100) * total_budget

            # --- Main page: Show the calculated budget
            st.subheader("Your Budget Allocation Summary:")
            st.write(f" Food: ${food_amt:.2f} ({food_pct:.1f}%)")
            st.write(f" Lodging: ${lodging_amt:.2f} ({lodging_pct:.1f}%)")
            st.write(f" Entertainment: ${entertainment_amt:.2f} ({entertainment_pct:.1f}%)")
            st.write(f" Airfare: ${airfare_amt:.2f} ({airfare_pct:.1f}%)")
            st.write(f" Spending Money: ${spending_amt:.2f} ({spending_pct:.1f}%)")
