print(" PERSONAL POCKET CGPA CALCULATOR (PPC) ")
print("==========================")
courses = int(input("Enter number of courses: "))
total_points = 0
total_units = 0

for i in range(courses):
    print("\nCourse", i + 1)
    unit = int(input("Course Unit: "))
    grade = input("Grade (A-F): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    else:
        point = 0
    total_points += point * unit
    total_units += unit
cgpa = total_points / total_units

print("\n===== RESULT =====")
print("Total Units:", total_units)
print("Total Grade Points:", total_points)
print("CGPA =", round(cgpa, 2))