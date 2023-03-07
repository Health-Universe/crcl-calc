import streamlit as st
from util import lbs_to_kg, umol_per_l_to_mgdl, calculate_creatinine_clearance

# Set page title
st.set_page_config(page_title="Creatinine Clearance Calculator")


# Create a function to display the calculator
def creatinine_clearance_calculator():
    st.write("# Creatinine Clearance Calculator")
    st.write(
        "This calculator estimates Creatinine Clearance (CrCl) using the Cockcroft-Gault equation."
    )

    # Collect patient information
    info_col1, info_col2 = st.columns(2)

    with info_col1:
        is_male = st.radio("Sex", options=["Male", "Female"]) == "Male"
        weight = st.number_input(
            "Weight", min_value=1.0, max_value=300.0, value=70.0, step=1.0
        )

    with info_col2:
        age = st.number_input("Age", min_value=1, max_value=120, value=30, step=1)
        creatinine = st.number_input(
            "Serum Creatinine", min_value=0.1, max_value=30.0, value=0.9, step=0.1
        )

    # Convert units
    units_col1, units_col2 = st.columns(2)

    with units_col1:
        if st.radio("Weight Units", options=["kg", "lbs"]) == "lbs":
            weight = lbs_to_kg(weight)

    with units_col2:
        if st.radio("Serum Creatinine Units", options=["mg/dL", "µmol/L"]) == "µmol/L":
            creatinine = umol_per_l_to_mgdl(creatinine)

    # Calculate Creatinine Clearance
    crcl = calculate_creatinine_clearance(is_male, age, weight, creatinine)

    # Display results
    st.write(f"### Result: {crcl:.2f} mL/min")


# Run the calculator
creatinine_clearance_calculator()
