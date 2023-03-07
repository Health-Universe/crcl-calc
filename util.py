
def lbs_to_kg(weight_in_lbs: float) -> float:
    """
    Converts weight in pounds to kilograms.
    """
    return weight_in_lbs / 2.20462


def umol_per_l_to_mgdl(creatinine_in_micromol_per_l: float) -> float:
    """
    Converts serum creatinine level in micromoles per liter to mg/dL.
    """
    return creatinine_in_micromol_per_l / 88.4


def calculate_creatinine_clearance(is_male: bool, age: int, weight: float, creatinine: float) -> float:
    """
    This function calculates Creatinine Clearance (Cockcroft-Gault Equation).

    Parameters:
    is_male (bool): Indicates whether the patient is male (True) or female (False).
    age (int): Age of the patient in years.
    weight (float): Weight of the patient in kilograms.
    creatinine (float): Serum creatinine level of the patient in mg/dL.

    Returns:
    float: Calculated Creatinine Clearance in mL/min.

    """
    if is_male:
        coefficient = 1
    else:
        coefficient = 0.85

    creatinine_clearance = ((140 - age) * weight * coefficient) / (72 * creatinine)

    return creatinine_clearance

