import streamlit as st

def calculate_gpa():
    st.subheader("GPA Calculator")
    subjects = st.number_input("Enter number of subjects:", min_value=1, step=1)

    total_grade_points = 0
    total_credits = 0
    grades = []
    credits = []

    for i in range(subjects):
        grade = st.number_input(f"Enter grade for subject {i+1}:", min_value=0.0, step=0.001, format="%.3f", key=f"g{i}")
        credit = st.number_input(f"Enter credit for subject {i+1}:", min_value=0.1, step=0.1, format="%.1f", key=f"c{i}")
        grades.append(grade)
        credits.append(credit)

    if st.button("Calculate GPA"):
        if all(credit == 0 for credit in credits):
            st.error("Total credits cannot be zero. Please enter valid credit values.")
            return

        for i in range(subjects):
            total_grade_points += grades[i] * credits[i]
            total_credits += credits[i]

        if total_credits > 0:
            gpa = total_grade_points / total_credits
            st.success(f"**GPA:** {gpa:.3f}")
            st.info(f"**Total Credits:** {total_credits:.1f}")

def calculate_cgpa():
    st.subheader("CGPA Calculator")
    semesters = st.number_input("Enter total number of semesters:", min_value=1, step=1)

    total_gpa = 0
    gpas = []

    for i in range(semesters):
        gpa = st.number_input(f"Enter GPA for semester {i+1}:", min_value=0.0, step=0.001, format="%.3f", key=f"sg{i}")
        gpas.append(gpa)

    if st.button("Calculate CGPA"):
        if all(gpa == 0 for gpa in gpas):  # Prevent division by zero
            st.error("CGPA cannot be calculated with all zero GPAs.")
            return

        for gpa in gpas:
            total_gpa += gpa

        if semesters > 0:
            cgpa = total_gpa / semesters
            st.success(f"**CGPA:** {cgpa:.3f}")

def main():
    st.title("📚 GPA & CGPA Calculator")
    option = st.radio("Select an option:", ("GPA Calculator", "CGPA Calculator"))

    if option == "GPA Calculator":
        calculate_gpa()
    elif option == "CGPA Calculator":
        calculate_cgpa()

if __name__ == "__main__":
    main()
