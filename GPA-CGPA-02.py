import streamlit as st

# INITIALIZE SESSION STATE VARIABLES
if "num_subjects" not in st.session_state:
    st.session_state.num_subjects = ""
if "num_semesters" not in st.session_state:
    st.session_state.num_semesters = ""
if "calculate_pressed" not in st.session_state:
    st.session_state.calculate_pressed = False
if "calculate_cgpa_pressed" not in st.session_state:
    st.session_state.calculate_cgpa_pressed = False

# FUNCTION TO RESET INPUTS
def reset_inputs():
    st.session_state.clear()
    st.session_state.num_subjects = ""
    st.session_state.num_semesters = ""
    st.session_state.calculate_pressed = False
    st.session_state.calculate_cgpa_pressed = False
    st.rerun()

# GPA CALCULATOR FUNCTION
def calculate_gpa():
    st.subheader("GPA Calculator")
    subjects = st.text_input("Enter number of subjects:", key="num_subjects")

    if subjects.isdigit() and int(subjects) > 0:
        subjects = int(subjects)

        grades = []
        credits = []
        total_grade_points = 0
        total_credits = 0

        for i in range(subjects):
            grade = st.text_input(f"Enter grade for subject {i+1}:", key=f"g{i}", value="")
            credit = st.text_input(f"Enter credit for subject {i+1}:", key=f"c{i}", value="")

            grades.append(grade)
            credits.append(credit)

        col1, col2 = st.columns(2)

        if col1.button("Calculate GPA"):
            st.session_state.calculate_pressed = True
            st.rerun()

        if col2.button("Reset"):
            reset_inputs()

        if st.session_state.calculate_pressed:
            for i in range(subjects):
                if grades[i] == "" or credits[i] == "":
                    st.error(f"⚠️ Please enter both grade and credit for subject {i+1}.")
                    return

                try:
                    grade = float(grades[i])
                    credit = float(credits[i])

                    if grade <= 0 or credit <= 0:
                        st.error(f"⚠️ Grade and credit must be greater than 0 for subject {i+1}.")
                        return

                    total_grade_points += grade * credit
                    total_credits += credit

                except ValueError:
                    st.error(f"⚠️ Invalid input in subject {i+1}. Please enter numeric values.")
                    return

            gpa = total_grade_points / total_credits
            st.success(f"✅ **GPA:** {gpa:.3f}")
            st.info(f"📘 **Total Credits:** {total_credits:.1f}")

# CGPA CALCULATOR FUNCTION
def calculate_cgpa():
    st.subheader("CGPA Calculator")
    semesters = st.text_input("Enter total number of semesters:", key="num_semesters")

    if semesters.isdigit() and int(semesters) > 0:
        semesters = int(semesters)

        gpas = []
        total_gpa = 0

        for i in range(semesters):
            gpa = st.text_input(f"Enter GPA for semester {i+1}:", key=f"sg{i}", value="")
            gpas.append(gpa)

        col1, col2 = st.columns(2)

        if col1.button("Calculate CGPA"):
            st.session_state.calculate_cgpa_pressed = True
            st.rerun()

        if col2.button("Reset"):
            reset_inputs()

        if st.session_state.calculate_cgpa_pressed:
            for i in range(semesters):
                if gpas[i] == "":
                    st.error(f"⚠️ Please enter GPA for semester {i+1}.")
                    return

                try:
                    gpa = float(gpas[i])

                    if gpa <= 0:
                        st.error(f"⚠️ GPA must be greater than 0 for semester {i+1}.")
                        return

                    total_gpa += gpa

                except ValueError:
                    st.error(f"⚠️ Invalid input in semester {i+1}. Please enter numeric values.")
                    return

            cgpa = total_gpa / semesters
            st.success(f"✅ **CGPA:** {cgpa:.3f}")

# MAIN FUNCTION
def main():
    st.title("📚 GPA & CGPA Calculator")

    option = st.radio("Select an option:", ("GPA Calculator", "CGPA Calculator"), key="option")

    if option == "GPA Calculator":
        calculate_gpa()
    elif option == "CGPA Calculator":
        calculate_cgpa()

if __name__ == "__main__":
    main()
