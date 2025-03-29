def calculate_gpa():
    print("\nGPA CALCULATOR")
    subjects = int(input("Enter number of subjects: "))
    
    total_grade_points = 0
    total_credits = 0

    for i in range(subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        credit = float(input(f"Enter credit for subject {i+1}: "))
        total_grade_points += (grade * credit)
        total_credits += credit

    gpa = total_grade_points / total_credits
    print(f"\nGPA: {gpa}")
    print(f"Total Credits: {total_credits}")


def calculate_cgpa():
    print("\nCGPA CALCULATOR")
    semesters = int(input("Enter total number of semesters: "))
    
    total_gpa = 0

    for i in range(semesters):
        gpa = float(input(f"Enter GPA for semester {i+1}: "))
        total_gpa += gpa

    cgpa = total_gpa / semesters
    print(f"\nCGPA: {cgpa}")


print("Welcome to GPA/CGPA Calculator")
choice = input("Select an option (1: GPA, 2: CGPA): ")

if choice == '1':
    calculate_gpa()
elif choice == '2':
    calculate_cgpa()
else:
    print("Invalid choice! Please enter 1 or 2.")
