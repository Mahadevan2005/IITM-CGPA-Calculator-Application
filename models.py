# models.py

# Mapping of grades to grade points (IITM BS system)
GRADE_POINTS = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 4,
}

def calculate_cgpa(grades, credits):
    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        grade = grade.strip().upper()
        credit = float(credit)

        if grade not in GRADE_POINTS:
            raise ValueError(f"Invalid grade: {grade}")

        total_points += GRADE_POINTS[grade] * credit
        total_credits += credit

    if total_credits == 0:
        raise ValueError("Total credits cannot be zero.")

    return round(total_points / total_credits, 2)